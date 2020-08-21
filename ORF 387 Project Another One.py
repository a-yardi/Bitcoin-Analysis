#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tarfile


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


tf = tarfile.open("/Users/anikayardi/Desktop/bitcoin.tar.gz")


# In[4]:


tf.extractall('/Users/anikayardi/Desktop/Tar')


# In[5]:


import pandas as pd
import numpy as np
import random


# In[6]:


df = pd.read_csv("/Users/anikayardi/Desktop/Tar/bitcoin/bitcoin.links.csv")


# In[6]:


# remove all columns except for
# merge historical data with the count table;


# In[8]:


sample = df.sample(5000)


# In[7]:


df_edit = df[["dst_id", "src_id", "count", "maxdate", "mindate"]]


# In[8]:


df1 = df_edit[['maxdate','count']]


# In[9]:


df1['maxdate'] = pd.to_datetime(df1['maxdate'])


# In[10]:


df1


# In[14]:


# ********************************** THIS IS ITTTTTTT **************************************


# In[11]:


dates = df1['maxdate'].dt.floor('D')
dates = df1['maxdate'].dt.date


# In[12]:


dfc = df1.groupby([dates]).sum().reset_index()


# In[13]:


dfc


# In[14]:


np.mean(dfc)


# In[15]:


np.max(dfc)


# In[17]:


np.std(dfc)


# In[18]:


np.min(dfc)


# In[18]:


dfc.columns = ['Date', 'count']


# In[75]:


dfc1 = dfc.drop(dfc.index[0:859])


# In[76]:


dfc1


# In[19]:


dfc


# In[42]:


df_a = df1.groupby(df1.maxdate.dt.date)["count"].sum()


# In[18]:


df_edit


# In[19]:


df_b = pd.read_csv("/Users/anikayardi/Desktop/BitcoinData.csv")


# In[20]:


df_b = df_b[['Date','Price']]
df_b['Date'] = pd.to_datetime(df_b['Date'])


# In[21]:


df_b.Date = df_b.Date.values[::-1]


# In[22]:


df_b.Price = df_b.Price.values[::-1]


# In[24]:


np.mean(df_b)


# In[30]:


df_b['Price'].median()


# In[25]:


np.std(df_b)


# In[26]:


np.max(df_b)


# In[27]:


np.min(df_b)


# In[78]:


plt.figure()

x = df_b['Price']
y = dfc1['count']

plt.scatter(x, y)


# In[ ]:





# In[29]:


df_t = pd.read_csv("/Users/anikayardi/Desktop/Tar/bitcoin/bitcoin.vertices.csv")


# In[11]:


sample_t = df_t.sample(10000)


# In[12]:


print(df_t.sample(10))


# In[14]:


df_s = sample_t[["vid", "first_transaction_date"]]


# In[30]:


df_t = df_t[["vid", "first_transaction_date"]]


# In[31]:


df_t


# In[16]:


df_s


# In[15]:


df_s.mean()


# Group the transaction values by dates, and sum up over the count

# In[ ]:




