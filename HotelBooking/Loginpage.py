from selenium import webdriver
from HotelBooking import HotelFramework as fw
from selenium.webdriver.common.by import By

USERNAME="//input[@name='username']"
PWD="//input[@name='password']"
LOGINBTN="//input[@name='login']"


def enteringUsername(driver,username):
    fw.passingData(driver,USERNAME,username)


def enteringPassword(driver,password):
    fw.passingData(driver,PWD,password)

def clickingLoginBtn(driver):
    fw.clickingtheElement(driver,LOGINBTN)


def loginApplication(driver,name,pwd):
    enteringUsername(driver,name)
    enteringPassword(driver,pwd)
    clickingLoginBtn(driver)







