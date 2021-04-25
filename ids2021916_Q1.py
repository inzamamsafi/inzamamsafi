#!/usr/bin/env python
# coding: utf-8

# In[1]:


def unique_lst1(List):
    List2 = []
    for i in List:
        if i not in List2:
            List2.append(i)
    print(*List2, sep = ",")
        
list1 = [int(x) for x in input("Enter the list items : ").split(",")]
unique_lst1(list1)

