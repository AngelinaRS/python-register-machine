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
    if os.name == "posix": #In linux
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"): #In windows
        os.system("cls")
reset()

def delete_lists():
    """This deletes the lists"""
    del SAVE_EXISTENT[:]
    del SAVE_PRICE[:]
    del CARDS[:]

def press_enter():
    """This says to the user press enter"""
    raw_input("\n\nPress Enter")

#test 1
def product_isalpha(product):
    """This verifies the valid name of the product"""
    if product.isalpha():  #This verifies if the product that has inserted, has a valid name
        return True
    else:
        return False

#test 2
def minuscule(product):
    """This converts the product in minuscule"""
    product = product.lower()
    return product

def valid_name_product():
    """This saves the name of the product"""
    reset()
    enter_product = False
    while enter_product == False:
        product = raw_input("Add the product: ")
        product_lower = minuscule(product)
        enter_product = product_isalpha(product)
        if enter_product == False:
            print "insert a valid name"
    return product_lower

def price_product():
    """This saves the price"""
    while True:
        price = raw_input("Add the price: ")
        try:
            price = float(price)
            return price
        except ValueError: #if the price is a number
            print "Insert a number"
    return price

def add_item(product, price):
    """This saves the products and prices in a dictionary"""
    ADD_PRODUCTS[product] = price

def add_product_with_price():
    """This adds the product with their respective price"""

    product = valid_name_product()
    price = price_product()
    add_item(product, price)

    while True:
        another = raw_input("\nDo you want to insert another article? y/n ")
        another = another.lower()
        if another == "y":
            product = valid_name_product()
            price = price_product()
            add_item(product, price)
        elif another == "n":
            reset()
            main_menu()
        else:
            reset()
            print "Insert y or n"

def insert_product_to_sell():
    """This inserts the product to buy"""
    product = raw_input("\n - ")
    sell = minuscule(product)
    return sell

def verify_done():
    """This verifies if the user not buys"""
    if SAVE_EXISTENT == []:
        print "\nCan't generate the invoice because You have not bought"
        press_enter()
        reset()
        show_products()
        sell_products()
    else:
        reset()
        invoice()
        press_enter()
        delete_lists()
        reset()
        main_menu()

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
            verify_done()
            main_menu()
        elif sell == "gold":
            CARDS.append("gold") #This adds the gold card
        elif sell == "silver":
            CARDS.append("silver") #This adds the silver card
        else:
            print "\nThis product is not available"

def show_products():
    """This shows the products in sale"""

    print "These are the products in sale"
    for key, value in ADD_PRODUCTS.iteritems():
        print "%s: Q%.2f" % (key, value)

def ask_if_want():
    """This asks to the user if wants to see the products"""
    while True:
        ask = raw_input("Do you want to see the products in sale? y/n ")
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


def option_two():
    """Verifies if the dictionary is empty"""
    if ADD_PRODUCTS == {}:
        print "\n**No products availabe**" #Cannot to buy
        press_enter()
        reset()
        main_menu()
    else:
        ask_if_want()

def count_products(list_products):
    """This counts each item"""
    for each_item in ADD_PRODUCTS: #This iterates in the dictionary
        num_of_products = list_products.count(each_item) #This count each product
        if num_of_products > 0:
            price = ADD_PRODUCTS[each_item]
            print num_of_products, each_item + "(s)", "a", ("Q%.2f c/u") % price

#test 3
def gold_card(subtotal):
    """This calculates the discount of the gold card"""
    return subtotal * 0.05

#test 4
def silver_card(subtotal):
    """This calculates the discount of the silver card"""
    return subtotal * 0.02

def sub_total():
    """This adds all the prices"""
    return sum(SAVE_PRICE)

def discount_card(subtotal):
    """This verifies the discount of the card"""

    if "gold" in CARDS:
        return gold_card(subtotal) #This calculates the 5%

    elif "silver" in CARDS:
        return silver_card(subtotal) #This calculates the 2%

    elif "gold" in CARDS and "silver" in CARDS:
        return gold_card(subtotal)

    else:
        return 0 #Whitout discount

#test 5
def tax(subtotal, discount):
    """This calculates the IVA"""
    return (subtotal - discount) * 0.12


#test 6
def total_final(subtotal, discount, iva):
    """This calculates the total final"""
    return (subtotal - discount) + iva

def invoice():
    """This prints the invoice"""
    name = raw_input("What is your name?  ")

    subtotal = sub_total()
    discount = discount_card(subtotal)
    iva = tax(subtotal, discount)
    total = total_final(subtotal, discount, iva)

    reset()
    print "---------------INVOICE---------------"
    print ""
    print "          DESPENSA FAMILIAR          \n"
    print "%s" % name
    print ""
    count_products(SAVE_EXISTENT)
    print "\nThe subtotal is:----------- Q%.2f" % subtotal
    print "The discount is:----------- Q%.2f" % discount
    print "The tax is:---------------- Q%.2f" % iva
    print "The total to pay is:------- Q%.2f" % total
    print "-------------------------------------"
    print "\n\n---Thank you for shopping with us---"

def main_menu():
    """This saves the main menu"""

    print "-------------------------------------"
    print "\n     Welcome to Register Machine\n"
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
            option_two()
        elif choose_user == "3":
            reset()
            sys.exit() #This forces the output of interpreter
        else:
            reset()
            print "*Election invalid, choose a valid option"
            main_menu()

if __name__ == "__main__":
    main_menu()
