from conftest import driver
from pages.buttons_page import ButtonsPage


class TestButtonsPage:

    def test_click_on_simple_button_success(self, driver):
        buttons_page = ButtonsPage(driver)
        buttons_page.open()
        buttons_page.is_opened()
        buttons_page.click_on_simple_button()
        buttons_page.get_result_text()
        assert buttons_page.get_result_text() == 'Submitted'

    def test_click_on_looks_like_button_success(self, driver):
        buttons_page = ButtonsPage(driver)
        buttons_page.open()
        buttons_page.is_opened()
        buttons_page.go_to_looks_like_button_tab()
        buttons_page.click_on_looks_like_button_click()
        buttons_page.get_result_text()
        assert buttons_page.get_result_text() == 'Submitted'

    def test_state_selector_success(self, driver):
        buttons_page = ButtonsPage(driver)
        buttons_page.open()
        buttons_page.is_opened()
        buttons_page.go_to_disabled_tab()
        buttons_page.click_on_state_selector()
        buttons_page.wait_visibility_of_enabled_state()
        buttons_page.click_on_enabled_state()
        buttons_page.click_on_simple_button()
        buttons_page.get_result_text()
        assert buttons_page.get_result_text() == 'Submitted'
