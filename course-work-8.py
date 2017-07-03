from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get('http://localhost/litecart/public_html/admin')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_css_selector('button.btn.btn-default').click()

    catalog = driver.find_elements_by_xpath('//*[@id="app-"]/a')
    catalog[2].click()

    driver.find_element_by_css_selector("td:nth-child(5) a").click()

    link = driver.find_elements_by_class_name('fa-external-link')
    for i in link:
        i.click()

    for x in driver.window_handles:
        driver.switch_to.window(x)
        driver.close()

    driver.quit()