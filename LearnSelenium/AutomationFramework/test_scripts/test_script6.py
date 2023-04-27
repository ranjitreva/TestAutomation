from generic.base_test6 import BaseTest
from generic.utility import Excel


class TestScript1(BaseTest):      # Here we are using inheritance concept (child class)

    def test_script1(self):
        print("This is my script1")
        print(self.driver.title)
        value2 = Excel.get_cell_value("../data/Input.xlsx", "Sheet1", 2, 1)
        print(value2)
