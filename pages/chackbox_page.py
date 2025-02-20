from pages.base_page import BasePage
from locators.checkbox_page_locators import CheckboxPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from links import Links


class CheckboxPage(BasePage):

    PAGE_URL = Links.CHECKBOX_PAGE

    def click_on_single_checkbox(self):
        self.click_on_element(CheckboxPageLocators.CHECKBOX)

    def click_on_submit_button(self):
        self.click_on_element(CheckboxPageLocators.SUBMIT_BUTTON)

    def get_result_text_checkbox(self):
        result = self.get_text_from_element(CheckboxPageLocators.RESULT_TEXT)
        return result.replace("Selected checkboxes:\n", "")