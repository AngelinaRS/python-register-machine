"""Register-machine"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def reset():
    """This cleans the screen"""
    os.system("reset")

def menu():
    """This saves the menu"""

    print "\nWelcome to Register Machine\n"
    print "1. Add an Item\n"
    print "2. Sell Articles\n"
    print "3. Exit\n"

    answer_menu = True
    while answer_menu == True:
        choose_user = raw_input(" - ") #This saves the election of the user
        if choose_user == "3":
            reset()
            sys.exit() #This forces the output of interpreter
        else:
            reset()
            print "* Election invalid, choose one option valid"
            menu()
menu()
