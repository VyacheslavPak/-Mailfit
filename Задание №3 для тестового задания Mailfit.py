#!/usr/bin/env python
# coding: utf-8

# # Задание №3 для тестового задания Mailfit

# In[4]:


import pandas as pd
import numpy as np

from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
import seaborn as sns
import plotly.express as px
from plotly import graph_objects as go 


# In[28]:


data = pd.read_excel("C:/Users/azaxa/Desktop/Data для тестового.xlsx", sheet_name="Data")
data


# In[29]:


data.info()


# In[55]:


data['Delivery rate'] = (data['Доставлено'] / data['Отправлено']) * 100
data['Open rate'] = (data['Открытия'] / data['Доставлено']) * 100
data['Click to Open rate'] = (data['Клики'] / data['Открытия']) * 100
data['Unsubscribe rate'] = (data['Отписки'] / data['Доставлено']) * 100


# In[67]:


delivery_rate_data = data[['Тема письма','Delivery rate']].sort_values('Delivery rate',ascending=False)
delivery_rate_data


# In[103]:


delivery_top = delivery_rate_data[delivery_rate_data['Delivery rate'] == 98.5]


# In[66]:


open_rate_data = data[['Тема письма','Open rate']].sort_values('Open rate',ascending=False)
open_rate_data


# In[65]:


click_to_open_rate_data = data[['Тема письма','Click to Open rate']].sort_values('Click to Open rate',ascending=False)
click_to_open_rate_data


# In[69]:


unsubscribe_rate_data = data[['Тема письма','Unsubscribe rate']].sort_values('Unsubscribe rate',ascending=True)
unsubscribe_rate_data


# In[120]:


data_metric = data[['Тема письма',
                    'Delivery rate',
                    'Open rate',
                    'Click to Open rate',
                    'Unsubscribe rate']].sort_values(by = ['Delivery rate',
                                                           'Open rate',
                                                           'Click to Open rate',
                                                            'Unsubscribe rate'], ascending = [False,False,False,True])
data_metric.head(5)


# In[119]:


datas = data[data['Unsubscribe rate'] < 0.5]
data_metric2 = datas[['Тема письма',
                    'Delivery rate',
                    'Open rate',
                    'Click to Open rate',
                    'Unsubscribe rate']].sort_values(by = ['Delivery rate',
                                                           'Open rate',
                                                           'Click to Open rate',
                                                            'Unsubscribe rate'], ascending = [False,False,False,True])
data_metric2.head(5)


# ### Лучшая тема по Delivery rate - в датасете delivery_top
# ### Лучшая тема по open_rate_data - Тема письма 1	и Тема письма 101
# ### Лучшая тема по click_to_open_rate_data - Тема письма 207	
# ### Лучшая тема по unsubscribe_rate_data - Тема письма 212
# 
# 
# ### По общим показателям лучшая тема - Тема письма 40 - хотя по Unsubscribe rate это нелучшая тема.                  Если рассматривать темы с Unsubscribe rate < 0.5 то лучшей темой будет - Тема письма 21

# In[93]:


open_data = data.groupby('День недели.1').agg(cnt_open=('Открытия','sum')).round().sort_values('cnt_open')


# In[95]:


open_data


# In[97]:


open_rate = data.groupby('День недели.1').agg(cnt_open=('Open rate','mean')).round().sort_values('cnt_open')


# In[99]:


open_rate


# In[98]:


click_to_Open = data.groupby('День недели.1').agg(cnt_open=('Click to Open rate','mean')).round().sort_values('cnt_open')


# In[100]:


click_to_Open


# ## По кол-ву открытий и по open_rate лучшим днем недели является пятница, но по показателю click_to_оpen лучшим днем является вторник.
# ### Стоит тестировать дни для отправки рассылок, так же важно проанализировать зависимость кол-ва открытий и тем писем, так как, возможно, что в конце рабочей недели люди не открывают письма, требующие высокой вовлеченности, в отличие от вторника, середины рабочей недели, когда готовность принимать решения выше. Но так же возможно и обратное, что в пятницу люди открывают чаще письма с отвлеченными темами, то есть в конце рабочей недели находят время для разбора рассылок. 
