from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


def test_google():

    driver = webdriver.Chrome();
    submenuCheck(driver)
    driver.quit()


def submenuCheck(driver):

    wait = WebDriverWait(driver, 3)
    submenuWait = WebDriverWait(driver, 0.5)
    headerPage = 'h1'
    driver.get("http://localhost/litecart/public_html/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector('button.btn.btn-default').click()
    wait.until(ec.title_is("My Store"))

    cssMenu = 'li[id="app-"]'
    presenceMenu = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, cssMenu)))
    menu = driver.find_elements_by_css_selector(cssMenu)

    for index in range(1, len(menu) + 1):
        menuItem = cssMenu + ':nth-child(' + str(index) + ')'
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, menuItem)))
        driver.find_element_by_css_selector(menuItem).click()
        assert (wait.until
                (ec.visibility_of_element_located((By.CSS_SELECTOR, headerPage)))), "Element h1 not found"

        #submenu
        cssSubMenu = 'li[id^="doc-"]'
        try:
            subMenuPresence = submenuWait.until(
                ec.presence_of_all_elements_located((By.CSS_SELECTOR, cssSubMenu)))
        except :
            subMenuPresence = False
        if subMenuPresence:
            subMenu = driver.find_elements_by_css_selector(cssSubMenu)
            for index in range(1, len(subMenu) + 1):
                subMenuItem = cssSubMenu + ':nth-child(' + str(index) + ')'
                wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, subMenuItem)))
                driver.find_element_by_css_selector(subMenuItem).click()
                assert (wait.until
                        (ec.visibility_of_element_located((By.CSS_SELECTOR, headerPage)))), "Element h1 not found"

    # Logout:
    logoutLocator = 'i[class="fa fa-sign-out fa-lg"]'
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, logoutLocator)))
    driver.find_element_by_css_selector(logoutLocator).click()