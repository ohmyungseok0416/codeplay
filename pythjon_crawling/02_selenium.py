import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://comic.naver.com/webtoon?tab=fri"

browser.get(url)
time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")

top5 = soup.find("ul", attrs = {"class" : "ContentList__content_list--q5KXY"})
t5_title = top5.findAll("span", attrs = {"class" : "ContentTitle__title--e3qXt"})
t5_author = top5.findAll("span", attrs = {"class" : "Rating__star_area--dFzsb"})

print("------금요웹툰 20개------")

for i in range(20):
    print(f"{i+1}순위 웹툰 제목 : {t5_title[i].text} / 작가 : {t5_author[i].text}")
#for j in top3[:10]:
#print(j.text)