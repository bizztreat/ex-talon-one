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
if "customerId" in conf and conf["endpoint"]!='customers':
        print("Choose parameter \'endpoint\'=\'customers\'", file=sys.stderr)
        sys.exit(1)

if "customerId" in conf and conf["endpoint"]=='customers':
        endpoint = "https://{0}.talon.one/v1/applications/{1}/{2}/{3}".format(conf["project"], conf["application-id"], conf["endpoint"], conf["customerId"])
else:
        endpoint = "https://{0}.talon.one/v1/applications/{1}/{2}".format(conf["project"], conf["application-id"], conf["endpoint"])

headers = {"authorization":"Bearer {0}".format(conf["#bearer"])}

try:
    r = requests.get(endpoint,headers=headers,timeout=180)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh,file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc,file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt,file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err,file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(2)

content = r.text

if "customerId" in conf or conf["endpoint"]=='customers':
        dic1 = json.loads(content)
        dic=dic1['attributes']
        dic['id']=dic1['id']    
        dic['created']=dic1['created']
        dic['integrationId']=dic1['integrationId']
        dic['accountId']=dic1['accountId']
        dic['closedSessions']=dic1['closedSessions']
        dic['totalSales']=dic1['totalSales']
        dic['loyaltyMemberships']=dic1['loyaltyMemberships']
        dic['lastActivity']=dic1['lastActivity']


        f = open("/data/out/tables/{0}_{1}.csv".format(conf["endpoint"],conf["customerId"]),'w')
        w = csv.DictWriter(f, fieldnames=dic.keys())
        w.writeheader()
        w.writerow(dic)
        f.close()
        
else:
        with open("/data/out/tables/content.csv","w") as outfile:
                outfile.write(content)

