import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Data = np.array(range(5))

def ecdf(data):
    x = np.sort(data)
    n = x.size
    y = np.arange(1, n+1) / n
    return(x,y)

x,y = ecdf(Data)
plt.scatter(x=x, y=y)
plt.show()