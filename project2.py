#!/usr/bin/env python
# coding: utf-8

# In[6]:


list=(2,3,6)

product=1

for item in list:
  product=product*item

print(product)


# In[2]:


def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 10), (1, 8), (4, 7), (2, 9), (2, 6)]))


# In[3]:


from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


# In[4]:


n=int(input("Input a number "))
d = dict()

for i in range(1,n+1):
    d[i]=i*i

print(d) 


# In[5]:


price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))


# In[ ]:




