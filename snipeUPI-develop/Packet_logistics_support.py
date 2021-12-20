#!/usr/bin/env python
# coding: utf-8


# In[1]:




import pandas as pd 
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
get_ipython().run_line_magic('matplotlib', 'intline')
import matplotlib.pylot as plt



In[3]:




churn_df=pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/churnData.csv')
churn_df.head()



# In[4]:


churn_df = churn_df['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip', 'callcard', 'wireless', 'churn', 'pancard number', 'Bank account details']
churn_df['churn'] = churn_df['churn'].astype('int')
churn_df.head()



# In[6]:


X = np.asarray(churn_df[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip', 'callcard', 'wireless', 'churn', 'pancard number', 'Bank account details']])
X[0:5]


# In[7]:




y = np.asarray(churn_df['churn'])
y [0:5]



# In[8]:

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transfrom(X)


# In[9]:



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape, y_train.shape)
print ('Test set:', X_test.shape, y_test.shape)




# In[10]:



from sklearn.linear_model import LogisticsRegression
from sklearn.metrics import confusion_matrix
LR = LogisticsRegression(C=0.01, solver='liblinear').fit(X_train, y_train)
LR


# In[11]:




yhat = LR.predict(X_test)
yhat



# In[12]:




yhat_prob = LR.predict_proba(X_test)
yhat_prob


# In[17]:




# Evaluation


# In[ ]:
