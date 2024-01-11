#!/bin/bash
## Copyright (c) Microsoft Corporation. All rights reserved.

rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
deactivate
