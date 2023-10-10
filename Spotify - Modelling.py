#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('COMPILED_DATA.csv')


# In[4]:


df.shape


# In[6]:


df.isna().sum()


# In[7]:


df.describe()


# In[9]:


df.columns


# In[58]:


df1 = df.drop(['URI', 'ArtistURI', 'uri', 'id', 'type', 'track_href', 'analysis_url'], axis = 1)


# In[59]:


df1


# In[60]:


df1['ArtistGenres'] = df1['ArtistGenres'].apply(lambda x: None if x == [] else x)


# In[61]:


df1.ArtistGenres


# In[62]:


import ast
i = 0
for x in df1.ArtistGenres:
#   print(x)
    y = ast.literal_eval(x)
#   print(y)
    df1['ArtistGenres'][i] = y
    i +=1
    
    


# In[65]:


df1['ArtistGenres']


# In[68]:


df2 = df1.explode('ArtistGenres')


# In[79]:


threshold = 10  # genres only present less than 1 percent in dataset

filtered_value_counts = df2['ArtistGenres'].value_counts()
filtered_value_counts = filtered_value_counts[filtered_value_counts >= threshold]

print(filtered_value_counts)


# In[82]:


df2


# In[83]:





# In[90]:


y = df1['TrackPopularity']
X = df1.drop(columns=['TrackPopularity','TrackName', 'ArtistName', 'ArtistGenres','Album','ReleaseDate'])


# In[91]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# In[92]:


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# In[96]:


from sklearn.ensemble import RandomForestRegressor
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# In[98]:


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# ## for exploded df

# In[99]:


y = df2['TrackPopularity']
X = df2.drop(columns=['TrackPopularity','TrackName', 'ArtistName', 'ArtistGenres','Album','ReleaseDate'])


# In[100]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# ## LM performs worse than df that hasnt been exploded on artistgenres

# In[102]:


from sklearn.ensemble import RandomForestRegressor
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# ## RF performs better than df that hasnt been exploded on artistgenres

# In[ ]:





# In[ ]:





# ### TODO: explore the performance when setting a threshold on track popularity and converting the core task to a classification problem

# In[ ]:




