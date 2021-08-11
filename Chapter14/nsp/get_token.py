from base64 import b64encode
import requests
import json

message = "username" + ':' + "password!"
message_bytes = message.encode('UTF-8')
basic_token = b64encode(message_bytes)
payload = json.dumps({
    "grant_type": "client_credentials"
})
# Base token is obtained by computing base64 encoding of username and password
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic {}'.format(str(basic_token, 'UTF-8'))
}

url = "https://10.52.90.101/rest-gateway/rest/api/v1/auth/token"
resp = requests.request("POST", url, headers=headers,
                        data=payload, verify=False)
token = resp.json()["access_token"]
print(token)
