__version__ = '$Revision: 43161 $'

#### Python/Jython Imports ####
import sys
import os
import re
from java.lang import System


#### DMA Imports ####
import parametertools
import pythontools
import steplog


io_params = parametertools.parse_dma_params()

#### Parameter Inputs ####
ASM_PASSWORD = io_params['ASM Password'].strip()
DATABASE_NAME = io_params['Database Name'].strip()
LISTENER_NAME = io_params['Listener Name'].strip()
TEMPLATE_NAME = io_params['DBCA Template Name'].strip()
response_dbca = io_params['DBCA Response File'].strip()
VARIABLES_FILE = io_params['Variables File'].strip()
DATAFILE_LOCATION = io_params['Datafile Location'].strip()
default_system_password = "manager"
RAC_ONE_NODE = io_params['RAC One Node'].strip()
RAC_ONE_NODE_SERVICE_NAME = io_params['RAC One Node Service Name'].strip()
POLICY_MANAGED = io_params['Policy Managed'].strip()
CRS_HOME = io_params['CRS Home'].strip()
NODE_LIST = io_params['Cluster Nodes'].strip()
DBCA_PASSWORD_ALL = io_params['DBCA Password ALL'].strip()
DBCA_PASSWORD_DBSNMP = io_params['DBCA Password DBSNMP'].strip()
DBCA_PASSWORD_SYS = io_params['DBCA Password SYS'].strip()
DBCA_PASSWORD_SYSTEM = io_params['DBCA Password SYSTEM'].strip()
DBCA_PASSWORD_SYSMAN = io_params['DBCA Password SYSMAN'].strip()
DBCA_CHARSET = io_params['DBCA Character Set'].strip()
DBCA_NATIONAL_CHARSET = io_params['DBCA National Character Set'].strip()
ORACLE_VERSION = io_params['Oracle Version'].strip()
CONTAINER_DATABASE = pythontools.bool_parameter(io_params['Container Database'].strip())
FRA_LOC = io_params['FRA Location'].strip()
ORACLE_SID = io_params['Oracle SID'].strip()


def node(x):
    return x.strip().split(".")[0]

NODE_LIST = ",".join(filter(bool, map(node, NODE_LIST.split(','))))


#### Methods ####

def main():
    global response_dbca
    storage_type = ""
    datafile_info = ""

    if DATAFILE_LOCATION:
        datafile_info, storage_type = get_datafile_and_storage()

    policy_params = ''
    if POLICY_MANAGED.lower() == 'true' and CRS_HOME:
        policy_params = get_policy_params()

    pwd_info = get_password_settings()
    #Added two lines for test purpose-sylesh
    print "Till here the value is passed"
    print DBCA_CHARSET
    charset = 'US7ASCII'
    if DBCA_CHARSET:
        charset = DBCA_CHARSET
        # Adding this line to test- sylesh
        print charset

    national_charset = 'UTF8'
    if DBCA_NATIONAL_CHARSET:
        national_charset = DBCA_NATIONAL_CHARSET

    container_params = get_container_params()

    default_response_file = get_default_response(policy_params, datafile_info,
                                                 storage_type, pwd_info,
                                                 charset, national_charset,
                                                 container_params)
    if response_dbca:
        # If the template exists, use it.
        steplog.info("Using existing response file %s" % response_dbca)
        modify_response(response_dbca)
    else:
        # If the response file does not exist, create it.
        steplog.info("Creating a new DBCA response file.")
        response_dbca = os.path.join(System.getProperty("java.io.tmpdir"), "%sDBCA.rsp" % DATABASE_NAME)
        create_response(default_response_file, response_dbca)

    print_header()
    sys.exit(0)


def get_datafile_and_storage():
    if DATAFILE_LOCATION[0] == '+':
        storage_type = 'STORAGETYPE=ASM\nASM_SYS_PASSWORD= "%s"' % ASM_PASSWORD
        datafile_info = 'DISKGROUPNAME = "%s"' % DATAFILE_LOCATION[1:]
    elif NODE_LIST:
        datafile_info = 'DATAFILEDESTINATION = "%s"' % DATAFILE_LOCATION
        if DATAFILE_LOCATION.startswith('/dev') or DATAFILE_LOCATION.startswith('/raw'):
            storage_type = "STORAGETYPE=RAW"
        else:
            storage_type = "STORAGETYPE=CFS"
    else:
        datafile_info = 'DATAFILEDESTINATION = "%s"' % DATAFILE_LOCATION
        storage_type = "STORAGETYPE=FS"
    return datafile_info, storage_type


