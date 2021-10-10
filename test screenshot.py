import pyautogui
from os import path

def udelejSS(nazev):
    roughPath = r"C:\Users\KDK\Desktop\screenshot_test\t"
    actualPath = roughPath+nazev
    print(actualPath)

    pyautogui.screenshot(roughPath + nazev)



def passengerName(pocetCestujicich):
    pocetCestujicich=str(pocetCestujicich)
    locator = "room.0.passenger." + pocetCestujicich + ".name.first"
    print(locator)
    return locator

passengerName(2)