#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd


# In[2]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier


# In[3]:


# Tree


# In[4]:


data_breast_cancer = datasets.load_breast_cancer(as_frame=True)


# In[5]:


X = data_breast_cancer.frame[['mean texture', 'mean symmetry']]
y = data_breast_cancer.frame.target


# In[6]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)


# In[7]:


tree_clf = DecisionTreeClassifier()
tree_clf.fit(X_train,y_train)
Xtree_pred_test = tree_clf.predict(X_test)
Xtree_pred_train = tree_clf.predict(X_train)


# In[8]:


tree_acc_test = accuracy_score(y_test,Xtree_pred_test)
tree_acc_train = accuracy_score(y_train,Xtree_pred_train)
print(tree_acc_test,tree_acc_train)


# In[9]:


# Logistic


# In[10]:


log_clf = LogisticRegression();
log_clf.fit(X_train,y_train)
ylog_pred_test = log_clf.predict(X_test)
ylog_pred_train = log_clf.predict(X_train)
log_acc_test = accuracy_score(y_test,ylog_pred_test)
log_acc_train = accuracy_score(y_train,ylog_pred_train)
print(log_acc_test,log_acc_train)


# In[11]:


# KNeighborsRegressor


# In[12]:


nei_clf = KNeighborsClassifier()
nei_clf.fit(X_train,y_train)
ynei_pred_test = nei_clf.predict(X_test)
ynei_pred_train = nei_clf.predict(X_train)
nei_acc_test = accuracy_score(y_test,ynei_pred_test)
nei_acc_train = accuracy_score(y_train,ynei_pred_train)
print(nei_acc_test,nei_acc_train)


# In[13]:


voting_clf = VotingClassifier(
    estimators=[('tree', tree_clf),
                ('log', log_clf),
                ('nei', nei_clf)],
    voting='hard')
voting_clf.fit(X_train,y_train)
vot_pred_test = voting_clf.predict(X_test)
vot_pred_train = voting_clf.predict(X_train)
vot_acc_hard_test = accuracy_score(y_test,vot_pred_test)
vot_acc_hard_train = accuracy_score(y_train,vot_pred_train)
print(vot_acc_hard_test,vot_acc_hard_train)


# In[14]:


#hard test
#for clf in (log_clf, tree_clf, nei_clf, voting_clf):
#    clf.fit(X_train, y_train)
#    y_pred = clf.predict(X_test)
#    print(clf.__class__.__name__,
#          accuracy_score(y_test, y_pred))


# In[15]:


#hard train
#for clf in (log_clf, tree_clf, nei_clf, voting_clf):
#    clf.fit(X_train, y_train)
#    y_pred = clf.predict(X_train)
#    print(clf.__class__.__name__,
#          accuracy_score(y_train, y_pred))


# In[16]:


voting_clfs = VotingClassifier(
    estimators=[('tree', tree_clf),
                ('log', log_clf),
                ('nei', nei_clf)],
    voting='soft')
voting_clfs.fit(X_train,y_train)
vot_pred_test = voting_clfs.predict(X_test)
vot_pred_train = voting_clfs.predict(X_train)
vot_acc_soft_test = accuracy_score(y_test,vot_pred_test)
vot_acc_soft_train = accuracy_score(y_train,vot_pred_train)
print(vot_acc_soft_test,vot_acc_soft_train)


# In[17]:


#soft train
#for clf in (log_clf, tree_clf, nei_clf, voting_clf):
#    clf.fit(X_train, y_train)
#    y_pred = clf.predict(X_train)
#    print(clf.__class__.__name__,
#          accuracy_score(y_train, y_pred))


# In[18]:


#soft test
#for clf in (log_clf, tree_clf, nei_clf, voting_clf):
#    clf.fit(X_train, y_train)
#    y_pred = clf.predict(X_test)
#    print(clf.__class__.__name__,
#          accuracy_score(y_test, y_pred))


# In[19]:


acc_list = [(tree_acc_train,tree_acc_test),(log_acc_train,log_acc_test),(nei_acc_train,nei_acc_test),
            (vot_acc_hard_train,vot_acc_hard_test),(vot_acc_soft_train,vot_acc_soft_test)]
acc_list


# In[20]:


with open('acc_vote.pkl', 'wb') as f:
  pickle.dump(acc_list, f)


pd.read_pickle("acc_vote.pkl")


# In[21]:


clf_list = [tree_clf,log_clf,nei_clf,voting_clf,voting_clfs]

clf_list


# In[22]:


with open('vote.pkl', 'wb') as f:
  pickle.dump(clf_list, f)


pd.read_pickle("vote.pkl")


# In[23]:


from sklearn.ensemble import BaggingClassifier
bag_clf = BaggingClassifier(
DecisionTreeClassifier(), n_estimators=30, bootstrap=True)
bag_clf.fit(X_train, y_train)
bag_pred = bag_clf.predict(X_test)
bg_acc_test = accuracy_score(y_test, bag_pred)
print(bg_acc_test)
bag_pred_train = bag_clf.predict(X_train)
bg_acc_train = accuracy_score(y_train, bag_pred_train)
print(bg_acc_train)


# In[24]:


bag_clf5 = BaggingClassifier(
DecisionTreeClassifier(), n_estimators=30,
max_samples=50, bootstrap=True)
bag_clf5.fit(X_train, y_train)
bag_pred = bag_clf5.predict(X_test)
bg_acc5_test = accuracy_score(y_test, bag_pred)
print(bg_acc5_test)
bag_pred_train = bag_clf5.predict(X_train)
bg_acc5_train = accuracy_score(y_train, bag_pred_train)
print(bg_acc5_train)


# In[25]:


#  Pasting,


# In[26]:


bootstrap=False


# In[27]:


bag_clfb = BaggingClassifier(
DecisionTreeClassifier(), n_estimators=30, bootstrap=False)
bag_clfb.fit(X_train, y_train)
bag_pred = bag_clfb.predict(X_test)
past_test = accuracy_score(y_test, bag_pred)
print(past_test)
bag_pred_train = bag_clfb.predict(X_train)
past_train = accuracy_score(y_train, bag_pred_train)
print(past_train)


# In[28]:


bag_clfb5 = BaggingClassifier(
DecisionTreeClassifier(), n_estimators=30,
max_samples=50, bootstrap=False)
bag_clfb5.fit(X_train, y_train)
bag_pred = bag_clfb5.predict(X_test)
past5_test = accuracy_score(y_test, bag_pred)
print(past5_test)
bag_pred_train = bag_clfb5.predict(X_train)
past5_train = accuracy_score(y_train, bag_pred_train)
print(past5_train)


# In[29]:


rnd_clf = RandomForestClassifier(n_estimators=30)
rnd_clf.fit(X_train, y_train)
y_pred_rf_test = rnd_clf.predict(X_test)
y_pred_rf_train = rnd_clf.predict(X_train)
forest_acc_test = accuracy_score(y_test, y_pred_rf_test)
print(forest_acc_test)
bag_pred_train = bag_clf.predict(X_train)
forest_acc_train = accuracy_score(y_train, y_pred_rf_train)
print(forest_acc_train)


# In[30]:


ada_clf = AdaBoostClassifier(n_estimators=30)
ada_clf.fit(X_train, y_train)
ada_pred_test = ada_clf.predict(X_test)
ada_pred_train = ada_clf.predict(X_train)
ada_acc_test = accuracy_score(y_test, ada_pred_test)
ada_acc_train = accuracy_score(y_train, ada_pred_train)
print(ada_acc_test)
print(ada_acc_train)


# In[31]:


gbrt = GradientBoostingClassifier(n_estimators=30)
gbrt.fit(X_train, y_train)
gbrt_pred_test = gbrt.predict(X_test)
gbrt_pred_train = gbrt.predict(X_train)
brad_acc_test = accuracy_score(y_test, gbrt_pred_test)
brad_acc_train = accuracy_score(y_train, gbrt_pred_train)
print(brad_acc_test)
print(brad_acc_train)


