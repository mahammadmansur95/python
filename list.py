# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:53:21 2020

@author: acre
"""
                        #list

my_list =[1,2,3]

my_list = ['A string',23,100.232,'o']
#we can add any type of into list



                        #indexing

my_list =[1,2,3]

my_list[0]

my_list[-1]

my_list[1:]

my_list[::-1]

my_list[0] = 5 #we can change by indexing

#string concatenate
my_list + ['new item']

# Make the list double
my_list * 2


                        #builtin methods

list1 = [1,2,3]

len(list1)

list1.append('append me!')

list1.pop(0)

list1.count(2)


#sorting
new_list = ['a','e','x','b','c']
new_list.sort()

new_list.reverse()


                        #nested list

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

matrix[0][0] #to grab


                        #iterating through list

list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)

for num in list1: #to print even num
    if num%2 ==0:
        print(num)
        
sum = 0     #sum in list
for num in list1:
    sum = sum +num
print(sum)


                        #operator

list(range(0,10))

list(range(0,10,3))

li=[1,2,3]
for i,num in enumerate(li):
    print('at index{} the num is {}'.format(i,num))


list(enumerate('abcde'))

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
list(zip(mylist1,mylist2))


for item1, item2 in zip(mylist1,mylist2):
    print('first item was {} and second item was {}'.format(item1,item2))


mylist = [10,20,30,40,100]
min(mylist)
max(mylist)

from random import shuffle
shuffle(mylist)
mylist

from random import randint
randint(0,100)

input('Enter Something into this box: ')

                    #list comprehensions

lst = [x for x in 'word']

lst = [x**2 for x in range(0,11)]

lst = [x for x in range(11) if x % 2 == 0]

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
fahrenheit

lst = [ x**2 for x in [x**2 for x in range(11)]]
lst











