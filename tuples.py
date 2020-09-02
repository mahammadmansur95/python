# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:24:53 2020

@author: acre
"""


                        #tuples
t = (1,2,3)

y = ('one',2,'one')

tuple_4 = tuple([1,2,3])
print(tuple_4)

t[0] #to access tuple


#slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)


#we cannot change the values in the tuple

#basic methods

y.index('one')

y.count('one')

len(t)

                        #iterating 

tup = (1,2,3,4,5)

for t in tup:
    print(t)

'''for tuple there is special '''

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)
    # Now with unpacking!
for (t1,t2) in list2:
    print(t1)


                        #operator
    
tuple(range(0,10))

tup1= ('a','b','c')
tup2= (1,2,3)

for item1, item2 in zip(tup1,tup2):
    print('first item was {} and second item was {}'.format(item1,item2))

tup =(10,20,50)
min(tup)
max(tup)




