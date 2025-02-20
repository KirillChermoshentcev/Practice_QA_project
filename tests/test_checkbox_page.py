from conftest import driver
from pages.chackbox_page import CheckboxPage


class TestCheckboxPage:

    def test_checkbox(self, driver):
        checkbox_page = CheckboxPage(driver)
        checkbox_page.open()
        checkbox_page.is_opened()
        checkbox_page.click_on_single_checkbox()
        checkbox_page.click_on_submit_button()
        result = checkbox_page.get_result_text_checkbox()
        assert result == 'select me or not'