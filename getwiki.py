import requests, urllib3, urllib,time
from bs4 import BeautifulSoup
from selenium import webdriver
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 截图网页保存


def capture(url, name):
    browser = webdriver.PhantomJS()  # 被标记过时了
    browser.set_window_size(1200, 900)
    browser.get(url)
    print(name)
    browser.save_screenshot(name)
    browser.close()


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
# 代理
proxies = {
    'http': '127.0.0.1:8087',
    'https': '127.0.0.1:8087'
}

filename_list = [file_ for file_ in os.listdir("./keywords") if ".txt" in file_]
print(filename_list)


# 逐行读关键字 保存文字
# with open('1data.txt', 'a', encoding='utf-8') as wf:
#     with open('1.txt', 'r') as f:
#         for line in f:
#             pic_name = line.strip()+'.png'
#             capture('https://zh.wikipedia.org/wiki/'+urllib.parse.quote(line.strip()), pic_name)
#             res = requests.get('https://zh.wikipedia.org/wiki/'+urllib.parse.quote(line.strip()),
#                                proxies=proxies, verify=False, headers=headers)  # 不做SSl证书认证
#             soup = BeautifulSoup(res.text, 'lxml')
#             contents = soup.select('.mw-body-content')
#             wf.write(contents[2].get_text())
def get_pic(file):
    with open(os.path.join("./keywords", file), 'r', encoding='utf-8') as f:
        for line in f:
            pic_name = line.strip()+'.png'
            res = requests.get('https://zh.wikipedia.org/wiki/'+urllib.parse.quote(line.strip()),
                                   proxies=proxies, verify=False, headers=headers)  # 不做SSl证书认证
            soup = BeautifulSoup(res.text, 'lxml')
            contents = soup.select('.mw-body-content')
            cont = contents[2].get_text()
            if '维基百科目前还没有与上述标题' not in cont:
                capture('https://zh.wikipedia.org/wiki/'+urllib.parse.quote(line.strip()), pic_name)
            else:
                print(line.strip()+'不存在')


for filename in filename_list:
    try:
        get_pic(filename)
    except Exception as e:
        print(e)



