#!/usr/bin/env python
# coding: utf-8

# In[3]:


userName = input('Enter your name:')
greeting = 'Hello'
print(f'{greeting}, {userName}!')


# In[6]:


import time
time.sleep(1)


# In[7]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'Greeting.ipynb'])


# In[ ]:




