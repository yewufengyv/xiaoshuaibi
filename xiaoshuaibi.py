import requests
from time import sleep
from pymongo import MongoClient
import re
from tqdm import tqdm


if __name__ == '__main__':
    cli = MongoClient('127.0.0.1:27017')
    db = cli.xiao
    jiaocheng = db.jiaocheng
    jiaocheng.drop()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 xingganpachong zaixianpaqvyoujiezhi",
        "cookie": "_ga=GA1.3.508727218.1587809193; _gid=GA1.3.1938797817.1587809193; _gat_gtag_UA_131395348_1=1"
    }
    for i in tqdm(range(1, 6)):
        k = 0
        if i == 1:
            web = 'https://wistbean.github.io/categories/python/'
        else:
            web = 'https://wistbean.github.io/categories/python/' + 'page/' + str(i) + '/'
        req = requests.get(web, headers=headers)
        com = re.compile('<a class="post-title-link.*?href="(.*?)">.*?</a>\n', re.S)
        lianjie = re.findall(com, req.text)
        co=re.compile('<a class="post-title-link" href=".*?">(.*?)</a>')
        neirong=re.findall(co,req.text)
        #print(lianjie,neirong)
        for i in lianjie:
            p='https://wistbean.github.io'+str(i)
            b={}
            #breakpoint()
            b={'neirong':neirong[k],'lianjie':p}
            #breakpoint()
            jiaocheng.insert_one(b)
            k=k+1
            #print(b)
    print("Data crawl completed")
