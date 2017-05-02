__version__ = '$Revision: 43161 $'

#### Python/Jython Imports ####
import sys

#### DMA Imports ####
import commonvalidation
import pythontools
import ostools
import oracletools
import oraclevalidation
import parametertools
import steplog
from validator import Validator


io_params = parametertools.parse_dma_params()
#### Parameter Inputs ####
PRIMARY_NODE_HOSTNAMES = filter(bool, [x.strip() for x in io_params['Primary Node Hostnames'].strip().split(',')])
STANDBY_NODE_HOSTNAMES = filter(bool, [x.strip() for x in io_params['Standby Node Hostnames'].strip().split(',')])
PRIMARY_DB_INSTANCE_NAME = io_params['Primary DB Instance Name'].strip()
PRIMARY_DB_NAME = io_params['Primary Database Name'].strip()
ORACLE_USER = "sys"
ORACLE_SYS_PASSWORD = io_params['Oracle sys Password'].strip()
ORACLE_OS_USER = io_params['Oracle OS User'].strip()
STANDBY_PREFIX = io_params['Standby DB Prefix Name'].strip()
DG_STANDBY_TYPE = io_params['Data Guard Standby Type'].strip()
DB_PROTECTION_MODE = io_params['Database Protection Mode'].strip()

PRIMARY_DB_LISTENER_PORT = io_params['Primary DB Listener Port Number'].strip()
STANDBY_DB_LISTENER_PORT = io_params['Standby DB Listener Port Number'].strip()
NUM_RMAN_AUX_CHANNELS = io_params['Number of RMAN Auxiliary Channels'].strip()
NUM_RMAN_PRIMARY_CHANNELS = io_params['Number of RMAN Primary Channels'].strip()
ARCHIVE_LAG_TARGET = io_params['Archive Lag Target'].strip()
CHG_REMOTE_LOGIN_PSWDFILE = io_params['Change Remote Login PasswordFile on Primary'].strip()
DB_FILE_NAME_CONVERT = io_params['DB File Name Convert'].strip()
STANDBY_CTL_FILE_LOCATION = io_params['Location for Controlfiles on Standby Server'].strip()
LOG_ARCHIVE_DEST_1 = io_params['Log Archive Dest 1'].strip()
LOG_FILE_NAME_CONVERT = io_params['Log File Name Convert'].strip()
LISTENER_FILE_LOCATION = io_params['Listener File Location'].strip()
ORATAB_LOCATION = io_params['Oratab File Location'].strip()
TNSNAMES_FILE_LOCATION = io_params['Tnsnames File Location'].strip()
UPDATE_STANDBY_ORATAB_FILE = io_params['Update oratab file on Standby Servers'].strip()
CRS_HOME = io_params['CRS Home'].strip()


#### Globals ####
oracle_home = ''
standby_svc_name = ''

VALID_DB_PRIMARY_PROTECTION_MODES = [
    'Maximum Protection',
    'Maximum Availability',
    'Maximum Performance',
]

VALID_DATA_GUARD_STANDBY_TYPES = [
    'Physical',
    'Logical',
    'Snapshot',
]


#### Methods ####

def main():
    steplog.info('Validate Provision Oracle Data Guard')

    Validator.register(check_standby_DB_name)
    Validator.register(check_required_parameters)
    Validator.register(check_for_reachable_hosts, args=[PRIMARY_NODE_HOSTNAMES])
    Validator.register(check_for_reachable_hosts, args=[STANDBY_NODE_HOSTNAMES])
    if DB_FILE_NAME_CONVERT:
        Validator.register(check_filename_convert_pattern, args=[DB_FILE_NAME_CONVERT])
    if LOG_FILE_NAME_CONVERT:
        Validator.register(check_filename_convert_pattern, args=[LOG_FILE_NAME_CONVERT])
    Validator.register(oraclevalidation.validate_optional_file_name, args=[ORATAB_LOCATION, "Oratab File Location"])
    Validator.register(oraclevalidation.validate_optional_file_name, args=[TNSNAMES_FILE_LOCATION, "Tnsnames File Location"])
    Validator.register(commonvalidation.validate_parameter_in_allowed_values, args=[DB_PROTECTION_MODE, VALID_DB_PRIMARY_PROTECTION_MODES, "Database Protection Mode"])
    Validator.register(commonvalidation.validate_parameter_in_allowed_values, args=[DG_STANDBY_TYPE, VALID_DATA_GUARD_STANDBY_TYPES, "Data Guard Standby Type"])
    Validator.register(commonvalidation.validate_parameter_in_allowed_values, args=[UPDATE_STANDBY_ORATAB_FILE, ["yes", "no"], "Update oratab file on Standby Servers"])
    Validator.register(commonvalidation.validate_parameter_in_allowed_values, args=[CHG_REMOTE_LOGIN_PSWDFILE, ["yes", "no"], "Change Remote Login PasswordFile on Primary"])
    Validator.validate()
    failures = Validator.str_failed_results()
    if failures:
        msg = 'Error(s) validating parameters for Provision Oracle Data Guard:\n\n%s' % failures
        steplog.info(msg)
        steplog.error(msg)
        sys.exit(1)

    # given the instance name in primary_db_instance_name,
    # identify the matching entry in the  /etc/oratab on the
    # primary_node_hostnames[0] and pluck out the corresponding
    # oracle_home value
    Validator.register(infer_oracle_home, args=[PRIMARY_NODE_HOSTNAMES[0], PRIMARY_DB_INSTANCE_NAME, ORATAB_LOCATION])
    Validator.validate()
    failures = Validator.str_failed_results()
    if failures:
        msg = 'Error(s) validating parameters for Provision Oracle Data Guard:\n\n%s' % failures
        steplog.info(msg)
        steplog.error(msg)
        sys.exit(1)

    Validator.register(oraclevalidation.validate_oracle_home, args=[oracle_home])
    Validator.register(check_working_credential)
    Validator.register(check_standby_service_name)
    Validator.validate()
    failures = Validator.str_failed_results()
    if failures:
        msg = 'Error(s) validating parameters for Provision Oracle Data Guard:\n\n%s' % failures
        steplog.info(msg)
        steplog.error(msg)
        sys.exit(1)

    steplog.info('Validate Provision Oracle Data Guard successful.  You may proceed.')
    print_header()
    sys.exit(0)


