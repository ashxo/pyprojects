from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

#def switchToWindowAfter(driver, windows_before):
    #new_window = [i for i in driver.window_handles if i not in windows_before][0]
    #new_window = [x for x in windows_after if x != windows_before][0]
    #return new_window[0]

def test_google():
    url = 'http://localhost/litecart/public_html/admin'
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get(url)
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_css_selector('button.btn.btn-default').click()

    catalog = driver.find_elements_by_xpath('//*[@id="app-"]/a')
    catalog[2].click()

    mainWindow = driver.current_window_handle

    driver.find_element_by_css_selector("td:nth-child(5) a").click()

    link = driver.find_elements_by_css_selector('i[class="fa fa-external-link"]')

    for i in link:
        windows_before = driver.window_handles
        i.click()
        #WebDriverWait(driver,5).until.ec.new_window_is_opened(driver.window_handles)
        WebDriverWait(driver,5).until(ec.new_window_is_opened(windows_before))
        new_window = [i for i in driver.window_handles if i not in windows_before][0]
        #newWindow = driver.switchToWindowAfter(driver.window_handles[-1])
        assert new_window, print("New windows are not opened")
        if new_window:
            driver.switch_to.window(new_window)
            driver.close()
            driver.switch_to.window(mainWindow)

    driver.quit()