# In[32]:


bag_list = [(bg_acc_train,bg_acc_test),(bg_acc5_train,bg_acc5_test),(past_train,past_test),(past5_train,past5_test),
            (forest_acc_train,forest_acc_test),(ada_acc_train,ada_acc_test),(brad_acc_train,brad_acc_test)]
bag_list


# In[33]:


with open('acc_bag.pkl', 'wb') as f:
  pickle.dump(bag_list, f)


pd.read_pickle("acc_bag.pkl")


# In[34]:


clf_list2 = [bag_clf,bag_clf5,bag_clfb,bag_clfb5,rnd_clf,ada_clf,gbrt]
clf_list2


# In[35]:


with open('bag.pkl', 'wb') as f:
  pickle.dump(clf_list2, f)


pd.read_pickle("bag.pkl")


# In[36]:


#7


# In[37]:


df1 = pd.DataFrame(data_breast_cancer.data, columns=data_breast_cancer.feature_names)
df1['target'] = data_breast_cancer.target
X2 = df1.iloc[:, 0:30]
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size=0.2)


# In[38]:


bgclf7 = BaggingClassifier(DecisionTreeClassifier(), n_estimators=30, bootstrap=False, max_features=2, max_samples=0.5)
bgclf7.fit(X2_train, y2_train)
bgclf7_pred_test = bgclf7.predict(X2_test)
bgclf7_pred_train = bgclf7.predict(X2_train)
acc_test = accuracy_score(y2_test, bgclf7_pred_test)
acc_train = accuracy_score(y2_train, bgclf7_pred_train)
print(acc_test)
print(acc_train)


# In[39]:


listacc = [acc_train,acc_test]
listacc


# In[40]:


with open('acc_fea.pkl', 'wb') as f:
  pickle.dump(listacc, f)


pd.read_pickle("acc_fea.pkl")


# In[41]:


listclf = [bgclf7]
listclf


# In[42]:


with open('fea.pkl', 'wb') as f:
  pickle.dump(listclf, f)


pd.read_pickle("fea.pkl")


# In[43]:


tab = [[0 for i in range(3)] for j in range(30)]
for i in range(30):
    tab[i][0] = bgclf7.estimators_[i]
    tab[i][1] = bgclf7.estimators_features_[i][0]
    tab[i][2] = bgclf7.estimators_features_[i][1]


# In[44]:


tab


# In[45]:


estimators_train_acc = []
estimators_test_acc = []
feature_names = []

for i in range(30):
  estimator_features_df_X_train = X2_train.iloc[:, [bgclf7.estimators_features_[i][0], bgclf7.estimators_features_[i][1]]]
  estimator_features_df_X_test = X2_test.iloc[:, [bgclf7.estimators_features_[i][0], bgclf7.estimators_features_[i][1]]]
  estimator_train_acc = accuracy_score(y2_train, bgclf7.estimators_[i].predict(estimator_features_df_X_train.values))
  estimator_test_acc = accuracy_score(y2_test, bgclf7.estimators_[i].predict(estimator_features_df_X_test.values))
  estimators_train_acc.append(estimator_train_acc)
  estimators_test_acc.append(estimator_test_acc)
  feature_names.append([df1.columns[bgclf7.estimators_features_[i][0]], df1.columns[bgclf7.estimators_features_[i][1]]])

allEstimators = pd.DataFrame(data={'train_accuracy': estimators_train_acc, 'test_accuracy': estimators_test_acc, 'feature_names': feature_names})
allEstimators = allEstimators.sort_values(by=['train_accuracy', 'test_accuracy'], ascending = False)


# In[46]:


allEstimators


# In[47]:


with open('acc_fea_rank.pkl', 'wb') as f:
  pickle.dump(allEstimators, f)


pd.read_pickle("acc_fea_rank.pkl")

