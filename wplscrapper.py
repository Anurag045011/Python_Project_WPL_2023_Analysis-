# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:07:28 2023

@author: Anurag
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.wplt20.com/auction"
r=requests.get(url)
# print(r)
soup = BeautifulSoup (r.text, "lxml")
# print(soup)
table = soup.find("div", class_="table")
title = table.find_all("div")
# print(title)
#print(table)
header=[]
for i in title:
    name=i.text
    header.append(name)

df=pd.DataFrame(columns=header)

rows = table.find_all("tr")

for i in rows[1:]:
   first_td=i.find_all("td")[0].find("div", class_ = "table-row batter").text.strip() 
   data =i.find_all("div")[1:]
   row =[tr.text for tr in data]
   # print(row)
   row.insert(0, first_td)
   l = len(df)
   df.loc[l]= row

print(df)
df.to_csv("ipl Auction stats.csv")