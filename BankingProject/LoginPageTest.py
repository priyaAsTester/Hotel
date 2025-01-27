from BankingProject import Loginpage as Lp
from selenium import webdriver

def test01_Login():
    global driver
    driver = webdriver.Chrome()
    Lp.launchingBrowser(driver,"https://demo.guru99.com/")
    Lp.CreatingAccount(driver)
    Lp.verifyingUrl(driver)
    Lp.verifyinghomepage(driver)

def test02_VerifyingCreateCustomer():
    Lp.CustomerCreation(driver)


def test03_VerifyingDeleteCustomer():
    pass


def test04_VerifyingLogout():
    pass