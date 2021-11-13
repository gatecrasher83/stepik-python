import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_form_add_to_basket_found(browser):
    browser.get(link)
    # find button
    basket = browser.find_elements_by_css_selector("#add_to_basket_form")

    # assert button
    assert basket, f" 'button not found !'"
