from selene.support.shared import browser


def select_date(year, month, day):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__day--0{day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()

# Well, I don't want to import from selenium from now, so I leave it commented
# from selenium.webdriver.common.keys import Keys
# def date_picker_typed_directly(date: str):
#    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL + 'a' + Keys.NULL, date).press_enter()
# OR something like
# browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
