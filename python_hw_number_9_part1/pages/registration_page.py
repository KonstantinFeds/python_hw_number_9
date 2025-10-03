import os
from pathlib import Path

from selene import browser,have

class Registration_page:

    def __init__(self):
        self.register = None
        browser.open('/')
        browser.execute_script("window.scrollBy(0, 250);")
        current_file = Path(__file__)
        self.resources_dir = current_file.parent.parent / 'resources'

    def fill_first_name(self,first_name):
        browser.element('#firstName').click().send_keys(first_name)
        return self

    def fill_last_name(self,last_name):
        browser.element('#lastName').click().send_keys(last_name)
        return self

    def fill_email(self,email):
        browser.element('#userEmail').click().send_keys(email)
        return self

    def select_gender(self):
        browser.element('[for="gender-radio-1"]').click()
        return self

    def fill_mobile_number(self,telephone):
        browser.element('[placeholder="Mobile Number"]').click().send_keys(telephone)
        return self

    def birth_of_date(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('[value="4"]').click()
        browser.element('[value="1940"]').click()
        browser.element('.react-datepicker__day--015').click()
        return self

    def fill_subjects(self,subject):
        browser.element('#subjectsInput').send_keys(subject).press_enter()
        return self

    def select_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        return self


    def resource_path(self,filename):
        file_path = self.resources_dir / filename
        browser.element('#uploadPicture').type(str(file_path))
        return self


    def fill_address(self,value):
        browser.element('#currentAddress').send_keys(value)
        return self

    def select_state(self):
        browser.element('#state').click()
        browser.element('//*[text()="Uttar Pradesh"]').click()
        return self

    def select_city(self):
        browser.element('#city').click()
        browser.element('//*[text()="Agra"]').click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_header_registered(self,value):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text
                                                                (value))
        return self

    def registered_user_info(self,student_name,student_email,gender,mobile,date_of_birth, subject, hobbies, file, address, state_and_city):
        browser.all('table tbody tr').should(have.exact_texts(student_name,
                                                              student_email,
                                                              gender,
                                                              mobile,
                                                              date_of_birth,
                                                              subject,
                                                              hobbies,
                                                              file,
                                                              address,
                                                              state_and_city))


    def close_submit(self):
        browser.element('#closeLargeModal').click()

















