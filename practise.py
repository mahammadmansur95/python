# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:49:09 2020

@author: acre
"""


"""print hello world"""

print('hello world')


"""add two numbers"""

n1=int(input('enter one numbers:'))
n2=int(input('enter one numbers:'))
r= n1+n2
print(r)


"""to square root"""

n = int(input('enter the number:'))
r=n**0.5
print(r)

"""swap of two variables"""

x=5
y=6

temp=x
x=y
y=temp

print(x)
print(y)

x,y=y,x

x = x + y
y = x - y
x = x - y

"""generate a random number"""

from random import randint

n=randint(0, 10)
print(n)

"""check even or odd"""

n=int(input('enter the number:'))
if n%2 ==0:
    print('even')
else:
    print('odd')
    
"""leap year or not"""

#A leap year is exactly divisible by 4 except for century years (years ending with 00). 
#The century year is a leap year only if it is perfectly divisible by 400. 

n=int(input('enter the year:'))

if n%4==0:
    if n%100 == 0:
        if n%400 == 0:
            print('{}is a leap year'.format(n))
        else:
            print('{}is not a leap year'.format(n))
            
    else:
        print('{} is a leap year'.format(n))
        
else:
    print('{}is not a leap year'.format(n))
    

"""to check prime or not"""

n = int(input('enter the num:'))

if n > 1 :
    
    for i in range(2,n):
        if n%i == 0:
            print('not a prime')
            break
    else :
        print('prime')
else:
    print('plz enter valid num')
    
"""print all the prime numbers in a interval"""

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           

"""factorial of a number"""

n=int(input('enter the number:'))

factorial=1

if n<0:
    print('fact dosenot exist')
    
elif n == 0:
    print('the fact is 1')
else:
    for i in range(1,n+1):
        factorial = factorial*i
    print('the fact is',factorial)
    
"""multiplication table"""

n=int(input('enter the num for table'))

for i in range(1,11):
    print(n, 'x', i, '=', n*i)
    
"""fibonacci sequence"""

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1,end=' ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

"""armstrong number"""

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10 #to take individual number from digit
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   
   
# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
       

"""sum of natural numbers"""

#n*(n+1)/2

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       print('{}-{}'.format(num,sum))
       sum += num
       num -= 1
   print("The sum is", sum)
    
"""Display Powers of 2 Using Anonymous Function"""

terms = 10

result = list(map(lambda x: 2 ** x, range(terms)))
    
print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
   

   
   
    
    
    
    

    






    
    
    


    














