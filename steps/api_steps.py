import os

import allure

from session.session import BaseSession


class ApiSteps:
    api_session: BaseSession

    @allure.step("Авторизация по API")
    def auth_by_api(self):
        self.api_session.json = {'Password': os.getenv('password'),
                                 'Contract': os.getenv('contract')}

        self.api_session.post('auth').json()
