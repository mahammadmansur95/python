# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:30:24 2020

@author: acre
"""


# As built-in Python functions like range(), map() and filter() are generators

def gencubes(n):
    for num in range(n):
        yield num**3
        
        
for x in gencubes(10):
    print(x)
    


#generate fibnocci series
    
    
def genfibon(n):
    
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)
    

    
