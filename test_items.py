import time


def test_addbutton_shoud_be_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(2)
    add_button = browser.find_element_by_xpath("//button[contains(@class, 'btn btn-lg btn-primary btn-add-to-basket')]")
    button_text = add_button.text
    assert button_text != '', 'кнопка не найдена'
