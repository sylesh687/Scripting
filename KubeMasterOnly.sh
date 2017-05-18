#------------------------------------------------------------------------------------------
# Name: KubMasterOnly
# Description : Configures Master 
# Author:Shailesh Thakur 
# Version:1.0
#------------------------------------------------------------------------------------------
 
ROOT_UID=0
E_NOTROOT=87  

ProgramName=$(basename $0)

[ -z "$TimeStamp" ] && \
TimeStamp=$(date +%H%M%S%d%m%Y)

LOGFILE=/var/${ProgramName}.${TimeStamp}.log

export ProgramName
export TimeStamp
export LOGFILE


if [ "$UID" -ne "$ROOT_UID" ]
then
 echo "Must be root to run this script."
 exit $E_NOTROOT
fi
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

	logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Creating kube-install  directory"
	
		mkdir /opt/kube-install
		
		cmd_status_exit " kube-install SuccessFully created !!!!" "Unable to Create  kube-install !!!!"
		
		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Changing dir to  kube-install "
		cd /opt/kube-install
		cmd_status_exit " Changing to kube-install SuccessFully Done !!!!" "Unable to Change to  kube-install !!!!"
		logging -p ${ProgramName} -f ${LOGFILE} -l INFO -m "Cloning kubernetes project from git  "
		git clone --depth 1 https://github.com/kubernetes/kubernetes.git 
		cmd_status_exit " SuccessFully cLoned !!!!" "Error Cloning !!!!"
		
		
}
Kube
