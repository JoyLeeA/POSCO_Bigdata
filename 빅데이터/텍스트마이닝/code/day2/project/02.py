import requests
import pandas as pd

client_id = "kV9KBToXgWIqyXY3CGjB"
client_secret = "tcQXerzca7"

url = "https://openapi.naver.com/v1/search/book.json?query=파이썬"
headers = {
    "X-Naver-Client-id": client_id,
    "X-Naver-Client-Secret": client_secret,
}

resp = requests.get(url, headers=headers)
resp = resp.json()
data = resp['items']

# DataFrame
df = pd.DataFrame(data=data)
print(df)
