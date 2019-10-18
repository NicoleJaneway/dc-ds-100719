#!/usr/bin/env python
# coding: utf-8

# # Unit Test Intro

# ## Goals:

# The purpose of this Coach Lab is to introduce students to the procedure of assessments by having them go through the motions once before their first assessment.
# 
# We hope to expose any environmental issues with running pytest and take necessary steps to update their environment. 

# ## Instructions:

# Install pytest using `conda install -c anaconda pytest`

# ### Question 1

# Create a list called `friends` with three names, all lower-cased.

# In[7]:


friends = ['sam','devin','alex']


# ### Question 2

# Create a function called 'capitalize' that will capitalize all the **values** of the dictionary.

# In[5]:


def capitalize(x):
    assert type(x) == list, "Not a list"
    capitalized_list = []
    for el in x:
        capitalized_list.append(el.title())
    return capitalized_list    


# Run the function to confirm that works on your `friends` dictionary

# In[6]:


capitalize(friends)


# ### Question 3

# Read in a csv from this website `https://data.austintexas.gov/views/9t4d-g238/rows.csv?accessType=DOWNLOAD`
# 
# And assign it to a dataframe variable called `animal_outcomes`

# In[10]:


import pandas as pd


# In[11]:


animal_outcomes = pd.read_csv('https://data.austintexas.gov/views/9t4d-g238/rows.csv?accessType=DOWNLOAD')


# ### Question 4

# set the variable `pi` to the value of pi as provided by the numpy library

# In[13]:


import numpy as np


# In[15]:


pi = np.pi


# In[16]:


pi

