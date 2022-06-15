from requests import request
from updateChecker import checkForUpdates
import json
import requests
import os

url = "https://maker.ifttt.com/trigger/website_changed/json/with/key/"

ifttt_key = os.getenv("IFTTT_KEY")
ifttt_event_name = os.getenv("IFTTT_EVENT_NAME")

# "dxVc2lttXOQyrvtwUD4_qA"

request_url = url + ifttt_key

payload = json.dumps({
  "update": checkForUpdates()
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
