XA, yA = exercise1(dataA, 'lpsa')

label = XA.columns
temp = list()
temp.append(label[0])
label = np.delete(label, 0, 0)
y = yA.values
X1 = XA.pop("intercept").values
X2 = XA.values
aic_val_p = sm.OLS(y, X1.T).fit().aic

while(any(label)):
    aic_select = list()
    for j in range(X2.shape[1]):
        X3 = np.vstack((X1, X2[:, j]))
        X3 = X3.T
        aic_val = sm.OLS(y, X3).fit().aic
        aic_select.append(aic_val)
    index = np.argmin(aic_select)
    if min(aic_select) < aic_val_p:
        aic_val_p = min(aic_select)
        temp.append(label[index])
        X1 = np.vstack((X1, X2[:, index]))
    X2 = np.delete(X2, index, 1)
    label = np.delete(label, index, 0)

temp