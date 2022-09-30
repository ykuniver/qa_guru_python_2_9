from typing import Tuple

from selene import have, command, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss

from demoqa_tests.model.controls import dropdown, modal, datepicker
from tests.test_data.users import Subject, Hobby

from demoqa_tests.utils import path

state = browser.element('#state')


def given_opened():
    browser.open('/automation-practice-form')
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def set_full_name(first_name: str, last_name: str):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)


def set_email(email: str):
    browser.element('#userEmail').type(email)


def set_gender(gender):
    browser.all('[for^=gender-radio]').by(have.exact_text(gender.value)).first.click()
    # it works too, so I keep to for myself
    # gender_xpath = "//input[@name='gender']/following-sibling::label[contains(text(),'" + gender.value + "')]"
    # browser.element(by.xpath(gender_xpath)).click()
    # please see also examples below in this file


def set_phone_number(user_number: str):
    browser.element('#userNumber').type(user_number)


def set_birth_date(birth_year, birth_month, birth_day):
    datepicker.select_date(birth_year, birth_month, birth_day)


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def get_subject_list(values: Tuple[Subject]):
    subjects = ''

    for subject in values:
        subjects = subjects + str(subject.value) + ', '

    subjects = subjects.rstrip(', ')

    return subjects


def add_hobbies(values: Tuple[Hobby]):
    for hobby in values:
        # browser.element(f'//label[contains(.,"{hobby.value}")]').click()
        # browser.element(by.text(hobby.value, tag='label')).click()
        # browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
        #     '..'
        # ).click()
        hobby_xpath = "//label[contains(.,'" + str(hobby.value) + "')]"
        browser.element(by.xpath(hobby_xpath)).click()


def get_hobby_list(values: Tuple[Subject]):
    hobbies = ''

    for hobby in values:
        hobbies = hobbies + str(hobby.value) + ', '

    hobbies = hobbies.rstrip(', ')

    return hobbies


def upload_picture(picture_file: str):
    browser.element('[id="uploadPicture"]').send_keys(
        path.to_resource(picture_file)
    )


def set_current_address(current_address: str):
    browser.element('#currentAddress').type(current_address)


def set_state(value: str):
    dropdown.select(state, value)


def set_city(value: str):
    dropdown.select(browser.element('#city'), value)


def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)


def submit_form():
    browser.element('#submit').perform(command.js.click)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))


'''
# OR
gender_male = browser.element('[for=gender-radio-1]')
gender_male.click()
# OR
browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
browser.element('[id^=gender-radio][value=Male]').element(
    './following-sibling::*'
).click()
# OR better:
browser.element('[id^=gender-radio][value=Male]').element('..').click()
# OR
browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()
browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()
'''
