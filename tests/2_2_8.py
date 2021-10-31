from selenium import webdriver
import time
import os

try:
# открываем браузер и открываем сайт
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

# ввод текста в поле "First name"
    input1 = browser.find_element_by_css_selector("input[name='firstname']")
    input1.send_keys('firstname')

# ввод текста в поле "Last name"
    input2 = browser.find_element_by_css_selector("input[name='lastname']")
    input2.send_keys('lastname')

# ввод email в поле "Email"
    input3 = browser.find_element_by_css_selector("input[name='email']")
    input3.send_keys('email')

# определяем путь к папке и путь к файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    
# находим кнопку и отправляем файл
    element = browser.find_element_by_css_selector("input#file")
    element.send_keys(file_path)

# нажимаем кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

finally:
    time.sleep(20)
    browser.quit()

    
    
