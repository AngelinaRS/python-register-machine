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

#test 1
def product_isalpha(product):
    """This verifies the valid name of the product"""
    if product.isalpha():  #This verifies if the product that has inserted, has a valid name
        return True
    else:
        return False

#test 2
def name_product(product=""):
    """This saves the name of the product"""
    if __name__ == '__main__':
        reset()
        enter_product = False
        while enter_product == False:
            product = raw_input("Add the product: ")
            product.lower()
            enter_product = product_isalpha(product)
            if enter_product == False:
                print "Insert a valid name"
    return product

#test 3
def price_product(price=0):
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

#Test 4
def insert_product_to_sell(sell=""):
    """This inserts the product to buy"""
    if __name__ == '__main__':
        sell = raw_input("\n - ")
    sell = sell.lower()
    return sell

def sell_products():
    """This verifies if the product is available"""

    print "\nInsert the products you want to buy: "
    print "Press done to finish\n"
    while True:
        sell = insert_product_to_sell()
        if ADD_PRODUCTS.has_key(sell) == True: #Verifies if the product belongs to the dictionary
            print "   Q%.2f " % (ADD_PRODUCTS.get(sell)) #This prints its price respective
            SAVE_EXISTENT.append(sell) #This adds the product to a list
            SAVE_PRICE.append(ADD_PRODUCTS[sell]) #This saves the prices in a list
        elif sell == "done":
            reset()
            invoice()
            raw_input("\n\npress enter")
            delete_lists()
            reset()
            main_menu()
        elif sell == "gold":
            CARDS.append("gold") #This adds the gold card
        elif sell == "silver":
            CARDS.append("silver") #This adds the silver card
        else:
            print "This product is not available"

def count_products(list_products):
    """This counts each item"""
    for each_item in ADD_PRODUCTS: #This iterates in the dictionary
        num_of_products = list_products.count(each_item) #This count each product
        if num_of_products > 0:
            price = ADD_PRODUCTS[each_item]
            print num_of_products, each_item+ "(s)", "a", ("Q%.2f c/u") % price

#test 5
def gold_card(subtotal):
    """This calculates the discount of the gold card"""
    return subtotal * 0.05

#test 6
def silver_card(subtotal):
    """This calculates the discount of the silver card"""
    return subtotal * 0.02

def sub_total():
    """This adds all the prices"""
    return sum(SAVE_PRICE)

def discount_card(subtotal=0):
    """This verifies the discount of the card"""
    subtotal = sub_total()

    if "gold" in CARDS:
        return gold_card(subtotal) #This calculates the 5%

    elif "silver" in CARDS:
        return silver_card(subtotal) #This calculates the 2%

    elif "gold" in CARDS and "silver" in CARDS:
        return gold_card(subtotal)

    else:
        return 0 #Whitout discount

    #test 7
def subtract_discount(subtotal=0, discount=0):
    """This discounts the card to the subtotal"""
    if __name__ == "__main__":
        subtotal = sub_total()
        discount = discount_card()
    return subtotal - discount

    #test 8
def tax(subtotal_less_discount=0):
    """This calculates the IVA"""
    if __name__ == "__main__":
        subtotal_less_discount = subtract_discount()
    return subtotal_less_discount * 0.12

    #test 9
def total_final(with_discount=0, iva=0):
    """This calculates the total final"""
    if __name__ == "__main__":
        with_discount = subtract_discount()
        iva = tax()
    return with_discount + iva

def invoice():
    """This prints the invoice"""
    name = raw_input("What is your name?  ")
    reset()
    print "---------------INVOICE---------------"
    print ""
    print "          DESPENSA FAMILIAR          \n"
    print "%s" % name
    print ""
    count_products(SAVE_EXISTENT)
    print "\nThe subtotal is:----------- Q%.2f" % sub_total()
    print "The discount is:----------- Q%.2f" % discount_card()
    print "The tax is:---------------- Q%.2f" % tax()
    print "The total to pay is:------- Q%.2f" % total_final()
    print "-------------------------------------"
    print "\n\n---Thank you for shopping with us---"


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

    print "\n-----Welcome to Register Machine-----\n"
    print "       1. Add an Item\n"
    print "       2. Sell Articles\n"
    print "       3. Exit\n"
    print "-------------------------------------"
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
            main_menu()
if __name__ == "__main__":
    main_menu()
