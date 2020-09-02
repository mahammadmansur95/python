# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:15:19 2020

@author: acre
"""


"""regular exprections"""

import re
count = 0
matcher = re.finditer('ab','abaaaabaaba')
for match in matcher:
    count +=1
    print(match.start(),"....",match.end(),"....",match.group())
print("the number of occurrences:",count)

    

re.match #to check at staring
re.fullmatch #given is full match to target string
re.search #to search given pattern in target
re.findall #to find all occurences of match . it will return list
re.finditer #
re.sub("[a-z]","#","a7b@9c45gh") #substitute
re.subn() # it returns no.of replacements also

