import os
import random
from time import sleep

import allure
from dotenv import load_dotenv
from selene.core import query
from selene.support.conditions import be, have
from selene.support.shared import browser
from models.product import Product


class UiSteps:

    @allure.step("Переход на главную страницу")
    def open_main_page(self):
        browser.open('')

    @allure.step("Открыть Юзер-меню")
    def open_user_menu(self):
        browser.element('.user-bar__icon').should(be.visible).click()

    @allure.step("Переход на страницу авторизации")
    def open_login_page(self):
        browser.element("[data-qa='VLOGIN_REGISTRATION_BAR_LOGIN_LINK']").should(be.visible).click()
        sleep(10)

    @allure.step("Переключение на страницу авторизации по контракту")
    def select_contract_auth(self):
        browser.element('[data-qa="SIGN_IN_BY_CONTRACT_OR_EMAIL"]').should(be.visible).click()

    @allure.step("Заполнение поля контракт")
    def fill_contract_field(self, contract):
        browser.element("input[name='contractOrEmail']").should(be.visible).click().type(contract)

    @allure.step("Заполнение поля телефон")
    def fill_phone_field(self, phone):
        browser.element('input[id="phone"]').should(be.visible).click().type(phone)

    @allure.step("Заполнение поля пароль")
    def fill_password_field(self, password):
        load_dotenv()
        browser.element("input[name='password']").should(be.visible).click().type(password)

    @allure.step("Нажатие кнопки 'Войти'")
    def press_enter_button(self):
        browser.element(".sw-button.sign-in__button").should(be.visible).click()

    @allure.step("Проверка имени пользователя после авторизации")
    def assert_user_name(self):
        browser.element("[data-qa='VUSERBAR_NAME']").should(have.exact_text("Testyyui Testeeoi"))

    @allure.step("Проверка появления снекбара с информацией об ошибке")
    def assert_error_snack_bar(self):
        browser.element("div[id='sw-snackbar-loginError']").should(be.visible)

    @allure.step("Выбор случайной карточки товара")
    def choice_random_product_index(self):
        return random.randint(1, len(browser.all(".product-card-c-for-slider.products-list-slider-v2__slide").should(
            have.size_greater_than(3))) - 1)

    @allure.step("Запись данных выбранного продукта")
    def get_product_data(self):
        test_product = Product(
            NameFull=browser.element(f'h1[class="product__name"]').get(query.text),
            Price=browser.element('div[class="product-sheet-b-price-block__price"]').get(
                query.text))
        return test_product

    @allure.step("Добавление продукта в корзину")
    def add_to_cart(self, test_product):
        browser.element("[data-qa='VCARTBUTTON_TITLE']").should(be.visible).click()
        Cart.add_product_to_cart(test_product, 1)

    @allure.step("Открыть малую корзину")
    def open_small_cart(self):
        browser.element("div[class='cart-bar__icon']").should(be.visible).click()

    @allure.step("Проверка наличия продукта в корзине")
    def assert_product_availability_in_small_cart(self):
        expected_product = Cart.cartPackages[0]['product']
        browser.element('div[class=cart-bar-cart-product__name]').should(have.text(expected_product.get_name_full()))
        browser.element('div[class=cart-bar-cart-product__price]').should(have.text(expected_product.get_price()))

    @allure.step("Переход на страницу карточки товара")
    def open_product_card(self):
        load_dotenv()
        browser.open(os.getenv('test_product_url'))

    @allure.step("Открыть страницу заглушку")
    def open_plug_page(self):
        browser.open('favico.ico')

    @allure.step("Открыть главную страницу как авторизованый пользователь")
    def open_main_page_with_auth(self, session):
        browser.driver.add_cookie({'name': 'token', 'value': session.headers['token']})
        browser.open('')
