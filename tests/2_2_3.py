from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = int(browser.find_element_by_id("num1").text)
    n2 = int(browser.find_element_by_id("num2").text)
    n = n1 + n2

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(n))

    option = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(20)
    browser.quit()



