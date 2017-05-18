#-----------------------------------------------------------------------
# Write a script that upon invocation shows the time and date, lists all logged-in users, and gives the
# system uptime. The script then saves this information to a logfile
#-----------------------------------------------------------------------

ProgramName=$(basename $0)
LOGFILE=/var/log/${ProgramName}.log

#--------------------------------------------------
# FINDING DATA AND TIME 

date "+DATE:  %m/%d/%y%n TIME: %H/%M/%S" >> ${LOGFILE}

#--------------------------------------------------
#  Finding the List of logged in Users

users >> ${LOGFILE}

#--------------------------------------------------
#  System Uptime 

uptime >> ${LOGFILE}



