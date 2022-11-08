#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Rescaling
from tensorflow import keras
import numpy as np


# In[2]:


fashion_mnist = tf.keras.datasets.fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data() 
assert X_train.shape == (60000, 28, 28)
assert X_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)


# In[3]:


plt.imshow(X_train[142], cmap="binary") 
plt.axis('off')
plt.show()


# Przeskaluj wartości z zakresu 0–255 do zakresu 0–1.

# In[4]:


#X_train = tf.keras.layers.Rescaling(scale=1./255)(X_train)
#X_test = tf.keras.layers.Rescaling(scale=1./255)(X_test)
#y_train = tf.keras.layers.Rescaling(scale=1./255)(y_train)
#y_test = tf.keras.layers.Rescaling(scale=1./255)(y_test)


# In[5]:


train_norm = X_train.astype('float32')
test_norm = X_test.astype('float32')
train_norm = train_norm / 255.0
test_norm = test_norm / 255.0
X_train = train_norm
X_test = test_norm


# In[6]:


#tf.keras.layers.Rescaling(scale=1./255)


# In[7]:


class_names = ["koszulka", "spodnie", "pulower", "sukienka", "kurtka",
               "sandał", "koszula", "but", "torba", "kozak"]
class_names[y_train[142]]


# In[8]:


model = tf.keras.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(300, activation='relu'))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))


# In[9]:


model.summary()
tf.keras.utils.plot_model(model, "fashion_mnist.png", show_shapes=True)


# In[10]:


model.compile(optimizer='sgd',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=["accuracy"])


# In[11]:


import os
root_logdir = os.path.join(os.curdir, "image_logs")

def get_run_logdir():
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

run_logdir = get_run_logdir()
tensorboard_cb = tf.keras.callbacks.TensorBoard(run_logdir)


# In[12]:


model.fit(X_train, y_train, epochs=20, validation_split = 0.1, callbacks=[tensorboard_cb])


# In[13]:


image_index = np.random.randint(len(X_test))
image = np.array([X_test[image_index]])
confidences = model.predict(image)
confidence = np.max(confidences[0])
prediction = np.argmax(confidences[0])
print("Prediction:", class_names[prediction])
print("Confidence:", confidence)
print("Truth:", class_names[y_test[image_index]])
plt.imshow(image[0], cmap="binary")
plt.axis('off')
plt.show()


# In[14]:


model.save('fashion_clf.h5')


# Regersja

# In[15]:


from sklearn.datasets import fetch_california_housing 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from keras import losses


# In[16]:


housing = fetch_california_housing()


# In[17]:


X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full,y_train_full, random_state=42)


# In[18]:


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)


# In[19]:


model2 = tf.keras.Sequential([
    keras.layers.Dense(30, activation='softmax', input_shape= X_train.shape[1:]),
    keras.layers.Dense(1)
])
model2.compile(loss = 'mean_squared_error',  
   optimizer = 'sgd', metrics=['mean_squared_error'])


# In[20]:


es = tf.keras.callbacks.EarlyStopping(patience=5,min_delta=0.01,verbose=1)


# In[21]:


calif_dir = os.path.join(os.curdir, "housing_logs")


# In[22]:


def get_run_logdir_cal():
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(calif_dir, run_id)

run_logdir_cal = get_run_logdir_cal()
tensorboard_cb = tf.keras.callbacks.TensorBoard(run_logdir_cal)


# In[23]:


model2.fit(X_train, y_train, epochs=20, validation_data=(X_valid, y_valid), callbacks=[es, tensorboard_cb])


# In[24]:


model2.save('reg_housing_1.h5')


# In[25]:


model2 = tf.keras.Sequential([
    keras.layers.Dense(300, activation='softmax', input_shape= X_train.shape[1:]),
   # keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(1)
])
model2.compile(loss = 'mean_squared_error',  
   optimizer = 'sgd', metrics=['mean_squared_error'])


# In[26]:


es = tf.keras.callbacks.EarlyStopping(patience=5,min_delta=0.01,verbose=1)


# In[27]:


run_logdir_cal = get_run_logdir_cal()
tensorboard_cb = tf.keras.callbacks.TensorBoard(run_logdir_cal)


# In[28]:


model2.fit(X_train, y_train,epochs = 30, validation_data=(X_valid, y_valid), callbacks=[es, tensorboard_cb])


# In[29]:


model2.save('reg_housing_2.h5')


# In[30]:


model2 = tf.keras.Sequential([
    keras.layers.Dense(300, activation='softmax', input_shape= X_train.shape[1:]),
    keras.layers.Dense(200, activation='relu'),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(1)
])
model2.compile(loss = 'mean_squared_error',  
   optimizer = 'sgd', metrics=['mean_squared_error'])


# In[31]:


run_logdir_cal = get_run_logdir_cal()
tensorboard_cb = tf.keras.callbacks.TensorBoard(run_logdir_cal)


# In[32]:


model2.fit(X_train, y_train,epochs = 30, validation_data=(X_valid, y_valid), callbacks=[es, tensorboard_cb])


# In[33]:


model2.save('reg_housing_3.h5')

