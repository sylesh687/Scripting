__version__ = '$Revision: 45855 $'

#### Python/Jython Imports ####
import sys
import socket
import re

#### DMA Imports ####
import parametertools
import steplog
import ostools
import oracletools


io_params = parametertools.parse_dma_params()

#### Parameter Inputs ####
tns_file_location = io_params['Tnsnames File Location'].strip()
lsnr_file_location = io_params['Listener File Location'].strip()
primary_lsnr_port_num = io_params['Primary DB Listener Port Number'].strip()
standby_lsnr_port_num = io_params['Standby DB Listener Port Number'].strip()
ASM_DISKGROUP = io_params['ASM Disk Group'].strip()
ORACLE_HOME = io_params['Oracle Home'].strip()
ORACLE_SID = io_params['Oracle SID'].strip()
PRIMARY_NODE_HOSTNAMES = filter(bool, [x.strip() for x in io_params['Primary Node Hostnames'].strip().split(',')])
STANDBY_NODE_HOSTNAMES = filter(bool, [x.strip() for x in io_params['Standby Node Hostnames'].strip().split(',')])
DB_UNIQUE_NAME = io_params['DB Unique Name'].strip()
STANDBY_PREFIX = io_params['Standby DB Prefix'].strip()
ENV_TYPE = io_params['Env Type'].strip()
ORATAB_FILE_LOCATION = io_params['Oratab File Location'].strip()
SERVICE_NAME = io_params['Service Name'].strip()
ORACLE_USER = io_params['Oracle OS User'].strip()


#### Globals ####
params = {}
asm_home = ''
asm_user = None
HOSTNAME = socket.gethostname()

TNSNAME_LOCAL_LISTENER = """
%s =
  (ADDRESS = (PROTOCOL = TCP)(HOST = %s)(PORT = %s))
"""

TEMPLATE_TNSNAMES = """
%s =
  (DESCRIPTION =
    (ADDRESS_LIST = %s
    )
      (CONNECT_DATA =
        (SERVER = DEDICATED)
        (SERVICE_NAME = %s)
      )
  )
"""

LISTENER_ENTRY = """
%s =
   (DESCRIPTION_LIST =
      (DESCRIPTION =
         (ADDRESS_LIST =
            (ADDRESS =
               (PROTOCOL = TCP)
               (HOST = %s)
               (PORT = %s)
               (IP = FIRST) )
         )
         (ADDRESS_LIST =
            (ADDRESS = (PROTOCOL = IPC) (KEY = EXTPROC) )
         )
      )
    )
"""

SID_LISTENER_ENTRY = """
SID_LIST_%s =
  (SID_LIST = %s
  )
"""

SID_LISTENER_DESC = """
    (SID_DESC =
      (GLOBAL_DBNAME=%s)
      (SID_NAME = %s)
      (ORACLE_HOME = """ + io_params['Oracle Home'] + r""")
    )
"""

TNSNAMES_ADDRESS = """
          (ADDRESS = (PROTOCOL = TCP)
                     (HOST = %s)
                     (PORT = %s) )
"""


#### Methods ####

def main():
    steplog.info('Setup Network Configuration on Primary and Standby Servers')
    set_defaults()

    get_listener_ports()

    steplog.info("ORACLE_HOME : %s" % ORACLE_HOME)
    steplog.info("tnsnames file location: %s" % tns_file_location)
    steplog.info("listener file location: %s" % lsnr_file_location)

    primary_hosts = PRIMARY_NODE_HOSTNAMES
    standby_hosts = STANDBY_NODE_HOSTNAMES
    # prime the status dict with True values
    status = {}  # key by host, boolean value
    for host in primary_hosts + standby_hosts:
        status[host] = True

    is_valid = update_tnsnames_all_nodes(primary_hosts, standby_hosts, status)
    if not is_valid:
        steplog.error('Error updating tnsnames on some host(s)')
        sys.exit(1)

    is_valid = update_listenerora_all_nodes(primary_hosts, standby_hosts, status)
    if not is_valid:
        steplog.error('Error updating listener.ora on some standby host(s)')
        sys.exit(1)

    # now, exit with a success code, if and only if there aren't any
    # False entries for any host in the status dict
    failures = [host for host in status.keys() if status[host] != True]
    if len(failures) > 0:
        sys.exit(1)

    set_params(params, standby_hosts[0])
    parametertools.print_header(params)
    steplog.info('Setup Network Configuration on Primary and Standby Servers successful.  You may proceed.')
    sys.exit(0)


def set_defaults():
    global tns_file_location, lsnr_file_location
    global asm_home, asm_user
    if not tns_file_location:
        tns_file_location = '%s/network/admin/tnsnames.ora' % ORACLE_HOME

    if not lsnr_file_location:
        if ASM_DISKGROUP:
            asm_home, asm_sid = oracletools.get_asm_info_from_oratab_file(ORATAB_FILE_LOCATION)
            if not asm_home:
                steplog.error('Unable to detect ASM entry in %s' % ORATAB_FILE_LOCATION)
                sys.exit(1)
            steplog.info('asm_home: %r' % asm_home)
            asm_user = ostools.get_file_owner(asm_home)
            steplog.info('asm_user: %r' % asm_user)
            lsnr_file_location = '%s/network/admin/listener.ora' % asm_home
        else:
            lsnr_file_location = '%s/network/admin/listener.ora' % ORACLE_HOME


def get_listener_ports():
    global primary_lsnr_port_num, standby_lsnr_port_num
    steplog.info('Attempt to get the primary db listener port and standby db listener port')

    primary_host = PRIMARY_NODE_HOSTNAMES[0]
    standby_host = STANDBY_NODE_HOSTNAMES[0]

    if ASM_DISKGROUP:
        p_lsnr_info = oracletools.fetch_listener(primary_host, HOSTNAME, asm_home)
        s_lsnr_info = oracletools.fetch_listener(standby_host, HOSTNAME, asm_home)
        primary_lsnr_port_num = p_lsnr_info['port']
        standby_lsnr_port_num = s_lsnr_info['port']
    else:
        primary_lsnr_port_num = oracletools.get_oracle_listener_port(oracle_home=ORACLE_HOME)
        standby_lsnr_port_num = oracletools.get_oracle_listener_port(oracle_home=ORACLE_HOME, host=standby_host)

    steplog.info('Found the listener port numbers')


def update_tnsnames_all_nodes(primary_hosts, standby_hosts, status):
    is_valid = True
    if ENV_TYPE == 'GRID_CLUSTER':
        standby_scan_name = oracletools.get_RAC_scan_name(ORACLE_HOME, standby_hosts[0], ORACLE_USER)
        primary_scan_name = oracletools.get_RAC_scan_name(ORACLE_HOME, primary_hosts[0], ORACLE_USER)
        primary_scan_port = get_scan_port(ORACLE_HOME, host=primary_hosts[0], user=ORACLE_USER)
        standby_scan_port = get_scan_port(ORACLE_HOME, host=standby_hosts[0], user=ORACLE_USER)
        standby_address_entries = TNSNAMES_ADDRESS % (standby_scan_name, standby_scan_port)
        primary_address_entries = TNSNAMES_ADDRESS % (primary_scan_name, primary_scan_port)
    else:
        standby_address_entries = [TNSNAMES_ADDRESS % (hostname, standby_lsnr_port_num) for hostname in standby_hosts]
        primary_address_entries = [TNSNAMES_ADDRESS % (hostname, primary_lsnr_port_num) for hostname in primary_hosts]
    augment_primary_db = TEMPLATE_TNSNAMES % (DB_UNIQUE_NAME, ''.join(primary_address_entries), DB_UNIQUE_NAME)
    augment_standby_db = TEMPLATE_TNSNAMES % (STANDBY_PREFIX + DB_UNIQUE_NAME, ''.join(standby_address_entries), SERVICE_NAME)
    augment = augment_primary_db + "\n" + augment_standby_db
    for host in primary_hosts + standby_hosts:
        steplog.debug('host: %r' % host)
        # check for pre-existing same database connection identifiers and delete if any
        # check first for the longer Database identifier (with prefix), cause the shorter regex will match the shorter config also
        connect_id_pattern = "%s\s*=\s*\(DESCRIPTION" % (STANDBY_PREFIX + DB_UNIQUE_NAME)
        removed = oracletools.remove_existing_network_config(tns_file_location, connect_id_pattern, host)
        # now we are getting perfectionists: remove multiple same database connect identifiers definitions, 
        # small chances that there will be, but still...
        while removed:
            removed = oracletools.remove_existing_network_config(tns_file_location, connect_id_pattern, host)
        connect_id_pattern = "%s\s*=\s*\(DESCRIPTION" % DB_UNIQUE_NAME
        removed = oracletools.remove_existing_network_config(tns_file_location, connect_id_pattern, host)
        while removed:
            removed = oracletools.remove_existing_network_config(tns_file_location, connect_id_pattern, host)
        steplog.debug('new tnsnames.ora content: %r' % augment)
        ok = ostools.write_file_remote(tns_file_location, augment, host, append=True)
        ostools.set_file_owner(tns_file_location, ORACLE_USER, host)
        if not ok:
            is_valid &= False
            status[host] = False
            steplog.error('Failed attempt to update tnsnames.ora with augment on %s' % host)
        if 'GRID' not in ENV_TYPE:
            lsnr_name = oracletools.get_oracle_listener_name(oracle_home=ORACLE_HOME)
            local_listener = TNSNAME_LOCAL_LISTENER % (lsnr_name, 'localhost', primary_lsnr_port_num)
            ok = ostools.write_file_remote(tns_file_location, local_listener, host, append=True)
            ostools.set_file_owner(tns_file_location, ORACLE_USER, host)
            if not ok:
                is_valid &= False
                status[host] = False
                steplog.error('Failed attempt to update tnsnames.ora with local_listener on %s' % host)
            oracletools.connect_and_run_sql("alter system set local_listener='%s' scope=both" % lsnr_name, 
                                            user_pass='/ as sysdba', oracle_home=ORACLE_HOME, oracle_sid=ORACLE_SID)
    return is_valid


def update_listenerora_all_nodes(primary_hosts, standby_hosts, status):
    is_valid = True
    #  Algorithm:
    #    If the Listener entry or LISTENER_SCAN1 entry are missing, add them.
    #  Next:
    #    For each line in the listener.ora file (or the defaults added) that
    #    starts with 'LISTENER' there must be a SID_LIST_%s % <that listener
    #    name> with the appropriate details.
    for index, host in enumerate(primary_hosts + standby_hosts):
        steplog.debug('host: %r' % host)
        if host in standby_hosts:
            n = index + 1 - len(primary_hosts)
            prefix_sid_listener = STANDBY_PREFIX
        else:
            n = index + 1
            prefix_sid_listener = ''
        if ENV_TYPE == 'GRID_CLUSTER':
            instance = ORACLE_SID[:-1] + str(n)
        else:
            instance = ORACLE_SID
        
        listener_lines = []
        amended_content = []

        catter = '/bin/cat %s' % lsnr_file_location
        out, err, rc = ostools.run_command(catter, host=host)
        if rc != 0:
            steplog.error('Failed to execute %s command on server %s' % (catter, host))
            is_valid = False
            status[host] = False
        else:
            lf_lines = out.split('\n')
            listener_lines = [line for line in lf_lines if line.strip()
                              and not line.startswith('ADR_BASE') and not line.startswith('SID_LIST')
                              and line[0] not in [' ', '#']]
        # Add defaults, unless there was an error executing the command above
        if len(listener_lines) == 0 and is_valid:
            listener_augment = LISTENER_ENTRY % ('LISTENER', DB_UNIQUE_NAME, ORACLE_SID)
            default_scan_lsnr_augment = LISTENER_ENTRY % ('LISTENER_SCAN1', DB_UNIQUE_NAME, ORACLE_SID)
            steplog.debug('No listener information found in listener.ora on host %s' % host)
            # Add default, add it to the listener lines too so that
            # sid_list_listener lines get created as well.
            amended_content.append(listener_augment)
            listener_lines.append(listener_augment)
            # TO RE-EVALUATE !!!!
            if ENV_TYPE == 'GRID_CLUSTER':
                amended_content.append(default_scan_lsnr_augment)
                listener_lines.append(default_scan_lsnr_augment)

        for line in listener_lines:
            line_items = [x.strip() for x in line.split('=')]
            lsnr_name = line_items[0]
            steplog.debug('lsnr_name: %r' % lsnr_name)
            dg_broker_desc = SID_LISTENER_DESC % ("%s%s_DGMGRL" % (prefix_sid_listener, DB_UNIQUE_NAME), "%s%s" % (prefix_sid_listener, instance))
            instance_desc = SID_LISTENER_DESC % ("%s%s" % (prefix_sid_listener, DB_UNIQUE_NAME), "%s%s" % (prefix_sid_listener, instance))
            s_lsnr_augment = SID_LISTENER_ENTRY % (lsnr_name, dg_broker_desc + instance_desc)

            # remove any already existing same SID_LIST_LISTENER entry of the corresponding listener in listener.ora file
            sid_list_listener_pattern = "SID_LIST_%s\s*=\s*\(SID_LIST" % lsnr_name
            removed = oracletools.remove_existing_network_config(lsnr_file_location, sid_list_listener_pattern, host)
            while removed:
                removed = oracletools.remove_existing_network_config(lsnr_file_location, sid_list_listener_pattern, host)
            # add this entry to listener.ora file
            amended_content.append(s_lsnr_augment)

        ok = True
        if len(amended_content) > 0:
            ok = ostools.write_file_remote(lsnr_file_location, '\n'.join(amended_content), host, append=True)
            if asm_user:
                ostools.set_file_owner(lsnr_file_location, asm_user, host)
            else:
                ostools.set_file_owner(lsnr_file_location, ORACLE_USER, host)
        if not ok or not is_valid:
            status[host] = False
            is_valid = False
            steplog.error('Failed attempt to augment listener.ora on host %r' % host)
    return is_valid


