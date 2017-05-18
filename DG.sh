#!/bin/sh

#----------------------------------------------------------------------------------
# Name:ConfigureStandyServer.sh
# Description: This Script Prepares Standby Server For DataGaurd
# Version: 1.0
# Maintainer: Shailesh Thakur
# Example:sh ConfigureStandyServer.sh -d "EONT12" -o "EONT12" -s "defreon3332.eontstmpc.svcs.hpe.com" -p "defreon3342.eontstmpc.svcs.hpe.com"
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
        echo "ConfigureStandyServer.sh -d Dbname -o PrimarySid -p StanbyServerHostname -s PrimaryServerHostname"

        [ -z "$ERRORNUM" ] && ERRORNUM=0

    exit $ERRORNUM;
}
#----------------------------------------------------------------------------------------
    if [ $# -ne 8 ]; then
        usage
        exit 1
    fi
#----------------------------------------------------------------------------------------
while getopts d:o:s:p: req;do
        case $req in

        d) Dbname=$OPTARG;;
        o) PrimarySid=$OPTARG;;
        s) StandbyHostName=$OPTARG;;
        p) PrimaryServer=$OPTARG;;

        esac

done
Port="1521"
#Domain=.$DomainName
OracleSid=S${PrimarySid}
OraEntry="${PrimarySid}:/oracle/11.2.0.4:N"

ProgramName=$(basename $0)

#------------------------------Setting the TimeStamp--------------------------------

[ -z "$TimeStamp" ] && \
TimeStamp=$(date +%H%M%S%d%m%Y)

#-------------------------- Exporting  Variables for the SubFunctions----------------

export ProgramName
export TimeStamp


LOGFILE=/var/${ProgramName}.${TimeStamp}.log

#---------------------------------------------------------------------------------------
#	Function to track the command Status / But will not terminate program during fauiure

cmd_status() {
if [ $? = 0 ]
then
	logging -p $ProgramName -f $LOGFILE -l INFO -m "$1"
else
	logging -p $ProgramName -f $LOGFILE -l WARNING -m "$2"
fi
}
#---------------------------------------------------------------------------------------
#	Function to track the command Status and will terminate program during fauiure

cmd_status_exit() {
if [ $? = 0 ]
then
	logging -p $ProgramName -f $LOGFILE -l INFO -m "$1"
else
	logging -p $ProgramName -f $LOGFILE -l ERROR -m "$2"
	exit 1
fi
}
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

#-----------------------------------------------------------------------------------
# Name: DataGaurdPreInstall
# Description : Creates a Pre Install Script for DataGaurd
#-----------------------------------------------------------------------------------

