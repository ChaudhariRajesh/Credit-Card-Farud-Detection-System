# -*- coding: utf-8 -*-
"""DSBDAL_Group_66.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1URjUkqfD1sdJne7BqakPpviZc1HfBepp

### **DSBDAL Mini Project**

# **Credit Card Fraud Detection System**

---

Class: TE-11
Batch: N-11
Group ID: 66 
---

Group Members:
Priyanka Ghuge (33361)
Rajesh Chaudhari (33362)
Shlok Shah (33373)
Ishwar Shelke (33376)

**Dataset Information:**
<a href="https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients">UCI Dataset on Credit Card Clients Data</a>
This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. 
This study reviewed the literature and used the following 23 variables as explanatory variables:

X1: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit.

X2: Gender (1 = male; 2 = female).

X3: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others).

X4: Marital status (1 = married; 2 = single; 3 = others).

X5: Age (year).

X6 - X11: History of past payment. We tracked the past monthly payment records (from April to September, 2005) as follows: X6 = the repayment status in September, 2005; X7 = the repayment status in August, 2005; . . .;X11 = the repayment status in April, 2005. The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.

X12-X17: Amount of bill statement (NT dollar). X12 = amount of bill statement in September, 2005; X13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005.

X18-X23: Amount of previous payment (NT dollar). X18 = amount paid in September, 2005; X19 = amount paid in August, 2005; . . .;X23 = amount paid in April, 2005.
"""

from google.colab import drive
drive.mount('/content/drive/')

#Importing the required packages

import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st

#Loading the dataset

path ="/content/drive/MyDrive/UCI_Credit_Card_New.csv"
data=pd.read_csv(path,header=[1])
data.head()

data.tail()

"""## **Data Preprocessing**"""

data.describe()

data.shape

data.isnull().sum()

data.info()

sns.countplot(data['default payment next month'])

sns.countplot(data['default payment next month'], hue=data['SEX'])

fig = plt.figure(figsize=(15, 15))

sns.heatmap(data.corr(),cmap='Blues',annot=True, fmt='.0f')

fig = plt.figure(figsize=(7, 7))
sns.lineplot(data['AGE'], data['LIMIT_BAL'], hue=data['default payment next month'])

list(data['EDUCATION'].value_counts())

data['EDUCATION'].unique()

d = data['EDUCATION']
plt.pie(list(data['EDUCATION'].value_counts()), labels=data['EDUCATION'].unique())

sns.violinplot(data['AGE'],hue=data['default payment next month'])

sns.barplot(x ="MARRIAGE", y ="default payment next month", data = data)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score, mean_squared_error as mse
from sklearn.preprocessing import StandardScaler

y = data['default payment next month']
X = data.drop('default payment next month', axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle = False, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""## **Logistic Regression**"""

log_reg = LogisticRegression()
parameters1 = [{'fit_intercept': [True, False]}]
log_reg = RandomizedSearchCV(estimator = log_reg,param_distributions = parameters1,n_jobs = -1, n_iter = 2,cv = 10)

log_reg = log_reg.fit(X_train, y_train)

from sklearn.metrics import classification_report

Y_test_pred = log_reg.predict(X_test)

print(classification_report(y_test,Y_test_pred))

"""## **Decision Tree**"""

dt_reg = DecisionTreeClassifier()
parameters2 = [{'max_depth':[3, 5, 10, None],'max_leaf_nodes' : [100, 120, 140, 160, 180, 200, None],}]
dt_reg = RandomizedSearchCV(estimator = dt_reg,param_distributions = parameters2,n_jobs = -1, n_iter = 11,cv = 10)

dt_reg = dt_reg.fit(X_train, y_train)

Y_test_pred = dt_reg.predict(X_test)

print(classification_report(y_test,Y_test_pred))

"""## **Random Forest**"""

rdm_fr = RandomForestClassifier(max_depth = 13)

rdm_fr = rdm_fr.fit(X_train, y_train)

Y_test_pred = rdm_fr.predict(X_test)

print(classification_report(y_test,Y_test_pred))

"""## **Naive Bayes**"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
nv = classifier.fit(X_train, y_train)

Y_test_pred  =  classifier.predict(X_test)

print(classification_report(y_test,Y_test_pred))

#From the performance analysis of all the four models, Decision Tree algorithm has the highest performance rate.
#So, we have used this model to give the input data and predict the corresponding output.

limit_bal = int(input("Limit Balance: "))
sex = int(input("Gender (Male: 1, Female: 2): "))
education = int(input("Education (Graduate School:1 University: 2, High School: 3, Others: 4): "))
marriage = int(input("Martial Status (Married: 1, Single: 2, Others: 3): "))
age = int(input("Age: "))
print("Past Payment Details")
print("Repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.")
pay_0 = int(input("April 2005: "))
pay_1 = int(input("May 2005: "))
pay_2 = int(input("June 2005: "))
pay_3 = int(input("July 2005: "))
pay_4 = int(input("August 2005: "))
pay_5 = int(input("September 2005: "))

print("Bill Amount Details")
bill_17 = int(input("April 2005: "))
bill_16 = int(input("May 2005: "))
bill_15 = int(input("June 2005: "))
bill_14 = int(input("July 2005: "))
bill_13 = int(input("August 2005: "))
bill_12 = int(input("September 2005: "))

print("Amount of Previous Payments")
pay_amt_23 = int(input("April 2005: "))
pay_amt_22 = int(input("May 2005: "))
pay_amt_21 = int(input("June 2005: "))
pay_amt_20 = int(input("July 2005: "))
pay_amt_19 = int(input("August 2005: "))
pay_amt_18 = int(input("September 2005: "))


test_data_array = [0,limit_bal,sex,education,marriage,age,pay_0,pay_1,pay_2,pay_3,pay_4,pay_5,bill_12,bill_13,bill_14,bill_15,bill_16,bill_17,pay_amt_18,pay_amt_19,pay_amt_20,pay_amt_21,pay_amt_22,pay_amt_23]
features = np.array([test_data_array])

#features = np.array([[20000,1,1,2,24,0,0,2,2,2,2,15376,18010,17428,18338,17905,19104,3200,0,1500,0,1650,0,1]])
output = dt_reg.predict(features)

print("Prediction: {}".format(output))

if(int(output) == 0):
  print("The person will not default the payment in the next month.")
else:
  print("The person will default the payment in the next month.")
