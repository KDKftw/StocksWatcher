import requests
import PySimpleGUI as sg
from bs4 import BeautifulSoup


def moneta():
    url = ("https://www.patria.cz/akcie/0ed24e40-9595-4758-ba4c-78f1ce8ca79e/moneta-money-bank/diskuze.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    monprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return monprice


def pm():
    url = ("https://www.patria.cz/akcie/TABKbl.PR/philip-morris-cr/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    pmprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return pmprice


def kb():
    url = ("https://www.patria.cz/akcie/BKOMbl.PR/komercni-banka/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    kbprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return kbprice


def o2():
    url = ("https://www.patria.cz/akcie/SPTTbl.PR/o2-cr/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    o2price = soup.find("td", class_="EquityHeaderCellStrong").text
    return o2price


def avast():
    url = ("https://www.patria.cz/akcie/6c4aaf22-3613-4221-b81b-ae4957004c0d/avast-rg/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    avastprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return avastprice


def erste():
    url = ("https://www.patria.cz/akcie/ERSTbl.PR/erste-bank/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    ersteprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return ersteprice


def cez():
    url = ("https://www.patria.cz/akcie/CEZPbl.PR/cez/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    cezprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return cezprice


def vig():
    url = ("https://www.patria.cz/akcie/VIGRbl.PR/vig/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    vigprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return vigprice


monCena = moneta()
pmCena = pm()
kbCena = kb()
o2Cena = o2()
avastCena = avast()
ersteCena = erste()
cezCena = cez()
vigCena = vig()

layout = [[sg.Text("Banky:"), sg.Text("Moneta = " + monCena, key="mon"), sg.Button("Refresh"), sg.Text("KB = " + kbCena), sg.Text("Erste = " + ersteCena)],
          [sg.Text("test")]]

window = sg.Window("dadsa", layout)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Refresh':
        window["mon"].update(moneta())

