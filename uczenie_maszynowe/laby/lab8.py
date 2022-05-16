#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
from sklearn.datasets import load_iris 
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np


# In[2]:


data_breast_cancer = datasets.load_breast_cancer()
data_iris = load_iris()


# In[3]:


df = pd.DataFrame(data_breast_cancer.data,columns = data_breast_cancer.feature_names)
X = df.iloc[:,0:30]
dfiris = pd.DataFrame(data_iris.data,columns = data_iris.feature_names)
#X = dfiris.iloc[:,0:4]


# In[4]:


pcac = PCA(n_components=0.9)
pca = PCA(n_components=0.9)


# In[5]:


scaler = StandardScaler()
sc = scaler.fit_transform(X)
X2D = pcac.fit_transform(sc)
l = pcac.explained_variance_ratio_
bc = pcac.components_


# In[6]:


scaler = StandardScaler()
si = scaler.fit_transform(dfiris)
XI = pca.fit_transform(si)
I = pca.explained_variance_ratio_
ir = pca.components_


# In[7]:


canlist = []
irlist = []


# In[8]:


for i in l:
    canlist.append(i)


# In[9]:


for i in I:
    irlist.append(i)


# In[10]:


canlist


# In[11]:


irlist


# In[12]:


with open('pca_bc.pkl','wb') as f:
    pickle.dump(canlist,f)
    
pd.read_pickle('pca_bc.pkl')    


# In[13]:


with open('pca_ir.pkl','wb') as f:
    pickle.dump(irlist,f)
    
pd.read_pickle('pca_ir.pkl') 


# In[14]:


pcac.components_


# In[15]:


pca.components_


# In[16]:


x = []
y = []


# In[17]:


for i in range(2):
    x.append(np.argmax(abs(pca.components_[i])))


# In[18]:


x


# In[19]:


for i in range(7):
    y.append(np.argmax(abs(pcac.components_[i])))


# In[20]:


y


# In[21]:


with open('idx_bc.pkl','wb') as f:
    pickle.dump(y,f)
    
pd.read_pickle('idx_bc.pkl') 


# In[22]:


with open('idx_ir.pkl','wb') as f:
    pickle.dump(x,f)
    
pd.read_pickle('idx_ir.pkl') 

