import requests
import json
token = 'VEtOLWFkbWluMWExNWU0MWQtMjk3Mi00YmM1LWIzMmQtMGVmNWNiNDcxOTQy'
payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
}
print(headers)
url = "https://10.52.90.10:8544/NetworkSupervision/rest/api/v1/networkElements"
resp = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(resp.text)
