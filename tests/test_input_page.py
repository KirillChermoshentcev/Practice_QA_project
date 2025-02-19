from conftest import driver
from pages.input_page import InputPage


class TestInputPage:

    def test_input_field(self, driver):
        input_page = InputPage(driver)
        input_page.open()
        input_page.click_on_input_field()
        input_text = input_page.enter_keys_to_input_field()
        input_page.wait_result_box()
        result_text = input_page.get_result_text().strip()
        assert input_text == result_text


