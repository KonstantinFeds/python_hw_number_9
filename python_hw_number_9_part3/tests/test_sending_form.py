from python_hw_number_9_part3.date import students
from python_hw_number_9_part3.pages.application import app


def test_sending_form_part3(open_browser):
    student = students.people

    app.simple_registration_form.simple_registration_text_box(student)
    app.simple_registration_form.assert_simple_registration_form(student)
