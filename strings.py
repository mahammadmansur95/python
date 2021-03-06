# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:47:07 2020

@author: acre
"""


                #Creating a String
'hello'
'this is a full phrase'
"Now I'm ready to use the single quotes inside a string!"

len('hello world') #build in method


                  #indexing

s = 'Hello World'
print(s[0])
      #slicing
s = 'Hello World'
print(s[1:])
print(s[:3])
s[-1]
s[:-1] #except that remainig will print
s[::1]
s[::2] # start to end with every second item
s[::-1] #string backwards
s + ' concatenate me!'
# We can reassign s completely though!
s = s + ' concatenate me!'
print(s)

letter = 'z'
letter*10 #zzzzzzzzzz

            #basic builtin methods

len('hello world')
s.upper()
s.lower()
s.split() # it will be stored in a array
s.split('W') #split using specific element
s.strip()  # remove white space
s.startswith('H') 
s.endswith('!')
s.find('W')
s.count('l')
s.replace('Hello', 'mansur')
my_string = "one,two,three"
a = my_string.split(",")
print(a)

my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)


    
                    #formating
    
    
a = "Hello {0} and {1}".format("Bob", "Tom")
print(a)
print('A {p} saved is a {p} earned.'.format(p='penny'))


# some special format rules for numbers
a = "The float value is {0:.3f}".format(2.1234)
print(a)
a = "The float value is {0:e}".format(2.1234)
print(a)
a = "The binary value is {0:b}".format(2)
print(a)

print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:<8}'.format(11,22,33))

                  #f-strings
name = "mansur"
age = 21
a = f"Hello, {name}. You are {age}."
print(a)

num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
#u will come to know why u added 10 print with and without


                             # Iterating over a string by using a for in loop

my_string = 'Hello world'
for i in my_string:
    print(i,end='') #important
    
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
    
input('Enter Something into this box: ')





#Find the position of a  substring within the string
#This gives us the first index during a left to right scan. If the string is not found, it returns -1
print "Find the index from which the substring 'llo' begins within the test string"
print testString1.find('llo')

print "Now, let's look for a substring which is not a part of the given string"
print testString1.find('xxy')

# Now, trying to find the index of a substring between specified indexes only
print "Now, trying to find a substring between specified indexes only: looking for 'l' between 4 and 9"
print testString1.find('l',4,9)

# rfind is used, to find the index from the reverse
# So, testString1.rfind('l') will look for the last index of l in the string
print "find('l') on the given string returns the following index (scanning the string from left to right):"
print testString1.find('l')

print "rfind('l') on the given string returns the following index (this scans the string from right to left):"
print testString1.rfind('l')
