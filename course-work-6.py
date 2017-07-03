from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time

def test_google():

    driver = webdriver.Chrome();
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_css_selector('button.btn.btn-default').click()

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//a[contains(.,'Catalog')]").click()
    driver.find_element_by_xpath("//a[contains(.,' Add New Product')]").click()
    driver.find_element_by_xpath("//label[contains(.,' Enabled')]").click()
    driver.find_element_by_xpath("//input[@name='code']").send_keys("010010001")
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys("Duffy")
    driver.find_element_by_xpath("//input[@name='sku']").send_keys("5849")
    driver.find_element_by_xpath("//input[@name='gtin']").send_keys("4209")
    driver.find_element_by_xpath("//input[@name='taric']").send_keys("2394")
    driver.find_element_by_xpath("//input[@name='quantity']").clear()
    driver.find_element_by_xpath("//input[@name='quantity']").send_keys("25")
    driver.find_element_by_xpath("//input[@name='weight']").clear()
    driver.find_element_by_xpath("//input[@name='weight']").send_keys("25")
    driver.find_element_by_xpath("//input[@name='dim_x']").clear()
    driver.find_element_by_xpath("//input[@name='dim_x']").send_keys("10")
    driver.find_element_by_xpath("//input[@name='dim_y']").clear()
    driver.find_element_by_xpath("//input[@name='dim_y']").send_keys("10")
    driver.find_element_by_xpath("//input[@name='dim_z']").clear()
    driver.find_element_by_xpath("//input[@name='dim_z']").send_keys("10")
    driver.find_element_by_xpath("//input[@name='date_valid_from']").send_keys("2015-05-09")
    driver.find_element_by_xpath("//input[@name='date_valid_to']").send_keys("2018-01-01")
    driver.find_element_by_xpath("//a[@href='#tab-information']").click()
    driver.find_element_by_xpath("//select[@name='manufacturer_id']").click()
    driver.find_element_by_xpath("//option[contains(.,'ACME Corp.')]").click()
    driver.find_element_by_xpath("//input[@name='keywords']").send_keys("duffy duck")
    driver.find_element_by_xpath("//input[@name='short_description[en]']").send_keys("this is a duck")
    driver.find_element_by_xpath("//div[@dir='ltr']").send_keys("awesome text")
    driver.find_element_by_xpath("//textarea[@class='form-control']").send_keys("awesome text")
    driver.find_element_by_xpath("//input[@name='head_title[en]']").send_keys("awesome text")
    driver.find_element_by_xpath("//input[@name='meta_description[en]']").send_keys("awesome text")
    driver.find_element_by_xpath("//button[@name='save']").click()

def isExist(xpath):
    try:
        webdriver.find_element_by_xpath("//a[contains(.,'Duffy')]")
    except NoSuchElementException:
        return False
    return True
    driver.quit()