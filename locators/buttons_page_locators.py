class ButtonsPageLocators:

    SUBMIT_BUTTON = ('xpath', '//input[@id="submit-id-submit"]')
    LOOKS_LIKE_BUTTON_TAB = ('xpath', '//a[contains(text(),"Looks like a button")]')
    LOOKS_LIKE_BUTTON_CLICK = ('xpath', '//a[@class="a-button"]')
    DISABLED_TAB = ('xpath', '//a[contains(text(),"Disabled")]')
    SELECT_STATE_FIELD = ('xpath', '//select[@id="id_select_state"]')
    ENABLED_STATE = ('xpath', '//option[contains(text(),"Enabled")]')
    RESULT_TEXT = ('xpath', '//p[@id="result-text"]')