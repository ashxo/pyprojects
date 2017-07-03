from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_google():

    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, 5)
    driver.get("http://localhost/litecart/public_html")
    goods = int(driver.find_element_by_xpath("//span[@class='quantity']").text)

    for i in range(3):
        driver.find_element_by_xpath("//img[@alt='Yellow Duck']").click()
        driver.find_element_by_xpath("//option[@value='Small']").click()
        driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
        goods += 1

        wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"),
                                             str(goods)))

        driver.find_element_by_xpath("//a[@href='/litecart/public_html/']").click()
        wait.until(EC.title_contains("Online"))

    driver.find_element_by_id('cart').click()

    WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
    driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()

    driver.quit()