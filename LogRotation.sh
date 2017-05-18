#!/bin/bash
#
oracleSidName="$1"
oracleDbName="$2"
ORACLE_HOME="$3"
oracleRedoLogSize="100"
groupLine1="group 1"
groupLine2="group 2"

E11SID E11DBP /oracle/11.2.0.4/


if [ -f oracle_inp1.tmp  ] ; then
    rm -f oracle_inp1.tmp 
fi
cat  << EOF >> oracle_inp1.tmp
set heading off
set linesize 200
COLUMN status FORMAT A20
COLUMN member FORMAT A70
select log.status, log.group#, file1.member from  V\$LOG  log left join  V\$LOGFILE  file1 on  log.group# = file1.group#  order by log.status desc;
exit
EOF

export ORACLE_SID=${oracleSidName}
export ORAENV_ASK=NO

. oraenv

${ORACLE_HOME}/bin/sqlplus "/ as sysdba" <  oracle_inp1.tmp  | grep -1 oracle

[6:16] 
change location of  first 2 :
cd /oracle/oradata/${oracleDbName}
mkdir controlfile datafile onlinelog

cd /oracle/recovery_area/${oracleDbName}
mkdir controlfile archivelog onlinelog flashback

if [ -f oracle_inp1.tmp  ] ; then
    rm -f oracle_inp1.tmp 
fi
cat  << EOF >> oracle_inp1.tmp
set heading off
set linesize 200
COLUMN status FORMAT A20
COLUMN member FORMAT A70
alter database drop logfile group ${groupLine1};
Alter database add logfile group  ${groupLine1} size ${oracleRedoLogSize}M;

alter database drop logfile group  ${groupLine2};
Alter database add logfile group  ${groupLine2} size ${oracleRedoLogSize}M;
alter system switch logfile;
select log.status, log.group#, file1.member from  V\$LOG  log left join  V\$LOGFILE  file1 on  log.group# = file1.group# where  log.group#='${groupLine3}' order by log.status desc;
exit
EOF

export ORACLE_SID=${oracleSidName}
export ORAENV_ASK=NO

. oraenv

${ORACLE_HOME}/bin/sqlplus "/ as sysdba" <  oracle_inp1.tmp  | grep -1 oracle