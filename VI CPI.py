#!/usr/bin/env python
# coding: utf-8

# In[172]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #Importo mappa per grafico
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("vi2.csv", index_col='Data di rilascio')

df.describe() # describe columns
df.columns # Analize columns

print(df) #print df

fig, axs  = plt.subplots(1, figsize=(50, 25))
plt.plot(df)
plt.xlabel('Data di rilascio')
plt.ylabel('Attuale ("%")')
plt.show()
plt.savefig('cpi.png') #save imagine as png


# In[165]:


head()


# In[ ]:




