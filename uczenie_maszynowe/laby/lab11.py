#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scikeras
import tensorflow as tf
import keras
import numpy as np
import os
import time
import pickle
import pandas as pd


# In[2]:


(X_train, y_train), (X_test, y_test) = tf.keras.datasets.boston_housing.load_data()


# In[3]:


def build_model(n_hidden =1, n_neurons = 25, optimizer = 'sgd', learning_rate = 1e-5, momentum=0): 
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Input(shape = X_train.shape[1:]))
    for x in range(n_hidden):
        model.add(tf.keras.layers.Dense(units = n_neurons,activation='relu'))
    model.add(tf.keras.layers.Dense(1))
    
    optimizers = ['sgd', 'adam', 'nesterov', 'momentum']
    if optimizer not in optimizers:
        return 'Wrong optimizer'
    if optimizer == 'adam':
        optimizer = tf.keras.optimizers.Adam(learning_rate = learning_rate)
    if optimizer == 'sgd':
        optimizer = tf.keras.optimizers.SGD(learning_rate = learning_rate, nesterov=False)
    if optimizer == 'nesterov':
        optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate, nesterov=True)
    if optimizer == 'momentum':
        optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate, nesterov=False, momentum=momentum)
    model.compile(optimizer = optimizer,loss=tf.keras.losses.MeanSquaredError(),metrics=[tf.keras.metrics.MeanAbsoluteError()])
    return model


# In[4]:


model = build_model()


# In[5]:


es = tf.keras.callbacks.EarlyStopping(patience = 10,min_delta = 1)
model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es])


# In[6]:


model.summary()


# In[7]:


tf.keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)


# In[8]:


calif_dir = os.path.join(os.curdir,"tb_logs")


# In[9]:


def get_dir(name,val):
    ts=int(time.time())
    dirname = str(ts)+"_"+name+"_"+str(val)
    return os.path.join(calif_dir,dirname)


# Eksperyment 1

# In[10]:


dirr = get_dir('lr',0.000001)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(learning_rate = 0.000001)
history_lr_1 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_lr_1 = history_lr_1.history['loss'][-1]
mae_lr_1 = history_lr_1.history['mean_absolute_error'][-1]

dirr = get_dir('lr',0.00001)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(learning_rate = 0.00001)
history_lr_2 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_lr_2 = history_lr_2.history['loss'][-1]
mae_lr_2 = history_lr_2.history['mean_absolute_error'][-1]

dirr = get_dir('lr',0.0001)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(learning_rate =0.0001)
history_lr_3 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_lr_3 = history_lr_3.history['loss'][-1]
mae_lr_3 = history_lr_3.history['mean_absolute_error'][-1]


# Eksperyment 2

# In[11]:


dirr = get_dir('hl',0)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model1 = build_model(n_hidden = 0)
history_hl_1 = model1.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_hl_1 = history_hl_1.history['loss'][-1]
mae_hl_1 = history_hl_1.history['mean_absolute_error'][-1]

dirr = get_dir('hl',1)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model2 = build_model(n_hidden = 1)
history_hl_2 = model2.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_hl_2 = history_hl_2.history['loss'][-1]
mae_hl_2 = history_hl_2.history['mean_absolute_error'][-1]

dirr = get_dir('hl',2)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model3 = build_model(n_hidden = 2)
history_hl_3 = model3.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_hl_3 = history_hl_3.history['loss'][-1]
mae_hl_3 = history_hl_3.history['mean_absolute_error'][-1]

dirr = get_dir('hl',3)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model4 = build_model(n_hidden = 3)
history_hl_4 = model4.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_hl_4 = history_hl_4.history['loss'][-1]
mae_hl_4 = history_hl_4.history['mean_absolute_error'][-1]


# Eksperyment 3

# In[12]:


dirr = get_dir('nn',5)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(n_neurons = 5)
history_nn_1 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_nn_1 = history_nn_1.history['loss'][-1]
mae_nn_1 = history_nn_1.history['mean_absolute_error'][-1]

dirr = get_dir('nn',25)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(n_neurons = 25)
history_nn_2 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_nn_2 = history_nn_2.history['loss'][-1]
mae_nn_2 = history_nn_2.history['mean_absolute_error'][-1]

dirr = get_dir('nn',125)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(n_neurons = 125)
history_nn_3 = model.fit(X_train,y_train, validation_split = 0.1,epochs =100,callbacks =[es,tensorboard_d])
mse_nn_3 = history_nn_3.history['loss'][-1]
mae_nn_3 = history_nn_3.history['mean_absolute_error'][-1]


# Eksperyment 4 <- co XD

# In[13]:


dirr = get_dir('opt','sgd')
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(optimizer = 'sgd')
history_opt_1 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_opt_1 = history_opt_1.history['loss'][-1]
mae_opt_1 = history_opt_1.history['mean_absolute_error'][-1]

dirr = get_dir('opt','nesterov')
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(optimizer = 'nesterov')
history_opt_2 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_opt_2 = history_opt_2.history['loss'][-1]
mae_opt_2 = history_opt_2.history['mean_absolute_error'][-1]

dirr = get_dir('opt','momentum')
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(optimizer = 'momentum', momentum = 0.5)
history_opt_3 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_opt_3 = history_opt_3.history['loss'][-1]
mae_opt_3 = history_opt_3.history['mean_absolute_error'][-1]

dirr = get_dir('opt','adam')
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(optimizer = 'adam')
history_opt_4 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es,tensorboard_d])
mse_opt_4 = history_opt_4.history['loss'][-1]
mae_opt_4 = history_opt_4.history['mean_absolute_error'][-1]


# Eksperyment 5

# In[14]:


dirr = get_dir('mom',0.1)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(momentum = 0.1)
history_mom_1 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es])
mse_mom_1 = history_mom_1.history['loss'][-1]
mae_mom_1 = history_mom_1.history['mean_absolute_error'][-1]

dirr = get_dir('mom',0.5)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(momentum = 0.5)
history_mom_2 = model.fit(X_train,y_train,validation_split = 0.1, epochs =100,callbacks =[es])
mse_mom_2 = history_mom_2.history['loss'][-1]
mae_mom_2 = history_mom_2.history['mean_absolute_error'][-1]

dirr = get_dir('mom',0.9)
tensorboard_d = tf.keras.callbacks.TensorBoard(dirr)
model = build_model(momentum = 0.9)
history_mom_3 = model.fit(X_train,y_train, validation_split = 0.1,epochs =100,callbacks =[es])
mse_mom_3 = history_mom_3.history['loss'][-1]
mae_mom_3 = history_mom_3.history['mean_absolute_error'][-1]


# In[15]:


#lr.pkl
listlr = [(0.000001,mse_lr_1,mae_lr_1),(0.00001,mse_lr_2,mae_lr_2),(0.0001,mse_lr_3,mae_lr_3)]
listlr


# In[16]:


with open('lr.pkl', 'wb') as f:
  pickle.dump(listlr, f)


pd.read_pickle("lr.pkl")


# In[17]:


#hl.pkl
listhl = [(0,mse_hl_1 ,mae_hl_1 ),(1,mse_hl_2 ,mae_hl_2),(2,mse_hl_3 ,mae_hl_3),(3,mse_hl_4 ,mae_hl_4)]
listhl


# In[18]:


with open('hl.pkl', 'wb') as f:
  pickle.dump(listhl, f)


pd.read_pickle("hl.pkl")


# In[19]:


#nn.pkl
listnn = [(5,mse_nn_1 ,mae_nn_1),(25,mse_nn_2 ,mae_nn_2),(125,mse_nn_3 ,mae_nn_3)]
listnn


# In[20]:


with open('nn.pkl', 'wb') as f:
  pickle.dump(listnn, f)


pd.read_pickle("nn.pkl")


# In[21]:


#opt.pkl
listopt = [('sgd',mse_opt_1 ,mae_opt_1),('nesterov',mse_opt_2 ,mae_opt_2),('momentum',mse_opt_3 ,mae_opt_3),('adam',mse_opt_4 ,mae_opt_4)]
listopt


# In[22]:


with open('opt.pkl', 'wb') as f:
  pickle.dump(listopt, f)


pd.read_pickle("opt.pkl")


# In[23]:


#mom.pkl
listmom = [(0.1,mse_mom_1 ,mae_mom_1),(0.5,mse_mom_2 ,mae_mom_2),(0.9,mse_mom_3 ,mae_mom_3)]
listmom


# In[24]:


with open('mom.pkl', 'wb') as f:
  pickle.dump(listmom, f)


pd.read_pickle("mom.pkl")


# Zadanie 2

# In[25]:


import scikeras
from scikeras.wrappers import KerasRegressor
from sklearn.model_selection import RandomizedSearchCV


# In[26]:


param_distribs = {
    "model__n_hidden": [0,1,2,3],
    "model__n_neurons": [5,25,125],
    "model__learning_rate": [10**-6,10**-5,10**-4],
    "model__optimizer": ['sgd','nesterov','momentum','adam'],
    "model__momentum": [0.1,0.5,0.9]
}


# In[27]:


es = tf.keras.callbacks.EarlyStopping(patience=10, min_delta=1.0, verbose=1)
keras_reg = KerasRegressor(build_model, callbacks=[es])


# In[28]:


rnd_search_cv = RandomizedSearchCV(keras_reg,
                                   param_distribs,
                                   n_iter=10,
                                   cv=3,
                                   verbose=2)
rnd_search_cv.fit(X_train, y_train, epochs=100, validation_split=0.1)
kk = rnd_search_cv.best_params_


# In[29]:


kk


# In[30]:


with open('rnd_search.pkl', 'wb') as f:
  pickle.dump(kk, f)


pd.read_pickle("rnd_search.pkl")


# In[ ]:




