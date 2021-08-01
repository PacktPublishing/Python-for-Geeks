import requests

token = 'VEtOLWFkbWluMDE5NDdhZWUtMjRjZi00ZjEwLTg5MDItYzBhNTdjOGU2NGE2'

url = "https://10.52.90.101:8544/nbi-notification/api/v1/notifications/subscriptions"

def create_subscription(category):
  headers = {'Authorization': 'Bearer {}'.format(token) }
  subscription = {
      "categories": [
        {
          "name": "{}".format(category)
        }
      ]
  }
  #print(subscription)
  response = requests.request("POST", url, json=subscription,
                              headers=headers, verify=False)
  print(response.text)

  subscriptionId = response.json()["response"]["data"]["subscriptionId"]
  topicId = response.json()["response"]["data"]["topicId"]
  timeOfSubscription = response.json()["response"]["data"]["timeOfSubscription"]
  expiresAt = response.json()["response"]["data"]["expiresAt"]
  sub_data = [subscriptionId,topicId,timeOfSubscription,expiresAt]
  print(sub_data)
  return sub_data

if __name__ == '__main__':
      #create_subscription("NSP-EQUIPMENT")
      create_subscription("NSP-PACKET-ALL")