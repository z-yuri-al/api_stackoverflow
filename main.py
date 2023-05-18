import requests
import time

url = 'https://api.stackexchange.com/2.3/questions'
from_date = int(time.time() - 86400 * 2)
to_date = int(time.time())
params = {
            "fromdate": from_date,
            "todate": to_date,
            "order": "desc",
            "sort": "activity",
            "site": "stackoverflow",
            "tagged": 'python'
        }
responce = requests.get(url=url, params=params)
result = responce.json()
for i in result['items']:
    print(i['title'])