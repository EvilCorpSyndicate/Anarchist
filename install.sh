#!/bin/sh
echo "WARNING: This script will install the requirements AND add it as an apt source."
echo ""
echo "If you do not want this, please press ctrl + C to cancel the script."
echo ""
echo "The script will start in 10 seconds."

sleep 10

echo "Running Anarchist app setup..."

# Install Python if necessary
which python3 > /dev/null
status=$?

if test $status -ne 0
then
	echo "Installing Python 3.6..."
	apt-get install python3.6 -y

else
	echo "Confirmed Python is installed."
	
	# Installs Pip even if a Python installation is found because some users don't install pip
	
	sudo apt install python3-pip

    ## Install Python Packages
    echo "Installing Python packages..."
    pip3 install -r requirements.txt
