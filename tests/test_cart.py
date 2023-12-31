import time

from dotenv import load_dotenv

from steps.test_steps import TestSteps
import allure


class TestCart:

    @allure.tag("UI")
    @allure.title("Добавление товара в корзину без авторизации")
    def test_add_product_to_cart_without_auth(self, set_config_browser):
        step = TestSteps()

        step.open_main_page()
        step.add_product_to_cart()
        step.open_small_cart()

        step.assert_product_availability_in_small_cart()

    @allure.tag("UI-API")
    @allure.title("Добавление товара в корзину авторизованного пользователя")
    def test_add_product_to_cart_with_auth(self, get_api_step, set_config_browser):
        step_api = get_api_step
        step_ui = TestSteps()

        step_api.auth_by_api()
        step_api.clear_cart()
        step_ui.open_main_page_as_auth(step_api.api_session)
        step_ui.add_product_to_cart()
        step_ui.open_small_cart()

        step_ui.assert_product_availability_in_small_cart()

    def test_test(self, get_api_step):
        api_step = get_api_step
        api_step.auth_by_api()
        api_step.add_random_product_to_cart()
        assert 2==2

    def test_remove_product(self, get_api_step):
        api_step = get_api_step
        api_step.auth_by_api()
        api_step.add_random_product_to_cart()
        time.sleep(3)
        api_step.remove_product()