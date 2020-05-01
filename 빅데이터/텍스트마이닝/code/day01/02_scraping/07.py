import requests

url = "http://www.naver.com"
response = requests.get(url)

print(type(response))
print(response.text)