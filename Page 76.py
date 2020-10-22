#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior',
 'Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
 columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[3]:


df2 = df.set_index(df['Names'])
df2.plot(kind="bar")


# In[4]:


df3 = df.set_index(df['Grades'])
df3.plot(kind="bar")


# In[ ]:




