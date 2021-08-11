import requests
import json
token = 'VEtOLWFkbWluMWExNWU0MWQtMjk3Mi00YmM1LWIzMmQtMGVmNWNiNDcxOTQy'
payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
}
url = "https://10.52.90.101:8544/NetworkSupervision/rest/api/v1/ports?filter=(name='Port 1/1/1' and neId='10.172.172.172')"
resp = requests.request("GET", url, headers=headers, data=payload, verify=False)
print(resp.text)
