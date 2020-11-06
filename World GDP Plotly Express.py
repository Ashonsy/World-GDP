#!/usr/bin/env python
# coding: utf-8

# ## Explore the Gapminder Dataset with Plotly Express

# About the Data:
# [Data Source](https://www.gapminder.org/tools/#$state$time$value=2007;;&chart-type=bubbles)

# ### Task 1: Loading the Data 

# In[3]:


import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import pandas as pd
import numpy as np


# In[4]:


from plotly.figure_factory import create_table
import plotly.express as px

gapminder = px.data.gapminder()

table = create_table(gapminder.head(10))
py.iplot(table)


# In[6]:


type(gapminder)


#  

# ### Task 2: Quick Visualizations with Custom Bar Charts

# In[7]:


data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop', height=400)
fig.show()


# In[8]:


fig = px.bar(data_canada, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
fig.show()


# ### Task 3: Plot Life Expectancy vs GDP per Capita

# In[9]:


gapminder2007 = gapminder.query("year == 2007")

px.scatter(gapminder2007, x="gdpPercap", y="lifeExp")


# In[10]:


px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent")


#  

# ### Task 4: Customize Interactive Bubble Charts

# In[11]:


px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60)


# In[12]:


px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60, hover_name="country")


#  

# ### Task 5: Create Interactive Animations and Facet Plots 

# In[13]:


px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60,
          hover_name="country", facet_col="continent", log_x=True)


# In[14]:


fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
fig.show()


# In[15]:


px.scatter(gapminder, x="gdpPercap", y="lifeExp",size="pop", size_max=60, color="continent", hover_name="country",
           animation_frame="year", animation_group="country", log_x=True, range_x=[100,100000], range_y=[25,90],
           labels=dict(pop="Population", gdpPercap="GDP per Capita", lifeExp="Life Expectancy"))


#  

# ### Task 6: Represent Geographic Data as Animated Maps

# In[16]:


fig = px.line_geo(gapminder.query("year==2007"), locations="iso_alpha", color="continent", projection="orthographic")
fig.show()


# In[17]:


px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year",
              color_continuous_scale=px.colors.sequential.Plasma, projection="natural earth")


# In[18]:


fig = px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", range_color=[20,80])
fig.show()


#  

# ### Task 7: Interactive Line Plots and Area Plots 

# In[19]:


fig = px.line(gapminder, x="year", y="lifeExp", color="continent", line_group="country", hover_name="country",
        line_shape="spline", render_mode="svg")
fig.show()


# In[20]:


fig = px.area(gapminder, x="year", y="pop", color="continent", line_group="country")
fig.show()

