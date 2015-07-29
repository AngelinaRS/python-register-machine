"""Register-machine"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

ADD_PRODUCTS = {}

def reset():
    """This cleans the screen"""
    os.system("reset")

def name_product():
    reset()
    while True:
        product = raw_input("Add the product: ")
        if product.isalpha() == True:
            return product.lower()
        else:
            print "Insert a valid name"

def price_product():
    while True:
        price = raw_input("Add the price: ")
        try:
            price = float(price)
            return price
        except:
            print "Insert a number"


def add_item(product, price):
    ADD_PRODUCTS[product] = price

def add_article():
    name_article = name_product()
    product_price = price_product()

    while True:
        another = raw_input("Do you want to insert another article? y/n ")
        another = another.lower()
        if another == "y":
            name_product()
            price_product()
        elif another == "n":
            reset()
            menu()
        else:
            reset()
            print "Insert y or n"


def menu():
    """This saves the menu"""

    print "\nWelcome to Register Machine\n"
    print "1. Add an Item\n"
    print "2. Sell Articles\n"
    print "3. Exit\n"

    answer_menu = True
    while answer_menu == True:
        choose_user = raw_input(" - ") #This saves the election of the user
        if choose_user == "1":
            reset()
            add_article()
        elif choose_user == "3":
            reset()
            sys.exit() #This forces the output of interpreter
        else:
            reset()
            print "*Election invalid, choose a valid option"
            menu()
menu()

