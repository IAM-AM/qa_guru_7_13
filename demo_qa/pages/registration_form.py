from selene import browser, command, have
import allure
from demo_qa.tests.conftest import resource_path


class RegistrationForm:
    def __init__(self):
        self.google_ad = browser.all('[id^=google_ads][id$=container__]')

    def open_site(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def first_name(self, value):
    def last_name(self, value):
    def email(self, value):
    def gender(self, value):
    def phonenumber(self, value):
    def birth_date(self, value):
    def subject(self, value):
    def hobbie(self, value):
    def upload_picture(self, value):
    def current_adress(self, value):

    def is_enabled(self, value):


    def state(self):
    def city(self):

    def press_submit(self):


    with allure.step('Fill form'):
        browser.element('#firstName').type('Jack')
        browser.element('#lastName').type('Sparrow')
        browser.element('#userEmail').type('Jack@pirate.com')
        browser.element('#userNumber').type('2960411232')
        browser.element('label[for="gender-radio-1"]').click()
        browser.all('#genterWrapper')[1].should(have.no.enabled)
        browser.all('#genterWrapper')[2].should(have.no.enabled)
        browser.all('#genterWrapper')[0].should(have.no.disabled)
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        browser.element('select[class="react-datepicker__year-select"]').click().element(
            'option[value="1900"]').click()
        browser.element('select[class="react-datepicker__month-select"]').click().element(
            'option[value="5"]').click()

        browser.element('div[class="react-datepicker__day react-datepicker__day--020"]').click()
        browser.element('#subjectsInput').type('Economics').press_tab()
        browser.element('label[for="hobbies-checkbox-2"]').click()
        browser.element('#hobbies-checkbox-0').should(have.no.enabled)
        browser.element('#hobbies-checkbox-2').should(have.no.disabled)
        browser.element('#currentAddress').type('1301 K Street NW Washington, DC 20071.').press_tab()
        browser.element('#react-select-3-input').type('NCR').press_enter().press_tab()
        browser.element('#react-select-4-input').type('Noida').press_enter().press_tab()
        browser.element('#submit').press_enter()

    with allure.step('Check results'):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text(
            'Thanks for submitting the form'))
        browser.element('.table').should(have.text('Jack'))
        browser.element('.table').should(have.text('Sparrow'))
        browser.element('.table').should(have.text('Jack@pirate.com'))
        browser.element('.table').should(have.text('Male'))
        browser.element('.table').should(have.text('2960411232'))
        browser.element('.table').should(have.text('20 June,1900'))
        browser.element('.table').should(have.text('Economics'))
        browser.element('.table').should(have.text('Reading'))
        browser.element('.table').should(have.text('1301 K Street NW Washington, DC 20071.'))
        browser.element('.table').should(have.text('NCR Noida'))
