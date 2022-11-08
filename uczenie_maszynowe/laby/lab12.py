#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from functools import partial
import numpy as np
import pickle
import pandas as pd


# In[2]:


[test_set_raw, valid_set_raw, train_set_raw], info = tfds.load(
    "tf_flowers",
    split=["train[:10%]", "train[10%:25%]", "train[25%:]"], as_supervised=True,
    with_info=True)


# In[3]:


#info


# In[4]:


class_names = info.features["label"].names
n_classes = info.features["label"].num_classes
dataset_size = info.splits["train"].num_examples


# In[5]:


plt.figure(figsize=(12, 8))
index = 0
sample_images = train_set_raw.take(9) 
for image, label in sample_images:
    index += 1
    plt.subplot(3, 3, index)
    plt.imshow(image)
    plt.title("Class: {}".format(class_names[label])) 
    plt.axis("off")
    
#plt.show(block=False)


# In[6]:


def preprocess(image, label):
   resized_image = tf.image.resize(image, [224, 224]) 
   return resized_image, label


# In[7]:


batch_size = 32
train_set = train_set_raw.map(preprocess).shuffle(dataset_size).batch(batch_size).prefetch(1)
valid_set = valid_set_raw.map(preprocess).batch(batch_size).prefetch(1)
test_set = test_set_raw.map(preprocess).batch(batch_size).prefetch(1)


# In[8]:


plt.figure(figsize=(8, 8)) 
sample_batch = train_set.take(1)
for X_batch, y_batch in sample_batch:
    for index in range(12):
        plt.subplot(3, 4, index + 1) 
        plt.imshow(X_batch[index]/255.0)
        plt.title("Class: {}".format(class_names[y_batch[index]])) 
        plt.axis("off")
#plt.show()


# # 2.2

# In[9]:


#model = tf.keras.models.Sequential()
#model.add(tf.keras.layers.Conv2D(filters = 32,kernel_size = 7, strides=1, padding='same', activation='relu'))
#model.add(tf.keras.layers.MaxPool2D(pool_size=2))
#model.add(tf.keras.layers.Conv2D(filters = 32,kernel_size = 3, strides=1, padding='same', activation='relu'))
#model.add(tf.keras.layers.MaxPool2D(pool_size=2))
#model.add(tf.keras.layers.Flatten())
#model.add(tf.keras.layers.Dense(32,activation='relu'))


# In[10]:


#model.compile(optimizer=tf.keras.optimizers.SGD(),
#              loss=tf.keras.losses.BinaryCrossentropy(),
#              metrics='accuracy')


# In[11]:


#model.fit(x=train_set,validation_data = valid_set, epochs =10)


# In[12]:


tf.keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)


# In[13]:


DefaultConv2D = partial(keras.layers.Conv2D, 
    kernel_size=3,       
    activation='relu',
    padding="SAME")


# In[14]:


model = keras.models.Sequential([
    tf.keras.layers.Rescaling(scale=1./127.5, offset=-1),
    DefaultConv2D(filters=64, kernel_size=7,
                  input_shape=[224, 224, 1]),
    keras.layers.MaxPooling2D(pool_size=2),
    DefaultConv2D(filters=128),
    DefaultConv2D(filters=128),
    keras.layers.MaxPooling2D(pool_size=2),
    DefaultConv2D(filters=256),
    DefaultConv2D(filters=256),
    keras.layers.MaxPooling2D(pool_size=2),
    keras.layers.Flatten(),
    keras.layers.Dense(units=128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(units=64, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(units=5, activation='softmax')])


# In[15]:


#optimizer = tf.keras.optimizers.SGD(learning_rate=0.2, momentum=0.9,decay=0.01)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.05)
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=optimizer, metrics=["accuracy"])


# In[16]:


history = model.fit(train_set, validation_data=valid_set, epochs=10)


# In[17]:


acc_train = model.evaluate(train_set)[1]
acc_test = model.evaluate(test_set)[1]
acc_valid = model.evaluate(valid_set)[1]


# In[18]:


listacc = (acc_train, acc_valid, acc_test)


# In[19]:


with open('simple_cnn_acc.pkl', 'wb') as f:
        pickle.dump(listacc, f)
        
pd.read_pickle("simple_cnn_acc.pkl")


# # 2.3

# In[20]:


def preprocess(image, label):
    resized_image = tf.image.resize(image, [224, 224])
    final_image = tf.keras.applications.xception.preprocess_input(resized_image)
    return final_image, label


# In[21]:


batch_size = 32
train_set = train_set_raw.map(preprocess).shuffle(dataset_size).batch(batch_size).prefetch(1)
valid_set = valid_set_raw.map(preprocess).batch(batch_size).prefetch(1)
test_set = test_set_raw.map(preprocess).batch(batch_size).prefetch(1)


# In[22]:


plt.figure(figsize=(8, 8))
sample_batch = train_set.take(1)
for X_batch, y_batch in sample_batch:
    for index in range(12):
        plt.subplot(3, 4, index + 1)
        plt.imshow(X_batch[index] / 2 + 0.5)
        plt.title("Class: {}".format(class_names[y_batch[index]]))
        plt.axis("off")
#plt.show()


# In[23]:


base_model = tf.keras.applications.xception.Xception(
    weights="imagenet",
    include_top=False)


# In[24]:


for index, layer in enumerate(base_model.layers):
    print(index, layer.name)


# In[25]:


avg = keras.layers.GlobalAveragePooling2D()(base_model.output)
output = keras.layers.Dense(n_classes, activation = "relu")(avg)
model = keras.Model(inputs = base_model.input, outputs = output)


# In[26]:


for layer in base_model.layers:
    layer.trainable = False


# In[27]:


model.compile(loss="sparse_categorical_crossentropy", optimizer = 'SGD', metrics = ["accuracy"])
history2 = model.fit(train_set, epochs = 2, validation_data = valid_set)


# In[28]:


for layer in base_model.layers:
    layer.trainable = True


# In[29]:


model.compile(loss="sparse_categorical_crossentropy", optimizer = 'SGD', metrics = ["accuracy"])
history2 = model.fit(train_set, epochs = 3, validation_data = valid_set)


# In[30]:


acc_train = model.evaluate(train_set)[1]
acc_test = model.evaluate(test_set)[1]
acc_valid = model.evaluate(valid_set)[1]
xception = (acc_train, acc_valid, acc_test)


# In[31]:


with open('xception_acc.pkl', 'wb') as f:
        pickle.dump(xception, f)
        
pd.read_pickle("xception_acc.pkl")


# In[ ]:




