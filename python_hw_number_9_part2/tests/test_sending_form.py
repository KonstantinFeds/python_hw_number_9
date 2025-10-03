from python_hw_number_9_part2.pages.registration_page import Registration_page
from python_hw_number_9_part2.date import users



def test_sending_form (open_browser):

    registration_page = Registration_page()
    student = users.student

    registration_page.register(student)
    registration_page.should_have_registered(student)








