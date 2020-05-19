import string
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import pyautogui
import csv
import pandas as pd

geckopath = "./geckodriver.exe"



def Bot():

    
    # info = ["first name", "last name", "number", "address", "city", "zip", "color", "size", "location", "state", "Login", "Password", "cc", "ed", "cvv", "ccname"]
    df = pd.read_csv("info.csv")
    first = str(df["first name"]).strip(" 0").replace("Name: first name, dtype: object", '').strip("\n").strip("\n")
    last = str(df["last name"]).strip(" 0").replace("Name: last name, dtype: object", '').strip("\n")
    number = str(df["number"]).strip(" 0").replace("Name: number, dtype: object", '').strip("\n")
    address = str(df["address"]).strip(" 0").replace("Name: address, dtype: object", '').strip("\n")
    city = str(df["city"]).strip(" 0").replace("Name: city, dtype: object", '').strip("\n")
    zip = str(df["zip"]).strip(" 0").replace("Name: zip, dtype: object", '').strip("\n")
    color = str(df["color"]).strip(" 0").replace("Name: color, dtype: object", '').strip("\n")
    size = str(df["size"]).strip(" 0").replace("Name: size, dtype: object", '').strip("\n")
    loc = str(df["location"]).strip(" 0").replace("Name: location, dtype: object", '').strip("\n")
    state = str(df["state"]).strip(" 0").replace("Name: state, dtype: object", '').strip("\n")
    uid = str(df["Login"]).strip(" 0").replace("Name: Login, dtype: object", '').strip("\n")
    upw = str(df["Password"]).strip(" 0").replace("Name: Password, dtype: object", '').strip("\n")
    cc = str(df["cc"]).strip(" 0").replace("Name: cc, dtype: object", '').strip("\n")
    ed = str(df["ed"]).strip(" 0").replace("Name: ed, dtype: object", '').strip("\n")
    cvv = str(df["cvv"]).strip(" 0").replace("Name: cvv, dtype: object", '').strip("\n")
    ccname = str(df["ccname"]).strip(" 0").replace("Name: ccname, dtype: object", '').strip("\n")
    

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get("https://undefeated.com/collections/all/products/undefeated-racquet-s-s-tee?variant=31341463830601")

    ChangeShipping = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/div/div/div[2]/div[3]/a"))
    )
    ChangeShipping.click()

    country = Select(driver.find_element_by_id("gle_selectedCountry"))
    country.select_by_value(loc)

    ChangeShippingsave = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/div/div/div[4]/input"))
    )
    ChangeShippingsave.click()

    # Add to Cart
    time.sleep(1.5)
    
    Selectcolor = Select(driver.find_element_by_id("SingleOptionSelector-0"))
    Selectcolor.select_by_value(color)
    
    
    Selectsize = Select(driver.find_element_by_id("SingleOptionSelector-1"))
    Selectsize.select_by_value(size)

    addcart = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "AddToCart--product-template_un"))
    )
    addcart.click()
    
    time.sleep(1)
    
    cart = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/header/div/div[1]/nav[2]/ul/li[3]/a"))
    )
    cart.click()
   
    loginpage = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/header/div/div[3]/div/div/div[2]/div/div/div/form/div[2]/button"))
    )
    loginpage.click()
    
    # Login
    CustomerEmail = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#AccountPage > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > input:nth-child(4)"))
    )
    CustomerEmail.send_keys(uid)
    
    CustomerPassword = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#AccountPage > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > input:nth-child(6)"))
    )
    CustomerPassword.send_keys(upw)
    
    login = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/div/div/div/div[2]/form/p[1]/input"))
    )
    login.click()

    # Page 1

    first_name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "checkout_shipping_address_first_name"))
    )
    first_name.send_keys(first)


    last_name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "checkout_shipping_address_last_name"))
    )
    last_name.send_keys(last)
    
    zipcode = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "checkout_shipping_address_zip"))
    )
    zipcode.send_keys(zip)
    
    Selectstate = Select(driver.find_element_by_id("checkout_shipping_address_province"))
    Selectstate.select_by_value(state)
    
    Selectcity = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "checkout_shipping_address_city"))
    )
    Selectcity.send_keys(city)
    
    addr = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "checkout_shipping_address_address1"))
    )
    addr.send_keys(address)

    hp = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "checkout_shipping_address_phone"))
    )
    hp.send_keys(number)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    

    print("Solve the captcha now!\n\n")
    captcha_solved = "1"
    while captcha_solved == "1":
        captcha_solved = input("[Y]Solved?\n")
    
    pyautogui.hotkey('alt', 'tab', interval=0.1)

    submit = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'continue_button'))
    )
    submit.click()

    print("\n\n[*] Login Done!")

    # Page 2

    SelectPayment = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'continue_button'))
    )
    SelectPayment.click()

    print("\n\n[*] UPS Ground Selected")

    # Page 3
    
    time.sleep(3)
    
    for i in range(8):
        pyautogui.press('tab')
        time.sleep(0.1)

    for i in range(16):
        pyautogui.typewrite(cc[i])
        time.sleep(0.1)
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(ccname)
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(ed)
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(cvv)
    

    print("\n\n[*] Bought!")

  #  driver.quit()


    
Bot()