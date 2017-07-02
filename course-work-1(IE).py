from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_explorer():

    driver = webdriver.Ie();

    driver.get("http://www.google.com")
    driver.quit()