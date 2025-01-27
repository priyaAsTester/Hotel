from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def passingData(driver,locator,data):
    driver.find_element(By.XPATH,locator).send_keys(data)

def clickingTheElement(driver,locator):
    driver.find_element(By.XPATH,locator).click()