def check_standby_DB_name():
    """
        Checks that the standby database name (STANDBY_PREFIX+PRIMARY_DB_NAME)
        doesn't exceed the size limit of 8 characters that Oracle imposes.
    """
    if len(STANDBY_PREFIX) + len(PRIMARY_DB_NAME) > 8:
        return False, 'Length of the standby database name (STANDBY_PREFIX+PRIMARY_DB_NAME) exceeds the size limit of 8 characters'
    return True, 'Completed Standby Database Name validation successfully'


def check_filename_convert_pattern(filename_convert_string):
    """
        Checks that the File Name Convert parameter respects the pattern
        "string1", "string2", "string3", "string4", with even number of database filename strings
    """
    filename_list = [s.strip() for s in filename_convert_string.split(",")]
    if len(filename_list) % 2 == 1:
        return False, 'File Name Convert parameter "%s" has an odd number of database filename strings' % filename_convert_string
    for s in filename_list:
        if not (s.startswith(('"', "'")) and s.endswith(('"', "'"))):
            return False, 'File Name Convert parameter %s does not respect the right pattern "string1", "string2", "string3", "string4"' % filename_convert_string
    return True, 'Completed File Name Convert validation for %s' % filename_convert_string


def check_required_parameters():
    is_valid = True
    required_params_dict = {"Primary Node Hostnames": ",".join(PRIMARY_NODE_HOSTNAMES),
                            "Standby Node Hostnames": ",".join(STANDBY_NODE_HOSTNAMES),
                            "Primary DB Instance Name": PRIMARY_DB_INSTANCE_NAME,
                            "Primary Database Name": PRIMARY_DB_NAME,
                            "Oracle sys Password": ORACLE_SYS_PASSWORD,
                            "Oracle Account": ORACLE_USER,
                            "Oracle OS User": ORACLE_OS_USER,
                            "Standby DB Prefix Name": STANDBY_PREFIX,
                            "Data Guard Standby Type": DG_STANDBY_TYPE,
                            "Database Protection Mode": DB_PROTECTION_MODE}
    required_params_not_set = pythontools.validate_required_parameters(required_params_dict)
    if len(required_params_not_set) > 0:
        is_valid = False
        msg = "Validate all required input parameters are set failed."
        for param in required_params_not_set:
            steplog.error("Required parameter %s is not set." % param)
    else:
        msg = "Validate all required input parameters are set succeeded."
    return is_valid, msg


def check_for_reachable_hosts(hosts):
    """
        Attempt to ping the hostnames.
        Return non-zero code if any of the hostnames are unreachable.
        Assumes a Linux platform.
    """
    is_valid = True
    hosts_reachable = 0
    for hostname in hosts:
        if not ostools.test_ping(hostname):
            steplog.error("Hostname %s is not available at ping." % hostname)
            is_valid = False
        else:
            print "Hostname: %s reachable via TCP/IP network" % hostname
            hosts_reachable += 1
    if hosts_reachable == len(hosts):
        msg = "Completed check for reachable hosts."
    else:
        msg = "Not all hosts verified are reachable."
    return is_valid, msg


def infer_oracle_home(primary_host, instance_name, oratab_file):
    global oracle_home
    is_valid = True
    cmd = '/usr/bin/ssh %s ls -l %s' % (primary_host, oratab_file)
    output, errors, rc = ostools.run_command(cmd)
    if rc != 0:
        return False, 'Unable to reference standard oratab file location on primary host\n'
    filename = output.strip().split().pop()
    if filename != oratab_file:
        steplog.error('Standard path for oratab file of: %s not valid\n' % oratab_file)
        is_valid = False

    cmd = '/usr/bin/ssh %s /bin/cat %s' % (primary_host, oratab_file)
    output, errors, rc = ostools.run_command(cmd)
    if rc != 0:
        steplog.error("Oratab file not accessible for unknown reason.")
        is_valid = False
    entries = [line.strip() for line in output.split('\n')]
    matches = [entry.split(':')[1] for entry in entries
               if entry.split(':')[0] == instance_name]
    if not matches:
        steplog.error('Unable to match any oratab entries to target instance name: %s\n' % instance_name)
        is_valid = False
    oracle_home = matches[0]  # take the oracle_home value for first instance that matched
    return is_valid, "Completed Oratab file validation and ORACLE_HOME discovery"


def check_working_credential():
    """ Attempt to establish a connection to the service using the user and
        password provided. Return a boolean indication of whether the
        connection attempt was successful.
        Verifies that the Oracle user provided has sysdba privileges.
    """
    passwd = '%s as sysdba' % ORACLE_SYS_PASSWORD
    steplog.debug('#### #### ####\npassword: %r\n#### #### ####' % passwd)
    oracle_sid = PRIMARY_DB_INSTANCE_NAME
    # here we determine the type of the environment in order to export the right ORACLE_SID
    if CRS_HOME:
        database_type = oracletools.get_RAC_database_type(oracle_home, PRIMARY_DB_INSTANCE_NAME)
        if database_type == "RACOneNode":
            # first case : when we have a One Node RAC database
            oracle_sid = PRIMARY_DB_INSTANCE_NAME + "_1"
        elif database_type == "RAC":
            #second case: when we have multinode RAC with policy based management
            is_policy_managed = oracletools.is_policy_managed(oracle_home, PRIMARY_DB_INSTANCE_NAME)
            if is_policy_managed is True:
                oracle_sid = PRIMARY_DB_INSTANCE_NAME + "_1"
            else:
                # here we treat the case when for Standard RAC using admin based management oracle_sid will become DBName1
                oracle_sid = PRIMARY_DB_INSTANCE_NAME + "1"
    result = oracletools.get_oracle_status(oracle_home=oracle_home,
                                           oracle_sid=oracle_sid,
                                           os_user=ORACLE_OS_USER,
                                           user=ORACLE_USER,
                                           user_pass=passwd)
    if 'shutdown' in result:
        steplog.error('Database %s does not appear to be running and needs to be running for this workflow execution.' % oracle_sid)
        return False

    if not result:
        steplog.error('No result from oracle status query')
        return False
    elif 'ERROR' in result.upper():
        steplog.error('Error during oracle status query, check output for details.')
        return False
    return True, "Completed check for valid 'sys' credential on Primary DB."


def check_standby_service_name():
    global standby_svc_name
    if not PRIMARY_DB_NAME or not STANDBY_PREFIX:
        return False, 'Cannot set the standby service name, either primary db name or standby prefix is not set'
    standby_svc_name = '%s%s' % (STANDBY_PREFIX, PRIMARY_DB_NAME)
    return True, 'Set the Standby Service Name to %r' % standby_svc_name


def print_header():
    parametertools.print_header({
        'Archive Lag Target': ARCHIVE_LAG_TARGET,
        'Change Remote Login Passwordfile on Primary': CHG_REMOTE_LOGIN_PSWDFILE,
        'DB File Name Convert': DB_FILE_NAME_CONVERT,
        'Data Guard Standby Type': DG_STANDBY_TYPE,
        'Database Protection Mode': DB_PROTECTION_MODE,
        'Listener File Location': LISTENER_FILE_LOCATION,
        'Location for Controlfiles on Standby Server': STANDBY_CTL_FILE_LOCATION,
        'Log Archive Dest 1': LOG_ARCHIVE_DEST_1,
        'Log File Name Convert': LOG_FILE_NAME_CONVERT,
        'Number of RMAN Auxiliary Channels': NUM_RMAN_AUX_CHANNELS,
        'Number of RMAN Primary Channels': NUM_RMAN_PRIMARY_CHANNELS,
        'Oracle Home': oracle_home,
        'Oracle OS User': ORACLE_OS_USER,
        'Oracle User': ORACLE_USER,
        'Oracle sys Password': ORACLE_SYS_PASSWORD,
        'Oratab File Location': ORATAB_LOCATION,
        'Primary DB Instance Name': PRIMARY_DB_INSTANCE_NAME,
        'Primary DB Listener Port Number': PRIMARY_DB_LISTENER_PORT,
        'Primary Database Name': PRIMARY_DB_NAME,
        'Primary Node Hostnames': ",".join(PRIMARY_NODE_HOSTNAMES),
        'Standby DB Listener Port Number': STANDBY_DB_LISTENER_PORT,
        'Standby DB Prefix Name': STANDBY_PREFIX,
        'Standby Node Hostnames': ",".join(STANDBY_NODE_HOSTNAMES),
        'Standby Service Name': standby_svc_name,
        'Tnsnames File Location': TNSNAMES_FILE_LOCATION,
        'Update oratab file on Standby Servers': UPDATE_STANDBY_ORATAB_FILE,
    })


#### Call to main ####

if __name__ == '__main__':
    try:
        main()
    except StandardError, e:
        steplog.handle_exception(e)
