from pages.base_page import BasePage
from locators.input_page_locators import InputPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import InputData
from links import Links


class InputPage(BasePage):

    PAGE_URL = Links.INPUT_PAGE

    def click_on_text_input_field(self):
        self.click_on_element(InputPageLocators.INPUT_FIELD)

    def enter_keys_to_text_input(self):
        self.send_keys_to_input(InputPageLocators.INPUT_FIELD,InputData.name)
        return InputData.name

    def click_on_email_tab(self):
        self.click_on_element(InputPageLocators.EMAIL_TAB)

    def click_on_email_input_field(self):
        self.click_on_element(InputPageLocators.EMAIL_FIELD)

    def enter_keys_to_email_input(self):
        self.send_keys_to_input(InputPageLocators.EMAIL_FIELD,InputData.email)
        return InputData.email

    def click_on_password_tab(self):
        self.click_on_element(InputPageLocators.PASSWORD_TAB)

    def click_on_password_input_field(self):
        self.click_on_element(InputPageLocators.PASSWORD_FIELD)

    def enter_keys_to_password_input(self):
        self.send_keys_to_input(InputPageLocators.PASSWORD_FIELD,InputData.password)
        return InputData.password

    def wait_result_box(self):
        wait = WebDriverWait(self.driver, timeout=20)
        wait.until(EC.visibility_of_element_located(InputPageLocators.RESULT_TEXT))

    def get_result_text(self):
        full_text = self.get_text_from_element(InputPageLocators.RESULT_TEXT)
        return full_text.replace("Your input was:\n", "")



