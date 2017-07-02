from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_google():
    driver = webdriver.Chrome();
    driver.get("http://localhost/litecart/public_html/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
   #driver.find_element_by_name("login").click()
    #driver.find_element_by_class_name("btn btn-default").click()
    driver.find_element_by_css_selector('button.btn.btn-default').click()
    driver.quit()