#!/bin/bash

# packages is an array of required packages

echo -e "\nDetecting System Package Manager"
declare -a packages=("tor" "python3" "python3-pip")
if command -v apt &> /dev/null
then

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

else
  echo -e "\e[1;31mDebian Based System not Detected \e[0m"
  echo -e "\e[1;31mSkipping Auto Package Installation \e[0m"
  echo -e "\e[1;31mCheck if ${packages[@]} are Installed for your respective Distro\e[0m"
fi

#pythonPackages is an array of required python packages
declare -a pythonpackages=("requests" "PySocks")
installed=$(pip3 list --no-color)

echo -e "\nDetecting if Pip Packages are Installed"
for i in "${pythonpackages[@]}"
do
  str=$(echo $installed | grep -e "$i")
  if [[ -z $str ]]; then
    echo -e "\e[1;31m$i is not installed \e[0m"
    pip install $i
  else
    echo -e "\e[1;32m$i is installed \e[0m"
fi
done

echo ""
python3 main.py