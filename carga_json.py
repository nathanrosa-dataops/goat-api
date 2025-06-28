import requests

url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/name/LeBron James"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
