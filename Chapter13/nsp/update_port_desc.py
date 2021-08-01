import requests
import json


token = 'VEtOLWFkbWluNjg0NGE2YjQtNjIwMy00NTEwLWI2YzItMjc1MGU1MDFkZmNm'
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
port_ofn = response.json()[0]['objectFullName']

payload2 = json.dumps({
  "fullClassName": "equipment.PhysicalPort",
  "properties": {
    "description": "description added by Python program2"
  }
})

url2 = "https://10.52.90.90:8443/nfm-p/rest/api/v1/managedobjects/"+port_ofn

response = requests.request("PUT", url2, headers=headers, data=payload2, verify=False)

print(response.text)