from selene import browser, command, have
import allure
from demo_qa.data.users import User
from demo_qa.tests.resources import resource_path


class RegistrationForm:
    def __init__(self):
        self.remove_google_ad = browser.all('[id^=google_ads][id$=container__]')

    @allure.step('Open main page')
    def open_site(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    @allure.step('Fill first name')
    def first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    @allure.step('Fill last name')
    def last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    @allure.step('Fill email')
    def email(self, email):
        browser.element('#userEmail').type(email)
        return self

    @allure.step('Fill gender')
    def gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element(
            '..'
        ).click()
        return self

    @allure.step('Fill phone number')
    def phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    @allure.step('Fill birth date')
    def birth_date(self, month, year, day):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element(f'[class="react-datepicker__month-select"]>option[value="{month}"]').click()
        browser.element(f'[class="react-datepicker__year-select"]>option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--00{day}').click()

    @allure.step('Select subject')
    def subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_tab()
        return self

    @allure.step('Select hobbie')
    def hobby(self, hobby):
        browser.all('[id^=hobby][type=checkbox]+label').element_by(
            have.exact_text(hobby)
        ).click()
        return self

    @allure.step('Upload picture')
    def upload_picture(self, picture_path):
        browser.element('#uploadPicture').set_value(resource_path(picture_path))
        return self

    @allure.step('Fill address')
    def current_address(self, address):
        browser.element('#currentAddress').type(address).press_tab()
        return self

    @allure.step('Select state')
    def state(self, state):
        browser.element('[id="react-select-3-input"]').type(state).press_enter()
        return self

    @allure.step('Select city')
    def city(self, city):
        browser.element('[id="react-select-4-input"]').type(city).press_enter()
        return self

    @allure.step('Submit the form')
    def press_submit(self):
        browser.element('#submit').perform(command.js.click)

    @allure.step('Fill the form')
    def registration(self, user: User):
        self.first_name(user.first_name)
        self.last_name(user.last_name)
        self.email(user.email)
        self.gender(user.gender)
        self.phone_number(user.phone_number)
        self.birth_date(user.date_of_birth_year,
                        user.date_of_birth_month,
                        user.date_of_birth_day
                        )
        self.subject(user.subject)
        self.hobby(user.hobby)
        self.upload_picture(user.picture)
        self.current_address(user.current_address)
        self.state(user.state)
        self.city(user.city)
        self.press_submit()

    @allure.step("Check user's data")
    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            user.first_name,
            user.last_name,
            user.email,
            user.gender,
            user.phone_number,
            f"{user.date_of_birth_day} {user.date_of_birth_month} {user.date_of_birth_year}",
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            user.state,
            user.city))
