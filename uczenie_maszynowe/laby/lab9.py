#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import numpy as np
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow import keras
import pickle


# In[2]:


iris = load_iris()


# In[3]:


X = iris["data"][:, (2, 3)]
y_0 = (iris["target"] == 0).astype(np.int8) 
y_1 = (iris["target"] == 1).astype(np.int8) 
y_2 = (iris["target"] == 2).astype(np.int8) 


# In[4]:


X_train_0, X_test_0, y_train_0, y_test_0 = train_test_split(X, y_0, test_size=0.2)
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X, y_1, test_size=0.2)
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X, y_2, test_size=0.2)


# In[5]:


per_clf = Perceptron()
per_clf.fit(X_train_0, y_train_0)
w_0 = (per_clf.intercept_[0], per_clf.coef_[0][0], per_clf.coef_[0][1])
print(w_0)
X_pred_test_0 = per_clf.predict(X_test_0)
X_pred_train_0 = per_clf.predict(X_train_0)
acc_test_0 = accuracy_score(y_test_0,X_pred_test_0)
acc_train_0 = accuracy_score(y_train_0,X_pred_train_0)
print(acc_test_0)
print(acc_train_0)


# In[6]:


per_clf.fit(X_train_1, y_train_1)
w_1 = (per_clf.intercept_[0], per_clf.coef_[0][0], per_clf.coef_[0][1])
print(w_1)
X_pred_test_1 = per_clf.predict(X_test_1)
X_pred_train_1 = per_clf.predict(X_train_1)
acc_test_1 = accuracy_score(y_test_1,X_pred_test_1)
acc_train_1 = accuracy_score(y_train_1,X_pred_train_1)
print(acc_test_1)
print(acc_train_1)


# In[7]:


per_clf.fit(X_train_2, y_train_2)
w_2 = (per_clf.intercept_[0], per_clf.coef_[0][0], per_clf.coef_[0][1])
print(w_2)
X_pred_test_2 = per_clf.predict(X_test_2)
X_pred_train_2 = per_clf.predict(X_train_2)
acc_test_2 = accuracy_score(y_test_2,X_pred_test_2)
acc_train_2 = accuracy_score(y_train_2,X_pred_train_2)
print(acc_test_2)
print(acc_train_2)


# In[8]:


acc_list = [(acc_train_0,acc_test_0),(acc_train_1,acc_test_1),(acc_train_2,acc_test_2)]
weight_list = [w_0,w_1,w_2]


# In[9]:


print(acc_list)
print(weight_list)


# In[10]:


with open('per_acc.pkl', 'wb') as f:
  pickle.dump(acc_list, f)


pd.read_pickle("per_acc.pkl")


# In[11]:


with open('per_wght.pkl', 'wb') as f:
  pickle.dump(weight_list, f)


pd.read_pickle("per_wght.pkl")


# Perceptron i XOR

# In[12]:


X = np.array([[0, 0],
[0, 1],
[1, 0],
[1, 1]])
y = np.array([0,
1,
1,
0])


# In[14]:


#print(history.history['loss'])
i = 0
while True:
    i += 1
    print(i)
    model = tf.keras.models.Sequential()
    #model.add(tf.keras.Input(shape=(2,)))
    model.add(tf.keras.layers.Dense(2, activation='tanh',input_dim = 2))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.2))
    history = model.fit(X, y, epochs=100, verbose=False)
    y_pred = model.predict(X)
    if (y_pred[0] < 0.1 and y_pred[1] > 0.9 and y_pred[2] > 0.9 and y_pred[3] <0.1):
        print(y_pred)
        break

#[0, 1, 1, 0])


# In[15]:


model.get_weights()


# In[16]:


with open('mlp_xor_weights.pkl', 'wb') as f:
  pickle.dump(model.get_weights(), f)


pd.read_pickle("mlp_xor_weights.pkl")

