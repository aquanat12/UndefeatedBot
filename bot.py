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
geckopath = "./geckodriver.exe"

def Bot():

    driver = webdriver.Firefox(executable_path=geckopath)

    driver.get(
        "https://undefeated.com/collections/all/products/undefeated-anointed-s-s-tee?variant=31341462945865")


    first = "nigel"
    last = "test"
    number = "202-555-0183"
    address = "test street"
    city = "ALCESTER"
    zip = "57001"
    color = "BLACK"
    size = "L"
    loc = "US"
    state = "SD"
    uid = ""
    upw = ""
    cc = "357321382046786"
    ed = "02/22"
    cvv = "5555"
    
   
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

    input_cc = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#number'))
    )
    input_cc.click()
    input_cc.send_keys(cc)

    input_name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#name'))
    )
    input_name.click()
    input_name.send_keys(first)

    input_ed = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#expiry'))
    )
    input_ed.send_keys(ed)

    input_ccv = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#verification_value'))
    )
    input_ccv.send_keys(ccv)


    time.sleep(2)
    time.sleep(2)

    print("\n\n[*] Page 3/3 Done!")

    driver.quit()


    
Bot()