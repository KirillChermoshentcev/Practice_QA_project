from conftest import driver
from pages.input_page import InputPage


class TestInputPage:

    def test_name_input_field(self, driver):
        input_page = InputPage(driver)
        input_page.open()
        input_page.is_opened()
        input_page.click_on_text_input_field()
        input_text = input_page.enter_keys_to_text_input()
        input_page.wait_result_box()
        result_text = input_page.get_result_text().strip()
        assert input_text == result_text

    def test_email_input_field(self, driver):
        input_page = InputPage(driver)
        input_page.open()
        input_page.is_opened()
        input_page.click_on_email_tab()
        input_page.click_on_email_input_field()
        input_text = input_page.enter_keys_to_email_input()
        input_page.wait_result_box()
        result_text = input_page.get_result_text().strip()
        assert input_text == result_text

    def test_password_input_field(self, driver):
        input_page = InputPage(driver)
        input_page.open()
        input_page.is_opened()
        input_page.click_on_password_tab()
        input_page.click_on_password_input_field()
        input_text = input_page.enter_keys_to_password_input()
        input_page.wait_result_box()
        result_text = input_page.get_result_text().strip()
        assert input_text == result_text



