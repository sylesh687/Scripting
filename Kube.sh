#------------------------------------------------------------------------------------------
# Name: Kube
# Description : Installs Supervisor and configures on 
# Author:Shailesh Thakur 
# Version:1.0
#------------------------------------------------------------------------------------------


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


		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Updating the system"
		
			sudo apt-get update 
			
			cmd_status_exit "System Update Successfull" "System update failed !! Check ur Internet Connection "
			
			logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Installing Bride Utils"
			
				sudo apt-get install -y apt-transport-https ca-certificates bridge-utils
				
				cmd_status_exit "Bridge utils installation Successfull" "Bridge utils installation !! Check ur Internet Connection "
				
				logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Adding Keys !!!"
				
				sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
				
				cmd_status_exit "Keys were added SuccessFully" "Key Addition Failed!! "
				
				echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | sudo tee /etc/apt/sources.list.d/docker.list 
				
				logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Updating the system again "
				sudo apt-get update
				cmd_status_exit "System Update Successfull" "System update failed !! Check ur Internet Connection "
				
				sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual 
				
				logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Installing Docker Engine "
				sudo apt-get install -y docker-engine
				cmd_status_exit "Docker Engine Was SuccessFully Installed " "Docker Installation Failed!! "
				logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Staring Docker !!! "
				sudo service docker start
				cmd_status_exit "Docker Engine Was SuccessFully Started " "Docker Start Failed!! "
				
				logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Adding a Group Docker !!! "
				sudo groupadd docker
				
				cmd_status_exit "Docker group was SuccessFully Added " "Docker group addition  Failed!! "
				
				logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Adding a User to  Group Docker !!! "
				sudo usermod -aG docker $USER
				
				cmd_status_exit "${USER} to Docker group was SuccessFully Added " "${USER} to Docker group addition  Failed!! "
				
				
				
				
				
				
				
				

}
Kube
