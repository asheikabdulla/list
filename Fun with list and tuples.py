#!/usr/bin/env python
# coding: utf-8

# In[2]:


sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]

def last_else(n):
    return n[-1]

sorted_list=sorted(sample_list,key=last_else)

print(sorted_list)


# In[ ]:




