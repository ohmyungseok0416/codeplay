import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Window NT 10.0; Win64; x64; rv:102.0)Gecko/20100101 Firefox/102.0'}
url = "https://damoon-e.goeyp.kr/damoon-e/ad/fm/foodmenu/selectFoodMenuView.do?mi=3281"
res = requests.get(url, headers = header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

menu = soup.find("div", attrs = {"class" : "tbl_st scroll_gr"})
print(menu.find("p", attrs = {"class" : ""}).get_text())
print(menu.findAll("div".get_text))

#print(soup.find("div", attrs = {"class" : "win-llose"}).get_text())
#print(soup.find("div", attrs = {"class" : "ratio"}).get_text())