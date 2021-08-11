import requests
payload = {}
headers = {}
url = "https://10.52.90.101/rest-gateway/rest/api/v1/location/services/endpoints?endPoint=/v1/auth/token"
resp = requests.request("GET", url, headers=headers, data=payload, verify=False)
print(resp.text)
