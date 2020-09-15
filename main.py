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


moneta()

import PySimpleGUI as sg
sg.Window(title="StocksWatcher", layout=[[]], margins=(400, 50)).read()