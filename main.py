from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service(r"C:\Users\Leighiam\Documents\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get(url="https://tinder.com/")
driver.maximize_window()
time.sleep(2)
window_before = driver.window_handles[0]
driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[contains(text(), "Log in with Facebook")]').click()
time.sleep(2)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.find_element(By.NAME, "email").send_keys(email_credentials)
driver.find_element(By.NAME, "pass").send_keys(email_password)
driver.find_element(By.NAME, "login").click()
driver.switch_to.window(window_before)
time.sleep(5)
driver.find_element(By.XPATH, '//button[@aria-label="Allow"]').click()
driver.find_element(By.XPATH, '//button[@aria-label="Enable"]').click()
like = driver.find_element(By.CSS_SELECTOR, "body")

for i in range(1, 95):
    try:
        time.sleep(5)
        like.send_keys(Keys.ARROW_RIGHT)
    except:
        random_popup = driver.find_element(By.XPATH, '//button[@data-testid="cancel"]').click()
        continue