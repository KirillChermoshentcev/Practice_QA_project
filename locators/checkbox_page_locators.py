class CheckboxPageLocators:

    CHECKBOX = ('xpath', '//label[contains(text(),"Select me or not")]')
    SUBMIT_BUTTON = ('xpath', '//input[@id="submit-id-submit"]')
    CHECKBOXES_TAB = ('xpath', '//a[contains(text(),"Checkboxes")]')
    ONE_CHECKBOX = ('xpath', '//input[@id="id_checkboxes_0"]')
    TWO_CHECKBOX = ('xpath', '//input[@id="id_checkboxes_1"]')
    THREE_CHECKBOX = ('xpath', '//input[@id="id_checkboxes_2"]')
    RESULT_TEXT = ('xpath', '//p[@id="result-text"]')
