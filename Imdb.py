#!/usr/bin/env python
# coding: utf-8

# # DataAnalysis_IMDB_Movies
# 
# 

# In[5]:


import numpy as np
import pandas as pd


# In[6]:


imdb_df = pd.read_csv('MovieData.xls')


# In[7]:


imdb_df.head(5)


# In[8]:


imdb_df.shape


# In[9]:


imdb_df.info


# # Cleaning the Data
# 

# In[11]:


imdb_df.isnull().sum()


# In[13]:


imdb_df.drop(columns=['color','director_facebook_likes','actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes','actor_2_name','cast_total_facebook_likes','actor_3_name','duration','facenumber_in_poster','content_rating','country','movie_imdb_link','aspect_ratio','plot_keywords'],inplace=True)


# In[15]:


imdb_df.head()


# In[17]:


imdb_df.isnull().sum()


# In[18]:


imdb_df['language'].fillna('English', inplace=True)


# In[19]:


imdb_df.isnull().sum()


# In[22]:


#Convert the unit of the budget and gross columns from $ to million $.
imdb_df['gross'] = imdb_df['gross']/1000000
imdb_df['budget'] = imdb_df['budget']/1000000
imdb_df.head()


# #Find the movies with highest profit

# In[23]:


imdb_df['Profit'] = imdb_df['gross'] - imdb_df['budget']


# In[25]:


imdb_df.head()


# In[27]:


imdb_df.sort_values(by=['Profit'], ascending=False)


# #Drop duplicate values

# In[30]:


imdb_df.drop_duplicates(inplace=True)


# In[31]:


imdb_df.sort_values(by=['Profit'], ascending=False)


# """Create a new dataframe IMDb_Top_250 and store the top 250 movies with the highest IMDb Rating (corresponding to the column:
# imdb_score). Also make sure that for all of these movies, the num_voted_users is greater than 25,000. 
# Also add a Rank column containing the values 1 to 250 indicating the ranks of the corresponding films."""

# In[32]:


final_df = imdb_df[imdb_df['num_voted_users']>25000]
IMDb_Top_250 = final_df.nlargest(250,'imdb_score')
IMDb_Top_250


# Extract all the movies in the IMDb_Top_250 dataframe which are not in the English language and store them in a new dataframe named Top_Foreign_Lang_Film.

# In[48]:


Top_Foreign_Lang_Film=IMDb_Top_250.loc[IMDb_Top_250['language'] != 'English']


# In[49]:


Top_Foreign_Lang_Film


# # Find the best directors
# 
# Group the dataframe using the director_name column.
# Find out the top 10 directors for whom the mean of imdb_score is the highest and store them in a new dataframe top10director.

# In[50]:


# Write your code for extracting the top 10 directors here
directors = final_df.groupby('director_name')['imdb_score'].mean()
#directors.loc[directors.index == 'Damien Chazelle']
directors = directors.sort_values(ascending=True)

top10directors = directors.nlargest(10)
#final_df.loc[final_df['director_name'] == 'Damien Chazelle']
top10directors


# In[ ]:




