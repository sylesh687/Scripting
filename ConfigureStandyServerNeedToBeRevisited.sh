#!/bin/bash

#----------------------------------------------------------------------------------
# Name:ConfigureStandyServer.sh
# Description: This Script Prepares Standby Server For DataGaurd
# Version: 1.0
# Maintainer: Shailesh Thakur
# ---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
usage () {
	ERRORNUM=$1

	echo "Version: 1.0"
	echo "Usage: The Script Sets Up the Server for DataGuard Installation "
	
	#Description
	echo 'The Script Script Sets Up the Server for DataGuard Installation by performing the below Tasks:'
	echo '1- Checks if necessary permission are given to oracle user' 
	echo '2- Checks of correct files and folders are present if not creates them'
	echo '3- Creates listener.ora and tnsnames.ora file with proper values ' 
	echo '4- Fires up the listener as oracle User'

	#Example
	echo "Example:"
	echo "ConfigureStandyServer.sh -d Dbname -f PrimarySid -g StanbyServerHostname -h PrimaryServerHostname"
		
	[ -z "$ERRORNUM" ] && ERRORNUM=0
	
    exit $ERRORNUM;
}
#----------------------------------------------------------------------------------------
    if [ $# -ne 8 ]; then
        usage
        exit 1
    fi
#----------------------------------------------------------------------------------------
//ULA: maybe other letters are more meaningful like -n <name>.
// But no effect, when we not need more inputs (see below questions).
while getopts d:f:g:h: req;do
	case $req in
 
	d) Dbname=$OPTARG;;
	f) PrimarySid=$OPTARG;;
	g) StandbyHostName=$OPTARG;;
	h) PrimaryServer=$OPTARG;;
	
	esac
	
done

// ULA: Is listner port really hardcoded or selectable in MPP, so we get this as input into the flows?
Port="1521"
#Domain=.$DomainName
// ULA: ?????? is this correct? Or must this be $Dbname?
OraEntry="SEONT12:/oracle/11.2.0.4:N"

// ULA: maybe also put 11.2.0.4 into a variable like OracleVersion use later this variable to 
use the script also for other releases.


ProgramName=$(basename $0)

#------------------------------Setting the TimeStamp--------------------------------

[ -z "$TimeStamp" ] && \
TimeStamp=$(date +%H%M%S%d%m%Y)

#-------------------------- Exporting  Variables for the SubFunctions----------------

export ProgramName
export TimeStamp

// ULA: better syntax in shell script, when the string containing "blanks".
#LOGFILE=/var/$ProgramName.$TimeStamp.log
// better use currly bracket, when you are concatinating!!!! Also possible in -z "${TimeStamp}"
LOGFILE=/var/${ProgramName}.${TimeStamp}.log


#-------------------------------------------------------------------------------
# Name: logging
# Description: This Function Creates log file
#-------------------------------------------------------------------------------

logging () {
	local OPTIND arg
nn	LOGTIMESTAMP=`date`
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


    logging -p $ProgramName -f $LOGFILE -l INFO -m "------------------------------------------------------"
    logging -p $ProgramName -f $LOGFILE -l INFO -m "!!! DATAGUARD PRE SETUP ON $StandbyHostName Started !!!"
    logging -p $ProgramName -f $LOGFILE -l INFO -m " ------------------------------------------------------"

#------------------------------------------------------------------------------------
#                        Checking the File ownership of /oracle dir


      logging -p $ProgramName -f $LOGFILE -l INFO -m "Changing the ownership or /oracle form root:root to oracle:oinstall !!!!"
        
            chown oracle:oinstall /oracle
            if [ $? -eq 0 ]; then


                  logging -p $ProgramName -f $LOGFILE -l INFO -m "The owenerhsip of /oracle is changed from root:root to oracle:oinstall"
      
            else

                  echo "Failed to to change ownership!! Due to some permission issues"
                  logging -p $ProgramName -f $LOGFILE -l INFO -m "Failed to to change ownership!! Due to some permission issues One Should be a root user to do so!!!"
                  
            fi
      
                
                
                
#---------------------------------------------------------------------------------------
      
      logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the Preinstalls for DataGaurd !!!!"
      logging -p $ProgramName -f $LOGFILE -l INFO -m "DataGaurd Preinstall Started !!!!"
      

      if [ ! -f /etc/oratab ]; then
          
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the oratab file !!!!! IT IS NOT PRESENT"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating New Oratab File !!!!!"
           
           touch /etc/oratab
           
           CommandExitStatus "/etc/oratab File is SuccessFully Crreated !!!" "Failure creating oratab "
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Writing the Valid Content to the file /etc/oratab FILE!!!!!"
          
           echo $OraEntry >> /etc/oratab
           
           CommandExitStatus "/etc/oratab FILE is written with a valid content !!!" "Failure writing oratab "
           
           
           
            
      else
          
            
            logging -p $ProgramName -f $LOGFILE -l INFO -m "/etc/oratab FILE Already Exists !! Now Checking  for the Valid Content !!!!!"
            
            if grep -Fxq "$OraEntry" /etc/oratab
                
                then
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "/etc/oratab File Has a  Valid Content !!!!!"
                  
                  
            else
                
                   logging -p $ProgramName -f $LOGFILE -l WARNING -m "/etc/oratab The File Has no Valid Content !!!!!"
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to /etc/oratab File !!!!!"
                   
                   echo $OraEntry >> /etc/oratab
                   
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "/etc/oratab FILE is written with a valid content !!!!!"
                   
      
            fi            
      fi

#---------------------------------------------------------------------------------------------------------------------
#                                    Adding Oracle SID to bash_profile

   
   logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking if ORACLE_SID is present in users bash_profile"
   logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating OracleSid Variable from OraEntry"
   
   OracleSid=$(grep "$OraEntry" /etc/oratab | cut -d':' -f1,1)
   
// ULA why echo, why not logging?
   echo $OracleSid
   
   if grep -Fxq "ORACLE_SID=$OracleSid" /home/oracle/.bash_profile
                
                then
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The bash_profile File Has a  Valid Content !!!!!"
                  
                  
            else
                
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The bash_profile  Has no Valid Content !!!!!"
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to bash_profile!!!!!"
                   echo "ORACLE_SID=$OracleSid" >> /home/oracle/.bash_profile
// ULA: I think,  export here the variable is correct like                   
                   echo "export ORACLE_SID=$OracleSid" >> /home/oracle/.bash_profile
                   
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to bash_profile is Done!!!!!"
                   
                   
      
            fi     
#------------------------------------------------------------------------------------------------------------------------
#                                Creating the Correct folder Structure

    
    logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the Currect Folder Structure !!!!"

// ULA: I would use here, but not having quotes is also fine.
    if [ ! -d "/oracle/oradata/${OracleSid}" ] && [ ! -d "/oracle/recovery_area/${OracleSid}" ]; then

    if [ ! -d /oracle/oradata/$OracleSid ] && [ ! -d /oracle/recovery_area/$OracleSid ]; then
    
           logging -p $ProgramName -f $LOGFILE -l WARNING -m "Correct Folder Structure  for oradata Doesnot Exist !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Correct folder Structure !!!!"
           
           mkdir -p /oracle/oradata/$OracleSid
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct folder Structure Created !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Changing to $OracleSid dir !!!!"
           
           cd /oracle/oradata/$OracleSid
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Changedto $OracleSid dir !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct three folders in $OracleSid dir !!!!"
          
           mkdir  controlfile datafile onlinelog
           
           logging -p $ProgramName -f $LOGFILE -l WARNING -m "Correct Folder Structure  for recovery area Doesnot Exist !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Correct folder Structure !!!!"
           
           mkdir -p /oracle/recovery_area/$OracleSid
           
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
    
    
    if [ ! -f $OracleHome/dbs/init$OracleSid.ora ]; then
    
          echo "NEED TO CREATE"
          
          
          touch $OracleHome/dbs/init$OracleSid.ora
          echo "db_name=$Dbname" >> $OracleHome/dbs/init$OracleSid.ora
          
    elif [ ! -f $OracleHome/network/admin/listener.ora ]; then
          
         
          logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Listener File on Standby Server !!!!!"
          touch $OracleHome/network/admin/listener.ora
          CommandExitStatus " Listener File  successfully Created !!!" "Failed to Listener please check with the permission"
          logging -p $ProgramName -f $LOGFILE -l INFO -m "Putting the Content to the listener.ora !!!!!"

echo "LISTENER_${OracleSid}_${Port} =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
// ULA: if the port is comming as input and not hard coded, is here EXTPROC1521 correct or also EXTPROC${Port}?????
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

SID_LIST_LISTENER_${OracleSid}_${Port} =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = $Dbname_DGMGRL)
      (ORACLE_HOME = $OracleHome)
      (SID_NAME = $OracleSid)
    )
  )

// ULA:  this curly bracket is correct????
//                          |
//                          |
//                          |
//                          |
ADR_BASE_LISTENER_$OracleSid}_${Port} = /oracle" >> $OracleHome/network/admin/listener.ora
  
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
          
                   
echo "LISTENER_${OracleSid}_${Port} =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
// ULA: see above about 1521!!!!
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

SID_LIST_LISTENER_${OracleSid}_${Port} =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = ${Dbname}_DGMGRL)
      (ORACLE_HOME = $OracleHome)
      (SID_NAME = ${OracleSid})
    )
  )

// ULA: Spelling of the variable seems to be wrong $ORacleSid vs $OracleSid
ADR_BASE_LISTENER_$ORacleSid_$Port = /oracle" > $OracleHome/network/admin/listener.ora
                   
      
            fi   
      fi
#----------------------------------------------------------------------------------------------------------------------------------------
#                                            tnsnames.ora

// ULA: why echo and not logging?
echo $Dbname

      logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the tnsnames.ora !!!!!"
      
      if [ ! -f $OracleHome/network/admin/tnsnames.ora ]; then
      logging -p $ProgramName -f $LOGFILE -l WARNING -m "tnsnames.ora file is not present NEED TO CREATE!!!!!"
      logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating tnsnames.ora file !!!!!"
            touch $OracleHome/network/admin/tnsnames.ora
      logging -p $ProgramName -f $LOGFILE -l INFO -m "tnsnames.ora if successfully Created !!!!!"
      
      logging -p $ProgramName -f $LOGFILE -l INFO -m "Writing the content to the tnsnames.ora file!!!!!"
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
  )
  
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
// ULA: here is PORT instead of $Port!!!!!!
    (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $PORT))
    (CONNECT_DATA =
      (SERVICE_NAME = ${OracleSid}_DGMGRL${Domain})
      (Instance_NAME = $OracleSid)
    )
  )
  
  LISTENER_${OracleSid}_${Port} = (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
  LISTENER_${PrimarySid}_${Port} = (ADDRESS = (PROTOCOL = TCP)(HOST = $PrimaryServer)(PORT = $Port))  " > $OracleHome/network/tnsnames.ora
 
 
 logging -p $ProgramName -f $LOGFILE -l INFO -m "tnsnames.ora file is Successfully written with correct content !!!!!"
  
            
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
  )
  
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
 

#--------------------------------------------------------------------------------------------------------------------
#                      Checking the listener status  on Standby and its owner 




        var4="LISTENER_${OracleSid}_${Port}"
        
        logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking the listener status on StandBy Server !!!!!"
// ULA: this is maybe not correct, because you also can find the "grep lsn" command itself in the ps output, so you don't see the listner process.
// ps -ef | grep lsn | grep -v grep | tail -n 1

              status=$(ps -ef | grep lsn | tail -n 1)
        
        logging -p $ProgramName -f $LOGFILE -l INFO -m "Listener Status has be Success Fully Determined !!!!!"
        
            echo $status | grep -q "tnslsnr"
            
            
        if [ $? -eq 0 ]; then

                      echo "Listener is running on the Standy Server"
                      
                      logging -p $ProgramName -f $LOGFILE -l INFO -m "Listener is running on the Standy Server !!!!!"
                      
                      owned=$(echo ${status} | cut -d ' ' -f1)
                      pid=(echo ${status} | cut -d ' ' -f2)
                      
                      

                      if [ "${owned}" == "oracle" ]; then
            
                             logging -p $ProgramName -f $LOGFILE -l INFO -m "IT IS FINE Listener on Stanby Server is Running as a oracle !!!!!"
                
                      else 
             
                           logging -p $ProgramName -f $LOGFILE -l INFO -m "This Process should be killed and started as oracle !!!!!"
                           echo "Killing the Process"
                           logging -p $ProgramName -f $LOGFILE -l INFO -m "Killing the Process !!!!!"
                           kill  -KILL $pid
                           if [ $? -eq 0 ]; then

                                  logging -p $ProgramName -f $LOGFILE -l INFO -m "Process is successfully killed!!!"
      
                            else
                                  logging -p $ProgramName -f $LOGFILE -l INFO -m "Failed to to kill this process! Due to some permission issues One should have root previleges!!!"
                                  

                           fi
                    fi
                
      else

        
        logging -p $ProgramName -f $LOGFILE -l INFO -m "Listener is not running on the $stbyServer !!! Need to Start Manyally"
        logging -p $ProgramName -f $LOGFILE -l INFO -m "Starting the listener process as oracle!!!"
        
          su - oracle -c "/oracle/11.2.0.4/bin/lsnrctl start ${var4}"
        
          if [ $? -eq 0 ]; then

                        logging -p $ProgramName -f $LOGFILE -l INFO -m "$var4 Process is successfully started as oracle!!!!!!"
      
          else

                        logging -p $ProgramName -f $LOGFILE -l INFO -m "$var4 Failed to to kill this process! Due to some permission issues"

          fi

      fi

      
#---------------------------------------------------------------------------------------------------------------------------------
}     


DataGaurdPreInstall
