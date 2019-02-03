# Talon.one writer

## What It Does

Download a file with the triggered effects or coupon.

https://developers.talon.one/Management-API/API-Reference

### Allowed data objects to extract
- extract coupons
- extract Effects

All the objects are mapped to output as CSV file

#### extract coupons

["id","created","campaignid","value","expirydate","startdate","attributes","applicationid","deleted","deleted_changelogid","accountid","referralid","recipientintegrationid","importid","batchid","counter","limitval"]

Represents coupon data

- "id": Id of the specific coupon
- "created": Timestamp YYYY-MM-DDTHH:mm:ssZ
- "campaignid": Id of the specific campaign
- "value": coupon number
- "expirydate": Timestamp YYYY-MM-DDTHH:mm:ssZ
- "startdate": Timestamp YYYY-MM-DDTHH:mm:ssZ
- "attributes":  format example: "{""Key1"": ""value"", ""Key2"": ""value""}"
- "applicationid": Id of the specific application
- "deleted": Boolian value
- "deleted_changelogid"
- "accountid"
- "referralid"
- "recipientintegrationid": customer Id
- "importid"
- "batchid"
- "counter"
- "limitval": is integer

#### extract Effects

["created","name","applicationid","campaignid","rulesetid","ruleindex","sessionintegrationid","profileintegrationid","sessionid","profileid","eventid","event_type","total_revenue","args"]

Represents Effects data

- "created": Timestamp YYYY-MM-DDTHH:mm:ssZ
- "name": Name of Effect
- "applicationid": Id of the specific application
- "campaignid": Id of the specific campaign
- "rulesetid": Id of the specific rules
- "ruleindex": Index of the specific rules
- "sessionintegrationid": Id of the specific session
- "profileintegrationid":
- "sessionid": Id of the specific session
- "profileid": Id of the specific profile
- "eventid": Id of the specific event
- "event_type":
- "total_revenue":
- "args":


## Configuration


### Parameters

from endpoint
https://example.talon.one/v1/applications/42/endpoint

<pre>
{
  "project": "<example>",
  "application-id": <id>,
  "endpoint": "<endpoint>",
  "#bearer": "$YOUR_TOKEN"
}
</pre>


- `endpoint` is an endpoint of the service (choose from 2 available)
- `#bearer` is your secret token
- `project` is your name of organization
- `application-id` is your application id

## Contact

BizzTreat, s.r.o
Řehořova 968/42
Prague

If you have any question contact support@bizztreat.com

Cheers!
