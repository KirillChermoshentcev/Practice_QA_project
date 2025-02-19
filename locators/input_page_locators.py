class InputPageLocators:

    INPUT_FIELD = ('xpath', '//input[@id="id_text_string"]')
    EMAIL_TAB = ('xpath', '//a[contains(text(),"Email field")]')
    EMAIL_FIELD = ('xpath', '//input[@id="id_email"]')
    PASSWORD_TAB = ('xpath', '//a[contains(text(),"Password field")]')
    PASSWORD_FIELD = ('xpath', '//input[@id="id_password"]')
    RESULT_TEXT = ('xpath', '//p[@id="result-text"]')