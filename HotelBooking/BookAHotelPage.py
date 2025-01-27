from HotelBooking import HotelFramework as fw

fIRST_NAME="//input[@name='first_name']"
LAST_NAME="//input[@name='last_name']"
ADDRESS="//textarea[@name='address']"
CC_NUM="//input[@name='cc_num']"
CC_TYPE="//select[@name='cc_type']"
CC_DATE="//select[@name='cc_exp_month']"
CC_YEAR="//select[@name='cc_exp_year']"
CVV="//input[@name='cc_cvv']"
BOOKNOW_BTN="//input[@type='button']"
PAGENAME="(//td[@class='login_title'])[2]"
PROCESSINGTEXT="//label[@id='process_span']"

def BookingaHotel(driver,firstname,lastname,address,creditCard,ccType,ccDate,ccYear,cvv):
    fw.passingData(driver, fIRST_NAME, "firstname")
    fw.passingData(driver, LAST_NAME, "lastname")
    fw.passingData(driver, ADDRESS, address)
    fw.passingData(driver, CC_NUM, creditCard)
    fw.selectByIndex(driver, CC_TYPE, ccType)
    fw.selectByIndex(driver, CC_DATE, ccDate)
    fw.selectByText(driver, CC_YEAR, ccYear)
    fw.passingData(driver, CVV, cvv)
    fw.clickingtheElement(driver, BOOKNOW_BTN)
    fw.isElementPresent(driver, PROCESSINGTEXT)
