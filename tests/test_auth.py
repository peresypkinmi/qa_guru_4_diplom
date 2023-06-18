from time import sleep
from steps.test_steps import Test_steps


class TestAuth:

    def test_auth_by_contract(self, set_config_browser):
        step = Test_steps()
        step.open_auth_page()
        step.fill_auth_form()
        step.submit_auth_form()
        step.assert_user_name()




    def test_auth_by_phone(self):
        pass

    def test_auth_with_wrong_password(self):
        pass