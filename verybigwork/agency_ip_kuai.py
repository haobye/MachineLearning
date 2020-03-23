#!/usr/bin/env python
# coding: utf-8

# In[154]:


"""
@outher: ExclusiveName
@name: 韩崇浩
@date:2020/03/08
@note:用于爬取快代理，存入代理池子
"""
import re
import time
import requests
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# In[155]:


def get_home_page(total):
    urls = ["https://www.kuaidaili.com/free/inha/"+str(page)+"/" for page in range(1,3)]
    for url in urls[:6]:
        ua = UserAgent()
        print("正在获取网页：",url)
        response = requests.get(url,headers={"User-Agent":ua.random})
        response.encoding = "utf-8"
        html = response.text
        soup = BeautifulSoup(html,"lxml")  
        lines = soup.select("tr > td")
        line = re.findall(r'<td data-title="IP">(.*?)</td>, <td data-title="PORT">(.*?)</td>',str(lines))
        for item in line:
            total.append(item)
        time.sleep(2)


# In[156]:


def save_data(total):
    with open("init_pond_sort.txt","w",encoding="utf-8") as f:
        for tup in total:
            f.write(tup[0]+','+tup[1]+"\n")


# In[157]:


def agency_ip_two():
    total = []
    get_home_page(total)
    save_data(total)


# In[158]:


# agency_ip_two()


# In[ ]:


def test():
    print("这里是快代理的爬取代码")

