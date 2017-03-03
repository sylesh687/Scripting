#!/bin/bash

userowner=$(ls -al / | grep oracle | cut -d ' ' -f4)
grpowner=$(ls -al / | grep oracle | cut -d ' ' -f5)


while getopts u:p:s: req;do
        case $req in
        u)username=$OPTARG;;
        p)primaryServer=$OPTARG;;
        s)standByServer=$OPTARG;;
        esac

done

pass=$(grep "$username" /etc/shadow | cut -d ':' -f2)
extract=${pass:0:1}
if [ $extract == '!' ]; then
        echo "The User is locked Need to Unlock"
        echo "unlocking $username"
        passwd -u $username
        echo "User is Unlocked Successfully"
else
        echo "User is actiive:"
fi

echo "Copying listener.ra from Primary  to STDBY"

        su - oracle -c "scp oracle@$primaryServer:/oracle/11.2.0.4/network/admin/listener.ora  oracle@$standByServer:/oracle/11.2.0.4/network/admin/ "

if [ $? -eq 0 ]; then

        echo "Listener.ora is copied from $primaryServer to $standByServer"
else

        echo "Failed to to copy !! Due to some permission issues"

fi

echo "Checking the hostname of the system"

        currHost=$(hostname)

if [ $currHost == $primaryServer ]; then

        echo "Login to the Seconday Server "
        ssh -l $user $standByServer
        echo "Edit the listener file on the Standby"
        echo "Check the Ownership of /oracle dir"
        echo "If it is own by root then change to oracle:oinstall"
		
		
        if [ $userowner -eq "oracle" ] && [ $grpowner -eq "oinstall" ]; then
		              echo "Permission is correctly set "
        else
                chown oracle:oinstal /oracle
                echo "Changing the Ownership of /oracle"
        fi
else
        echo "Edit the Listener ORA FILE "
fi

