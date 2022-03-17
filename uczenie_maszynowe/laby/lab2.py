#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import fetch_openml
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix


# In[2]:


mnist = fetch_openml('mnist_784', version=1)


# In[3]:


# ad 5 - > wszystko jedno na ktorym zbiorze


# In[4]:


print((np.array(mnist.data.loc[40]).reshape(28, 28) > 0).astype(int))


# In[5]:


X,y = mnist["data"], mnist["target"].astype(np.uint8)


# In[6]:


print(y)


# In[7]:


y = y.sort_values()
print(y)


# In[8]:


print(y.index)


# In[9]:


X = X.reindex(y.index)


# In[10]:


#X_train, X_test = X[:56000], X[56000:]
#y_train, y_test = y[:56000], y[56000:]
#print(X_train.shape, y_train.shape)
#print(X_test.shape, y_test.shape)


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,train_size = 0.8)


# In[12]:


print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)


# In[13]:


pd.unique(y_test)


# In[14]:


# Naucz klasyfikator Stochastic Gradient Descent wykrywać cyfrę 0.


# In[15]:


y_train_0 = (y_train == 0)
y_test_0 = (y_test == 0)


# In[16]:


sgd_clf = SGDClassifier()
sgd_clf.fit(X_train, y_train_0)


# In[17]:


sgd_clf.predict(X_test)


# In[18]:


acc_test = accuracy_score(y_test_0,sgd_clf.predict(X_test))
print(acc_test)


# In[19]:


acc_train = accuracy_score(y_train_0,sgd_clf.predict(X_train))
print(acc_train)


# In[32]:


list = [acc_train, acc_test]


# In[33]:


with open('sgd_acc.pkl', 'wb') as f: #nazwa do amiany
    pickle.dump(list, f)


# In[34]:


with open('sgd_acc.pkl', 'rb') as f:
    mynewlist = pickle.load(f)
 
mynewlist


# In[35]:


score = cross_val_score(sgd_clf, X_train, y_train_0, cv=3, scoring="accuracy", n_jobs=-1)
print(score)


# In[36]:


s = score.tolist()
with open('sgd_cva.pkl', 'wb') as f:
    pickle.dump(s, f)


# In[37]:


with open('sgd_cva.pkl', 'rb') as f:
    mynewlist = pickle.load(f)
 
mynewlist


# In[38]:


sgd_m_clf = SGDClassifier(n_jobs=-1)
sgd_m_clf.fit(X_train, y_train)
print(sgd_m_clf.predict(X_test))


# In[39]:


y_train_pred = cross_val_predict(sgd_m_clf, X_train, y_train, cv=3, n_jobs=-1)


# In[40]:


conf_mx = confusion_matrix(y_train, y_train_pred)
print(conf_mx)


# In[41]:


c = conf_mx.tolist()
with open('sgd_cmx.pkl', 'wb') as f:
    pickle.dump(c, f)


# In[42]:


with open('sgd_cmx.pkl', 'rb') as f:
    mynewlist = pickle.load(f)
 
mynewlist


# In[ ]:




