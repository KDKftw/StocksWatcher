import requests
from bs4 import BeautifulSoup


# class="EquityHeaderCellStrong"


# page = requests.get("https://www.patria.cz/akcie/0ed24e40-9595-4758-ba4c-78f1ce8ca79e/moneta-money-bank/diskuze.html")
# status = page.status_code
# content = page.content
# print(status)
# print(content)


def moneta():
    url = ("https://www.patria.cz/akcie/0ed24e40-9595-4758-ba4c-78f1ce8ca79e/moneta-money-bank/diskuze.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    monprice = soup.find("td", class_="EquityHeaderCellStrong").text
    print(monprice)


def philipM():
    url = ("https://www.patria.cz/akcie/TABKbl.PR/philip-morris-cr/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    philipMprice = soup.find("td", class_="EquityHeaderCellStrong").text
    print(philipMprice)

def KB():
    url = ("https://www.patria.cz/akcie/BKOMbl.PR/komercni-banka/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    KBprice = soup.find("td", class_="EquityHeaderCellStrong").text
    print(KBprice)

def o2():
    url = ("https://www.patria.cz/akcie/SPTTbl.PR/o2-cr/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    o2price = soup.find("td", class_="EquityHeaderCellStrong").text
    print(o2price)

def avast():
    url = ("https://www.patria.cz/akcie/6c4aaf22-3613-4221-b81b-ae4957004c0d/avast-rg/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    avastPrice = soup.find("td", class_="EquityHeaderCellStrong").text
    print(avastPrice)

def erste():
    url = ("https://www.patria.cz/akcie/ERSTbl.PR/erste-bank/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    erstePrice = soup.find("td", class_="EquityHeaderCellStrong").text
    print(erstePrice)

def cez():
    url = ("https://www.patria.cz/akcie/CEZPbl.PR/cez/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    cezPrice = soup.find("td", class_="EquityHeaderCellStrong").text
    print(cezPrice)

def vig():
    url = ("https://www.patria.cz/akcie/VIGRbl.PR/vig/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    vigPrice = soup.find("td", class_="EquityHeaderCellStrong").text
    print(vigPrice)

vig()
cez()
erste()
avast()
o2()
KB()
philipM()
moneta()

import PySimpleGUI as sg

sg.Window(title="StocksWatcher", layout=[[]], margins=(400, 50)).read()
