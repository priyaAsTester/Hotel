from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.XPATH,"//input[@name='username_show']").