def get_policy_params():
    #verify if a server pool already exists -> srvctl status srvpool
    command = os.path.join(CRS_HOME, "bin", "srvctl")
    steplog.info("Running command %s" % command + " status srvpool")
    status_srvpool = os.popen(command + " status srvpool").read()
    steplog.info("Srvpool status: %s" % status_srvpool)
    matches = re.finditer('Server pool name: (.*)', status_srvpool)
    server_pools = [match.group(1) for match in matches if match.group(1) not in ("Free", "Generic")]
    srvpool_name = "%sClusterPool" % NODE_LIST.split(',')[0][0:4]
    if len(server_pools) == 0:
        steplog.info("No server pool exists on the system.")
        steplog.info("%s server pool will be created." % srvpool_name)
        create_srvpool = "true"
    else:
        steplog.info("%d server pools found on the system." % len(server_pools))
        steplog.info("%s server pool will be used." % server_pools[0])
        create_srvpool = "false"
        srvpool_name = server_pools[0]
    return """CREATESERVERPOOL = "%s"
FORCE = "false"
SERVERPOOLNAME = %s
CARDINALITY = %d""" % (create_srvpool, srvpool_name, len(NODE_LIST.split(',')))


def get_password_settings():
    pwd_info = ""

    if not pythontools.is_dma_param_null(DBCA_PASSWORD_ALL):
        pwd_info += "SYSPASSWORD = %s\n" % DBCA_PASSWORD_ALL
    elif pythontools.is_dma_param_null(DBCA_PASSWORD_SYS):
        pwd_info += "SYSPASSWORD = %s\n" % default_system_password
    else:
        pwd_info += "SYSPASSWORD = %s\n" % DBCA_PASSWORD_SYS

    if not pythontools.is_dma_param_null(DBCA_PASSWORD_ALL):
        pwd_info += "SYSTEMPASSWORD = %s" % DBCA_PASSWORD_ALL
    elif pythontools.is_dma_param_null(DBCA_PASSWORD_SYSTEM):
        pwd_info += "SYSTEMPASSWORD = %s" % default_system_password
    else:
        pwd_info += "SYSTEMPASSWORD = %s" % DBCA_PASSWORD_SYSTEM

    if not pythontools.is_dma_param_null(DBCA_PASSWORD_ALL):
        pwd_info += "\nSYSMANPASSWORD = %s" % DBCA_PASSWORD_ALL
    elif not pythontools.is_dma_param_null(DBCA_PASSWORD_SYSMAN):
        pwd_info += "\nSYSMANPASSWORD = %s" % DBCA_PASSWORD_SYSMAN

    if not pythontools.is_dma_param_null(DBCA_PASSWORD_ALL):
        pwd_info += "\nDBSNMPPASSWORD = %s" % DBCA_PASSWORD_ALL
    elif not pythontools.is_dma_param_null(DBCA_PASSWORD_DBSNMP):
        pwd_info += "\nDBSNMPPASSWORD = %s" % DBCA_PASSWORD_DBSNMP
    return pwd_info


def get_container_params():
    special = "#"
    template = "%sCREATEASCONTAINERDATABASE=\"%s\""
    if not CONTAINER_DATABASE:
        return template % (special, "")
    return template % ("", "true")


