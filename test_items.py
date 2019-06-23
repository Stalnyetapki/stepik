import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_presence_button_add_to_basket(driver):
    driver.get(link)
    time.sleep(30)
    driver.find_element_by_class_name('btn-add-to-basket')
