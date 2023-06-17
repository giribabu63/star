#imporing module
import requests
from bs4 import BeautifulSoup
import csv
import pandas as p

#url of the flipkart pageto scrape
url="https://www.flipkart.com/search?q=mobiles+5g"

#send get request to the  url
response=requests.get(url)
#create beautifulsoup object to parser the html content
soup=BeautifulSoup(response.content, "lxml")

#find the desired eement on the page using css selectors
title=soup.find_all('div',class_="_2kHMtA")
reviews=soup.find_all('span',class_="_2_R_DZ")
price = soup.find_all('div',class_="_30jeq3 _1_WHN1")

mt=[]
mr=[]
mp=[]

for title,reviews,price in zip(title,reviews,price):
    mt.append(title.text)
    mr.append(reviews.text)
    mp.append(price.text)
print(mt, mr,mp)




