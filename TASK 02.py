#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("Population_Dataset_Task_1.xlsx")
data.head()


# In[2]:


data.shape
# Just to know the size of the dataset we have used.


# In[9]:


data.info()


# In[4]:


data.describe()
# Here we have get some souceful discrption about our dataset.


# In[10]:


#After searching finding the top most populated countries in the dataset
top = data.sort_values(by = 2022, ascending = False)[15:17]
top
# Thus from the dataset we have conclued the top 5 countries 


# In[11]:


top = data.sort_values(by = 2022, ascending = False)[45:49]
top


# In[12]:


#Creating a Dictionary for top 5 populated countries
dct = {"India" : 1429734552.0 , "China" :1425629510.0 ,"United States": 333287557.0, "Indonesia" :275501339.0,"Pakistan" : 235824862.0 }


# In[13]:


#Plotting a bar graph
names = list(dct.keys())
values = list(dct.values())
plt.rcParams["figure.figsize"] = (9,6.5)
plt.bar(range(len(dct)), values, tick_label=names)
plt.xlabel("Country",fontsize = 14)
plt.ylabel("Population Reference",fontsize = 14)
plt.title("Most Populated Countries in the World",fontsize = 16)
plt.show()


# In[ ]:


# Thus from the dataset 

