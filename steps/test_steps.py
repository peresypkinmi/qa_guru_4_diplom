import allure

from steps.ui_steps import UiSteps


class Test_steps(UiSteps):

    @allure.step("Переход на страницу авторизации")
    def open_auth_page(self):
        self.open_main_page()
        self.open_user_menu()
        self.open_login_page()
        self.select_contract_auth()

    @allure.step("Заполнение полей авторизации")
    def fill_auth_form(self):
        self.fill_contract_field()
        self.fill_password_field()

    @allure.step("Отправка формы авторизации")
    def submit_auth_form(self):
        self.press_enter_button()
