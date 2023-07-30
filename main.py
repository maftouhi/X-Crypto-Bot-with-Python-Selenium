
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def login(username, password):
    driver.get('https://twitter.com/i/flow/login')
    try:
        input_field_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="text"]')))
        input_field_username.send_keys(username)
        input_field_username.send_keys(Keys.RETURN)
        try:
            input_field_password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
            input_field_password.send_keys(password)
            input_field_password.send_keys(Keys.RETURN)
            while True:  # keeping the home screen on
                print()
        except:
            driver.quit()
    except:
        driver.quit()


login('Xcryptobot', 'wyjKiz-pibgyn-poxwi2')

