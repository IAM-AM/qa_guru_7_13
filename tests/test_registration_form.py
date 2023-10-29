import allure
from allure_commons._allure import step
from allure_commons.types import Severity
from demo_qa.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Aliaksandr Manko")
@allure.feature("Registration Form")
@allure.story("User is successfully registered")
@allure.link("https://demoqa.com/", name="Testing")
def test_successful_student_registration_form():
    with step("Open registration page"):
        registration_page = RegistrationPage()
        registration_page.open()

    with step("Fill in the first name"):
        registration_page.fill_first_name("Jack")

    with step("Fill in the last name"):
        registration_page.fill_last_name("Sparrow")

    with step("Fill in the email"):
        registration_page.fill_user_email("Jack@pirate.com")

    with step("Fill in the gender"):
        registration_page.fill_gender("Male")

    with step("Fill in the phone number"):
        registration_page.fill_phone_number("6049524551")

    with step("Fill in the birthday date"):
        registration_page.fill_date_of_birth("July", "1900", "23")

    with step("Fill in the subjects"):
        registration_page.fill_subjects("Economics")

    with step("Fill in the hobbies"):
        registration_page.fill_hobbies("Reading")

    with step("Fill in the picture"):
        registration_page.upload_picture("test_image.png")

    with step("Fill in the current address"):
        registration_page.fill_current_address(
            "1301 K Street NW Washington, DC 20071."
        )
    with step("Fill in the state"):
        registration_page.fill_state("NCR")

    with step("Fill in the city"):
        registration_page.fill_city("Noida")

    with step("Submit the form"):
        registration_page.submit_form()

    with step("Verify the confirmation modal form pops up"):
        registration_page.modal_form_pops_up()

    with step("Verify the student is registered with the correct data"):
        registration_page.should_be_registered(
            "Jack Sparrow",
            "Jack@pirate.com",
            "Male",
            "6049524551",
            "23 July,1900",
            "Economics",
            "Reading",
            "test_image.png",
            "1301 K Street NW Washington, DC 20071.",
            "NCR Noida",
        )
