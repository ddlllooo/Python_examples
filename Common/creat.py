import requests
from bs4 import BeautifulSoup

url = "http://219.231.219.88/eportal/InterFace.do?method=login"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
    "upgrade-insecure-requests": "1",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
post_data = {
    'userId': '2021213532',
    'password': 'B-9v40015'
}
run = requests.post(url, data=post_data, headers=headers)
print('Successful')