DataGaurdPreInstall(){


    logging -p $ProgramName -f $LOGFILE -l INFO -m "------------------------------------------------------"
    logging -p $ProgramName -f $LOGFILE -l INFO -m "!!! DATAGUARD PRE SETUP ON $StandbyHostName Started !!!"
    logging -p $ProgramName -f $LOGFILE -l INFO -m " ------------------------------------------------------"
	
	logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the Preinstalls for DataGaurd !!!!"
    logging -p $ProgramName -f $LOGFILE -l INFO -m "DataGaurd Preinstall Started !!!!"


#------------------------------------------------------------------------------------
#                        Checking the File ownership of /oracle dir


      
	  
      userStatus=$(passwd -S oracle | cut -d '(' -f2 | cut -d ',' -f1)
      
      actualValue="Password set"
	  
                if [ "${userStatus}" == "${actualValue}" ]; then
				
                        logging -p $ProgramName -f $LOGFILE -l INFO -m "Setting Password for the oracle user !!!!"
                        echo -e "Oracle123\nOracle123" | (passwd oracle)
						
						cmd_status_exit "Password is SuccessFully Set !!!!" "Password Set Failed!!!!"
						
                        logging -p $ProgramName -f $LOGFILE -l INFO -m "Password for the Oracle User is already Set and is Unlocked !!!!"

                else
				
                        logging -p $ProgramName -f $LOGFILE -l INFO -m "User Oracle is locked Need to Unlock !!!!"
                        logging -p $ProgramName -f $LOGFILE -l INFO -m "Unlocking the Oracle User !!!!"
                        
						pam_tally2  -u oracle  -r
						
						cmd_status_exit "Oracle User is Successfully unlocked !!!!" "Unable to Unlock !!!!"
						
						logging -p $ProgramName -f $LOGFILE -l INFO -m "Setting Password for the oracle user !!!!"
						echo -e "Oracle123\nOracle123" | (passwd oracle)
						
						cmd_status_exit "Password is SuccessFully Set !!!!" "Password Set Failed!!!!"
						 

                fi
			
			logging -p $ProgramName -f $LOGFILE -l INFO -m "Setting the ownership for /oracle dir !!!!"
			
            chown oracle:oinstall /oracle
			cmd_status_exit "The owenerhsip of /oracle is changed from root:root to oracle:oinstall" "Failed to to change ownership!! Due to some permission issues One Should be a root user to do so!!!"
            
#---------------------------------------------------------------------------------------

     

      if [ ! -f /etc/oratab ]; then

           logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the oratab file !!!!! IT IS NOT PRESENT"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating New Oratab File !!!!!"

            su - oracle -c "touch /etc/oratab"

           exit_status "/etc/oratab File is SuccessFully Crreated !!!" "Failure creating oratab "
		   
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Writing the Valid Content to the file /etc/oratab FILE!!!!!"

           su - oracle -c echo $OraEntry >> /etc/oratab

           exit_status "/etc/oratab FILE is written with a valid content !!!" "Failure writing oratab "




      else


            logging -p $ProgramName -f $LOGFILE -l INFO -m "/etc/oratab FILE Already Exists !! Now Checking  for the Valid Content !!!!!"

            if grep -Fxq "$OraEntry" /etc/oratab

                then

                   logging -p $ProgramName -f $LOGFILE -l INFO -m "/etc/oratab File Has a  Valid Content !!!!!"


            else

                   logging -p $ProgramName -f $LOGFILE -l WARNING -m "/etc/oratab The File Has no Valid Content !!!!!"
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to /etc/oratab File !!!!!"

                   echo $OraEntry >> /etc/oratab
				   
				   exit_status "/etc/oratab FILE is written with a valid content !!!" "Failure writing oratab "

                   logging -p $ProgramName -f $LOGFILE -l INFO -m "/etc/oratab FILE is written with a valid content !!!!!"


            fi
      fi

#---------------------------------------------------------------------------------------------------------------------
#                                    Adding Oracle SID to bash_profile


   logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking if ORACLE_SID is present in users bash_profile"
   logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating OracleSid Variable from OraEntry"

   #OracleSid=$(grep "$OraEntry" /etc/oratab | cut -d':' -f1,1)

   #echo $OracleSid

   if grep -Fxq "export ORACLE_SID=${OracleSid}" /home/oracle/.bash_profile ; then

                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The bash_profile File Has a  Valid Content !!!!!"


            else

                   logging -p $ProgramName -f $LOGFILE -l INFO -m "The bash_profile  Has no Valid Content !!!!!"
                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to bash_profile!!!!!"

                   echo "export ORACLE_SID=${OracleSid}" >> /home/oracle/.bash_profile
				  
				  exit_status "SID is added to users bash file !!!" "Failure writing bash_profile "

                   logging -p $ProgramName -f $LOGFILE -l INFO -m "Adding a Entry to bash_profile is Done!!!!!"



            fi
#------------------------------------------------------------------------------------------------------------------------
#                                Creating the Correct folder Structure


    logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking for the Currect Folder Structure !!!!"

    if [ ! -d /oracle/oradata/$OracleSid ] && [ ! -d /oracle/recovery_area/$OracleSid ]; then

           logging -p $ProgramName -f $LOGFILE -l WARNING -m "Correct Folder Structure  for oradata Doesnot Exist !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Correct folder Structure !!!!"

           su - oracle -c "mkdir  /oracle/oradata/$OracleSid"

		   exit_status "Correct folder Structure Created --  /oracle/oradata/${OracleSid} !!!!" "Failed writing to create /oracle/oradata/${OracleSid} "
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Changing to $OracleSid dir !!!!"

           cd /oracle/oradata/${OracleSid}
		  
		   exit_status "Changedto ${OracleSid} dir !!!!" "Failed changing to ${OracleSid} "
           
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Creating controlfile datafile onlinelog in   ${OracleSid dir} !!!!"

           su - oracle -c "mkdir  controlfile datafile onlinelog"

		   exit_status "Created controlfile datafile onlinelog in   ${OracleSid} !!!!" "Failed  to create controlfile datafile onlinelog  ${OracleSid} "
		   
           logging -p $ProgramName -f $LOGFILE -l WARNING -m "Correct Folder Structure  for recovery area Doesnot Exist !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Correct folder Structure !!!!"

           su - oracle -c "mkdir  /oracle/recovery_area/$OracleSid"
		   exit_status "Created controlfile datafile onlinelog in   ${OracleSid} !!!!" "Failed  to create controlfile datafile onlinelog  ${OracleSid} "
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct folder Structure Created !!!!"

           cd /oracle/recovery_area/$OracleSid

           logging -p $ProgramName -f $LOGFILE -l INFO -m " Changedto $OracleSid dir !!!!"
           logging -p $ProgramName -f $LOGFILE -l INFO -m " Correct three folders in $OracleSid dir !!"

           su - oracle -c "mkdir controlfile archivelog onlinelog"


    else
        echo "FOLDER STRUCTURE EXISTS"

    fi

#-----------------------------------------------------------------------------------------------------------------------------
#
    OracleHome=$(grep $OraEntry /etc/oratab | cut -d':' -f2)

    logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking if init${OracleSid}.ora exits  !!!!!"


    
   if [ ! -f $OracleHome/network/admin/listener.ora ]; then

          logging -p $ProgramName -f $LOGFILE -l WARNING -m "Listener file Does not Exists !!!!!"

          logging -p $ProgramName -f $LOGFILE -l INFO -m "Creating the Listener File on Standby Server !!!!!"
          sudo - oracle -c "touch $OracleHome/network/admin/listener.ora"
          exit_status " Listener File  successfully Created !!!" "Failed to Listener please check with the permission"
          logging -p $ProgramName -f $LOGFILE -l INFO -m "Putting the Content to the listener.ora !!!!!"


echo "LISTENER_${OracleSid}_${Port} =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = $StandbyHostName)(PORT = $Port))
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

ADR_BASE_LISTENER_$OracleSid}_${Port} = /oracle" > $OracleHome/network/admin/listener.ora

          logging -p $ProgramName -f $LOGFILE -l INFO -m "Putting the Content to the listener.ora  has been done !!!!!"

          else
		  
