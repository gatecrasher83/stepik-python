from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

# найти и нажать на кнопку
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
    time.sleep(3)

# переключаемся на confirm окно
    confirm = browser.switch_to.alert
    confirm.accept()


# считываем х
    x = browser.find_element_by_css_selector("span#input_value").text

# подставляем х и решаем задачу
    y = str(math.log(abs(12*math.sin(int(x)))))

# подставляем решение задачи в поле для ввода
    input1 = browser.find_element_by_css_selector("input.form-control").send_keys(y)

# жмем кнопку "Submit"
    button = browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(20)
    browser.quit()
