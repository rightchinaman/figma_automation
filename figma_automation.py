from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time


driver = webdriver.Chrome()  

driver.get("https://www.figma.com/login")

time.sleep(5)

email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

email_input.send_keys("#email#")
password_input.send_keys("#password#")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(5)  

driver.get("https://www.figma.com/files/team/1406855575909587373/all-projects?fuid=1406844920450176090")

time.sleep(5)  

dropdown_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Open team dropdown']")
dropdown_button.click()

time.sleep(5)

viewsettings_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='View settings ']") 
viewsettings_button.click()

time.sleep(5)


members_button = driver.find_element(By.CSS_SELECTOR, "button[class='tab--base--26PPx text--fontPos13--xW8hS text--_fontBase--QdLsd desktop_tool_bar--toolBarTabContentBase--CoAtY tab--unselected--u-2SW '] span[class='desktop_tool_bar--toolBarTabContent--a1orn ellipsis--ellipsis--Tjyfa']")
members_button.click()

time.sleep(5)


user_elements = driver.find_elements(By.CSS_SELECTOR, "div.members_list--memberRowForModal--g9CYe")  # Use the correct selector


users = []
for user in user_elements:
    name = user.find_element(By.CSS_SELECTOR, "span.avatar--handle--wlTXK").text    
    email = user.find_element(By.CSS_SELECTOR, "div.avatar--email--G3FcZ").text
    users.append({"name": name, "email": email})


with open("team_users.json", "w") as file:
    json.dump(users, file, indent=4)


driver.quit()
