from steps.test_steps import TestSteps
import os
from dotenv import load_dotenv


class TestAuth:

    def test_auth_by_contract(self, set_config_browser):
        load_dotenv()

        step = TestSteps()

        step.open_auth_page()
        step.select_contract_auth()
        step.fill_auth_form_by_contract(contract=os.getenv("contract"), password=os.getenv("password"))
        step.submit_auth_form()

        step.assert_user_name()

    def test_auth_by_phone(self, set_config_browser):
        step = TestSteps()

        step.open_auth_page()
        step.fill_auth_form_by_phone(phone=os.getenv("phone"), password=os.getenv("password"))
        step.submit_auth_form()

        step.assert_user_name()

    def test_auth_by_contract_with_wrong_password(self, set_config_browser):
        load_dotenv()

        step = TestSteps()

        step.open_auth_page()
        step.select_contract_auth()
        step.fill_auth_form_by_contract(contract=os.getenv("contract"), password="12345")
        step.submit_auth_form()

        step.assert_error_snack_bar()
