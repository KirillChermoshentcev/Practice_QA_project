import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.qa-practice.com/')
    driver.maximize_window()
    yield driver
    driver.quit()