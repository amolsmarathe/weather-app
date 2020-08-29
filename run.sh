#!/bin/bash

source venv/bin/activate
export FLASK_APP="app.py"
export FLASK_DEBUG=1
export DEPLOY=local

HOST=${1:-127.0.0.1}
python -m flask run --host=$HOST