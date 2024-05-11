import re
from bs4 import BeautifulSoup
import os
import requests

Url = "https://catmigame.com/tuijiandazuo/page/"
page = 1
all_page = Url + str(page)

# def login():
#     url_login = "https://catmigame.com/tuijiandazuo"
#     Session = requests.session()
#     Session.headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"
#     }
#     re_1 = Session.get(url_login, timeout=3).content.decode()
fp = open("D:\\Url\\Game_url.txt", "w", encoding="utf-8")
fp_1 = open("D:\\Url\\Game_name.txt", "w", encoding="utf-8")


def askUrl(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
        "cookie": "__51vcke__JhraBiOlggDKrEm9=d3d40253-0db7-5513-83c2-bbd4d77af82f; __51vuft__JhraBiOlggDKrEm9=1661863612956; __51uvsct__JhraBiOlggDKrEm9=24; __51vcke__K3lg8HfyzCzvWuu8=3909dd09-2ff6-5e1d-9aaa-9a151fc4331f; __51vuft__K3lg8HfyzCzvWuu8=1684650199760; cao_notice_cookie=1; PHPSESSID=cfr60oplfn0irrpmmdqh4ra1f8; __51uvsct__K3lg8HfyzCzvWuu8=6; Hm_lvt_c728a71d259ebffe27b4f9531e8719e9=1682955262,1682995555,1684650200,1684727579; wordpress_test_cookie=WP%20Cookie%20check; __vtins__K3lg8HfyzCzvWuu8=%7B%22sid%22%3A%20%22e9c185b4-4dcf-5080-adac-dafde0b79611%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%2022671%2C%20%22dr%22%3A%2010232%2C%20%22expires%22%3A%201684729401488%2C%20%22ct%22%3A%201684727601488%7D; Hm_lpvt_c728a71d259ebffe27b4f9531e8719e9=1684727602; wordpress_logged_in_7a0a54bd167296e79134f1040bc9c1cb=liuyuheng%7C1684900411%7C9Ev9gqLWbzi9ls8RO83vOVeHc1Tgqty28Mu91NvWqsK%7C4fddf925d45ee6466fe39b1c318bc0ac6b34c88c4f8305ecbe1192ea62f97379"
    }
    Session = requests.session()
    re_1 = Session.get(url=url, headers=headers)
    soup = BeautifulSoup(re_1.text, 'html.parser')
    # Request = requests.get(url=url, headers=headers, timeout=3)
    # Request.encoding = "utf-8"
    # test = Request.text
    return soup


# print(askUrl(all_page))

for page in range(1, 2):
    all_page = Url + str(page)
    print(all_page)
    html = askUrl(all_page)
    urls = html.find("div", attrs={"class": "col-lg-1-5 col-6 col-sm-6 col-md-4 col-lg-3"}).find_all("header", attrs={"class": "entry-header"})
    print(urls)
#     for i in urls:
#         href = i.get("href")
#         Request = requests.get(href)
#         Request.encoding = "utf-8"
#         Game_in = BeautifulSoup(Request.text, 'html.parser')
#         Game_name = Game_in.find("div", attrs={"class": "cao_entry_header"}).find("a").get("title")
#         #Game_url = Game_in.find("div", attrs={"class": "content-hide-tips"}).find("p").get("href")
#         fp.write(str(Game_name))
#         #fp_1.write(str(Game_url))
# print("完成")