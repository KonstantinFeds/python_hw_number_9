from selene import browser, have

from python_hw_number_9_part3.date.students import Student
from python_hw_number_9_part3.pages.locators_page_text_box import LocatorsSimpleRegistrationsTextBox


class SimpleRegistrationForm:

    def open_browser(self):
        browser.open('/')

    def fill_user_name(self, value):
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_FULL_NAME).type(value)

    def fill_email(self, value):
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_EMAIL).type(value)

    def fill_current_address(self, value):
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_CURRENT_ADDRESS).type(value)

    def fill_permanent_address(self, value):
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_PERMANENT_ADDRESS).type(value)

    def submit(self):
        browser.element(LocatorsSimpleRegistrationsTextBox.SUBMIT_BUTTON).click()

    def simple_registration_text_box(self, people: Student):
        self.open_browser()
        self.fill_user_name(people.fill_name)
        self.fill_email(people.email)
        self.fill_current_address(people.current_address)
        self.fill_permanent_address(people.permanent_address)
        self.submit()

    def assert_simple_registration_form(self, people: Student):
        (browser.element(LocatorsSimpleRegistrationsTextBox.ASSERT_SIMPLE_REGISTRATION_FORM).all('p')
        .should(have.exact_texts(
            f'Name:{people.fill_name}',
            f'Email:{people.email}',
            f'Current Address :{people.current_address}',
            f'Permananet Address :{people.permanent_address}')))
