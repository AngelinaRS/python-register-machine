import application
import unittest

class RegisterMachineTest(unittest.TestCase):
    #test function 1
    def test_product_isalpha(self):
        self.assertTrue(application.product_isalpha("Hay"))
        self.assertFalse(application.product_isalpha("5"))

    #test function 2
    def test_minuscule(self):
        self.assertTrue(application.minuscule("DULCE"), "dulce")

    #test function 3
    def test_gold_card(self):
        self.assertEqual(application.gold_card(100), 5)

    #test function 4
    def test_silver_card(self):
        self.assertEqual(application.silver_card(100),2)

    #test function 5
    def test_tax(self):
        self.assertEqual(application.tax(100, 0), 12)

    #test function 7
    def test_total_final(self):
        self.assertEqual(application.total_final(100, 0, 12), 112)


if __name__ == "__main__":
    unittest.main()