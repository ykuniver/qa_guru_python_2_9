from demoqa_tests.model import app
from demoqa_tests.model.pages import registration_form

from tests.test_data.users import student

import allure
from allure_commons.types import Severity


def test_submit_student_registration_form():

    allure.dynamic.tag('Web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Student registration form")
    allure.dynamic.story("A registration process for the given user")
    allure.dynamic.link('https://demoqa.com')

    # GIVEN

    with allure.step("Given: open the page with the form"):
        app.registration_form.given_opened()

    # WHEN

    with allure.step("When: filling the form"):
        app.registration_form.set_full_name(student.name, student.last_name)

        app.registration_form.set_email(student.email)

        app.registration_form.set_gender(student.gender)

        app.registration_form.set_phone_number(student.user_number)

        app.registration_form.set_birth_date(student.birth_year, student.birth_month, student.birth_day)

        app.registration_form.add_subjects(student.subjects)

        app.registration_form.add_hobbies(student.hobbies)

        app.registration_form.upload_picture(student.picture_file)

        app.registration_form.set_current_address(student.current_address)

        app.registration_form.scroll_to_bottom()

        app.registration_form.set_state(student.state)

        app.registration_form.set_city(student.city)

        app.registration_form.submit_form()

    # THEN

    with allure.step("Then: verifying the result"):
        subjects = app.registration_form.get_subject_list(student.subjects)
        hobbies = app.registration_form.get_hobby_list(student.hobbies)

        registration_form.should_have_submitted(
            [
                ('Student Name', f'{student.name} {student.last_name}'),
                ('Student Email', student.email),
                ('Gender', student.gender.value),
                ('Mobile', student.user_number),
                ('Date of Birth', f'{student.birth_day} {student.birth_month},{student.birth_year}'),
                ('Subjects', subjects),
                ('Hobbies', hobbies),
                ('Picture', student.picture_file),
                ('Address', student.current_address),
                ('State and City', f'{student.state} {student.city}')
            ],
        )
