#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    streamlit_run.py
# @Author:      ikbal
# @Time:        12/10/2023 00:00 AM

import json
import subprocess

config = json.load(open('Config/InterfaceParameters.json', 'r'))

subprocess.run(["streamlit", "run", "main.py", "--server.enableCORS=false", f"--server.port={config['streamlit_service']['port']}"])
