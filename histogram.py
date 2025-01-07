import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
bins=120
df=pd.read_csv('Book1.csv')
plt.style.use('bmh')
x=df['date']
y=df['vehicles passing']
plt.xlabel('date',fontsize=18)
plt.ylabel('vehicle',fontsize=18)
plt.bar(x,y,width=0.8,color=['red','green'])
plt.show()