def set_params(params, host):
    if ENV_TYPE == 'GRID_CLUSTER':
        # get the scan name of the standby server
        standby_scan_name = oracletools.get_RAC_scan_name(ORACLE_HOME, host, ORACLE_USER)
        standby_scan_port = get_scan_port(ORACLE_HOME, host=STANDBY_NODE_HOSTNAMES[0], user=ORACLE_USER)
        remote_listener = standby_scan_name + ":" + str(standby_scan_port)
        params['Primary DB Listener Name'] = oracletools.get_oracle_listener_name(oracle_home=asm_home)
        params['Standby DB Listener Name'] = oracletools.get_oracle_listener_name(oracle_home=asm_home, host=host)
    else:
        remote_listener = STANDBY_NODE_HOSTNAMES[0] + ":" + str(standby_lsnr_port_num)
        params['Primary DB Listener Name'] = oracletools.get_oracle_listener_name(oracle_home=ORACLE_HOME)
        params['Standby DB Listener Name'] = oracletools.get_oracle_listener_name(oracle_home=ORACLE_HOME, host=host)
    params['Primary DB Listener Port Number'] = primary_lsnr_port_num

    params['Standby DB Listener Port Number'] = standby_lsnr_port_num
    params['Remote Listener'] = remote_listener
    return


def get_scan_port(oracle_home, host=None, user=None):
    """
    Gets the RAC scan name
    """
    env_str = oracletools.get_oracle_env_string(oracle_home)
    if host:
        command = 'ssh %s "%s; %s/bin/srvctl config scan_listener"' % (host, env_str, oracle_home)
    else:
        command = "%s; %s/bin/srvctl config scan_listener" % (env_str, oracle_home)
    if user:
        output, err, rc = ostools.sudo_run_command(command, user=user)
    else:
        output, err, rc = ostools.run_command(command)
    if rc != 0:
        raise ValueError('Unable to run srvctl config scan command')
    m = re.search("TCP:(.*)", output, re.IGNORECASE)
    if not m:
        raise ValueError('Unable to find scan port')
    steplog.debug("RAC Scan name = %s" % m.group(1))
    return m.group(1)


#### Call to main() ####

if __name__ == '__main__':
    try:
        main()
    except StandardError, e:
        steplog.handle_exception(e)
