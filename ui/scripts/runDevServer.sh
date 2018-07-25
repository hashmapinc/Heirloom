#!/bin/bash

export FLASK_APP=heirloom/ui/main.py
export FLASK_DEBUG=1
python3 -m flask run --port 8123 --host '0.0.0.0'