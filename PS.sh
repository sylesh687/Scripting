#!/bin/bash

#----------------------------------------------------------------------------------
# Name:PS.sh
# Description: This Script Prepares Primary Server For DataGaurd
# Version: 1.0
# Maintainer: Shailesh Thakur
# Example: ./PS.sh or sh PS.sh
# ---------------------------------------------------------------------------------

ROOT_UID=0
E_NOTROOT=87 

if [ "$UID" -ne "$ROOT_UID" ]
then
	echo "ONE Should must be root to execute this Script Try su - ."
 exit $E_NOTROOT
fi 

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
	logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "$1"
else
	logging -p ${ProgramName} -f ${LOGFILE} -l WARNING -m "$2"
fi
}

#---------------------------------------------------------------------------------------
#	Function to track the command Status and will terminate program during fauiure

cmd_status_exit() {
if [ $? = 0 ]
then
	logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "$1"
else
	logging -p ${ProgramName} -f ${LOGFILE} -l ERROR -m "$2"
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
# Name: PS
# Description : Creates a Pre Install Script for DataGaurd
#-----------------------------------------------------------------------------------


PS(){

		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "------------------------------------------------------"
		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "		Script Started on Primary Server 			"
		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "------------------------------------------------------"
		
		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m " Checking If User is Locked "
		
		 
      userStatus=$(passwd -S oracle | cut -d '(' -f2 | cut -d ',' -f1)
      
      actualValue="Password set"
	  
				if [ "${userStatus}" == "${actualValue}" ]; then
				
                        logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Setting Password for the oracle user !!!!"
                        echo -e "Oracle123\nOracle123" | (passwd oracle)
						
						cmd_status_exit "Password is SuccessFully Set !!!!" "Password Set Failed!!!!"
						
                        logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Password for the Oracle User is already Set and is Unlocked !!!!"

                else
				
                        logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "User Oracle is locked Need to Unlock !!!!"
                        logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Unlocking the Oracle User !!!!"
                        
						pam_tally2  -u oracle  -r
						
						cmd_status_exit "Oracle User is Successfully unlocked !!!!" "Unable to Unlock !!!!"
						
						logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Setting Password for the oracle user !!!!"
						echo -e "Oracle123\nOracle123" | (passwd oracle)
						
						cmd_status_exit "Password is SuccessFully Set !!!!" "Password Set Failed!!!!"
						 

                fi
				
			
			logging -p $ProgramName -f $LOGFILE -l INFO -m "Setting the ownership for /oracle dir !!!!"
			
            chown oracle:oinstall /oracle
			cmd_status_exit "The owenerhsip of /oracle is changed from root:root to oracle:oinstall" "Failed to to change ownership!! Due to some permission issues One Should be a root user to do so!!!"
			
			
}
