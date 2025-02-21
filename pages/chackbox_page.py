from pages.base_page import BasePage
from locators.checkbox_page_locators import CheckboxPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
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

    def go_to_checkboxes_tab(self):
        self.click_on_element(CheckboxPageLocators.CHECKBOXES_TAB)

    def select_random_checkboxes(self):
        item_list = self.wait_visibility_of_elements(CheckboxPageLocators.CHECKBOXES_LIST)
        selected_checkboxes = random.sample(range(len(item_list)), 3)

        for index in selected_checkboxes:
            if not item_list[index].is_selected():
                item_list[index].click()

    def get_selected_checkboxes(self):
        box = self.wait_visibility_of_element(CheckboxPageLocators.RESULT_TEXT)
        title_items = box.find_elements(*CheckboxPageLocators.RESULT_TEXT)
        return str([item.text for item in title_items])

    def get_output_result(self):
        result_list = self.elements_are_visible(CheckboxPageLocators.RESULT_TEXT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower()


