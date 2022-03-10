#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, sys, tarfile, gzip, urllib
import pandas as pd
import matplotlib.pyplot as plt
import shutil
import seaborn as sns
from sklearn.model_selection import train_test_split
import pickle

data = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz'
urllib.request.urlretrieve(data,'housing.tar')


# In[2]:


def extract(data, extract_path='.'):
    print (data)
    tar = tarfile.open(data, 'r')
    for item in tar:
        tar.extract(item, extract_path)
        if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
            extract(item.name, "./" + item.name[:item.name.rfind('/')])


# In[3]:


extract('housing.tar')


# In[4]:


with open('housing.csv', 'rb') as f_in:
    with gzip.open('housing.csv.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


# In[5]:


df = pd.read_csv('housing.csv.gz')


# In[6]:


df.head()
#df.info()


# In[7]:


s = df['ocean_proximity']
s.value_counts()
s.describe()


# In[8]:


df.hist(bins=50, figsize=(20,15))
plt.savefig('obraz[1].png')


# In[9]:


df.plot(kind="scatter", x="longitude", y="latitude",
        alpha=0.1, figsize=(7,4))
plt.savefig('obraz[2].png')


# In[10]:


df.plot(kind="scatter", x="longitude", y="latitude",
        alpha=0.4, figsize=(7,3), colorbar=True,
        s=df["population"]/100, label="population", 
        c="median_house_value", cmap=plt.get_cmap("jet"))
plt.savefig('obraz[3].png')


# In[11]:


#cor = df.corr()["median_house_value"].sort_values(ascending=False)
df.corr()["median_house_value"].sort_values(ascending=False).reset_index().rename(columns={'index': 'atrybuty', 'median_house_value': 'wspolczynnik_korelacji'}).to_csv('korelacja.csv', sep=',', index=False)


# In[12]:


sns.pairplot(df)


# In[13]:


train_set, test_set = train_test_split(df,
                                       test_size=0.2,
                                       random_state=42)
len(train_set),len(test_set)


# In[14]:


train_set.head()
train_set.describe()


# In[15]:


test_set.head()
test_set.describe()


# In[16]:


test_set.corr()


# In[17]:


test_set.corr()["median_house_value"].sort_values(ascending=False)


# In[18]:


train_set.corr()["median_house_value"].sort_values(ascending=False)


# In[19]:


train_set.corr()


# In[20]:


#są podobne


# In[21]:


train_set.to_pickle('train_set.pkl')
test_set.to_pickle('test_set.pkl')

