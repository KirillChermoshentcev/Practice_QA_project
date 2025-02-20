from pages.base_page import BasePage
from locators.input_page_locators import InputPageLocators
from locators.buttons_page_locators import ButtonsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from links import Links


class ButtonsPage(BasePage):

    PAGE_URL = Links.BUTTONS_PAGE

    def click_on_simple_button(self):
        self.click_on_element(ButtonsPageLocators.SUBMIT_BUTTON)

    def get_result_text(self):
        result = self.get_text_from_element(ButtonsPageLocators.RESULT_TEXT)
        return result

    def go_to_looks_like_button_tab(self):
        self.click_on_element(ButtonsPageLocators.LOOKS_LIKE_BUTTON_TAB)

    def click_on_looks_like_button_click(self):
        self.click_on_element(ButtonsPageLocators.LOOKS_LIKE_BUTTON_CLICK)

    def go_to_disabled_tab(self):
        self.click_on_element(ButtonsPageLocators.DISABLED_TAB)

    def click_on_state_selector(self):
        self.click_on_element(ButtonsPageLocators.SELECT_STATE_FIELD)

    def wait_visibility_of_enabled_state(self):
        enabled_state = WebDriverWait(self.driver, timeout=10)
        enabled_state.until(EC.visibility_of_element_located(ButtonsPageLocators.ENABLED_STATE))

    def click_on_enabled_state(self):
        self.click_on_element(ButtonsPageLocators.ENABLED_STATE)


