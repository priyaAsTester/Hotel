from operator import index

from select import select
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from HotelBooking import HotelFramework as fw
WELCOME="//input[@name='username_show']"
LOCATION="//select[@name='location']"
HOTELS="//select[@name='hotels']"
ROOMTYPE="//select[@name='room_type']"
ROOM_NOS="//select[@name='room_nos']"
DATE_IN="//input[@name='datepick_in']"
DATE_OUT="//input[@name='datepick_out']"
ADULTSIN_ROOM="//select[@name='adult_room']"
CHILDRENIN_ROOM="//select[@name='child_room']"
SEARCHBTN="//input[@name='Submit']"

def welcomeMsgVerification(driver):
    #driver.find_element(By.XPATH, "//input[@name='username_show']")
    msg=driver.find_element(By.XPATH, WELCOME)
    print(msg.get_attribute("value"))


def selectingLocation(driver,index):
    fw.selectByIndex(driver, LOCATION, index)

def selectingHotels(driver,index):
    fw.selectByIndex(driver,HOTELS,index)

def selectingRoomtype(driver,index):
    fw.selectByIndex(driver,ROOMTYPE,index)

def selectingNumOfRooms(driver,num):
    fw.selectByValue(driver,ROOM_NOS,num)

def CheckinDate(driver,date):
    fw.passingData(driver,DATE_IN,date)

def CheckOutDate(driver,date):
    fw.passingData(driver,DATE_OUT,date)

def selectingAdultsinRoom(driver,num):
    fw.selectByValue(driver,ADULTSIN_ROOM,num)

def selectingChildinRoom(driver,num):
    fw.selectByValue(driver,CHILDRENIN_ROOM,num)

def typingRequirementforHotel(driver,location,hotelindex,roomtype,numOfRooms,datein,dateout,adultsno,childno):
    fw.clickingtheElement(driver, LOCATION)
    selectingLocation(driver,location)
    selectingHotels(driver,hotelindex)
    selectingRoomtype(driver,roomtype)
    selectingNumOfRooms(driver,numOfRooms)
    CheckinDate(driver, datein)
    CheckOutDate(driver,dateout)
    selectingAdultsinRoom(driver,adultsno)
    selectingChildinRoom(driver,childno)
    fw.clickingtheElement(driver,SEARCHBTN)





