import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def page_is_loading(driver):
    while True:
        x = driver.execute_script("return document.readyState")
        if x == "complete":
            return True
        else:
            yield False

def test_web():
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_driver.get('https://www.ixigo.com/')
    chrome_driver.maximize_window()

    page_is_loading(chrome_driver)

    title = "ixigo - Flights, Train Reservation, Hotels, Air Tickets, Bus Booking"
    assert title == chrome_driver.title

    one_way_field = chrome_driver.find_element_by_xpath("//*[text()='One Way']")
    one_way_field.click()

    from_text = "CCU"
    from_text_field = chrome_driver.find_element_by_xpath("//*[text()='From']/following-sibling::input")
    sleep(5)
    from_text_field.click()
    sleep(5)
    from_text_field.send_keys(from_text)
    sleep(2)
    from_text_field.send_keys(Keys.ENTER)

    to_text = "HYD"
    to_text_field = chrome_driver.find_element_by_xpath("//*[text()='To']/following-sibling::input")
    to_text_field.send_keys(to_text)
    sleep(2)
    to_text_field.send_keys(Keys.ENTER)
    sleep(2)
    to_text_field.send_keys(Keys.TAB)

    sleep(2)
    date_field = chrome_driver.find_element_by_xpath("(//td[contains(@class,'rd-day-selected')]/ancestor::tr/following-sibling::tr/td)[2]")
    date_field.click()

    search_field = chrome_driver.find_element_by_xpath("//button[text()='Search']")
    search_field.click()

    page_is_loading(chrome_driver)

    book_field_path = "//*[contains(@class,'flight-listing')]//*[text()='Book']"
    WebDriverWait(chrome_driver, 20).until(EC.presence_of_element_located((By.XPATH, book_field_path)))
    book_field = chrome_driver.find_element_by_xpath(book_field_path)
    assert book_field.text == "BOOK"

    book_field.click()
    sleep(2)
    WebDriverWait(chrome_driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'fare-select-btn')]/button")))
    book_field2 = chrome_driver.find_element_by_xpath("//*[contains(@class,'fare-select-btn')]/button")
    book_field2.click()

    login_field_path = "//*[text()='login to proceed']"
    WebDriverWait(chrome_driver, 20).until(EC.presence_of_element_located((By.XPATH, login_field_path)))
    login_field = chrome_driver.find_element_by_xpath(login_field_path)
    assert login_field.text == "LOGIN TO PROCEED"

    sleep(2)
    chrome_driver.quit()