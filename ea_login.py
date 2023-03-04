import string
import os
import sys
from time import sleep
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from twocaptcha import TwoCaptcha
import random
import re
import time
import subprocess
from datetime import datetime

solver = TwoCaptcha('api')


def open_ea_to_create_account(email, emailpass):
    driver.get('https://www.ea.com/register')
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'countryDobNextBtn')))
    sleep(2)
    driver.switch_to.active_element
    # day
    ActionChains(driver).send_keys(Keys.TAB*8).perform()
    ActionChains(driver).send_keys(Keys.SPACE).perform()
    for i in range(random.randint(1, 28)):
        ActionChains(driver).send_keys(Keys.DOWN).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    # month
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.SPACE).perform()
    for i in range(random.randint(1, 12)):
        ActionChains(driver).send_keys(Keys.DOWN).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    # year
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.SPACE).perform()
    for i in range(random.randint(20, 34)):
        ActionChains(driver).send_keys(Keys.DOWN).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    # enter
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # email pass
    new_password = generate_password()
    ActionChains(driver).send_keys(Keys.TAB*2).perform()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'email'))).send_keys(email)
    while True:
        try:
            originId = random.choice(first_names) + (str(random.randint(999, 9999))
                                                     if random.choice([True, False]) else generate_username1())
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.ID, 'originId'))).send_keys(originId)
            ActionChains(driver).send_keys(Keys.TAB).perform()
            error_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "form-error-eaid-duplicated"))
                or EC.presence_of_element_located((By.ID, "form-error-eaid-too-long"))
            )
            print("Error: " + error_element.aria_role())
            if error_element.aria_role() == 'none':
                break
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'originId'))).clear()
        except:
            break

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'password'))).send_keys(new_password + "\n")

    # cant find verify button to click
    pop_up_div=WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'app')))
    driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].style.height = 'auto';", pop_up_div)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "home_children_button"))).click()

    code = from_email(email, emailpass)
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, 'continueDoneBtn')))
    ActionChains(driver).send_keys(Keys.TAB*4).perform()
    ActionChains(driver).send_keys(Keys.SPACE).perform()
    ActionChains(driver).send_keys(Keys.TAB*3).perform()
    ActionChains(driver).send_keys(Keys.SPACE).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'continueDoneBtn'))).click()
    sleep(3)
    print('something')
    
    
    open_ea_to_create_account(username, '7NBcEHkRvR')
    
