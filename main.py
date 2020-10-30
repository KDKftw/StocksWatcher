import requests
import time
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

def pilule():
    url = ("https://www.patria.cz/akcie/e5420968-1c02-44ef-baaa-9ee6809b666e/pilulka-lekarny/online.html")
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    piluleprice = soup.find("td", class_="EquityHeaderCellStrong").text
    return piluleprice


def refreshAll():
    window["erste"].update("Erste123 = " + erste())
    window["mon"].update("MMB = " + moneta())
    window["kb"].update("KB = " + kb())
    window["PM"].update("PM = " + pm())
    window["O2"].update("O2 = " + o2())
    window["cez"].update("CEZ = " + cez())
    window["avast"].update("Avast = " + avast())
    window["vig"].update("VIG = " + vig())
    window["pilule"].update("Pilule = " + pilule())

def timeRefresh():
    while True:
        x = 0
        if x < 10:
            time.sleep(1)
            x+1
        else:
            refreshAll()





ersteCena = erste()
kbCena = kb()
monCena = moneta()

pmCena = pm()
o2Cena = o2()
cezCena = cez()

avastCena = avast()
vigCena = vig()
piluleCena = pilule()

layout =[[sg.Text("Banky:"), sg.Text("MMB = " + monCena, key="mon"), sg.Button("RFmb"), sg.Text("KB = " + kbCena, key="kb"), sg.Button("RFkb"), sg.Text("Erste = " + ersteCena, key="erste"), sg.Button("RFes")],
        [sg.Text("2:"), sg.Text("PM = " + pmCena, key="PM"), sg.Text("O2 = " + o2Cena, key="O2"), sg.Text("CEZ = " + cezCena, key="cez")],
        [sg.Text("3:"), sg.Text("Avast = " + avastCena, key="avast"), sg.Text("VIG = " + vigCena, key="vig"), sg.Text("Pilule = " + piluleCena, key="pilule" )],
        [sg.Button("REFRESH ALL")],
         [sg.Text("ahoj"), sg.Image(r"C:\Users\KDK\Desktop\StocksWatcher\Photos\greenUP.png")]]


window = sg.Window("Stocks Watcher", layout)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'RFmb':
        window["mon"].update("MMB = " + moneta())
    if event == 'RFkb':
        window["kb"].update("KB = " + kb())
    if event == 'REFRESH ALL':
        refreshAll()

while True:
    timeRefresh()



