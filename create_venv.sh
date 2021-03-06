#!/usr/bin/env bash

PYTHON_PATH=$(which python3)
VENV_DIR=venv

rm -rf $VENV_DIR
mkdir $VENV_DIR
virtualenv -p $PYTHON_PATH $VENV_DIR
. ./venv/bin/activate
pip3 install -r requirements.txt
