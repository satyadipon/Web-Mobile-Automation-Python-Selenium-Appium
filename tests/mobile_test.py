from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {

    "deviceName": "Nexus 5 API 28",
    "platformName": "Android",
    "browserName": "Chrome",
    "chromedriverExecutable": "/Users/satya/Desktop/Work/UpworkProjects/demo-test-python/chromedriver",
    "autoGrantPermissions": True
}


def test_mobile():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.toggle_location_services()
    driver.get('https://www.amazon.in/')

    title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    assert title == driver.title

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, "gwm-SignIn-button")))
    profile_field = driver.find_element_by_id("gwm-SignIn-button")
    profile_field.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, "ap_email_login")))
    email_phone_field = driver.find_element_by_id("ap_email_login")
    email_phone_field.send_keys("8876787678")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CSS_SELECTOR, "span#continue")))
    continue_field = driver.find_element_by_css_selector("span#continue")
    continue_field.click()

    time.sleep(5)
    assert driver.find_element_by_css_selector(".a-alert-heading").text == "Incorrect phone number"

    driver.quit()

