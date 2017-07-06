from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import time


class Logger(AbstractEventListener):

    def exception_case(self, exception, driver):
        print(driver.get_log("browser"))
        driver.save_screenshot("Screenshot" + str(time.time()) + ".png")

    def before_find(self, by, value, driver):
        print(driver.get_log("browser"))
        print(by, value)

    def after_find(self, by, value, driver):
        print(driver.get_log("browser"))
        print(by, value)


def test_google():
    driver = EventFiringWebDriver(webdriver.Chrome(), Logger())
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_css_selector('button.btn.btn-default').click()
    driver.implicitly_wait(10)

    links = len(driver.find_elements_by_css_selector("ul#box-apps-menu li#app-"))

    for i in range(links):
        driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")[i].click()
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