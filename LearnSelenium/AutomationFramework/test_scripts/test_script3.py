from generic.base_test3 import BaseTest


class TestScript1(BaseTest):       # Here we are using inheritance concept (child class)

    def test_script1(self):
        print("This is my script1")
        print(self.driver.title)
