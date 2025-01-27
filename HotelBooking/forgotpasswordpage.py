from HotelBooking import HotelFramework as fw

FORGOTPWD="//div[@class='login_forgot']/child::a"
EMAILID="//input[@name='emailadd_recovery']"
EMAILPWDBTN="//input[@value='Email Password']"
RESET="//input[@type='reset']"


def clickingForgotPwd(driver,Xpath):
    fw.clickingtheElement(driver,FORGOTPWD)


def enteringEMailid(driver,xpath,data):
    fw.passingData(driver,EMAILID,data)



