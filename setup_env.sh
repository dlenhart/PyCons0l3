#!/bin/bash

## chmod +x setup_venv.sh

# Name the virtual environment
environment_name="venv"

# Create the virtual environment
python3 -m venv $environment_name

# Activate the virtual environment
source $environment_name/bin/activate

# Install required packages
pip3 install -r requirements.txt