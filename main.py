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
if "project" not in conf:
   print("Missing required parameter \'project\'", file=sys.stderr)
   sys.exit(1)
if "application-id" not in conf:
   print("Missing required parameter \'application-id\'", file=sys.stderr)
   sys.exit(1)
if "endpoint" not in conf:
   print("Choose parameter \'endpoint\'", file=sys.stderr)
   sys.exit(1)


endpoint = "https://{0}.talon.one/v1/applications/{1}/{2}".format(conf["project"], conf["application-id"], conf["endpoint"])
headers = {"authorization":"Bearer {0}".format(conf["#bearer"])}

data = requests.get(endpoint,headers=headers)
content = data.text

if "message" in content:
    print("ERROR:" ,content, file=sys.stderr)
    sys.exit(1)


with open("/data/out/tables/content.csv","w") as outfile:
  outfile.write(content)

