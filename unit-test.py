#!/usr/bin/env python
# -*- coding: utf-8 -*-


import application
import unittest

class RegisterMachineTest(unittest.TestCase):

    #Test 1
    def test_name_product(self):
        self.assertTrue(application.name_product("HAY").islower())
        self.assertTrue(application.nam_product("pro").isalpha())

    #Test 2
    def test_price_product(self):
        self.assertTrue(application.price_product(5))


if __name__ == '__main__':
    unittest.main() 
