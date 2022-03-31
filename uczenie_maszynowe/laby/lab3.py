#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import sklearn.neighbors
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error


# In[2]:


size = 300
X = np.random.rand(size)*5-2.5
w4, w3, w2, w1, w0 = 1, 2, 1, -4, 2
y = w4*(X**4) + w3*(X**3) + w2*(X**2) + w1*X + w0 + np.random.randn(size)*8-4 
df = pd.DataFrame({'x': X, 'y': y}) 
df.to_csv('dane_do_regresji.csv',index=None)
df.plot.scatter(x='x',y='y')


# In[3]:


X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.2)
X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)


# In[4]:


#regresja liniowa


# In[5]:


X_new = np.array([[0], [2]])


# In[6]:


lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
print(lin_reg.intercept_, lin_reg.coef_, "\n",lin_reg.predict(X_new))


# In[7]:


y_pred = lin_reg.predict(X_new)


# In[8]:


y_predrr = lin_reg.predict(X_train)
mean_lin_reg_r = mean_squared_error(y_train, y_predrr)
y_predrt = lin_reg.predict(X_test)
mean_lin_reg_t = mean_squared_error(y_test, y_predrt)


# In[9]:


print(mean_lin_reg_r,mean_lin_reg_t)


# In[10]:


#KNN 3
import sklearn.neighbors
knn_reg3 = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
knn_reg3.fit(X_train, y_train)
print(knn_reg3.predict(X_new))


# In[11]:


y_predkr = knn_reg3.predict(X_train)
mean_knn3_r = mean_squared_error(y_train, y_predkr)
y_predkt = knn_reg3.predict(X_test)
mean_knn3_t = mean_squared_error(y_test, y_predkt)


# In[12]:


print(mean_knn3_r,mean_knn3_t)


# In[13]:


#KNN 5 somsiadow
import sklearn.neighbors
knn_reg5 = sklearn.neighbors.KNeighborsRegressor(n_neighbors=5)
knn_reg5.fit(X_train, y_train)
print(knn_reg5.predict(X_new))


# In[14]:


y_predkr5 = knn_reg5.predict(X_train)
mean_knn5_r = mean_squared_error(y_train, y_predkr5)
y_predkt5 = knn_reg5.predict(X_test)
mean_knn5_t = mean_squared_error(y_test, y_predkt5)


# In[15]:


print(mean_knn5_r,mean_knn5_t)


# In[16]:


#wielomianowa 2


# In[17]:


poly_features2 = PolynomialFeatures(degree=2, include_bias=False)
X_poly2 = poly_features2.fit_transform(X_train)
poly_reg2 = lin_reg.fit(X_poly2, y_train)


# In[18]:


print(lin_reg.intercept_, lin_reg.coef_)


# In[19]:


y_pred_poly2r = lin_reg.predict(poly_features2.fit_transform(X_train))
mean_poly2r = mean_squared_error(y_train, y_pred_poly2r)
y_pred_poly2t = lin_reg.predict(poly_features2.fit_transform(X_test))
mean_poly2t = mean_squared_error(y_test, y_pred_poly2t)


# In[20]:


print(mean_poly2r, mean_poly2t)


# In[21]:


#wielomianowa 3


# In[22]:


poly_features3 = PolynomialFeatures(degree=3, include_bias=False)
X_poly3 = poly_features3.fit_transform(X_train)
poly_reg3 = lin_reg.fit(X_poly3, y_train)


# In[23]:


print(lin_reg.intercept_, lin_reg.coef_)


# In[24]:


y_pred_poly3r = lin_reg.predict(poly_features3.fit_transform(X_train))
mean_poly3_r = mean_squared_error(y_train, y_pred_poly3r)
y_pred_poly3t = lin_reg.predict(poly_features3.fit_transform(X_test))
mean_poly3_t = mean_squared_error(y_test, y_pred_poly3t)


# In[25]:


print(mean_poly3_r, mean_poly3_t)


# In[26]:


#wielomianowa 4


# In[27]:


poly_features4 = PolynomialFeatures(degree=4, include_bias=False)
X_poly4 = poly_features4.fit_transform(X_train)
poly_reg4 = lin_reg.fit(X_poly4, y_train)


# In[28]:


print(lin_reg.intercept_, lin_reg.coef_)


# In[29]:


y_pred_poly4r = lin_reg.predict(poly_features4.fit_transform(X_train))
mean_poly4r = mean_squared_error(y_train, y_pred_poly4r)
y_pred_poly4t = lin_reg.predict(poly_features4.fit_transform(X_test))
mean_poly4t = mean_squared_error(y_test, y_pred_poly4t)


# In[30]:


print(mean_poly4r, mean_poly4t)


# In[31]:


#wielomianowa 5


# In[32]:


poly_features5 = PolynomialFeatures(degree=5, include_bias=False)
X_poly5 = poly_features5.fit_transform(X_train)
poly_reg5 = lin_reg.fit(X_poly5, y_train)


# In[33]:


print(lin_reg.intercept_, lin_reg.coef_)


# In[34]:


y_pred_poly5r = lin_reg.predict(poly_features5.fit_transform(X_train))
mean_poly5r = mean_squared_error(y_train, y_pred_poly5r)
y_pred_poly5t = lin_reg.predict(poly_features5.fit_transform(X_test))
mean_poly5t = mean_squared_error(y_test, y_pred_poly5t)


# In[35]:


print(mean_poly5r, mean_poly5t)


# In[36]:


#plik 1
#kolumny: train_mse, test_mse, wiersze: lin_reg, knn_3_reg, knn_5_reg,
#poly_2_reg, poly_3_reg, poly_4_reg, poly_5_reg


# In[37]:


msea = {
'train_mse':[mean_lin_reg_r,mean_knn3_r,mean_knn5_r,mean_poly2r,mean_poly3_r,mean_poly4r,mean_poly5r],
'test_mse' :[mean_lin_reg_t,mean_knn3_t,mean_knn5_t,mean_poly2t,mean_poly3_t,mean_poly4t,mean_poly5t]
}
mse = pd.DataFrame(data = msea,index = ["lin_reg", "knn_3_reg", "knn_5_reg","poly_2_reg", "poly_3_reg", "poly_4_reg", "poly_5_reg"])


# In[38]:


mse


# In[39]:


import pickle


# In[40]:


mse.to_pickle("mse.pkl")


# In[41]:


pd.read_pickle("mse.pkl")


# In[42]:


#[(lin_reg, None), (knn_3_reg, None), (knn_5_reg, None), (poly_2_reg,
#poly_feature_2), (poly_3_reg, poly_feature_3), (poly_4_reg, poly_feature_4),
#(poly_5_reg, poly_feature_5)]


# In[43]:


regga = [(lin_reg, None), (knn_reg3, None), (knn_reg5, None), (poly_reg2,
poly_features2), (poly_reg3, poly_features3), (poly_reg4, poly_features4),
(poly_reg5, poly_features5)]
regg = pd.DataFrame(data = regga)


# In[44]:


regga


# In[45]:


with open('reg.pkl','wb') as fp:
    pickle.dump(regga,fp)


# In[46]:


pd.read_pickle("reg.pkl")

