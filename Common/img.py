from bs4 import BeautifulSoup
import requests
import os

Url = "https://wallhaven.cc/search?categories=110&purity=100&atleast=2560x1600&ratios=16x9&sorting=hot&order=desc&page="
path = "D:\\Img_Book"
Page = int(input("请输入页数进行下载: "))
Num = (Page - 1) * 24 + 1
url = Url + str(Page)


def askurl(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
        "upgrade-insecure-requests": "1"
        }
    Request = requests.get(url=url, headers=headers, timeout=3)
    Request.encoding = "utf-8"
    test = Request.text
    return test


def creat_list(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("已创建新文件夹，将开始下载")
    else:
        print("该路径已存在,将开始下载")


creat_list(path)
html = BeautifulSoup(askurl(url), "html.parser")
uls = html.find("div", attrs={"id": "thumbs"}).find_all("a", attrs={"class": "preview"})
for i in uls:
    href = i.get("href")
    Request = requests.get(href)
    Request.encoding = "utf-8"
    img_in = BeautifulSoup(Request.text, "html.parser")
    real_img = img_in.find("div", attrs={"class": "scrollbox"}).find("img").get("src")
    with open(os.path.join(path, "%s_Imgcreat.png" % Num), "ab") as f:
        f.write(requests.get(real_img).content)
    Num += 1
    print("已完成第%s图片下载" % (Num - 1))
print("已全部下载完成")
