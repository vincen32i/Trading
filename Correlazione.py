#!/usr/bin/env python
# coding: utf-8

# In[86]:


import yfinance as yf #importo dati da Yahoo Finance
data = yf.download("AAPL V XOM OXY BTC-USD TSLA MSFT KO AMZN NQ=F GC=F EURUSD=X ^VIX", start="2021-01-01", end="2022-09-30") #Selezione Titoli
data


# In[ ]:





# In[87]:


df = data["Adj Close"] #Prendo le chiusure di ogni titolo selezionato
df


# In[88]:


returns = df.pct_change() #Differenze percentuale
returns


# In[89]:


correlations = returns.corr() #Calcolo della correlazione
correlations


# In[90]:


import seaborn as sns #Importo mappa per grafico
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(20,10)})
sns.heatmap(correlations, annot= True)


# In[ ]:




