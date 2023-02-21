from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

username = ""
password = ""

driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.messenger.com")

print(driver.title)

user_bar = driver.find_element("name", "email")
user_bar.clear()
user_bar.send_keys(username)

pass_bar = driver.find_element("name", "pass")
pass_bar.clear()
pass_bar.send_keys(password)
pass_bar.send_keys(Keys.RETURN)

time.sleep(5)

driver.get("https://www.messenger.com/t/5806877362685490") 
# I am not sure if this one is the same for all of us its just the link for the SUS Crew 
# this can be refactored to be less hard coded
time.sleep(10)

search_bar = driver.find_element(By.CSS_SELECTOR, '.notranslate')
search_bar.clear()
search_bar.send_keys("sent with python selenium")
search_bar.send_keys(Keys.RETURN)

print(driver.current_url)

driver.close()