#!/bin/bash

datagen_model_name=$1

if [ "$datagen_model_name"x == "x" ]; then
  echo "Usage: test.sh DATAGEN_MODEL_NAME"
	exit -1
fi

venv_directory="venv_"$datagen_model_name

# Check if $venv_directory exists ?

source $venv_directory/bin/activate

# Run the Python DataGen_MODEL
