import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
df=pd.read_csv('Book1.csv')
x=df['date']
y=df['vehicles passing']
plt.xlabel('date',fontsize=18)
plt.ylabel('vehicle',fontsize=18)
plt.plot(x,y,color='red',linewidth=2)
start_index=0
end_index=1200
ystart=0
yend=70000
plt.xlim(start_index,end_index)
plt.ylim(ystart,yend)
plt.show()