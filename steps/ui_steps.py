from time import sleep
import os
from dotenv import load_dotenv

import allure
from selene.support.conditions import be

from utils import attach
from selene.support.shared import browser, config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
    def fill_contract_field(self):
        load_dotenv()
        browser.element("input[name='contractOrEmail']").should(be.visible).click().type(os.getenv("contract"))
        sleep(5)

    @allure.step("Заполнение поля пароль")
    def fill_password_field(self):
        load_dotenv()
        browser.element("input[name='password']").should(be.visible).click().type(os.getenv("password"))
        sleep(5)

    @allure.step("Нажатие кнопки 'Войти'")
    def press_enter_button(self):
        browser.element(".sw-button.sign-in__button").should(be.visible).click()
        sleep(3)

