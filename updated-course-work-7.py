from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_google():

    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, 5)
    driver.get("http://localhost/litecart/public_html")
    goods = int(driver.find_element_by_xpath("//span[@class='quantity']").text)

    for i in range(3):
        products_css = 'div[id="box-campaign-products"]'
        first_product_css = products_css + ' div[class^="col-xs"]:nth-child(1)'
        first_product = driver.find_element_by_css_selector(first_product_css)
        first_product.click()
        #driver.find_element_by_xpath("//img[@alt='Yellow Duck']").click()

        try:
            size_presence = wait.until(
                ec.presence_of_element_located((By.CSS_SELECTOR, 'select[class ="form-control"] option[value="Small"]')))
        except:
            size_presence = False
        if size_presence:
            driver.find_element_by_css_selector('select[class ="form-control"] option[value="Small"]').click()

        driver.find_element_by_css_selector('select[class ="form-control"] option[value="Small"]').click()
        driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
        goods += 1
        driver.find_element_by_xpath("//a[@href='/litecart/public_html/']").click()
        wait.until(ec.title_contains("Online"))

    driver.find_element_by_id('cart').click()

    WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
    driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()

    driver.quit()