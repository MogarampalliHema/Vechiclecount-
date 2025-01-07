import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv('Book1.csv')
plt.style.use('bmh')
x=df['date']
y=df['vehicles passing']
plt.xlabel('date',fontsize=18)
plt.ylabel('vehicle',fontsize=18)
plt.scatter(x,y,color='red',linewidth=2,marker='.',linestyle='--')
plt.show()
