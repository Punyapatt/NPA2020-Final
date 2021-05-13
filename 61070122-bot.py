import requests
import json
import time
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url_read = "https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3"

payload={}
headers = {
  'Authorization': 'Bearer ZDY3ZGNkNzctOGM5MS00NTdhLWIxYWEtOWRhMTIzYjhhMGJiZTViYmIzNmMtMzVj_PF84_consumer',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url_read, headers=headers, data=payload)

# print(response.json())

def printBytesAsJSON(bytes):
	print(json.dumps(json.loads(bytes), indent=2))



# response = requests.get(
# 	url = 'https://10.0.15.109/restconf/data/ietf-interfaces:interfaces/interface=Loopback61070122',
# 	auth = ('admin', 'cisco'),
# 	headers = {
# 		'Accept': 'application/yang-data+json'
# 	},
# 	verify = False)



# Pretty print our JSON response
# printBytesAsJSON(response.content)

# data = response.json()
# status_int = data["ietf-interfaces:interface"]["enabled"]

old = ""
while(1):
    print('start')
    response = requests.get(
        url = 'https://10.0.15.109/restconf/data/ietf-interfaces:interfaces/interface=Loopback61070122',
        auth = ('admin', 'cisco'),
        headers = {
            'Accept': 'application/yang-data+json'
        },
        verify = False)
    data = response.json()
    status_int = data["ietf-interfaces:interface"]["enabled"]


    response_ms = requests.request("GET", url_read, headers=headers, data=payload)
    response_ms = response_ms.json()
    new_ms = response_ms['items'][0]['text']
    print(new_ms)
    if new_ms != old: 
        if new_ms == "61070122":
            if status_int == True:
                payloads = json.dumps({
                    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3",
                    "text": "Loopback61070122 - Operational status is up"
                })
            else:
                payloads = json.dumps({
                    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3",
                    "text": "Loopback61070122 - Operational status is down"
                })
            send = requests.request("POST", url_read, headers=headers, data=payloads)
    old = new_ms
    time.sleep(1)






