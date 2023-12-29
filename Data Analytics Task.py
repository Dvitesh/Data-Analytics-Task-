#!/usr/bin/env python
# coding: utf-8

# ### Dataset Name
# 
# # Employee Data

# ### Import Library

# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


import seaborn as sns


# #### Read Data 

# In[7]:


df = pd.read_excel(r'C:\Users\admin\python\Employee Sample Data.xlsx')


# #### View Data

# In[8]:


df


# #### This method returns the first five records from the dataset

# In[9]:


df.head()


# #### This method returns the last five records from the dataset

# In[10]:


df.tail()


# #### It returns a tuple of array dimensions representing the shape of Data

# In[11]:


df.shape


# ####  This method about dataframe including index dtype and columns, non nulls values and memory usage

# In[52]:


df.info()


# ## Data Cleaning

# #### A new Data Frame with no empty cells

# In[53]:


new_df = df.dropna()
new_df


# #### Remove all rows with NULL values
# 

# In[55]:


new_df.dropna(axis=0,inplace = True)


# In[56]:


new_df


# ## Remove Duplicated Values

# In[57]:


new_df.duplicated()


# ## Calculate summary statistics

# In[59]:


new_df.describe()


# ## Visualization using Histogram And Bar Charts

# ##### Bar Chart

# In[104]:


ax = sns.countplot(x = 'Gender',data =new_df,hue='Gender')

plt.title('Gender Wise Bar Chart')
sns.set(rc={'figure.figsize':(9,6)})
for bars in ax.containers:
    ax.bar_label(bars)


# ##### Histogram Chart

# In[145]:


plt.hist(new_df['Annual Salary'],color='black')
 
plt.title('Annual Salary Wise Histogram')
plt.show()


# ##### Ethnicity And Age Wise Scatterplot

# In[146]:


sns.scatterplot(x='Ethnicity', y='Age',data=new_df,color='red')

plt.xlabel('Ethnicity')
plt.ylabel('Age')
 
plt.show()


# ##### Country And Age Wise Line Chart

# In[151]:


sns.lineplot(x='Country', y='Age',data=new_df,color='orange')

plt.xlabel('Country')
plt.ylabel('Age')
 
plt.show()


# ## Pivot Table

# In[149]:


table = pd.pivot_table(new_df,index =['Full Name','Country','Department'])


# In[150]:


table

