#!/usr/bin/env python
# coding: utf-8

# In[4]:


from collections import Counter

str1 = input()
# Returns the first items value in the list of tuples (i.e) the largest number
# from Counter().most_common()
max_count: int = Counter(str1).most_common()[0][1]

# If the tuples value is equal to the max value, append it to the list
list1: list = [(x)
                         for x, y in Counter(str1).items() if y == max_count]

seprator = ","
print(seprator.join(list1))


# In[ ]:




