import os

import requests
from requests import Response
from models.user import User

import allure

from session.session import BaseSession
from pytest_voluptuous import S
import random


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

    def get_cart(self):
        return self.api_session.get('cart').json()['List']['Id']

    def clear_cart(self):
        self.api_session.delete('cart/', entity=self.get_cart())

    def get_cart_package_id(self):
        return self.api_session.get('cart').json()['List']['CartPackages'][0]['Id']

    def get_cart_package_productid(self):
        self.api_session.params = {
            'RegionId': 22,
            'LanguageId': 9,
            'CityId': 271,
            'CurrentPage': 1,
            'PerPage': 100,
            'IsArchived': False,
        }
        return self.api_session.get('cart').json()['List']['CartPackages'][0]['CartPackageProducts'][0]['Id']

    def get_product_list(self):
        self.api_session.params = {'CurrentPage': 1,
                                   'PerPage': 16,
                                   'LanguageId': 9,
                                   'RegionId': 22,
                                   'CityId': 271,
                                   'IsActive': True,
                                   'noMutation': True,
                                   'UserTimeZone': 7}
        return self.api_session.get('product').json()['List']

    def get_random_item(self, any_list):
        return any_list[random.randint(0, len(any_list) - 1)]

    def get_random_product_id(self):
        return self.get_random_item(self.get_product_list())['Id']

    def add_random_product_to_cart(self):
        self.api_session.json = {"CartId": self.get_cart(), "CartPackageId": self.get_cart_package_id(),
                                 "ProductId": self.get_random_product_id(), "Quantity": 1}
        self.api_session.post('cartPackageProduct')

    def remove_product(self):
        cart_pcg_id = self.get_cart_package_productid()
        self.api_session.delete('cartPackageProduct/', cart_pcg_id)
