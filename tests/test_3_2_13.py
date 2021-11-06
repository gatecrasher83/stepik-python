from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAssert(unittest.TestCase):
    def test1(self):
            try:
                link = "http://suninjuly.github.io/registration1.html"
                browser = webdriver.Chrome()
                browser.get(link)

                # Ваш код, который заполняет обязательные поля

                first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(
                        'First name')

                last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(
                        'Last name')

                email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(
                        'email@ya.ru')

                # Отправляем заполненную форму
                button = browser.find_element_by_css_selector("button.btn")
                button.click()

                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
                time.sleep(1)

                # находим элемент, содержащий текст
                welcome_text_elt = browser.find_element_by_tag_name("h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
                welcome_text = welcome_text_elt.text

                self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

            finally:
                # ожидание чтобы визуально оценить результаты прохождения скрипта
                time.sleep(10)
                # закрываем браузер после всех манипуляций
                browser.quit()


    def test2(self):
            try:
                link = "http://suninjuly.github.io/registration2.html"
                browser = webdriver.Chrome()
                browser.get(link)

                # Ваш код, который заполняет обязательные поля

                first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(
                        'First name')

                last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(
                        'Last name')

                email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(
                        'email@ya.ru')

                # Отправляем заполненную форму
                button = browser.find_element_by_css_selector("button.btn")
                button.click()

                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
                time.sleep(1)

                # находим элемент, содержащий текст
                welcome_text_elt = browser.find_element_by_tag_name("h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
                welcome_text = welcome_text_elt.text

                self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

            finally:
                # ожидание чтобы визуально оценить результаты прохождения скрипта
                time.sleep(10)
                # закрываем браузер после всех манипуляций
                browser.quit()

if __name__ == "__main__":
    unittest.main()


