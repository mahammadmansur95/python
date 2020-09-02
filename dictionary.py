# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:36:43 2020

@author: acre
"""


                            #dictionary

my_dict = {'key1':'value1','key2':'value2'}

#accessing them
my_dict['key1']

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
my_dict['key3']
my_dict['key3'][0].upper()

d = {}
d['animal'] = 'Dog' #it will be added into dict

#nested dict
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
d['key1']['nestkey']['subnestkey']


#dict methods
d = {'key1':1,'key2':2,'key3':3}

d.keys()  #dict_keys(['key1', 'key2', 'key3'])

d.values()

d.items() #dict_items([('key1', 1), ('key2', 2), ('key3', 3)])

d['key1'] = 5 #to change values

                            #iterators

d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item) #only keys will be printed
    
for k,v in d.items():
    print(k)
    print(v)
    
list(d.keys())    #it will store in list
sorted(d.values())  #it will store in list


