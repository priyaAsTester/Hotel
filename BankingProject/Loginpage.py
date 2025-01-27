import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from BankingProject import bankingframework as bfw


def launchingBrowser(driver,url):

    driver.maximize_window()
    driver.get(url)

def CreatingAccount(driver):

    bfw.passingData(driver,"//input[@name='emailid']","testerbee742@gmail.com")
    bfw.clickingTheElement(driver,"//input[@type='submit']")
    bfw.clickingTheElement(driver,"//a[text()='Bank Project']")
    bfw.passingData(driver,"//input[@type='text']","mngr604283")
    bfw.passingData(driver,"//input[@type='password']","AdUpuvy")
    bfw.clickingTheElement(driver,"//input[@type='submit']")

def verifyingUrl(driver):

    url="https://demo.guru99.com/V1/html/Managerhomepage.php"
    homepageURl=driver.current_url
    if homepageURl.__contains__(url):
        assert True

def verifyinghomepage(driver):
    title="Guru99 Bank Home page"
    homepagetitle=driver.title
    if homepagetitle.__contains__(title):
        assert True

def CustomerCreation(driver):

    bfw.clickingTheElement(driver,"//a[text()='New Customer']")
    bfw.passingData(driver,"//input[@type='text']","sriya")
    bfw.clickingTheElement(driver,"(//input[@type='radio'])[2]")
    bfw.passingData(driver,"//input[@type='date']","25-12-2024")
    bfw.passingData(driver,"//textarea[@rows='5']","4,bourbon street")
    bfw.passingData(driver,"//input[@name='city']","chennai")
    bfw.passingData(driver,"//input[@name='state']","Tamilnadu")
    bfw.passingData(driver,"//input[@name='pinno']","600197")
    bfw.passingData(driver,"//input[@name='telephoneno']","6087888887")
    bfw.passingData(driver,"//input[@name='emailid']","abcd@gmail.com")
    bfw.clickingTheElement(driver,"//input[@type='submit']")
    time.sleep(20)
    print("Customer created")

