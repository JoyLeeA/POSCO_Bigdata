import requests
import datetime

url = "https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw"
resp = requests.get(url)
data = resp.json()

timestamp = data['timestamp']
last = data['last']
ts = datetime.datetime.fromtimestamp(timestamp/1000)

print(ts)
print(last)
