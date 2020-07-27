#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import itertools
a = random.randint(1,100)
for i in itertools.count(start=1):
    print("Attempt Number: ",i)
    x= int(input("Guess the number between 1-100: "))
    if x>a:
        print("The value is high")
    elif x<a:
        print("The value is low")
    else :
        print("You're right!!!")  
        break

