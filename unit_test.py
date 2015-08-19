import application
import unittest

class RegisterMachineTest(unittest.TestCase):
    #test function 1
    def test_product_isalpha(self):
        self.assertTrue(application.product_isalpha("hay"))
        self.assertFalse(application.product_isalpha("5"))
    #test function 2

    def test_name_product(self):
        self.assertTrue(application.name_product("PRO").isalpha())
        self.assertTrue(application.name_product(5))

    #test function 3
    def test_price_product(self):
        self.assertTrue(application.price_product(5))

    #test function 4
    def test_insert_product_to_sell(self):
        self.assertTrue(application.insert_product_to_sell("HAY").islower())

    #test function 5
    def test_gold_card(self):
        self.assertEqual(application.gold_card(100), 5)

    #test function 6
    def test_silver_card(self):
        self.assertEqual(application.silver_card(100),2)




if __name__ == "__main__":
    unittest.main()