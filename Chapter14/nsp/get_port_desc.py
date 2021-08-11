import requests
import json

token = 'VEtOLWFkbWluYTIyNTIzODktNmZhYy00ZGU2LTg5ZjUtYTEyMDc4ZmQwMTdl'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
}

url1 = "https://10.52.90.90:8443/nfm-p/rest/api/v1/managedobjects/searchWithFilter"
payload1 = json.dumps({
  "fullClassName": "equipment.PhysicalPort",
  "filterExpression": "siteId = '10.172.172.172' AND portName='1/1/1'",
  "resultFilter":[
    "objectFullName",
    "description"
  ]
})
response = requests.request("POST", url1, headers=headers, data=payload1, verify=False)
print(response.json()[0]['objectFullName'])
print(response.json()[0]['description'])