def get_default_response(policy_params, datafile_info, storage_type, pwd_info,
                         charset, national_charset, container_params):
    return """[GENERAL]
RESPONSEFILE_VERSION = "%s"
OPERATION_TYPE = "createDatabase"
CREATE_TYPE = "createDatabase"
[CREATEDATABASE]
GDBNAME = "%s"
RACONENODE  = "%s"
RACONENODESERVICENAME = "%s"
POLICYMANAGED = "%s"
%s
NODELIST = "%s"
TEMPLATENAME = "%s"
EMCONFIGURATION = "NONE"
%s
%s
%s
CHARACTERSET = "%s"
NATIONALCHARACTERSET= "%s"
LISTENERS = "%s"
MEMORYPERCENTAGE = "40"
DATABASETYPE = "MULTIPURPOSE"
ISEARCH="false"
OMS="false"
SPATIAL="false"
ODM="false"
IMEDIA="false"
ORACLE_TEXT="false"
XDB_PROTOCOLS="false"
CWMLITE="false"
SAMPLE_SCHEMA="false"
%s
""" % (ORACLE_VERSION, DATABASE_NAME, RAC_ONE_NODE, RAC_ONE_NODE_SERVICE_NAME, POLICY_MANAGED, policy_params, NODE_LIST, TEMPLATE_NAME, datafile_info, storage_type, pwd_info, charset, national_charset, format_listener(LISTENER_NAME, NODE_LIST), container_params)


def format_listener(listener_name, node_list):
    if node_list:
        listener_list = None
        for node in node_list.split(','):
            if listener_list:
                listener_list += " %s_%s" % (listener_name.upper(), node.strip().upper())
            else:
                listener_list = "%s_%s" % (listener_name.upper(), node.strip().upper())
        return listener_list
    else:
        return listener_name.upper()


def create_response(default_response_file, file_name):
    fh = open(file_name, 'w')
    for line in default_response_file.splitlines():
        if line.upper().startswith('NODELIST'):
            if NODE_LIST:
                fh.write(line + '\n')
        else:
            fh.write(line + '\n')
    fh.close()


def modify_response(file_name):
    response = open(file_name, "r")
    lines = response.readlines()
    response.close()
    response = open(file_name, "w")

    for line in lines:
        if line.upper().startswith('GDBNAME'):
            steplog.info("Updating GDBNAME in %s." % file_name)
            response.write('GDBNAME = "%s"\n' % DATABASE_NAME)        
        elif line.upper().startswith('SID'):
            steplog.info("Updating SID in %s." % file_name)
            response.write('SID = "%s"\n' % ORACLE_SID)
        elif line.upper().startswith('NODELIST'):
            steplog.info("Updating NODELIST in %s." % file_name)
            if NODE_LIST:
                response.write('NODELIST = "%s"\n' % NODE_LIST)
        elif line.upper().startswith('SYSTEMPASSWORD'):
            if pythontools.is_dma_param_null(DBCA_PASSWORD_SYSTEM):
                system_password = line.split('=')[1].strip().strip('"')
                response.write('SYSTEMPASSWORD = "%s"\n' % system_password)
            else:
                response.write('SYSTEMPASSWORD = "%s"\n' % DBCA_PASSWORD_SYSTEM)
        elif line.upper().startswith('TEMPLATENAME'):
            if TEMPLATE_NAME:
                steplog.info("Updating TEMPLATENAME in %s." % file_name)
                response.write('TEMPLATENAME = "%s"\n' % TEMPLATE_NAME)
            else:
                response.write(line)
        elif line.upper().startswith('VARIABLESFILE'):
            if VARIABLES_FILE:
                steplog.info("Updating VARIABLESFILE in %s." % file_name)
                response.write('VARIABLESFILE = "%s"\n' % VARIABLES_FILE)
            else:
                response.write(line)
        elif line.upper().startswith('CREATEASCONTAINERDATABASE'):
            if CONTAINER_DATABASE:
                steplog.info("Updating CREATEASCONTAINERDATABASE in %s." % file_name)
                response.write('CREATEASCONTAINERDATABASE="true"\n')
            else:
                response.write(line)        
        else:
            response.write(line)
    response.close()
    steplog.info("Success.")


def print_header():
    system_password = default_system_password
    if not pythontools.is_dma_param_null(DBCA_PASSWORD_ALL):
        system_password = DBCA_PASSWORD_ALL
    elif not pythontools.is_dma_param_null(DBCA_PASSWORD_SYSTEM):
        system_password = DBCA_PASSWORD_SYSTEM
    parametertools.print_header({
        'DBCA Response File': response_dbca .encode('ascii'),
        'System Password': system_password,
        'System Username': 'SYSTEM',
        'FRA Location': FRA_LOC,    
    })


if __name__ == '__main__':
    try:
        main()
    except StandardError, e:
        steplog.handle_exception(e)