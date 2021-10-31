import math
import time

# импортируем класс By
from selenium.webdriver.common.by import By

# импортируем WebDriverWait 
from selenium.webdriver.support.ui import WebDriverWait

# импортируем expected_conditions и переименуем его в EC
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # ждем, пока цена дома опустится до 100$
    house_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    # жмем кнопку Book
    button = browser.find_element_by_id("book").click()

    # считываем x, высчитываем формулу
    x = browser.find_element_by_css_selector("span#input_value").text
    y = calc(x)

    # подставляем значение в поле для ввода
    inpu_t = browser.find_element_by_id("answer").send_keys(y)

    # жмем кнопку Submit
    button = browser.find_element_by_css_selector("button#solve").click()


finally:
    time.sleep(20)
    browser.quit()



