09 May 13:04 - 09 May 13:05Exit: 0Server: defreou0977.eontstmpc.svcs.hpe.com, Instance: EONB12, Database: EONTSTP
  [DEBUG]: Creating directory (/oracle/recovery_area/SEONTSTP)
  [DEBUG]: Checking if directory (u'/oracle/recovery_area/SEONTSTP') exists
  [DEBUG]: Running command: ssh defreou0978.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/recovery_area/SEONTSTP
  [DEBUG]: stdout = 
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [.....]: /bin/ls: cannot access /oracle/recovery_area/SEONTSTP: No such file or directory
  [DEBUG]: rc = 2
  [DEBUG]: Checking if directory (u'/oracle/recovery_area') exists
  [DEBUG]: Running command: ssh defreou0978.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/recovery_area
  [DEBUG]: stdout = /oracle/recovery_area
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [DEBUG]: rc = 0
  [DEBUG]: Running command: id -a oracle
  [DEBUG]: stdout = uid=600(oracle) gid=1100(oinstall) groups=1100(oinstall),1101(dba),1102(oper)
  [DEBUG]: stderr = 
  [DEBUG]: rc = 0
  [DEBUG]: Group for user oracle:  'oinstall'
  [DEBUG]: Running command: ssh defreou0978 /bin/mkdir -p -m 755 /oracle/recovery_area/SEONTSTP;ssh defreou0978 /bin/chown oracle:oinstall /oracle/recovery_area/SEONTSTP
  [DEBUG]: stdout = 
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [.....]: +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [DEBUG]: rc = 0
  [DEBUG]: Checking if directory (u'/oracle/recovery_area/SEONTSTP') exists
  [DEBUG]: Running command: ssh defreou0978.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/recovery_area/SEONTSTP
  [DEBUG]: stdout = /oracle/recovery_area/SEONTSTP
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [DEBUG]: rc = 0
  [INFO]: Directory /oracle/recovery_area/SEONTSTP created on host defreou0978.eontstmpc.svcs.hpe.com.
  [DEBUG]: Creating directory (/oracle/oradata/SEONTSTP)
  [DEBUG]: Checking if directory (u'/oracle/oradata/SEONTSTP') exists
  [DEBUG]: Running command: ssh defreou0978.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/oradata/SEONTSTP
  [DEBUG]: stdout = 
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [.....]: /bin/ls: cannot access /oracle/oradata/SEONTSTP: No such file or directory
  [DEBUG]: rc = 2
  [DEBUG]: Checking if directory (u'/oracle/oradata') exists
  [DEBUG]: Running command: ssh defreou0978.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/oradata
  [DEBUG]: stdout = /oracle/oradata
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [DEBUG]: rc = 0
  [DEBUG]: Running command: id -a oracle
  [DEBUG]: stdout = uid=600(oracle) gid=1100(oinstall) groups=1100(oinstall),1101(dba),1102(oper)
  [DEBUG]: stderr = 
  [DEBUG]: rc = 0
  [DEBUG]: Group for user oracle:  'oinstall'
  [DEBUG]: Running command: ssh defreou0978 /bin/mkdir -p -m 755 /oracle/oradata/SEONTSTP;ssh defreou0978 /bin/chown oracle:oinstall /oracle/oradata/SEONTSTP
  [DEBUG]: stdout = 
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [.....]: +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [DEBUG]: rc = 0
  [DEBUG]: Checking if directory (u'/oracle/oradata/SEONTSTP') exists
  [DEBUG]: Running command: ssh defreou0978.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/oradata/SEONTSTP
  [DEBUG]: stdout = /oracle/oradata/SEONTSTP
  [DEBUG]: stderr = +---------------------------------------------------------------------+
  [.....]: |                                                                     |
  [.....]: |  This computing system is a company owned asset and provided for    |
  [.....]: |  the exclusive use of authorized personnel for business purposes.   |
  [.....]: |  All information and data created, accessed, processed or stored    |
  [.....]: |  using this system (including personal information) are subject to  |
  [.....]: |  monitoring, auditing or review to the extent permitted by          |
  [.....]: |  applicable law. Unauthorized use or abuse of this system may lead  |
  [.....]: |  to corrective action including termination of employment, civil    |
  [.....]: |  and/or criminal penalties.                                         |
  [.....]: |                                                                     |
  [.....]: +---------------------------------------------------------------------+
  [DEBUG]: rc = 0
  [INFO]: Directory /oracle/oradata/SEONTSTP created on host defreou0978.eontstmpc.svcs.hpe.com.
  [DEBUG]: value is set for data_file_name_convert and data_file_name_convert2 because the value is not set
  [DEBUG]: value is set for data_file_name_convert and data_file_name_convert2 because the value is not set
  [DEBUG]: RMAN input: 
  [.....]: RUN {
  [.....]: ALLOCATE CHANNEL d1 TYPE DISK;
  [.....]: ALLOCATE CHANNEL d2 TYPE DISK;
  [.....]: 
  [.....]: ALLOCATE AUXILIARY CHANNEL cnv1 TYPE DISK;
  [.....]: ALLOCATE AUXILIARY CHANNEL cnv2 TYPE DISK;
  [.....]: 
  [.....]: CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/recovery_area/EONTSTP/snapcf_EONB12.f';
  [.....]: DUPLICATE TARGET DATABASE
  [.....]:     FOR STANDBY
  [.....]:     FROM ACTIVE DATABASE
  [.....]:     DORECOVER
  [.....]:     SPFILE
  [.....]:         SET instance_number='1'
  [.....]:         SET db_unique_name='SEONTSTP'
  [.....]:         SET control_files='/oracle/recovery_area/SEONTSTP/control01.dbf'
  [.....]:         SET db_file_name_convert='/oracle/recovery_area/EONTSTP', '/oracle/recovery_area/SEONTSTP'
  [.....]:         SET db_file_name_convert='/oracle/oradata/EONTSTP', '/oracle/oradata/SEONTSTP'
  [.....]:         SET log_file_name_convert='/oracle/recovery_area/EONTSTP', '/oracle/recovery_area/SEONTSTP'
  [.....]:         SET log_file_name_convert='/oracle/oradata/EONTSTP', '/oracle/oradata/SEONTSTP'
  [.....]:         SET log_archive_dest_1='location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SEONTSTP'
  [.....]:         SET log_archive_dest_2='service=EONTSTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=EONTSTP'
  [.....]:         SET Audit_File_Dest='/oracle/admin/SEONTSTP/adump'
  [.....]:         SET fal_client='SEONTSTP'
  [.....]:         SET fal_server='EONTSTP'
  [.....]:         SET standby_file_management='AUTO'
  [.....]:         SET archive_lag_target='600'
  [.....]:         SET remote_listener=''
  [.....]:         SET log_archive_config='dg_config=(EONTSTP,SEONTSTP)'
  [.....]:         SET remote_login_passwordfile='EXCLUSIVE'
  [.....]:     NOFILENAMECHECK;
  [.....]: }
  [DEBUG]: Running command: ORACLE_HOME=/oracle/11.2.0.4; export ORACLE_HOME; LD_LIBRARY_PATH=/oracle/11.2.0.4/lib; export LD_LIBRARY_PATH; SHLIB_PATH=/oracle/11.2.0.4/lib; export SHLIB_PATH; ORACLE_SID=EONB12; export ORACLE_SID; /oracle/11.2.0.4/bin/rman target sys/*** auxiliary sys/***@SEONTSTP
  [DEBUG]: stdin = 
  [.....]: RUN {
  [.....]: ALLOCATE CHANNEL d1 TYPE DISK;
  [.....]: ALLOCATE CHANNEL d2 TYPE DISK;
  [.....]: 
  [.....]: ALLOCATE AUXILIARY CHANNEL cnv1 TYPE DISK;
  [.....]: ALLOCATE AUXILIARY CHANNEL cnv2 TYPE DISK;
  [.....]: 
  [.....]: CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/recovery_area/EONTSTP/snapcf_EONB12.f';
  [.....]: DUPLICATE TARGET DATABASE
  [.....]:     FOR STANDBY
  [.....]:     FROM ACTIVE DATABASE
  [.....]:     DORECOVER
  [.....]:     SPFILE
  [.....]:         SET instance_number='1'
  [.....]:         SET db_unique_name='SEONTSTP'
  [.....]:         SET control_files='/oracle/recovery_area/SEONTSTP/control01.dbf'
  [.....]:         SET db_file_name_convert='/oracle/recovery_area/EONTSTP', '/oracle/recovery_area/SEONTSTP'
  [.....]:         SET db_file_name_convert='/oracle/oradata/EONTSTP', '/oracle/oradata/SEONTSTP'
  [.....]:         SET log_file_name_convert='/oracle/recovery_area/EONTSTP', '/oracle/recovery_area/SEONTSTP'
  [.....]:         SET log_file_name_convert='/oracle/oradata/EONTSTP', '/oracle/oradata/SEONTSTP'
  [.....]:         SET log_archive_dest_1='location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SEONTSTP'
  [.....]:         SET log_archive_dest_2='service=EONTSTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=EONTSTP'
  [.....]:         SET Audit_File_Dest='/oracle/admin/SEONTSTP/adump'
  [.....]:         SET fal_client='SEONTSTP'
  [.....]:         SET fal_server='EONTSTP'
  [.....]:         SET standby_file_management='AUTO'
  [.....]:         SET archive_lag_target='600'
  [.....]:         SET remote_listener=''
  [.....]:         SET log_archive_config='dg_config=(EONTSTP,SEONTSTP)'
  [.....]:         SET remote_login_passwordfile='EXCLUSIVE'
  [.....]:     NOFILENAMECHECK;
  [.....]: }
  [DEBUG]: stdout = 
  [.....]: Recovery Manager: Release 11.2.0.4.0 - Production on Tue May 9 11:04:26 2017
  [.....]: 
  [.....]: Copyright (c) 1982, 2011, Oracle and/or its affiliates.  All rights reserved.
  [.....]: 
  [.....]: connected to target database: EONTSTP (DBID=1744319367)
  [.....]: connected to auxiliary database: SEONTSTP (not mounted)
  [.....]: 
  [.....]: RMAN> 
  [.....]: RMAN> 2> 3> 4> 5> 6> 7> 8> 9> 10> 11> 12> 13> 14> 15> 16> 17> 18> 19> 20> 21> 22> 23> 24> 25> 26> 27> 28> 29> 30> 31> 32> 
  [.....]: using target database control file instead of recovery catalog
  [.....]: allocated channel: d1
  [.....]: channel d1: SID=181 device type=DISK
  [.....]: 
  [.....]: allocated channel: d2
  [.....]: channel d2: SID=196 device type=DISK
  [.....]: 
  [.....]: allocated channel: cnv1
  [.....]: channel cnv1: SID=266 device type=DISK
  [.....]: 
  [.....]: allocated channel: cnv2
  [.....]: channel cnv2: SID=332 device type=DISK
  [.....]: 
  [.....]: new RMAN configuration parameters:
  [.....]: CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/recovery_area/EONTSTP/snapcf_EONB12.f';
  [.....]: new RMAN configuration parameters are successfully stored
  [.....]: 
  [.....]: Starting Duplicate Db at 09-MAY-17
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    backup as copy reuse
  [.....]:    targetfile  '/oracle/11.2.0.4/dbs/orapwEONB12' auxiliary format 
  [.....]:  '/oracle/11.2.0.4/dbs/orapwSEONB12'   targetfile 
  [.....]:  '/oracle/11.2.0.4/dbs/spfileEONB12.ora' auxiliary format 
  [.....]:  '/oracle/11.2.0.4/dbs/spfileSEONB12.ora'   ;
  [.....]:    sql clone "alter system set spfile= ''/oracle/11.2.0.4/dbs/spfileSEONB12.ora''";
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: Starting backup at 09-MAY-17
  [.....]: Finished backup at 09-MAY-17
  [.....]: 
  [.....]: sql statement: alter system set spfile= ''/oracle/11.2.0.4/dbs/spfileSEONB12.ora''
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    sql clone "alter system set  instance_number = 
  [.....]:  1 comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  db_unique_name = 
  [.....]:  ''SEONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  control_files = 
  [.....]:  ''/oracle/recovery_area/SEONTSTP/control01.dbf'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  db_file_name_convert = 
  [.....]:  ''/oracle/recovery_area/EONTSTP'', ''/oracle/recovery_area/SEONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  db_file_name_convert = 
  [.....]:  ''/oracle/oradata/EONTSTP'', ''/oracle/oradata/SEONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_file_name_convert = 
  [.....]:  ''/oracle/recovery_area/EONTSTP'', ''/oracle/recovery_area/SEONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_file_name_convert = 
  [.....]:  ''/oracle/oradata/EONTSTP'', ''/oracle/oradata/SEONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_archive_dest_1 = 
  [.....]:  ''location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SEONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_archive_dest_2 = 
  [.....]:  ''service=EONTSTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=EONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  Audit_File_Dest = 
  [.....]:  ''/oracle/admin/SEONTSTP/adump'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  fal_client = 
  [.....]:  ''SEONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  fal_server = 
  [.....]:  ''EONTSTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  standby_file_management = 
  [.....]:  ''AUTO'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  archive_lag_target = 
  [.....]:  600 comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  remote_listener = 
  [.....]:  '''' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_archive_config = 
  [.....]:  ''dg_config=(EONTSTP,SEONTSTP)'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  remote_login_passwordfile = 
  [.....]:  ''EXCLUSIVE'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    shutdown clone immediate;
  [.....]:    startup clone nomount;
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: sql statement: alter system set  instance_number =  1 comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  db_unique_name =  ''SEONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  control_files =  ''/oracle/recovery_area/SEONTSTP/control01.dbf'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  db_file_name_convert =  ''/oracle/recovery_area/EONTSTP'', ''/oracle/recovery_area/SEONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  db_file_name_convert =  ''/oracle/oradata/EONTSTP'', ''/oracle/oradata/SEONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_file_name_convert =  ''/oracle/recovery_area/EONTSTP'', ''/oracle/recovery_area/SEONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_file_name_convert =  ''/oracle/oradata/EONTSTP'', ''/oracle/oradata/SEONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_archive_dest_1 =  ''location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SEONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_archive_dest_2 =  ''service=EONTSTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=EONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  Audit_File_Dest =  ''/oracle/admin/SEONTSTP/adump'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  fal_client =  ''SEONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  fal_server =  ''EONTSTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  standby_file_management =  ''AUTO'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  archive_lag_target =  600 comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  remote_listener =  '''' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_archive_config =  ''dg_config=(EONTSTP,SEONTSTP)'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  remote_login_passwordfile =  ''EXCLUSIVE'' comment= '''' scope=spfile
  [.....]: 
  [.....]: Oracle instance shut down
  [.....]: 
  [.....]: connected to auxiliary database (not started)
  [.....]: Oracle instance started
  [.....]: 
  [.....]: Total System Global Area    7499329536 bytes
  [.....]: 
  [.....]: Fixed Size                     2267832 bytes
  [.....]: Variable Size               1358955848 bytes
  [.....]: Database Buffers            6123683840 bytes
  [.....]: Redo Buffers                  14422016 bytes
  [.....]: allocated channel: cnv1
  [.....]: channel cnv1: SID=114 device type=DISK
  [.....]: allocated channel: cnv2
  [.....]: channel cnv2: SID=130 device type=DISK
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    backup as copy current controlfile for standby auxiliary format  '/oracle/recovery_area/SEONTSTP/control01.dbf';
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: Starting backup at 09-MAY-17
  [.....]: channel d1: starting datafile copy
  [.....]: copying standby control file
  [.....]: output file name=/oracle/recovery_area/EONTSTP/snapcf_EONB12.f tag=TAG20170509T110438 RECID=1 STAMP=943527878
  [.....]: channel d1: datafile copy complete, elapsed time: 00:00:01
  [.....]: Finished backup at 09-MAY-17
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    sql clone 'alter database mount standby database';
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: sql statement: alter database mount standby database
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    set newname for tempfile  1 to 
  [.....]:  "/oracle/oradata/SEONTSTP/temp01.dbf";
  [.....]:    switch clone tempfile all;
  [.....]:    set newname for datafile  1 to 
  [.....]:  "/oracle/oradata/SEONTSTP/system01.dbf";
  [.....]:    set newname for datafile  2 to 
  [.....]:  "/oracle/oradata/SEONTSTP/sysaux01.dbf";
  [.....]:    set newname for datafile  3 to 
  [.....]:  "/oracle/oradata/SEONTSTP/undotbs01.dbf";
  [.....]:    set newname for datafile  4 to 
  [.....]:  "/oracle/oradata/SEONTSTP/users01.dbf";
  [.....]:    backup as copy reuse
  [.....]:    datafile  1 auxiliary format 
  [.....]:  "/oracle/oradata/SEONTSTP/system01.dbf"   datafile 
  [.....]:  2 auxiliary format 
  [.....]:  "/oracle/oradata/SEONTSTP/sysaux01.dbf"   datafile 
  [.....]:  3 auxiliary format 
  [.....]:  "/oracle/oradata/SEONTSTP/undotbs01.dbf"   datafile 
  [.....]:  4 auxiliary format 
  [.....]:  "/oracle/oradata/SEONTSTP/users01.dbf"   ;
  [.....]:    sql 'alter system archive log current';
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: executing command: SET NEWNAME
  [.....]: 
  [.....]: renamed tempfile 1 to /oracle/oradata/SEONTSTP/temp01.dbf in control file
  [.....]: 
  [.....]: executing command: SET NEWNAME
  [.....]: 
  [.....]: executing command: SET NEWNAME
  [.....]: 
  [.....]: executing command: SET NEWNAME
  [.....]: 
  [.....]: executing command: SET NEWNAME
  [.....]: 
  [.....]: Starting backup at 09-MAY-17
  [.....]: channel d1: starting datafile copy
  [.....]: input datafile file number=00001 name=/oracle/oradata/EONTSTP/system01.dbf
  [.....]: channel d2: starting datafile copy
  [.....]: input datafile file number=00002 name=/oracle/oradata/EONTSTP/sysaux01.dbf
  [.....]: output file name=/oracle/oradata/SEONTSTP/system01.dbf tag=TAG20170509T110447
  [.....]: channel d1: datafile copy complete, elapsed time: 00:00:07
  [.....]: channel d1: starting datafile copy
  [.....]: input datafile file number=00003 name=/oracle/oradata/EONTSTP/undotbs01.dbf
  [.....]: output file name=/oracle/oradata/SEONTSTP/sysaux01.dbf tag=TAG20170509T110447
  [.....]: channel d2: datafile copy complete, elapsed time: 00:00:07
  [.....]: channel d2: starting datafile copy
  [.....]: input datafile file number=00004 name=/oracle/oradata/EONTSTP/users01.dbf
  [.....]: output file name=/oracle/oradata/SEONTSTP/undotbs01.dbf tag=TAG20170509T110447
  [.....]: channel d1: datafile copy complete, elapsed time: 00:00:01
  [.....]: output file name=/oracle/oradata/SEONTSTP/users01.dbf tag=TAG20170509T110447
  [.....]: channel d2: datafile copy complete, elapsed time: 00:00:01
  [.....]: Finished backup at 09-MAY-17
  [.....]: 
  [.....]: sql statement: alter system archive log current
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    backup as copy reuse
  [.....]:    archivelog like  "/oracle/recovery_area/1_9_943527049.dbf" auxiliary format 
  [.....]:  "/oracle/recovery_area/1_9_943527049.dbf"   archivelog like 
  [.....]:  "/oracle/recovery_area/1_8_943527049.dbf" auxiliary format 
  [.....]:  "/oracle/recovery_area/1_8_943527049.dbf"   ;
  [.....]:    catalog clone archivelog  "/oracle/recovery_area/1_9_943527049.dbf";
  [.....]:    catalog clone archivelog  "/oracle/recovery_area/1_8_943527049.dbf";
  [.....]:    switch clone datafile all;
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: Starting backup at 09-MAY-17
  [.....]: channel d1: starting archived log copy
  [.....]: input archived log thread=1 sequence=9 RECID=6 STAMP=943527896
  [.....]: channel d2: starting archived log copy
  [.....]: input archived log thread=1 sequence=8 RECID=5 STAMP=943527890
  [.....]: output file name=/oracle/recovery_area/1_9_943527049.dbf RECID=0 STAMP=0
  [.....]: channel d1: archived log copy complete, elapsed time: 00:00:01
  [.....]: output file name=/oracle/recovery_area/1_8_943527049.dbf RECID=0 STAMP=0
  [.....]: channel d2: archived log copy complete, elapsed time: 00:00:01
  [.....]: Finished backup at 09-MAY-17
  [.....]: 
  [.....]: cataloged archived log
  [.....]: archived log file name=/oracle/recovery_area/1_9_943527049.dbf RECID=1 STAMP=943527897
  [.....]: 
  [.....]: cataloged archived log
  [.....]: archived log file name=/oracle/recovery_area/1_8_943527049.dbf RECID=2 STAMP=943527897
  [.....]: 
  [.....]: datafile 1 switched to datafile copy
  [.....]: input datafile copy RECID=1 STAMP=943527897 file name=/oracle/oradata/SEONTSTP/system01.dbf
  [.....]: datafile 2 switched to datafile copy
  [.....]: input datafile copy RECID=2 STAMP=943527897 file name=/oracle/oradata/SEONTSTP/sysaux01.dbf
  [.....]: datafile 3 switched to datafile copy
  [.....]: input datafile copy RECID=3 STAMP=943527897 file name=/oracle/oradata/SEONTSTP/undotbs01.dbf
  [.....]: datafile 4 switched to datafile copy
  [.....]: input datafile copy RECID=4 STAMP=943527897 file name=/oracle/oradata/SEONTSTP/users01.dbf
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    set until scn  965023;
  [.....]:    recover
  [.....]:    standby
  [.....]:    clone database
  [.....]:     delete archivelog
  [.....]:    ;
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: executing command: SET until clause
  [.....]: 
  [.....]: Starting recover at 09-MAY-17
  [.....]: 
  [.....]: starting media recovery
  [.....]: 
  [.....]: archived log for thread 1 with sequence 8 is already on disk as file /oracle/recovery_area/1_8_943527049.dbf
  [.....]: archived log for thread 1 with sequence 9 is already on disk as file /oracle/recovery_area/1_9_943527049.dbf
  [.....]: archived log file name=/oracle/recovery_area/1_8_943527049.dbf thread=1 sequence=8
  [.....]: archived log file name=/oracle/recovery_area/1_9_943527049.dbf thread=1 sequence=9
  [.....]: media recovery complete, elapsed time: 00:00:01
  [.....]: Finished recover at 09-MAY-17
  [.....]: Finished Duplicate Db at 09-MAY-17
  [.....]: released channel: d1
  [.....]: released channel: d2
  [.....]: released channel: cnv1
  [.....]: released channel: cnv2
  [.....]: 
  [.....]: RMAN> 
  [.....]: 
  [.....]: Recovery Manager complete.
  [DEBUG]: stderr = 
  [DEBUG]: rc = 0
  [INFO]: Duplicated database EONTSTP on defreou0978.eontstmpc.svcs.hpe.com as SEONTSTP