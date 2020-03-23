#!/usr/bin/env python
# coding: utf-8

# In[19]:


"""
@outher: ExclusiveName
@name: 韩崇浩
@date:2020/03/08
@note:用于清洗代理，合格的放入另一个代理池中
"""
import time
import random
import requests
import telnetlib
from fake_useragent import UserAgent
# from agency_ip_66 import *
# from agency_ip_kuai import *


# In[20]:


def check_long():
    with open("init_pond_long.txt","r",encoding="utf-8") as f:
        content = f.readlines() 
    succeed = []
    for agency in content:
        try:
            ua = UserAgent()
            response = requests.get("http://icanhazip.com/",headers={"User-Agent":ua.random},proxies={"http":agency[:-2]},timeout=5)
            print(response.status_code)
            print(response.text)
            if agency.split(":")[1][2:] == response.text:
                print("解析成功：",agency)
                agency = agency.strip()
                succeed.append("\""+agency.split(":")[0]+"\":\""+agency+"\"")
            else:
                print("解析失败：",agency)
        except:
            print("解析失败：",agency)
    print("本次加入合格代理池中有{}个。".format(len(succeed)))
    with open("succ_pond.txt","a",encoding="utf-8") as f:
        f.write("\n".join(succeed))


# In[87]:


def check_sort():
    succeed = []
    with open("init_pond_sort.txt","r",encoding="utf-8") as f:
        content = f.readlines() 
    for line in content:
        ip,port = line.strip().split(",")
        try:
            telnetlib.Telnet(ip,port,timeout=2)
            print("代理有效：{}:{}".format(ip,port))
            succeed.append('\"http\":\"http://'+ip+":"+port+'\"')
        except:
            print("代理失效：{}:{}".format(ip,port))
    print("本次加入合格代理池中有{}个。".format(len(succeed)))
    with open("succ_pond.txt","a",encoding="utf-8") as f:
        f.write("\n".join(succeed))


# In[89]:


"""
@outher: ExclusiveName
@name: 韩崇浩
@date:2020/03/08
@note:爬取各个网页的代理并进行合格检查,使用多线程
"""
def check_agency():
    agency_ip_66.agency_ip_one()
    agency_ip_kuai.agency_ip_one()
    check_long()
    check_sort()


# In[85]:


"""
@outher: ExclusiveName
@name: 韩崇浩
@date:2020/03/08
@note:调用此方法，返回parxy直接使用
"""
def use_agency():
    with open("succ_pond.txt","r",encoding="utf-8") as f:
        content = f.readlines()
    try:
        res = content.pop(random.randint(0,len(content)))
        with open("succ_pond.txt","w",encoding="utf-8") as f:
            f.write("".join(content))
        return res.strip()
    except:
        print("代理池已空，正在补充")
#         check_agency()


# In[86]:


# use_agency()


# In[ ]:


# check_agency()


# In[88]:


# check_sort()


# In[ ]:




