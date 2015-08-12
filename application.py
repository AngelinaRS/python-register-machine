"""Register-machine"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

ADD_PRODUCTS = {} #This saves the products added by manager
SAVE_EXISTENT = [] #This saves the products existent

def reset():
    """This cleans the screen"""
    os.system("reset")

#Test #1
def name_product():
    """This saves the name of the product"""
    reset()
    if __name__ == '__main__':
        while True:
            product = raw_input("Add the product: ")
            if product.isalpha(): #This verifies if the product that has inserted, has a valid name
                return product.lower()
            else:
                print "Insert a valid name"
    return product

#Test 2
def price_product():
    """This saves the price of the product"""
    if __name__ == '__main__':
        while True:
            price = raw_input("Add the price: ")
            try:
                price = float(price) #This verifies if the price is a number
                return price
            except ValueError:
                print "Insert a number"
    return price

def add_item(product, price):
    """This saves the products and prices in a dictionary"""
    ADD_PRODUCTS[product] = price


def add_product_with_price():
    """This adds the product with their respective price"""

    product = name_product()
    price = price_product()
    add_item(product, price)

    while True:
        another = raw_input("Do you want to insert another article? y/n ")
        another = another.lower()
        if another == "y":
            product = name_product()
            price = price_product()
            add_item(product, price)
        elif another == "n":
            reset()
            menu()
        else:
            reset()
            print "Insert y or n"
#Test 3
def insert_product_to_sell():
    """This inserts the product to buy"""
    sell = raw_input(" - ")
    sell = sell.lower()
    return sell

def sell_products():
    """This verificate if the product is available"""

    print "Insert the products you want to buy: "
    print "Press done to finish"
    while True:
        sell = insert_product_to_sell()
        if ADD_PRODUCTS.has_key(sell) == True: #Verifies if the product belongs to the dictionary
            print "%.2f" % ADD_PRODUCTS.get(sell) #This prints its price respective
            SAVE_EXISTENT.append(sell) #This adds the product to a list
        elif sell == "done":
            reset()
            menu()
        else:
            print "This product is not available"

def products_to_sell():
    """This shows the products in sale"""

    print "These are the products in sale"
    for key, value in ADD_PRODUCTS.iteritems():
        print "%s: Q%.2f" % (key, value)

def ask_if_want():
    """This asks to the user if wants to see the products"""
    while True:
        ask = raw_input("Do you want to see the products in sale? ")
        ask = ask.lower()
        if ask == "y":
            reset()
            products_to_sell()
            sell_products()
        elif ask == "n":
            reset()
            sell_products()
        else:
            print "Election invalid"
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
            add_product_with_price()
        elif choose_user == "2":
            reset()
            ask_if_want()
        elif choose_user == "3":
            reset()
            sys.exit() #This forces the output of interpreter
        else:
            reset()
            print "*Election invalid, choose a valid option"
            print SAVE_EXISTENT
            menu()
menu()

if __name__ == '__main__':
    menu()
