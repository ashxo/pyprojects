from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_firefox():

    driver = webdriver.Firefox();

    driver.get("http://www.google.com")
    driver.quit()