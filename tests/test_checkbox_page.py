import pytest
from locators.checkbox_page_locators import CheckboxPageLocators
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

    def test_select_random_checkboxes(self, driver):
        checkbox_page = CheckboxPage(driver)
        checkbox_page.open()
        checkbox_page.is_opened()
        checkbox_page.go_to_checkboxes_tab()
        checkbox_page.select_random_checkboxes()
        checkbox_page.click_on_submit_button()

        input = checkbox_page.get_selected_checkboxes()
        output = checkbox_page.get_output_result()

        assert input == output
