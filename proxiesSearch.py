# -*- coding: UTF-8 -*-

import requests as r
from bs4 import BeautifulSoup as bs
from threading import Thread
from Queue import Queue
from datetime import datetime

NUM_THREADS = 8
# 檔案輸出的位置
exportPath = "E:/Python/IP/ips.txt"
#  用痞客邦做測試是否能連線
# testUrl = "https://www.pixnet.net/searcharticle?q=%E8%A6%AA%E5%AD%90%E9%A4%90%E5%BB%B3&page=1"
testUrl = "http://you.ctrip.com/"
# testUrl = "https://www.expedia.com.tw/"
# testUrl = "http://www.booking.com/"
# 抓PROXY的網址
baseUrl = "https://incloak.com/proxy-list/?type=h&start={}#list"

queue = Queue();
ipSet = set()

def crawler(page):
    n = 0
    url = baseUrl.format(page)
    res = r.get(url)
    soup = bs(res.text,"lxml")
    proxies = soup.findAll("td")
    ips = ""
    for j, proxy in enumerate(proxies):
        if (j+1) % 7 == 1:
            ip = proxy.text.strip()
        if (j+1) % 7 == 2:
            port = proxy.text.strip()
            ips = ip + ":" + port
            proxy = {"http": "http://{}".format(ips)}
            try:
                n += 1
                res = r.get(testUrl, proxies=proxy, timeout=5)
                if res.status_code==200:
                    # print res.text
                    ipSet.add(ips)
                    print "res200"
            except:
                pass

def worker():
    while not queue.empty():
        page=queue.get()
        crawler(page)

for i in range(0, 8):
    page = 64 * i
    queue.put(page)

s1 = datetime.now()
try:
    # 設定THREAD數量及執行的FUNCTION
    threads = map(lambda i: Thread(target=worker), xrange(NUM_THREADS))
    # 啟動THREAD
    map(lambda th: th.start(), threads)
    map(lambda th: th.join(), threads)
except:
    print "thread error"
finally:
    s2 = datetime.now()
    with open(exportPath, "w") as f:
        for item in ipSet:
            print item
            f.write(item+"\n")
        f.close()
    print "All  Finish - " + str(s2 - s1) + "!!"
#All  Finish - 0:08:36.199000!!