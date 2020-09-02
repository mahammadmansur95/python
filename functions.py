# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:36:44 2020

@author: acre
"""

"""functions"""


def say_hello():
    print('hello')

say_hello()  #calling a ffunction
#------------------------------------------------
def greeting(name):    #with a parameter
    print(f'Hello {name}') 
    
greeting('mansur')


#----------------------------------------------------

def add_num(num1,num2):
    return num1+num2      #using return

result  = add_num(1,2)

print(result)


def even_check(number):
    return number % 2 == 0
even_check(20)

#----------------------------------------------------

#Returning Tuples for Unpacking

stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]

for item in stock_prices:
    print(item)

for stock,price in stock_prices:
    print(stock)
    
#-------------------------------------

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
    
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   
       
    return len(code) == 1
spy_game([1,2,4,0,0,7,5])

#--------------------------------------

#map function

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

done=list(map(square,my_nums))
""" another"""
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
         return mystring[0]
mynames = ['John','Cindy','Sarah','Kelly','Mike']
list(map(splicer,mynames))

#--------------------------------------

#filter function

def check_even(num):
    return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]
list(filter(check_even,nums))

#------------------------------------------


#*args

def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)

#-----------------------------------------

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
    

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)














