from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def test_google():

    driver = webdriver.Chrome();
    driver.implicitly_wait(3)
    driver.get("http://localhost/litecart/public_html")
    WebDriverWait(driver, 3).until(ec.title_is("My Store | Online Store"))

    MainPageTitle = driver.find_element_by_xpath("//div[@class='name']").text
    MainPageRegularPrice = driver.find_element_by_xpath("//s[@class='regular-price']").text
    MainPageRPriceColor = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('color')
    MainPageRPriceTextD = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("text-decoration-line")
    MainPageDPrice = driver.find_element_by_xpath("//strong[@class='campaign-price']").text
    MainPageDPriceColor = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('color')
    MainPageDFontWeight = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')

    driver.find_element_by_xpath("(//*[@title='Yellow Duck'])").click()
    ItemPageTitle = driver.find_element_by_xpath("//h1[@class='title']").text
    ItemPageRegularPrice = driver.find_element_by_xpath("//del[@class='regular-price']").text
    ItemPageRPriceColor = driver.find_element_by_xpath("//del[@class='regular-price']").value_of_css_property('color')
    ItemPageRPriceTextD = driver.find_element_by_xpath("//del[@class='regular-price']").value_of_css_property("text-decoration-line")
    ItemPageDPrice = driver.find_element_by_xpath("//strong[@class='campaign-price']").text
    ItemPageDPriceColor = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('color')
    ItemPageDFontWeight = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')

    assert (MainPageTitle == ItemPageTitle), "Product Name is not equal on Main Page and Item Page"
    assert (MainPageRegularPrice == ItemPageRegularPrice), "Product Regular Price is not equal on Main Page and Item Page"
    assert (MainPageDPrice == ItemPageDPrice), "Product discount is not equal on Main Page and Item Page"
    assert (MainPageRPriceColor == ItemPageRPriceColor), "Regular Price is not gray on both pages"
    assert (MainPageDPriceColor == ItemPageDPriceColor), "Dicsount Price is not red on both pages"
    assert (MainPageRPriceTextD == ItemPageRPriceTextD), "Regular Price decoration is not equal on both pages"
    assert (MainPageDFontWeight == ItemPageDFontWeight), "Discount Price decoration is not equal on both pages"

    driver.quit()