from selene import have
from python_hw_number_9_part1.Pages.registration_page import Registration_page


def test_sending_form (open_browser):

    registration_page = Registration_page()

    (
    registration_page.fill_first_name('Иван')
     .fill_last_name('Иванов')
     .fill_email('IIvanon23@gmai.com')
     .select_gender()
     .fill_mobile_number('1234567891')
     .birth_of_date()
     .fill_subjects('Maths')
     .select_hobbies()
     .resource_path('фото.jpg')
     .fill_address('Улица Пушкина, дом Колотушкина')
     .select_state()
     .select_city()
     .submit()

    )

    registration_page.should_have_header_registered('Thanks for submitting the form')
    registration_page.registered_user_info('Student Name Иван Иванов',
                                                          'Student Email IIvanon23@gmai.com',
                                                          'Gender Male',
                                                          'Mobile 1234567891',
                                                          'Date of Birth 15 May,1940',
                                                          'Subjects Maths',
                                                          'Hobbies Sports',
                                                          'Picture фото.jpg',
                                                          'Address Улица Пушкина, дом Колотушкина',
                                                          'State and City Uttar Pradesh Agra')

    registration_page.close_submit()







