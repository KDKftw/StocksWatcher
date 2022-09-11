import requests
import time
import PySimpleGUI as sg
from bs4 import BeautifulSoup
from lxml import html
import requests

url = ('https://www.nasdaq.com/market-activity/stocks/orc/dividend-history.html')
content = requests.get(url).text

soup = BeautifulSoup(content, "html.parser")
print(content)


monprice = soup.find("td", class_="EquityHeaderCellStrong").text

