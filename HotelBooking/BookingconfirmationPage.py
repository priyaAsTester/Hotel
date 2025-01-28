import pytest

from HotelBooking import HotelFramework as fw
ORDER_NO="//input[@name='order_no']"
SEARCH_HOTEL_BTN="//input[@name='search_hotel']"
BookingConfirmation="//td[@class='login_title']"
My_itinerary="//input[@name='my_itinerary']"


def navigationToBookingConfirmationPage(driver):
    fw.isElementPresent(driver, BookingConfirmation)
    fw.isElementPresent(driver, ORDER_NO)
    text = fw.gettingElementAttribute(driver, ORDER_NO)

