#!/usr/bin/env python3

import requests
import csv
import json
import os
import sys
import traceback

conf_path = ("/data/config.json" if os.path.exists("/data/config.json") else ("/code/config.json" if os.path.exists("/code/config.json") else "config.json"))


if (not os.path.exists(conf_path)):
	print("Cannot run without configuration")
	sys.exit(0)

with open("/data/config.json","r") as conf_file:
    conf = json.load(conf_file)["parameters"]

if "#bearer" not in conf:
   print("Missing required parameter \'#bearer\'", file=sys.stderr)
   sys.exit(1)
if "endpoint" not in conf:
   print("Missing required parameter \'endpoint\'", file=sys.stderr)
   sys.exit(1)


endpoint = "{0}".format(conf["endpoint"])
headers = {"authorization":"Bearer {0}".format(conf["#bearer"])}

data = requests.get(endpoint,headers=headers)
content = data.text

with open("/data/out/tables/content.csv","w") as outfile:
  outfile.write(content)
