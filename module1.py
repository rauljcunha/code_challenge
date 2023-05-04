from selenium import webdriver
from selenium.webdriver.common.by import By
nav = webdriver.Chrome()
nav.set_window_size(1024, 600)
nav.maximize_window()
nav.get("https://www.google.com")
nav.implicitly_wait(1.0)
nav.find_element(By.NAME, 'q').send_keys('weather londom right now')
nav.implicitly_wait(1.0)
nav.find_element(By.NAME, 'btnK').click()
temp = nav.find_element(By.ID, 'wob_tm').text
print('The temperature righ now in Londom is: ' + temp + ' Celsius degrees!')