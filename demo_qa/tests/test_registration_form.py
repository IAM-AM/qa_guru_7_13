import allure
from demo_qa.data import users
from allure_commons.types import Severity
import pytest
from demo_qa.data.users import User
from demo_qa.model.registration_form import RegistrationForm


def test_user():
    test_user = User(
        first_name='Jack',
        last_name='Sparrow',
        email='Jack@pirate.com',
        gender='Male',
        phone_number='2960411232',
        date_of_birth_day=20,
        date_of_birth_month=6,
        date_of_birth_year=1900,
        subject=['Economics'],
        hobby=['Reading'],
        picture='test_pict.png',
        current_address='1301 K Street NW Washington, DC 20071.',
        state='NCR',
        city='Noida'
    )
    return test_user


@allure.title('Successful user registration form')
def test_successful_registration(setup_browser, test_user):
    registration_page = RegistrationForm()
    registration_page.open_site()

    registration_page.first_name(test_user.first_name)
    registration_page.last_name(test_user.last_name)
    registration_page.email(test_user.email)
    registration_page.gender(test_user.gender)
    registration_page.phone_number(test_user.phone_number)
    registration_page.birth_date(test_user.date_of_birth_day,
                                 test_user.date_of_birth_month,
                                 test_user.date_of_birth_year
                                 )
    registration_page.subject(test_user.subject)
    registration_page.hobby(test_user.hobby)
    registration_page.upload_picture(test_user.picture)
    registration_page.current_address(test_user.current_address)
    registration_page.state(test_user.state)
    registration_page.city(test_user.city)

    registration_page.press_submit()
    registration_page.should_have_registered(test_user)
