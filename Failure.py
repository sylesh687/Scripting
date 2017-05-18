  [DEBUG]: Creating directory (/oracle/oradata/SGFTESTP)
  [DEBUG]: Checking if directory (u'/oracle/oradata/SGFTESTP') exists
  [DEBUG]: Running command: ssh defreou0974.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/oradata/SGFTESTP
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
  [.....]: /bin/ls: cannot access /oracle/oradata/SGFTESTP: No such file or directory
  [DEBUG]: rc = 2
  [DEBUG]: Checking if directory (u'/oracle/oradata') exists
  [DEBUG]: Running command: ssh defreou0974.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/oradata
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
  [DEBUG]: Running command: ssh defreou0974 /bin/mkdir -p -m 755 /oracle/oradata/SGFTESTP;ssh defreou0974 /bin/chown oracle:oinstall /oracle/oradata/SGFTESTP
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
  [DEBUG]: Checking if directory (u'/oracle/oradata/SGFTESTP') exists
  [DEBUG]: Running command: ssh defreou0974.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/oradata/SGFTESTP
  [DEBUG]: stdout = /oracle/oradata/SGFTESTP
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
  [INFO]: Directory /oracle/oradata/SGFTESTP created on host defreou0974.eontstmpc.svcs.hpe.com.
  [DEBUG]: Creating directory (/oracle/recovery_area/SGFTESTP)
  [DEBUG]: Checking if directory (u'/oracle/recovery_area/SGFTESTP') exists
  [DEBUG]: Running command: ssh defreou0974.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/recovery_area/SGFTESTP
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
  [.....]: /bin/ls: cannot access /oracle/recovery_area/SGFTESTP: No such file or directory
  [DEBUG]: rc = 2
  [DEBUG]: Checking if directory (u'/oracle/recovery_area') exists
  [DEBUG]: Running command: ssh defreou0974.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/recovery_area
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
  [DEBUG]: Running command: ssh defreou0974 /bin/mkdir -p -m 755 /oracle/recovery_area/SGFTESTP;ssh defreou0974 /bin/chown oracle:oinstall /oracle/recovery_area/SGFTESTP
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
  [DEBUG]: Checking if directory (u'/oracle/recovery_area/SGFTESTP') exists
  [DEBUG]: Running command: ssh defreou0974.eontstmpc.svcs.hpe.com /bin/ls -d /oracle/recovery_area/SGFTESTP
  [DEBUG]: stdout = /oracle/recovery_area/SGFTESTP
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
  [INFO]: Directory /oracle/recovery_area/SGFTESTP created on host defreou0974.eontstmpc.svcs.hpe.com.
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
  [.....]: CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/oradata/GFTESTP/snapcf_GFSID.f';
  [.....]: DUPLICATE TARGET DATABASE
  [.....]:     FOR STANDBY
  [.....]:     FROM ACTIVE DATABASE
  [.....]:     DORECOVER
  [.....]:     SPFILE
  [.....]:         SET instance_number='1'
  [.....]:         SET db_unique_name='SGFTESTP'
  [.....]:         SET control_files='/oracle/oradata/SGFTESTP/control01.dbf'
  [.....]:         SET db_file_name_convert='/oracle/oradata/GFTESTP', '/oracle/oradata/SGFTESTP'
  [.....]:         SET db_file_name_convert='/oracle/recovery_area/GFTESTP', '/oracle/recovery_area/SGFTESTP'
  [.....]:         SET log_file_name_convert='/oracle/oradata/GFTESTP', '/oracle/oradata/SGFTESTP'
  [.....]:         SET log_file_name_convert='/oracle/recovery_area/GFTESTP', '/oracle/recovery_area/SGFTESTP'
  [.....]:         SET log_archive_dest_1='location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SGFTESTP'
  [.....]:         SET log_archive_dest_2='service=GFTESTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=GFTESTP'
  [.....]:         SET Audit_File_Dest='/oracle/admin/SGFTESTP/adump'
  [.....]:         SET fal_client='SGFTESTP'
  [.....]:         SET fal_server='GFTESTP'
  [.....]:         SET standby_file_management='AUTO'
  [.....]:         SET archive_lag_target='600'
  [.....]:         SET remote_listener=''
  [.....]:         SET log_archive_config='dg_config=(GFTESTP,SGFTESTP)'
  [.....]:         SET remote_login_passwordfile='EXCLUSIVE'
  [.....]:     NOFILENAMECHECK;
  [.....]: }
  [DEBUG]: Running command: ORACLE_HOME=/oracle/11.2.0.4; export ORACLE_HOME; LD_LIBRARY_PATH=/oracle/11.2.0.4/lib; export LD_LIBRARY_PATH; SHLIB_PATH=/oracle/11.2.0.4/lib; export SHLIB_PATH; ORACLE_SID=GFSID; export ORACLE_SID; /oracle/11.2.0.4/bin/rman target sys/*** auxiliary sys/***@SGFTESTP
  [DEBUG]: stdin = 
  [.....]: RUN {
  [.....]: ALLOCATE CHANNEL d1 TYPE DISK;
  [.....]: ALLOCATE CHANNEL d2 TYPE DISK;
  [.....]: 
  [.....]: ALLOCATE AUXILIARY CHANNEL cnv1 TYPE DISK;
  [.....]: ALLOCATE AUXILIARY CHANNEL cnv2 TYPE DISK;
  [.....]: 
  [.....]: CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/oradata/GFTESTP/snapcf_GFSID.f';
  [.....]: DUPLICATE TARGET DATABASE
  [.....]:     FOR STANDBY
  [.....]:     FROM ACTIVE DATABASE
  [.....]:     DORECOVER
  [.....]:     SPFILE
  [.....]:         SET instance_number='1'
  [.....]:         SET db_unique_name='SGFTESTP'
  [.....]:         SET control_files='/oracle/oradata/SGFTESTP/control01.dbf'
  [.....]:         SET db_file_name_convert='/oracle/oradata/GFTESTP', '/oracle/oradata/SGFTESTP'
  [.....]:         SET db_file_name_convert='/oracle/recovery_area/GFTESTP', '/oracle/recovery_area/SGFTESTP'
  [.....]:         SET log_file_name_convert='/oracle/oradata/GFTESTP', '/oracle/oradata/SGFTESTP'
  [.....]:         SET log_file_name_convert='/oracle/recovery_area/GFTESTP', '/oracle/recovery_area/SGFTESTP'
  [.....]:         SET log_archive_dest_1='location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SGFTESTP'
  [.....]:         SET log_archive_dest_2='service=GFTESTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=GFTESTP'
  [.....]:         SET Audit_File_Dest='/oracle/admin/SGFTESTP/adump'
  [.....]:         SET fal_client='SGFTESTP'
  [.....]:         SET fal_server='GFTESTP'
  [.....]:         SET standby_file_management='AUTO'
  [.....]:         SET archive_lag_target='600'
  [.....]:         SET remote_listener=''
  [.....]:         SET log_archive_config='dg_config=(GFTESTP,SGFTESTP)'
  [.....]:         SET remote_login_passwordfile='EXCLUSIVE'
  [.....]:     NOFILENAMECHECK;
  [.....]: }
  [DEBUG]: stdout = 
  [.....]: Recovery Manager: Release 11.2.0.4.0 - Production on Tue May 9 07:43:13 2017
  [.....]: 
  [.....]: Copyright (c) 1982, 2011, Oracle and/or its affiliates.  All rights reserved.
  [.....]: 
  [.....]: connected to target database: GFTESTP (DBID=2349246810)
  [.....]: connected to auxiliary database: SGFTESTP (not mounted)
  [.....]: 
  [.....]: RMAN> 
  [.....]: RMAN> 2> 3> 4> 5> 6> 7> 8> 9> 10> 11> 12> 13> 14> 15> 16> 17> 18> 19> 20> 21> 22> 23> 24> 25> 26> 27> 28> 29> 30> 31> 32> 
  [.....]: using target database control file instead of recovery catalog
  [.....]: allocated channel: d1
  [.....]: channel d1: SID=182 device type=DISK
  [.....]: 
  [.....]: allocated channel: d2
  [.....]: channel d2: SID=198 device type=DISK
  [.....]: 
  [.....]: allocated channel: cnv1
  [.....]: channel cnv1: SID=266 device type=DISK
  [.....]: 
  [.....]: allocated channel: cnv2
  [.....]: channel cnv2: SID=332 device type=DISK
  [.....]: 
  [.....]: new RMAN configuration parameters:
  [.....]: CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/oradata/GFTESTP/snapcf_GFSID.f';
  [.....]: new RMAN configuration parameters are successfully stored
  [.....]: 
  [.....]: Starting Duplicate Db at 09-MAY-17
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    backup as copy reuse
  [.....]:    targetfile  '/oracle/11.2.0.4/dbs/orapwGFSID' auxiliary format 
  [.....]:  '/oracle/11.2.0.4/dbs/orapwSGFSID'   targetfile 
  [.....]:  '/oracle/11.2.0.4/dbs/spfileGFSID.ora' auxiliary format 
  [.....]:  '/oracle/11.2.0.4/dbs/spfileSGFSID.ora'   ;
  [.....]:    sql clone "alter system set spfile= ''/oracle/11.2.0.4/dbs/spfileSGFSID.ora''";
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: Starting backup at 09-MAY-17
  [.....]: Finished backup at 09-MAY-17
  [.....]: 
  [.....]: sql statement: alter system set spfile= ''/oracle/11.2.0.4/dbs/spfileSGFSID.ora''
  [.....]: 
  [.....]: contents of Memory Script:
  [.....]: {
  [.....]:    sql clone "alter system set  instance_number = 
  [.....]:  1 comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  db_unique_name = 
  [.....]:  ''SGFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  control_files = 
  [.....]:  ''/oracle/oradata/SGFTESTP/control01.dbf'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  db_file_name_convert = 
  [.....]:  ''/oracle/oradata/GFTESTP'', ''/oracle/oradata/SGFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  db_file_name_convert = 
  [.....]:  ''/oracle/recovery_area/GFTESTP'', ''/oracle/recovery_area/SGFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_file_name_convert = 
  [.....]:  ''/oracle/oradata/GFTESTP'', ''/oracle/oradata/SGFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_file_name_convert = 
  [.....]:  ''/oracle/recovery_area/GFTESTP'', ''/oracle/recovery_area/SGFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_archive_dest_1 = 
  [.....]:  ''location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SGFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  log_archive_dest_2 = 
  [.....]:  ''service=GFTESTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=GFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  Audit_File_Dest = 
  [.....]:  ''/oracle/admin/SGFTESTP/adump'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  fal_client = 
  [.....]:  ''SGFTESTP'' comment=
  [.....]:  '''' scope=spfile";
  [.....]:    sql clone "alter system set  fal_server = 
  [.....]:  ''GFTESTP'' comment=
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
  [.....]:  ''dg_config=(GFTESTP,SGFTESTP)'' comment=
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
  [.....]: sql statement: alter system set  db_unique_name =  ''SGFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  control_files =  ''/oracle/oradata/SGFTESTP/control01.dbf'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  db_file_name_convert =  ''/oracle/oradata/GFTESTP'', ''/oracle/oradata/SGFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  db_file_name_convert =  ''/oracle/recovery_area/GFTESTP'', ''/oracle/recovery_area/SGFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_file_name_convert =  ''/oracle/oradata/GFTESTP'', ''/oracle/oradata/SGFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_file_name_convert =  ''/oracle/recovery_area/GFTESTP'', ''/oracle/recovery_area/SGFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_archive_dest_1 =  ''location=/oracle/recovery_area valid_for=(ALL_LOGFILES,ALL_ROLES) db_unique_name=SGFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_archive_dest_2 =  ''service=GFTESTP SYNC AFFIRM valid_for=(ONLINE_LOGFILE,PRIMARY_ROLE) db_unique_name=GFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  Audit_File_Dest =  ''/oracle/admin/SGFTESTP/adump'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  fal_client =  ''SGFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  fal_server =  ''GFTESTP'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  standby_file_management =  ''AUTO'' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  archive_lag_target =  600 comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  remote_listener =  '''' comment= '''' scope=spfile
  [.....]: 
  [.....]: sql statement: alter system set  log_archive_config =  ''dg_config=(GFTESTP,SGFTESTP)'' comment= '''' scope=spfile
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
  [.....]:    backup as copy current controlfile for standby auxiliary format  '/oracle/oradata/SGFTESTP/control01.dbf';
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: Starting backup at 09-MAY-17
  [.....]: channel d1: starting datafile copy
  [.....]: copying standby control file
  [.....]: output file name=/oracle/oradata/GFTESTP/snapcf_GFSID.f tag=TAG20170509T074324 RECID=1 STAMP=943515804
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
  [.....]:  "/oracle/oradata/GFTESTP/temp01.dbf";
  [.....]:    switch clone tempfile all;
  [.....]:    set newname for datafile  1 to 
  [.....]:  "/oracle/oradata/GFTESTP/system01.dbf";
  [.....]:    set newname for datafile  2 to 
  [.....]:  "/oracle/oradata/GFTESTP/sysaux01.dbf";
  [.....]:    set newname for datafile  3 to 
  [.....]:  "/oracle/oradata/GFTESTP/undotbs01.dbf";
  [.....]:    set newname for datafile  4 to 
  [.....]:  "/oracle/oradata/GFTESTP/users01.dbf";
  [.....]:    backup as copy reuse
  [.....]:    datafile  1 auxiliary format 
  [.....]:  "/oracle/oradata/GFTESTP/system01.dbf"   datafile 
  [.....]:  2 auxiliary format 
  [.....]:  "/oracle/oradata/GFTESTP/sysaux01.dbf"   datafile 
  [.....]:  3 auxiliary format 
  [.....]:  "/oracle/oradata/GFTESTP/undotbs01.dbf"   datafile 
  [.....]:  4 auxiliary format 
  [.....]:  "/oracle/oradata/GFTESTP/users01.dbf"   ;
  [.....]:    sql 'alter system archive log current';
  [.....]: }
  [.....]: executing Memory Script
  [.....]: 
  [.....]: executing command: SET NEWNAME
  [.....]: 
  [.....]: renamed tempfile 1 to /oracle/oradata/GFTESTP/temp01.dbf in control file
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
  [.....]: input datafile file number=00001 name=/oracle/oradata/GFTESTP/system01.dbf
  [.....]: channel d2: starting datafile copy
  [.....]: input datafile file number=00002 name=/oracle/oradata/GFTESTP/sysaux01.dbf
  [.....]: RMAN-03009: failure of backup command on d1 channel at 05/09/2017 07:43:35
  [.....]: ORA-17628: Oracle error 19505 returned by remote Oracle server
  [.....]: continuing other job steps, job failed will not be re-run
  [.....]: channel d1: starting datafile copy
  [.....]: input datafile file number=00003 name=/oracle/oradata/GFTESTP/undotbs01.dbf
  [.....]: RMAN-03009: failure of backup command on d2 channel at 05/09/2017 07:43:35
  [.....]: ORA-17628: Oracle error 19505 returned by remote Oracle server
  [.....]: continuing other job steps, job failed will not be re-run
  [.....]: channel d2: starting datafile copy
  [.....]: input datafile file number=00004 name=/oracle/oradata/GFTESTP/users01.dbf
  [.....]: RMAN-03009: failure of backup command on d1 channel at 05/09/2017 07:43:35
  [.....]: ORA-17628: Oracle error 19505 returned by remote Oracle server
  [.....]: continuing other job steps, job failed will not be re-run
  [.....]: released channel: d1
  [.....]: released channel: d2
  [.....]: released channel: cnv1
  [.....]: released channel: cnv2
  [.....]: RMAN-00571: ===========================================================
  [.....]: RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
  [.....]: RMAN-00571: ===========================================================
  [.....]: RMAN-03002: failure of Duplicate Db command at 05/09/2017 07:43:36
  [.....]: RMAN-05501: aborting duplication of target database
  [.....]: RMAN-03015: error occurred in stored script Memory Script
  [.....]: RMAN-03009: failure of backup command on d2 channel at 05/09/2017 07:43:36
  [.....]: ORA-17628: Oracle error 19505 returned by remote Oracle server
  [.....]: 
  [.....]: RMAN> 
  [.....]: 
  [.....]: Recovery Manager complete.
  [DEBUG]: stderr = 
  [DEBUG]: rc = 1