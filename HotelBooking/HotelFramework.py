from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wt
from selenium.webdriver.support import expected_conditions as ec


def launchingBrowser(name):
    if str(name).__contains__("chrome"):
        driver = webdriver.Chrome()
    elif str(name).__contains__("firefox"):
        driver = webdriver.Firefox()
    return driver



def navigateToUrl(driver,url):
    driver.get(url)


def passingData(driver,Xpath,data):
    driver.find_element(By.XPATH,Xpath).send_keys(data)

def clickingtheElement(driver,Xpath):
    driver.find_element(By.XPATH,Xpath).click()

def clearingtheElement(driver,Xpath):
    driver.find_element(By.XPATH,Xpath).clear()

def isElementPresent(driver,Xpath):
    driver.find_element(By.XPATH,Xpath).is_displayed()

def selectByValue(driver,Xpath,value):
    Select(driver.find_element(By.XPATH,Xpath))

def selectByIndex(driver,Xpath,value):
    Select(driver.find_element(By.XPATH,Xpath)).select_by_index(value)

def selectByText(driver,Xpath,value):
    Select(driver.find_element(By.XPATH,Xpath)).select_by_visible_text(value)

def verifying_elementText(driver,Xpath,name1):
    element=driver.find_element(By.XPATH,Xpath)
    str(element.text).__eq__(name1)
    assert True

def gettingElementText(driver,Xpath):
    element=driver.find_element(By.XPATH,Xpath)
    return element.text

def gettingElementAttribute(driver,Xpath):
    element=driver.find_element(By.XPATH,Xpath)
    element_text = element.get_attribute("value")
    return element_text


def alertOk(driver):
    driver.switch_to.alert.accept()

def alertCancel(driver):
    driver.switch_to.alert.dismiss()

def alertPassingData(driver,data):
    driver.switch_to.alert.send_keys(data)


