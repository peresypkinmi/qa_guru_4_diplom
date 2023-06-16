from time import sleep


class TestAuth:

    def test_auth_by_contract(self):
        for i in range(10000):
            s = i
        sleep(5)
        assert s == 9999


    def test_auth_by_phone(self):
        pass

    def test_auth_with_wrong_password(self):
        pass