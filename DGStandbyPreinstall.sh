#!/bin/bash

#----------------------------------------------------------------------------------
# Name:ConfigureStandyServer.sh
# Description: This Script Prepares Standby Server For DataGaurd
# Version: 1.0
# Maintainer: Shailesh Thakur
# usage:sh test.sh -d "EONTST" -e "1521" -f "EON123" -g "defren3281" -h "defreon3280" -i "oracle.com" -k "DREONTST:/oracle/11.2.0.4:N"
# ---------------------------------------------------------------------------------


while getopts d:e:f:g:h:i:k: req;do
	case $req in
 
	d) Dbname=$OPTARG;;
	e) Port=$OPTARG;;
	f) PrimarySid=$OPTARG;;
	g) StandbyHostName=$OPTARG;;
	h) PrimaryServer=$OPTARG;;
	i) DomainName=$OPTARG;;
  k) OraEntry=$OPTARG;;
	
	esac
	
done

Domain=.$DomainName

ProgramName=$(basename $0)

#------------------------------Setting the TimeStamp--------------------------------

[ -z "$TimeStamp" ] && \
TimeStamp=$(date +%H%M%S%d%m%Y)

#-------------------------- Exporting  Variables for the SubFunctions----------------

export ProgramName
export TimeStamp


LOGFILE=/var/$ProgramName.$TimeStamp.log


#-------------------------------------------------------------------------------
# Name: logging
# Description: This Function Creates log file
#-------------------------------------------------------------------------------

logging () {
	local OPTIND arg
	LOGTIMESTAMP=`date`
        SILENTFLAG=0
        EXITFLAG=0
        while getopts "f:p:l:m:seh" arg; do
        case "$arg" in
                f) LOGFILE="$OPTARG";;
                p) PROCESSNAME="$OPTARG";;
                l) LOGLEV="$OPTARG";;
                m) LOGMSG="$OPTARG";;
                s) SILENTFLAG=1;;
                e) EXITFLAG=1;;
                h) echo Synopsis logging -p PROCESSNAME -f LOGFILE -l LOGLEV -m LOGMSG [-s] [-e]; exit;;
        esac
        done


        [ -z "$LOGFILEOFF" ] && printf "$LOGTIMESTAMP $PROCESSNAME $LOGLEV $LOGMSG\n" >> $LOGFILE
        if [ "$SILENTFLAG" -eq 0 ] && [ -z "$SCREENOFF" ]
        then
                printf "$LOGTIMESTAMP $PROCESSNAME $LOGLEV $LOGMSG\n"
        fi

}

#------------------------------------------------------------------------------------
# Name: CommanExitStatus
# Description : Checks th Exit status of Command and loggs
#------------------------------------------------------------------------------------

CommandExitStatus() {

	if [ $? = 0 ]
		then
			logging -p $PROGNAME -f $LOGFILE -l INFO -m "$1"
	else
			logging -p $PROGNAME -f $LOGFILE -l ERROR -m "$2"
	exit 1
	fi
}




#-----------------------------------------------------------------------------------
# Name: DataGaurdPreInstall
# Description : Creates a Pre Install Script for DataGaurd 
#-----------------------------------------------------------------------------------

