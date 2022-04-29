#!/bin/bash

#Install Script for Debian Based Systems
PACKAGESTOINSTALL=""
COUNTER=0

#Checks if apt Package Manager is Present
if [ -x "$(command -v apt)" ]
then

    if [ -x "$(command -v tor)" ]
    then
        echo "Tor Proxy is Installed"
    else
        PACKAGESTOINSTALL+=" tor"
        COUNTER += 1
    fi

    if [ -x "$(command -v python3)" ]
    then 
        echo "Python3 is Installed"
    else
        PACKAGESTOINSTALL+=" python3"
        COUNTER += 1
    fi

    if [ -x "$(command -v pip3)" ]
    then
        echo "Pip3 is Installed"
    else
        PACKAGESTOINSTALL+=" python3-pip"
        COUNTER += 1
    fi

else
echo "Linux Distro NOT supported"
#Exits Code if Distro is NOT supported
exit 1
fi

#Checks if there is need to install the Required Packages
if [ $COUNTER -gt 0 ]
then
    echo "test"
    sudo apt update
    sudo apt install $PACKAGESTOINSTALL
fi

#Executes main.py
python3 main.py