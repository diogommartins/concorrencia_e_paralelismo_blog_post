import requests

urls = (
    'http://www.americanas.com',
    'http://www.submarino.com',
    'http://www.shoptime.com',
    'http://www.soubarato.com',
)

for url in urls:
    response = requests.get(url)
    print(response.text)
