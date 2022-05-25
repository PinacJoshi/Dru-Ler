#!/bin/bash

# packages is an array of required packages
declare -a packages=("tor" "python3" "python3-pip")
for REQUIRED_PKG in "${packages[@]}"
do
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")

if [ "" = "$PKG_OK" ]; then
  echo "Setting up $REQUIRED_PKG."
  sudo apt-get --yes install $REQUIRED_PKG 
else
echo "$REQUIRED_PKG is installed"
fi
done

#pythonPackages is an array of required python packages
declare -a pythonpackages=("requests" "PySocks")
installed=$(pip3 list)

for i in "${pythonpackages[@]}"
do
str=$(echo $installed | grep -e "$i")

if [[ -z $str ]]; then
echo "$i not installed"
pip install $i
else
echo "$i installed"
fi
done

