# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:32:48 2020

@author: acre
"""


                                #oops
"""instance variable"""
class employee:
    
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first+'.'+last+'@company.com'
      
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 =employee('mansur', 'mahammad', 50000)


print(emp_1.email)

#both work same 
print(emp_1.fullname())
print(employee.fullname(emp_1)) #if we take class


"""class variable"""

class employee:
    
    num_of_emps = 0
    
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first+'.'+last+'@company.com'
        
        employee.num_of_emps += 1
      
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        
        
print(employee.num_of_emps)

emp_1 =employee('mansur', 'mahammad', 50000)
emp_2 =employee('munavar', 'mahammad', 60000)

#emp_1.raise_amount = 1.05

print(employee.num_of_emps)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


"""classmethods and staticmethods"""


class employee:
    
    num_of_emps = 0
    
    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first+'.'+last+'@company.com'
        
        employee.num_of_emps += 1
      
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
        
        
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day): #they dont work on instance
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 =employee('mansur', 'mahammad', 50000)
emp_2 =employee('munavar', 'mahammad', 60000)

"""
emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jane-doe-90000'



new_emp_1 = employee.from_string(emp_str_1)

print(new_emp_1.email) """

import datetime
my_date = datetime.date(2016,7,10)

print(employee.is_workday(my_date))




"""Inheritance - Creating Subclasses"""


class employee:
    
    
    
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first+'.'+last+'@company.com'
        
      
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        
class developer(employee):
    #pass
    raise_amt = 1.10
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        #employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang
        
class manager(employee):
    
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        #employee.__init__(self,first,last,pay)
        if employee is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    
    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())
            
            
            
dev_1 = developer('corey', 'schfaer', 50000,'python')
dev_2 = employee('test','employee',60000)


mgr_1 = manager('sue', 'smith', 90000,[dev_1])

"""
print(mgr_1.email)

mgr_1.print_emps()


#print(dev_1.prog_lang)
#print(dev_2.email)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay) """

#built-in 
print(isinstance(mgr_1,employee))
print(issubclass(mgr_1,employee))





""" Special (Magic/Dunder) Methods"""


class employee:
    
    
    
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first+'.'+last+'@company.com'
        
      
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        
        
    def __repr__(self):
        return "employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return '{}'.format(self.email)
        
emp_1 =employee('mansur', 'mahammad', 50000)
emp_2 =employee('munavar', 'mahammad', 60000)



#print(emp_1)

print(repr(emp_1))
print(str(emp_2))


"""Property Decorators - Getters, Setters, and Deleters"""

class employee:
    
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @property    #as it is a method we can acces it as attribute in down
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self): #it takes only self
        print('delete name')
        self.first = None
        self.last = None
    
    
    
emp_1 = employee('john','smith')

#emp_1.first ='jim' """we can change here like this""" 

emp_1.fullname = 'corey schafer'  #we can change fullname like it ,but first and last wont chage also we get error,so above .setter methods comes into action 


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)    #we can acces here without () because @property decorator

del emp_1.fullname








        