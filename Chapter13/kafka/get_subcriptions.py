import requests

token = 'VEtOLWFkbWluNjg0NGE2YjQtNjIwMy00NTEwLWI2YzItMjc1MGU1MDFkZmNm'

NSP_KAFKA_API = url = "https://10.52.90.101:8544/nbi-notification/api/v1/notifications/subscriptions"

def get_subscription():
  headers = {'Authorization': 'Bearer {}'.format(token) }

  response = requests.request("GET", url, data={}, headers=headers, verify=False)
  print(response.text)


if __name__ == '__main__':
      get_subscription()