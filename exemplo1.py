import requests

response = requests.get('http://www.americanas.com')
print(response.text)
