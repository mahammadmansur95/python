# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:22:14 2020

@author: acre
"""


class student:
    def __init__(self,name,roll,marks): #constructor
        self.name = name
        self.roll = roll        #instance variable
        self.marks=marks
        
    def display(self):          #method
        print('hello my name is:',self.name)
        print('roll no:',self.roll)
        print('marks:',self.marks)
        
s1=student('mansur',95,7)
s1.display()
s2=student('anuragh',69,8)
s2.display()


"""instance variable vs static variable"""


class test:
    x=10
    def __init__(self):
        self.y=20
t1=test()
t2=test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
test.x=30
t1.y=40
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)


"""modify the values of static variable"""

class test:
    a=777
    @classmethod
    def m1(cls):
        cls.a=888
    @staticmethod
    def m2():
        test.a=999

print(test.a)
test.m1()
print(test.a)
test.m2()
print(test.a)


"""instance method"""

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print('hi',self.name)
        print('your marks',self.marks)
    
    def grade(self):
        if self.marks >=60:
            print('you got first grade')
        elif self.marks>=50:
            print('you got second grade')
        elif self.marks >=35:
            print('you got third grade')
        else:
            print('you are failed')

n=int(input('enter number of students:'))
for i in range(n):
    name=input('enter name:')
    marks = int(input('enter marks:'))
    s=student(name,marks)
    s.display()
    s.grade()
    print()


"""get and set"""
#get is used to get values of instance variable
#set is used toset the values of instance variable

class student:
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
        
    def getMarks(self):
        return self.marks
    
n=int(input('enter the no of students:'))
for i in range(n):
    s=student()
    name=input('enter name:')
    s.setName(name)
    marks=int(input('enter marks'))
    s.setMarks(marks)
    
    
    print('hi',s.getName())
    print('your marks are:',s.getMarks())
    




"""class method"""
#if we are using only class variables (static variables), then such type
#of methods we should declare as class method.

#For class method we should provide cls variable at the time of declaration


class animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print('{} walks with {}legs'.format(name,cls.legs))
        
animal.walk('dog')
animal.walk('cat')


"""static method"""

#Inside these methods we won't use any instance or class variables
#Here we won't provide self or cls arguments at the time of declaration.
#We can access static methods by using classname or object reference

class mansurMath:
    
    @staticmethod
    def add(x,y):
        print('the sum: ',x+y)
    
    @staticmethod
    def product(x,y):
        print('the product:',x*y)
        
mansurMath.add(10,20)
mansurMath.product(10,20)

"""inner class"""

#without existing outer class object there is no chance of existing inner clas object.
#hence inner class object is always associated with outer class object

class outer:
    
    def __init__(self):
        print('outer class object creation')
        
    class inner:
        def __init__(self):
            print('inner class object creation')
        def m1(self):
            print('inner class method')
            
o=outer()
i=o.inner()
i.m1()


class person:
    
    def __init__(self):
        self.name='mansur'
        self.db=self.Dob()
    def display(self):
        print('name:',self.name)
    
    class Dob:
        
        def __init__(self):
            self.dd=19
            self.mm=5
            self.yyyy=1998
        def display(self):
            print('DOB:{}/{}/{}'.format(self.dd,self.mm,self.yyyy))
            
            
p=person()
p.display()
x=p.db
x.display()
            


            
            





































        