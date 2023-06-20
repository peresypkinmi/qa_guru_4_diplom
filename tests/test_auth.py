import allure
from pytest_voluptuous import S

from models.user import User
from steps.test_steps import TestSteps
import os
from dotenv import load_dotenv


class TestAuth:

    @allure.tag("UI")
    @allure.title("Авторизация по контракту")
    def test_auth_by_contract(self, set_config_browser):
        load_dotenv()

        step = TestSteps()

        step.open_auth_page()
        step.select_contract_auth()
        step.fill_auth_form_by_contract(contract=os.getenv("contract"), password=os.getenv("password"))
        step.submit_auth_form()

        step.assert_user_name()

    @allure.tag("UI")
    @allure.title("Авторизация по номеру телефона")
    def test_auth_by_phone(self, set_config_browser):
        step = TestSteps()

        step.open_auth_page()
        step.fill_auth_form_by_phone(phone=os.getenv("phone"), password=os.getenv("password"))
        step.submit_auth_form()

        step.assert_user_name()

    @allure.tag("UI")
    @allure.title("Попытка авторизации с неверным паролем")
    def test_auth_by_contract_with_wrong_password(self, set_config_browser):
        load_dotenv()

        step = TestSteps()

        step.open_auth_page()
        step.select_contract_auth()
        step.fill_auth_form_by_contract(contract=os.getenv("contract"), password="12345")
        step.submit_auth_form()

        step.assert_error_snack_bar()

    @allure.tag("API")
    @allure.title("Проверка схемы ответа авторизации")
    def test_auth_api(self, get_api_step):
        api_step = get_api_step

        api_step.auth_by_api()

        assert S(User.auth_user_schema) == api_step.response.json()
