from pages.base_page import BasePage
from locators.input_page_locators import InputPageLocators
from helpers import InputData
from links import Links


class InputPage(BasePage):

    PAGE_URL = Links.INPUT_PAGE

    def click_on_input_field(self):
        self.click_on_element(InputPageLocators.INPUT_FIELD)

    def enter_keys_to_input_field(self):
        self.send_keys_to_input(InputPageLocators.INPUT_FIELD,InputData.name)
        return InputData.name

    def wait_result_box(self):
        self.wait_visibility_of_element(InputPageLocators.RESULT_TEXT)

    def get_result_text(self):
        full_text = self.get_text_from_element(InputPageLocators.RESULT_TEXT)
        return full_text.replace("Your input was:\n", "")



