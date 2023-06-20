import os
from requests import Response
from models.user import User

import allure

from session.session import BaseSession
from pytest_voluptuous import S


class ApiSteps:
    api_session: BaseSession
    response: Response

    @allure.step("Авторизация по API")
    def auth_by_api(self):
        self.api_session.json = {'Password': os.getenv('password'),
                                 'Contract': os.getenv('contract')}

        self.response = self.api_session.post('auth')

    @allure.step("Проверка схемы ответа авторизации")
    def assert_auth_user_schema(self):
        assert S(User.auth_user_schema) == self.response.json()

