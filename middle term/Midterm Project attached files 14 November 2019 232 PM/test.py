from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import pandas as pd
import numpy as np


df = pd.read_csv('E:\semester 1\past paper for data pro\HouseVotes84.csv')
df.head()

class_val = df['Class'].values
l = list()
for i in class_val:
    if i == 'republican':
        l.append(0)
    else:
        l.append(1)

num_democrat = sum(l)
num_republican = len(l) - sum(l)

V16_val = df['V16']


def map_fun(x):
    x = x.fillna(0)
    for i in range(len(x)):
        if x[i] == 'y':
            x[i] = 1
        elif x[i] == 'n':
            x[i] = -1
    return x


rep_16 = map_fun(V16_val)
rep_16.value_counts()

df = df.drop('Class', axis=1).apply(map_fun)
df = sm.add_constant(df,1)
df['z'] = l
z = df.pop('z').values
X = df.values


X_train, X_test, z_train, z_test = train_test_split(
    X, z, train_size=326, random_state=0)


hot_log = sm.Logit(z_train, X_train)
model = hot_log.fit()
model.summary()

z_pred = model.predict(z_train)
table = pd.crosstab(z_test,z_pred)
table