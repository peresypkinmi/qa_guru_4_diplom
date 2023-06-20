from dotenv import load_dotenv

from steps.test_steps import TestSteps


class TestCart:

    def test_add_random_product_to_cart_without_auth(self, set_config_browser):
        load_dotenv()

        step = TestSteps()

        step.open_main_page()
        step.add_product_to_cart()
        step.open_small_cart()

        step.assert_product_availability_in_small_cart()

    def test_add_random_product_to_cart_with_auth(self, get_api_step, set_config_browser):
        step_api = get_api_step
        step_ui = TestSteps()

        step_api.auth_by_api()
        step_ui.open_main_page_as_auth(step_api.api_session)
        step_ui.add_product_to_cart()
        step_ui.open_small_cart()

        step_ui.assert_product_availability_in_small_cart()