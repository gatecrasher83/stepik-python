import pytest
import time
import math

from selenium import webdriver

# переменная для сбора текста Correct
total = ""


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print("Total result is '" + total + "'")


# ссылки, по которым пройдет тест
addresses = [
    ("address_1", "https://stepik.org/lesson/236895/step/1"),
    ("address_2", "https://stepik.org/lesson/236896/step/1"),
    ("address_3", "https://stepik.org/lesson/236897/step/1"),
    ("address_4", "https://stepik.org/lesson/236898/step/1"),
    ("address_5", "https://stepik.org/lesson/236899/step/1"),
    ("address_6", "https://stepik.org/lesson/236903/step/1"),
    ("address_7", "https://stepik.org/lesson/236904/step/1"),
    ("address_8", "https://stepik.org/lesson/236905/step/1")
]


# число для правильного ответа на задачу
def answer():
    return math.log(int(time.time()))


@pytest.mark.parametrize("code, site", addresses)
class Test_3_6_3:
    def test_open_site(self, browser, code, site):
        global total
        # определяем адрес сайта
        link = f"{site}"
        # пишем какой сайт открывается (код сайта)
        print(f"\nopen {code} site..")
        browser.get(link)
        # ввод в поле числа "answer"
        browser.implicitly_wait(5)
        browser.find_element_by_class_name("ember-text-area").send_keys(str(answer()))
        # нажать кнопку "Отправить"
        browser.find_element_by_css_selector("button.submit-submission").click()
        # дожидаемся фидбека о том,что ответ верный
        correct_text = browser.find_element_by_class_name("smart-hints__hint").text
        try:
            # сверяем с верным вариантом
            assert "Correct!" == correct_text, f"wrong expected value: {correct_text}"
        except AssertionError:
            total += correct_text
