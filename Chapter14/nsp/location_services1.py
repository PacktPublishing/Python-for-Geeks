import requests
payload = {}
headers = {}
url = "https://10.52.90.10/rest-gateway/rest/api/v1/location/services"
resp = requests.request("GET", url, headers=headers, data=payload, verify=False)
print(resp.text)
