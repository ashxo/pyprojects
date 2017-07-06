from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def test_google():

    driver = webdriver.Google()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_css_selector('button.btn.btn-default').click()

    driver.implicitly_wait(3)

    links = len(driver.find_elements_by_css_selector("ul#box-apps-menu li#app-"))

    for l in range(links):
        driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")[l].click()
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1")))
        if len(driver.find_elements_by_css_selector("ul#box-apps-menu li.selected ul li")) != 0:
            sublinks = len(driver.find_elements_by_css_selector("ul#box-apps-menu "
                                                                "li.selected ul li"))
            for s in range(sublinks):
                driver.find_elements_by_css_selector("ul#box-apps-menu "
                                                     "li.selected ul li")[s].click()
                WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.TAG_NAME, "h1")))
    driver.close()