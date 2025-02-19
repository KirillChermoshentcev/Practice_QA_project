from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def find_element_with_wait(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_visibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def check_element_is_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys_to_input(self, locator, keys):
        element = self.driver.find_element(*locator)
        element.send_keys(keys)
        element.send_keys(Keys.ENTER)

    def get_text_from_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        return element.text