DataGaurdPreInstall(){

      logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the Preinstalls for DataGaurd !!!!"
      logging -p $ProgramName -f $LOGFILE -l INFO -m "DataGaurd Preinstall Started !!!!"
      

      if [ ! -f /etc/oratab ]; then
          
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the oratab file !!!!! IT IS NOT PRESENT"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating New Oratab File !!!!!"
           
           touch /etc/oratab
           
           CommandExitStatus "File is SuccessFully Crreated !!!" "Failure creating oratab "
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Writing the Valid Content to the file !!!!!"
          
           echo $OraEntry >> /etc/oratab
           
           CommandExitStatus "oratab file is written with a valid content !!!" "Failure writing oratab "
           
           
           
            
      else
          
            
            logging -p $ProgramName -f $LOGFILE -l INFO -m "File IS Already Dere Now check for the Valid Content !!!!!"
            
            if grep -Fxq "$OraEntry" /etc/oratab
                
                then
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The File Has a  Valid Content !!!!!"
                  
                  
            else
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The File Has no Valid Content !!!!!"
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to Oratab !!!!!"
                   
                   echo $OraEntry >> /etc/oratab
                   
                   
      
            fi            
      fi

#---------------------------------------------------------------------------------------------------------------------
#                                    Adding Oracle SID to bash_profile

   logging -p $ProgramName -f $LOGFILE -l INFO -m "Oratab File Has Been Updated With Required Content !!!!"
   logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking if ORACLE_SID is present in users bash_profile"
   logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating OracleSid Variable from OraEntry"
   
   OracleSid=$(grep "$OraEntry" /etc/oratab | cut -d':' -f1,1)
   
   if grep -Fxq "ORACLE_SID=$OracleSid" ~/.bash_profile
                
                then
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The bash_profile File Has a  Valid Content !!!!!"
                  
                  
            else
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The bash_profile  Has no Valid Content !!!!!"
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to bash_profile!!!!!"
                   
                   echo "ORACLE_SID=$OracleSid" >> ~/.bash_profile
                   
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to bash_profile is Done!!!!!"
                   
                   
      
            fi     
#------------------------------------------------------------------------------------------------------------------------
#                                Creating the Correct folder Structure

    
    logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the Currect Folder Structure !!!!"
    
    if [ ! -d /oracle/oradata/$OracleSid ] && [ ! -d /oracle/recovery_area/$OracleSid ]; then
    
           logging -p $ProgramName -f $LOGFILE -l WARNING -m "Correct Folder Structure  for oradata Doesnot Exist !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Correct folder Structure !!!!"
           
           mkdir /oracle/oradata/$OracleSid
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct folder Structure Created !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Changing to $OracleSid dir !!!!"
           
           cd /oracle/oradata/$OracleSid
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Changedto $OracleSid dir !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct three folders in $OracleSid dir !!!!"
          
           mkdir  controlfile datafile onlinelog
           
           logging -p $ProgramName -f $LOGFILE -l WARNING -m "Correct Folder Structure  for recovery area Doesnot Exist !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Correct folder Structure !!!!"
           
           mkdir /oracle/recovery_area/$OracleSid
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct folder Structure Created !!!!"
           
           cd /oracle/recovery_area/$OracleSid
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Changedto $OracleSid dir !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct three folders in $OracleSid dir !!"
           
          
           mkdir controlfile archivelog onlinelog
 
       
    else
        echo "FOLDER STRUCTURE EXISTS"
        
    fi
    
#-----------------------------------------------------------------------------------------------------------------------------

    OracleHome=$(grep $OraEntry /etc/oratab | cut -d':' -f2)
    
    logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating initORacleSid.ora !!!!!"
    
    
    if [ ! -f $OracleHome/dbs/init$OracleSid.ora ] && [ ! -f $OracleHome/network/admin/listener.ora ]; then
    
          echo "NEED TO CREATE"
          logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Listener File on Standby Server !!!!!"
          
          touch $OracleHome/dbs/init$OracleSid.ora
          echo "db_name=$Dbname" >> $OracleHome/dbs/init$OracleSid.ora
          
          CommandExitStatus " Listener File  successfully Created !!!" "Failed to Listener please check with the permission"

          touch $OracleHome/network/admin/listener.ora

          logging -p $ProgramName -f $LOGFILE -l INFO -m "Putting the Content to the listener.ora !!!!!"

echo "LISTENER_$OracleSid_$Port =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

SID_LIST_LISTENER_$OracleSid_$Port =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = $Dbname_DGMGRL)
      (ORACLE_HOME = $OracleHome)
      (SID_NAME = $OracleSid)
    )
  )

ADR_BASE_LISTENER_$ORacleSid_$Port = /oracle" >> $OracleHome/network/admin/listener.ora
  
          logging -p $ProgramName -f $LOGFILE -l INFO -m "Putting the Content to the listener.ora  has been done !!!!!"
          
          else 
          
              if grep -Fxq "db_name=$Dbname" $OracleHome/dbs/init$OracleSid.ora
                
                then
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The $OracleHome/dbs/init$OracleSid.ora File Has a  Valid Content !!!!!"
                  
                  
            else
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The $OracleHome/dbs/init$OracleSid.ora Has no Valid Content !!!!!"
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to $OracleHome/dbs/init$OracleSid.ora !!!!!"
                   
                   echo "db_name=$Dbname" $OracleHome/dbs/init$OracleSid.ora
                   
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to $OracleHome/dbs/init$OracleSid.ora is Done!!!!!"
          
                   
echo "LISTENER_$OracleSid_$Port =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

SID_LIST_LISTENER_$OracleSid_$Port =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = $Dbname_DGMGRL)
      (ORACLE_HOME = $OracleHome)
      (SID_NAME = $OracleSid)
    )
  )

ADR_BASE_LISTENER_$ORacleSid_$Port = /oracle" > $OracleHome/network/admin/listener.ora
                   
      
            fi   
      fi
#----------------------------------------------------------------------------------------------------------------------------------------
#                                            tnsnames.ora

echo $Dbname

      logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the tnsnames.ora !!!!!"
      
      if [ ! -f $OracleHome/network/admin/tnsnames.ora ]; then
      
            touch $OracleHome/network/admin/tnsnames.ora
echo "
 ${Dbname}$Domain =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer )(PORT = $Port))
    )
    (CONNECT_DATA =
      (SID = $Dbname)
      (SERVICE_NAME = $Dbname$Domain)
      (UR = A)
    )
  )

${OracleSid}$Domain =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
    )
    (CONNECT_DATA =
      (SID = $OracleSid)
      (SERVICE_NAME = ${OracleSid}$Domain)
      (UR = A)
    )
  )" >> $OracleHome/network/admin/tnsnames.ora
  
  echo "
  ${Dbname}DG${Domain} =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer )(PORT = $Port))
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName )(PORT = $Port))
      (LOAD_BALANCE = no)
    )
    (CONNECT_DATA =
      (SERVICE_NAME =${Dbname}DG${Domain})
    )
  )

${PrimarySid}_DGMGRL${Domain} =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer)(PORT = $Port))
    (CONNECT_DATA =
      (SERVICE_NAME = ${PrimarySid}_DGMGRL${Domain})
      (Instance_NAME = $PrimarySid)
    )
  )

${OracleSid}_DGMGRL${Domain} =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $PORT))
    (CONNECT_DATA =
      (SERVICE_NAME = ${OracleSid}_DGMGRL${Domain})
      (Instance_NAME = $OracleSid)
    )
  )
  
  LISTENER_${OracleSid}_${Port} = (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
  LISTENER_${PrimarySid}_${Port} = (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer)(PORT = $Port))  " >> $OracleHome/network/tnsnames.ora
 
  
            
      else 
      
           echo "
 ${Dbname}$Domain =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer )(PORT = $Port))
    )
    (CONNECT_DATA =
      (SID = $Dbname)
      (SERVICE_NAME = $Dbname$Domain)
      (UR = A)
    )
  )

${OracleSid}$Domain =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
    )
    (CONNECT_DATA =
      (SID = $OracleSid)
      (SERVICE_NAME = ${OracleSid}$Domain)
      (UR = A)
    )
  )" >> $OracleHome/network/admin/tnsnames.ora
  
  echo "
  ${Dbname}DG${Domain} =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer )(PORT = $Port))
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName )(PORT = $Port))
      (LOAD_BALANCE = no)
    )
    (CONNECT_DATA =
      (SERVICE_NAME =${Dbname}DG${Domain})
    )
  )

${PrimarySid}_DGMGRL${Domain} =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer)(PORT = $Port))
    (CONNECT_DATA =
      (SERVICE_NAME = ${PrimarySid}_DGMGRL${Domain})
      (Instance_NAME = $PrimarySid)
    )
  )

${OracleSid}_DGMGRL${Domain} =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
    (CONNECT_DATA =
      (SERVICE_NAME = ${OracleSid}_DGMGRL${Domain})
      (Instance_NAME = $OracleSid)
    )
  )
  
  LISTENER_${OracleSid}_$Port = (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
  LISTENER_${PrimarySid}_$Port = (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer)(PORT = $Port))  " > $OracleHome/network/admin/tnsnames.ora
 
  
      
      
      fi 
 
#--------------------------------------------------------------------------------------------------------------------------------


}     


DataGaurdPreInstall