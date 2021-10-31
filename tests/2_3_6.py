import math
from selenium import webdriver
import time

# функция для капчи
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
# открываем страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

# нажимаем кнопку
    button = browser.find_element_by_css_selector("button.trollface").click()
    time.sleep(2)

# узнаём имя новой вкладки
    new_window = browser.window_handles[1]

# (необязательно, для себя) узнаём имя текущей вкладки
    first_window = browser.window_handles[0]

# переходим на новую вкладку
    browser.switch_to.window(new_window)

# узнаём значение х
    x = browser.find_element_by_css_selector("span#input_value").text

# решаем капчу и подставляем решение в поле для ввода
    y = calc(x)
    input1 = browser.find_element_by_css_selector("input#answer").send_keys(y)

# находим кнопку "Submit" и жмем ее
    button = browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(20)
    browser.quit()


    
