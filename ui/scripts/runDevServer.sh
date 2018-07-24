#!/bin/bash

export FLASK_APP=heirloom/ui/app.py
python3 -m flask run --port 8123 --host '0.0.0.0'