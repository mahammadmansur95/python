# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:04:42 2020

@author: acre
"""

                            #files

#Python uses file objects to interact with external files on your computer.

fhand = open('mansur.txt','w')
fhand.write('anantham is my frnd')
fhand.close()
fhand=open('C:\\Users\\acre\\Desktop\\spyder\\test.txt','r')
for lines in fhand:
    print(lines)

myfile = open ('C:\\Users\\acre\\Desktop\\py roundup\\hello.txt')
for lines in myfile:
    print(lines)
myfile.close()

myfile.read()
myfile.seek(0)
myfile.readlines()
# Readlines returns a list of the lines in the file

myfile.write('This is a new line') #to write a file

                         #somethings wrong

