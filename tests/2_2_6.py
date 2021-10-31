import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
# считываем x
    x = browser.find_element_by_id("input_value").text

# скролл вниз, до первой кнопки
    button = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)

# считаем функцию и вставляем в поле
    input1 = browser.find_element_by_id("answer").send_keys(calc(x))

# скролл до чек-бокса и кликаем чек-бокс 
    checkb = browser.find_element_by_css_selector("input#robotCheckbox")
    browser.execute_script('return arguments[0].scrollIntoView(true);', checkb)
    click1 = browser.find_element_by_css_selector("input#robotCheckbox").click()

# скролл до чек-бокса и выбираем радиокнопку "Robots rule"
    r_b = browser.find_element_by_css_selector("input#robotsRule")
    browser.execute_script('return arguments[0].scrollIntoView(true);', r_b)

    click2 = browser.find_element_by_css_selector("input#robotsRule").click()
    
# скролл до кнопки жмем кнопку Submit
    button = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)

    click3 = browser.find_element_by_css_selector("button[type='submit']").click()
    
finally:
    time.sleep(20)
    browser.quit()
                                                            
                                                        
    
    
    
