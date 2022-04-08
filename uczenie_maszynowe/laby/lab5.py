#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
size = 300
X = np.random.rand(size)*5-2.5
w4, w3, w2, w1, w0 = 1, 2, 1, -4, 2
y = w4*(X**4) + w3*(X**3) + w2*(X**2) + w1*X + w0 + np.random.randn(size)*8-4 
df = pd.DataFrame({'x': X, 'y': y})
df.plot.scatter(x='x',y='y')


# In[2]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)


# In[3]:


from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
tree_reg2 = DecisionTreeRegressor(max_depth=2)
tree_reg2.fit(X_train, y_train)
y_predrr2 = tree_reg2.predict(X_train)
mean_tree_reg_r2 = mean_squared_error(y_train, y_predrr2)
y_predrt2 = tree_reg2.predict(X_test)
mean_tree_reg_t2 = mean_squared_error(y_test, y_predrt2)
print(mean_tree_reg_r2,mean_tree_reg_t2)


# In[4]:


tree_reg = DecisionTreeRegressor(max_depth=3)
tree_reg.fit(X_train, y_train)
y_predrr = tree_reg.predict(X_train)
mean_tree_reg_r = mean_squared_error(y_train, y_predrr)
y_predrt = tree_reg.predict(X_test)
mean_tree_reg_t = mean_squared_error(y_test, y_predrt)
print(mean_tree_reg_r, mean_tree_reg_t)


# In[5]:


tree_reg3 = DecisionTreeRegressor(max_depth=4)
tree_reg3.fit(X_train, y_train)
y_predrr3 = tree_reg3.predict(X_train)
mean_tree_reg_r3 = mean_squared_error(y_train, y_predrr3)
y_predrt3 = tree_reg3.predict(X_test)
mean_tree_reg_t3 = mean_squared_error(y_test, y_predrt3)
print(mean_tree_reg_r3, mean_tree_reg_t3)


# In[6]:


tree_reg3 = DecisionTreeRegressor(max_depth=5)
tree_reg3.fit(X_train, y_train)
y_predrr3 = tree_reg3.predict(X_train)
mean_tree_reg_r3 = mean_squared_error(y_train, y_predrr3)
y_predrt3 = tree_reg3.predict(X_test)
mean_tree_reg_t3 = mean_squared_error(y_test, y_predrt3)
print(mean_tree_reg_r3, mean_tree_reg_t3)


# In[7]:


tree_reg3 = DecisionTreeRegressor(max_depth=6)
tree_reg3.fit(X_train, y_train)
y_predrr3 = tree_reg3.predict(X_train)
mean_tree_reg_r3 = mean_squared_error(y_train, y_predrr3)
y_predrt3 = tree_reg3.predict(X_test)
mean_tree_reg_t3 = mean_squared_error(y_test, y_predrt3)
print(mean_tree_reg_r3, mean_tree_reg_t3)


# In[8]:


tree_reg3 = DecisionTreeRegressor(max_depth=7)
tree_reg3.fit(X_train, y_train)
y_predrr3 = tree_reg3.predict(X_train)
mean_tree_reg_r3 = mean_squared_error(y_train, y_predrr3)
y_predrt3 = tree_reg3.predict(X_test)
mean_tree_reg_t3 = mean_squared_error(y_test, y_predrt3)
print(mean_tree_reg_r3, mean_tree_reg_t3)


# In[9]:


tree_reg3 = DecisionTreeRegressor(max_depth=8)
tree_reg3.fit(X_train, y_train)
y_predrr3 = tree_reg3.predict(X_train)
mean_tree_reg_r3 = mean_squared_error(y_train, y_predrr3)
y_predrt3 = tree_reg3.predict(X_test)
mean_tree_reg_t3 = mean_squared_error(y_test, y_predrt3)
print(mean_tree_reg_r3, mean_tree_reg_t3)


# In[10]:


tree_reg3 = DecisionTreeRegressor(max_depth=9)
tree_reg3.fit(X_train, y_train)
y_predrr3 = tree_reg3.predict(X_train)
mean_tree_reg_r3 = mean_squared_error(y_train, y_predrr3)
y_predrt3 = tree_reg3.predict(X_test)
mean_tree_reg_t3 = mean_squared_error(y_test, y_predrt3)
print(mean_tree_reg_r3, mean_tree_reg_t3)


# In[11]:


tree_reg3 = DecisionTreeRegressor(max_depth=10)
tree_reg3.fit(X_train, y_train)
y_predrr3 = tree_reg3.predict(X_train)
mean_tree_reg_r3 = mean_squared_error(y_train, y_predrr3)
y_predrt3 = tree_reg3.predict(X_test)
mean_tree_reg_t3 = mean_squared_error(y_test, y_predrt3)
print(mean_tree_reg_r3, mean_tree_reg_t3)


# In[12]:


from sklearn.tree import export_graphviz
f = "reg.dot"
export_graphviz(
        tree_reg,
        out_file=f,
        rounded=True,
        filled=True
)


# In[13]:


from subprocess import call


# In[14]:


call(['dot', '-Tpng', 'reg.dot', '-o', 'reg.png'])


# In[15]:


from sklearn import datasets
data_breast_cancer = datasets.load_breast_cancer(as_frame=True)
#print(data_breast_cancer['DESCR'])


# In[16]:


Xb = data_breast_cancer.frame[['mean texture', 'mean symmetry']]
yb = data_breast_cancer.frame.target


# In[17]:


Xb_train, Xb_test, yb_train, yb_test = train_test_split(Xb, yb, test_size=0.2)


# In[18]:


from sklearn.tree import DecisionTreeClassifier
tree_clf2 = DecisionTreeClassifier(max_depth=2)
tree_clf2.fit(Xb_train, yb_train)


# In[19]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


# In[20]:


Xb_pred = tree_clf2.predict(Xb_test)
acctest = accuracy_score(yb_test,Xb_pred)
Xb_predr = tree_clf2.predict(Xb_train)
acctrain = accuracy_score(yb_train,Xb_predr)
print(acctest,acctrain)
f1test = f1_score(yb_test, Xb_pred)
f1train = f1_score(yb_train,Xb_predr)
print(f1test, f1train)


# In[21]:


#3
tree_clf3 = DecisionTreeClassifier(max_depth=3)
tree_clf3.fit(Xb_train, yb_train)
Xb_pred = tree_clf3.predict(Xb_test)
acctest3 = accuracy_score(yb_test,Xb_pred)
Xb_predr = tree_clf3.predict(Xb_train)
acctrain3 = accuracy_score(yb_train,Xb_predr)
print(acctest3,acctrain3)
f1test3 = f1_score(yb_test, Xb_pred)
f1train3 = f1_score(yb_train,Xb_predr)
print(f1test3, f1train3)


# In[22]:


#4
tree_clf4 = DecisionTreeClassifier(max_depth=4)
tree_clf4.fit(Xb_train, yb_train)
Xb_pred = tree_clf4.predict(Xb_test)
acctest4 = accuracy_score(yb_test,Xb_pred)
Xb_predr = tree_clf4.predict(Xb_train)
acctrain4 = accuracy_score(yb_train,Xb_predr)
print(acctest,acctrain4)
f1test4 = f1_score(yb_test, Xb_pred)
f1train4 = f1_score(yb_train,Xb_predr)
print(f1test4, f1train4)


# In[23]:


#5
tree_clf5 = DecisionTreeClassifier(max_depth=5)
tree_clf5.fit(Xb_train, yb_train)
Xb_pred = tree_clf5.predict(Xb_test)
acctest5 = accuracy_score(yb_test,Xb_pred)
Xb_predr = tree_clf5.predict(Xb_train)
acctrain5 = accuracy_score(yb_train,Xb_predr)
print(acctest5,acctrain5)
f1test5 = f1_score(yb_test, Xb_pred)
f1train5 = f1_score(yb_train,Xb_predr)
print(f1test5, f1train5)


# In[24]:


f = "bc.dot"
export_graphviz(
        tree_clf3,
        out_file=f,
        feature_names=Xb.columns,
        class_names=[str(num)+", "+name for num, name in zip(set(y), Xb.columns)],
        rounded=True,
        filled=True
)


# In[25]:


call(['dot', '-Tpng', 'bc.dot', '-o', 'bc.png'])


# In[26]:


import pickle


# In[27]:


f1acc_tree = [3,f1train3,f1test3,acctrain3,acctest3]
with open('f1acc_tree.pkl', 'wb') as f:
  pickle.dump(f1acc_tree, f)


pd.read_pickle("f1acc_tree.pkl")


# In[28]:


mse_tree = [3,mean_tree_reg_r, mean_tree_reg_t]
with open('mse_tree.pkl', 'wb') as f:
  pickle.dump(mse_tree, f)


pd.read_pickle("mse_tree.pkl")

