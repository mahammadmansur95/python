# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:42:03 2020

@author: acre
"""


"""well explained example"""


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
    
ordinary() #I am ordinary

pretty = make_pretty(ordinary)
pretty() #it gets decorated

#Generally, we decorate a function and reassign it as,
ordinary = make_pretty(ordinary)




#to decorate it using @symbol
     
@make_pretty
def ordinary():
    print("I am ordinary")


#example
    
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)




















