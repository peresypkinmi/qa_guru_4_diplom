import allure

from session.session import BaseSession
from steps.ui_steps import UiSteps


class TestSteps(UiSteps):
    api_session: BaseSession = ''

    @allure.step("Переход на страницу авторизации")
    def open_auth_page(self):
        self.open_main_page()
        self.open_user_menu()
        self.open_login_page()

    @allure.step("Заполнение полей авторизации по контракту")
    def fill_auth_form_by_contract(self, contract, password):
        self.fill_contract_field(contract)
        self.fill_password_field(password)

    @allure.step("Заполнение полей авторизации по телефону")
    def fill_auth_form_by_phone(self, phone, password):
        self.fill_phone_field(phone)
        self.fill_password_field(password)

    @allure.step("Отправка формы авторизации")
    def submit_auth_form(self):
        self.press_enter_button()

    @allure.step("Добавить случайный продукт в корзину с главной страницы")
    def add_random_product_to_cart(self):
        index = self.choice_random_product_index()
        test_product = self.get_product_data(index)
        self.add_product_to_cart(index, test_product)

    @allure.step("Переход на страницу карточки товара")
    def add_product_to_cart(self):
        self.open_product_card()
        test_product = self.get_product_data()
        self.add_to_cart(test_product)

    def open_main_page_as_auth(self, api_session):
        self.open_plug_page()
        self.open_main_page_with_auth(api_session)
