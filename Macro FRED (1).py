#!/usr/bin/env python
# coding: utf-8

# In[16]:


from fredapi import Fred 
fred = Fred(api_key='d75335cd352413d18b32b71910ec6269')
cons = fred.get_series('CONSUMER', observation_start='2022-1-1') # Consumer Loans, commerical banks 
gdp = fred.get_series('GDPC1', observation_start='2022-1-1') # Seasonally adjusted real GDP # seasonally ajusted non-fram employment in thousands
unemp =fred.get_series('UNRATE', observation_start='2022-1-1') # seasonally ajusted unemployment rate in percent
CPIAUCSL=fred.get_series('CPIAUCSL', observation_start='2022-1-1')  # Consumer Price Index

import matplotlib.pyplot as plt #graphing module with matlab-like properties
get_ipython().run_line_magic('matplotlib', 'inline')


fig, axs  = plt.subplots(2, 2,figsize=(20, 8))
fig.suptitle('US Economy since January 2022')

# plt.subplot(221)

axs[0][0].plot(gdp.index,gdp.values)
axs[0][0].set_title("Real GDP, SA")
axs[0,0].set_ylabel("2022 $bn")

axs[0][1].plot(cons.index,cons.values)
axs[0][1].set_title("Consumer Loans, SA")
axs[0,1].set_ylabel("thousands")

axs[1][0].plot(unemp.index,unemp.values)
axs[1][0].set_title("Unemployment, SA")
axs[1,0].set_ylabel("%")


axs[1][1].plot(CPIAUCSL.index,CPIAUCSL.values)
axs[1][1].set_title("CPIAUCSL")


plt.show()


# In[ ]:




