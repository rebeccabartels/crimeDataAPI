import requests
import json

response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
    'page': 2
})
data = json.loads(response.content)
print(data['page'])
print(data['items'][0]['title'])
