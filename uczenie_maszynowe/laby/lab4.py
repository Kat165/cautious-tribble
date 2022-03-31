#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
import numpy as np
import pickle


# In[2]:


data_breast_cancer = datasets.load_breast_cancer()
#print(data_breast_cancer['DESCR'])


# In[3]:


#print(data_breast_cancer)


# In[4]:


data_iris = datasets.load_iris()
#print(data_iris['DESCR'])


# In[5]:


#print(data_iris)


# In[6]:


from sklearn.model_selection import train_test_split


# In[7]:


#mean smoothness mean area features


# In[8]:


Xb = data_breast_cancer["data"][:, (3,4)]
yb = (data_breast_cancer["target"]).astype(np.int8) #malignant


# In[9]:


Xb_train, Xb_test, yb_train, yb_test = train_test_split(Xb, yb, test_size=0.2)


# In[10]:


X = data_iris["data"][:, (2, 3)]
y = (data_iris["target"] == 2).astype(np.int8) 


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# In[12]:


from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# In[13]:


svm_clf = Pipeline([
        ("scaler", StandardScaler()),
        ("linear_svc", LinearSVC(C=1,
                                 loss="hinge")),])
svm_clf.fit(X_train, y_train)


# In[14]:


print(svm_clf.predict([[5.5, 1.7],
                       [4.5, 1.7]]))


# In[15]:


svm_clf.score(X_test, y_test)


# In[16]:


from sklearn.metrics import accuracy_score


# In[17]:


X_pred = svm_clf.predict(X_test)


# In[18]:


irispedskaltest = accuracy_score(y_test,X_pred)
irispedskaltest


# In[19]:


X_predr = svm_clf.predict(X_train)


# In[20]:


irisperdskaltrain = accuracy_score(y_train,X_predr)
irisperdskaltrain


# In[21]:


svm_clf2 = Pipeline([("linear_svc", LinearSVC(C=1,loss="hinge"))])


# In[22]:


svm_clf2.fit(X_train, y_train)


# In[23]:


X_predb = svm_clf.predict(X_test)
irispredbezskaltest = accuracy_score(y_test,X_pred)
irispredbezskaltest


# In[24]:


X_predbr = svm_clf.predict(X_train)
irispredbezskaltrain = accuracy_score(y_train,X_predbr)
irispredbezskaltrain


# In[25]:


###########breast cancer###############


# In[26]:


#svm_clf = Pipeline([
#        ("scaler", StandardScaler()),
#        ("linear_svc", LinearSVC(C=1,
#                                 loss="hinge",random_state = 42)),])
svm_clf.fit(Xb_train, yb_train)


# In[27]:


Xb_pred = svm_clf.predict(Xb_test)
cancerskaltest = accuracy_score(yb_test,Xb_pred)
cancerskaltest


# In[28]:


Xb_predbr = svm_clf.predict(Xb_train)
cancerskaltrain = accuracy_score(yb_train,Xb_predbr)
cancerskaltrain


# In[29]:


svm_clf2.fit(Xb_train, yb_train)


# In[30]:


Xb_predbez = svm_clf2.predict(Xb_test)
cancerbezskaltest = accuracy_score(yb_test,Xb_predbez)
cancerbezskaltest


# In[31]:


Xb_predbbezr = svm_clf2.predict(Xb_train)
cancerbezskaltrain = accuracy_score(yb_train,Xb_predbbezr)
cancerbezskaltrain


# In[32]:


irislist = [irispredbezskaltrain,irispredbezskaltest,irisperdskaltrain,irispedskaltest]


# In[33]:


cancerlist = [cancerbezskaltrain,cancerbezskaltest,cancerskaltrain,cancerskaltest]


# In[34]:


with open('bc_acc.pkl', 'wb') as f:
    pickle.dump(cancerlist, f)


# In[35]:


with open('iris_acc.pkl', 'wb') as f:
    pickle.dump(irislist, f)


# In[36]:


with open('bc_acc.pkl', 'rb') as f:
    mynewlist = pickle.load(f)


# In[37]:


mynewlist


# In[38]:


with open('iris_acc.pkl', 'rb') as f:
    mynewlist = pickle.load(f)


# In[39]:


mynewlist