echo "LISTENER_${OracleSid}_${Port} =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = ${StandbyHostName})(PORT = ${Port}))
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

ADR_BASE_LISTENER_${ORacleSid}_${Port} = /oracle" > $OracleHome/network/admin/listener.ora


            
      fi

#--------------------------------------------------------------------------------------------------------------------
#                      Checking the listener status  on Standby and its owner

        var4="LISTENER_${OracleSid}_${Port}"

        logging -p $ProgramName -f $LOGFILE -l INFO -m "Checking the listener status on StandBy Server !!!!!"

              status=$(ps -ef | grep lsn | tail -n 1)

        logging -p $ProgramName -f $LOGFILE -l INFO -m "Listener Status has be Success Fully Determined !!!!!"

            echo ${status} | grep -q "tnslsnr"

			exit_status_exit "Listener is running on the Standy Server !!!!" "Listener is not running on the ${StandbyHostName} !!! Need to Start Manyally"

			logging -p $ProgramName -f $LOGFILE -l INFO -m "Listener is running on the Standy Server !!!!!"

                      owned=$(echo ${status} | cut -d ' ' -f1)
                      pid=$(echo ${status} | cut -d ' ' -f2)
					  
					
                      if [ "${owned}" == "oracle" ]; then

                             logging -p $ProgramName -f $LOGFILE -l INFO -m "IT IS FINE Listener on Stanby Server is Running as a oracle !!!!!"

                      else

                           logging -p $ProgramName -f $LOGFILE -l INFO -m "This Process should be killed and started as oracle !!!!!"
                           echo "Killing the Process"
                           logging -p $ProgramName -f $LOGFILE -l INFO -m "Killing the Process !!!!!"
                           kill  -KILL $pid
						   
						   exit_status_exit "Process is successfully killed" "Failed to to kill this process! Due to some permission issues One should have root previleges!!!"
						   logging -p $ProgramName -f $LOGFILE -l INFO -m "Starting the listener process as oracle!!!"
						   su - oracle -c "/oracle/11.2.0.4/bin/lsnrctl start ${var4}"
						   exit_status_exit "$var4 Process is successfully started as oracle!!!!!" "$var4 Failed to to kill this process! Due to some permission issues!!"
         
                    fi
					


}

DataGaurdPreInstall
