#------------------------------------------------------------------------------------------
# Name: KubConfig
# Description : Installs Supervisor and configures
# Author:Shailesh Thakur 
# Example ./KubConfig <bashfile>
# Version:1.0
#------------------------------------------------------------------------------------------

Target_file=$1
ProgramName=$(basename $0)

[ -z "$TimeStamp" ] && \
TimeStamp=$(date +%H%M%S%d%m%Y)

LOGFILE=/var/${ProgramName}.${TimeStamp}.log

export ProgramName
export TimeStamp
export LOGFILE

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
Kube(){

#------------------------------------------------------------------------------------------------------------
#											Setting up Supervisor
#------------------------------------------------------------------------------------------------------------

	logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "----------------------------------------------------"
	logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "	Kubenetes Configuration on VMs Started"
	logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "-----------------------------------------------------"
	
		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Setting up Supervisord on the machine !!!!!!"
		
		sudo apt-get install  supervisor -y 
		
		cmd_status_exit "SuccessFully Installed Supervisor !!!!" "Unable to Install !!!!"		
		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Starting the Supervisor !!!!!!"
		sudo service supervisor restart
		
		cmd_status_exit "Supervisor has SuccessFully started " " Supervisor start Failed"
#--------------------------------------------------------------------------------------------------------------
# 										Putting Commands in SuperVisor
#--------------------------------------------------------------------------------------------------------------


		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Creating Configuration File for SuperVisord"
		
		sudo touch /etc/supervisor/conf.d/${Target_file}.conf
		
		
		
		echo "		
[supervisord]
nodaemon=true
[program:supervisord]
command=/usr/bin/apt-get update
autostart=true
autorestart=true
stderr_logfile=/var/log/${Target_file}.err.log
stdout_logfile=/var/log/${Target_file}.out.log" > /etc/supervisor/conf.d/supervisord.conf
		
		/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
		
		sudo supervisorctl reread
		
		sudo supervisorctl update
		
		sudo service supervisor restart

}

Kube