#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import fetch_openml 
import numpy as np
mnist = fetch_openml('mnist_784', version=1, as_frame=False) 
mnist.target = mnist.target.astype(np.uint8)
X = mnist["data"]
y = mnist["target"]


# In[2]:


from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import pickle
from sklearn.metrics import confusion_matrix
from numpy.linalg import norm
from sklearn.cluster import DBSCAN


# In[3]:


kmeans8 = KMeans(n_clusters=8)
pred8 = kmeans8.fit_predict(X)


# In[4]:


kmeans9 = KMeans(n_clusters=9)
pred9 = kmeans9.fit_predict(X)


# In[5]:


kmeans10 = KMeans(n_clusters=10)
pred10 = kmeans10.fit_predict(X)


# In[6]:


kmeans11 = KMeans(n_clusters=11)
pred11 = kmeans11.fit_predict(X)


# In[7]:


kmeans12 = KMeans(n_clusters=12)
pred12 = kmeans12.fit_predict(X)


# In[8]:


k8 = silhouette_score(X, kmeans8.labels_)
k9 = silhouette_score(X, kmeans9.labels_)
k10 = silhouette_score(X, kmeans10.labels_)
k11 = silhouette_score(X, kmeans11.labels_)
k12 = silhouette_score(X, kmeans12.labels_)


# In[9]:


import pandas as pd


# In[10]:


sillist = [k8,k9,k10,k11,k12]
with open('kmeans_sil.pkl', 'wb') as f:
  pickle.dump(sillist, f)


pd.read_pickle("kmeans_sil.pkl")


# In[11]:


m10 = confusion_matrix(y,pred10)


# In[12]:


np.argmax(m10,axis=0)
m = []
for row in m10:
    m.append(np.argmax(row))
ind =list(set(m))
print(ind)


# In[13]:


with open('kmeans_argmax.pkl', 'wb') as f:
  pickle.dump(ind, f)


pd.read_pickle("kmeans_argmax.pkl")


# In[14]:


temp = []
for i in range(300):
    for j in range(70000):
        if j > i:
            temp.append(np.linalg.norm(X[i]-X[j]))
temp = sorted(temp)


# In[15]:


t= []
for k in temp:
    if k != 0:
        t.append(k)


# In[16]:


maxlist = []
for i in range(10):
    maxlist.append(t[i])


# In[17]:


with open('dist.pkl', 'wb') as f:
  pickle.dump(maxlist, f)


pd.read_pickle("dist.pkl")


# In[18]:


s = (t[0] + t[1] + t[2])/3
x = s+0.1*s
print(s)
x
m = 0.04*s
j = s
print(x)


# In[19]:


eps=[]
while j < x:
    eps.append(j)
    j = j + m
eps


# In[20]:


dbscan1 = DBSCAN(eps = eps[0])
db1 = dbscan1.fit(X)


# In[21]:


l1 = list(set(db1.labels_))


# In[22]:


dbscan2 = DBSCAN(eps = eps[1])
db2 = dbscan2.fit(X)


# In[23]:


l2 = list(set(db2.labels_))


# In[24]:


dbscan3 = DBSCAN(eps = eps[2])
db3 = dbscan3.fit(X)


# In[25]:


l3 = list(set(db3.labels_))


# In[26]:


lellist = [len(l1),len(l2),len(l3)]


# In[27]:


with open('dbscan_len.pkl', 'wb') as f:
  pickle.dump(lellist, f)


pd.read_pickle("dbscan_len.pkl")


# In[ ]:




