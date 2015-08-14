"""Register-machine"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

ADD_PRODUCTS = {} #This saves the products added by manager
SAVE_EXISTENT = [] #This saves the products existent
SAVE_PRICE = [] #This saves the prices
CARDS = [] #This saves the cards


def reset():
    """This cleans the screen"""
    os.system("reset")

def delete_lists():
    """This deletes the lists"""
    del SAVE_EXISTENT[:]
    del SAVE_PRICE[:]
    del CARDS[:]
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
            main_menu()
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
    """This verifies if the product is available"""

    print "Insert the products you want to buy: "
    print "Press done to finish"
    while True:
        sell = insert_product_to_sell()
        if ADD_PRODUCTS.has_key(sell) == True: #Verifies if the product belongs to the dictionary
            print "Q%.2f" % ADD_PRODUCTS.get(sell) #This prints its price respective
            SAVE_EXISTENT.append(sell) #This adds the product to a list
        elif sell == "done":
            reset()
            invoice()
            raw_input("press enter")
            reset()
            count_products()
            raw_input("press enter")
            delete_lists()
            reset()
            main_menu()
        elif sell == "gold":
            CARDS.append("gold") #This adds the gold card
        elif sell == "silver":
            CARDS.append("silver") #This adds the silver card
        else:
            print "This product is not available"

def count_products():
    """This counts each item"""
    for each_item in SAVE_EXISTENT:
        num_of_products = SAVE_EXISTENT.count(each_item)
        print num_of_products, (each_item) + "(s)", "a" , ("Q%.2f c/u") % (ADD_PRODUCTS[each_item])

def discount_card():
    """This verifies the discount of the card"""
    if "gold" in CARDS:
        return sum(SAVE_PRICE) * 0.05 #This calculates the 5%
    elif "silver" in CARDS:
        return sum(SAVE_PRICE) * 0.02 #This calculates the 2%
    elif "gold" in CARDS and "silver" in CARDS:
        return sum(SAVE_PRICE) * 0.05
    else:
        return 0 #Whitout discount

def sub_total():
    """This prints the subtotal"""
    for price in SAVE_EXISTENT:
        SAVE_PRICE.append(ADD_PRODUCTS[price]) #This saves the prices in a list
    return sum(SAVE_PRICE)

def discount():
    """This discounts the card to the subtotal"""
    return sum(SAVE_PRICE) - discount_card()

def tax():
    """This calculates the IVA"""
    return discount() * 0.12

def total():
    return discount() + tax()

def invoice():
    """This prints the invoice"""
    print "The subtotal is:     Q%.2f" % sub_total()
    print "The discount is:     Q%.2f" % discount_card()
    print "The tax is:          Q%.2f" % tax()
    print "The total to pay is: Q%.2f" % total()

def show_products():
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
            show_products()
            sell_products()
        elif ask == "n":
            reset()
            sell_products()
        else:
            print "Election invalid"

def main_menu():
    """This saves the main_menu"""

    print "\nWelcome to Register Machine\n"
    print "1. Add an Item\n"
    print "2. Sell Articles\n"
    print "3. Exit\n"

    answer_main_menu = True
    while answer_main_menu == True:
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
            main_menu()
main_menu()

if __name__ == '__main__':
    pass
