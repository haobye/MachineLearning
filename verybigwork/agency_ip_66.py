#!/usr/bin/env python
# coding: utf-8

# In[72]:


"""
@outher: ExclusiveName
@name: 韩崇浩
@date:2020/03/08
@note:用于爬取66免费代理，存入代理池子
"""
import re
import time
import requests
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# In[73]:


def get_home_page():
    url_list = []
    for page in range(1,6):
        if page == 1:
            page = "index"
        url = "http://www.66ip.cn/"+str(page)+".html"
        url_list.append(url)
    return url_list


# In[74]:


def get_parxy(url,charset="gb2312"):
    ua = UserAgent()
    print("正在获取网页：",url)
    response = requests.get(url,headers={"User-Agent":ua.random})
    response.encoding = charset
    html = response.text
    lines = re.findall(r'<tr><td>(.*?)</td><td>(\d+)</td><td>',html)
    return lines 


# In[75]:


def join_pond(total,lines):
    for line in lines:
        after = ":".join(line)
        complete = "http://"+after
        total.append(complete)


# In[76]:


def save_data(total,url):
    data = "\n".join(total)+"\n"
    with open("init_pond_long.txt","w",encoding="utf-8") as f:
        f.write(data)


# In[77]:


def agency_ip_one():
    total = []
    url_list = get_home_page()
    for url in url_list:
        lines = get_parxy(url)
        join_pond(total,lines)
        time.sleep(2)
    save_data(total,url)


# In[78]:


# agency_ip_one()


# In[ ]:




