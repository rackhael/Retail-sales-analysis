#!/usr/bin/env python
# coding: utf-8

# ## Task 1: Load the Data

# In[6]:


# Importing necessary libraries

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


# Load the dataset


# In[4]:


file_path = 'Online Retail.xlsx'
data = pd.read_excel(file_path)


# In[5]:


# Display the first few rows


# In[6]:


print("Dataset Overview:")
print(data.head())


# In[7]:


# Display basic info about the dataset


# In[8]:


print("\nDataset Information:")
print(data.info())


# ## Task 2: Data Cleaning

# In[9]:


# Check for missing values


# In[10]:


print("\nmissing Values:")
print(data.isnull().sum())


# In[11]:


# Drop rows with missing CustomerID 


# In[12]:


data_cleaned = data.dropna(subset=['CustomerID'])


# In[13]:


# Ensure 'Quantity' and 'UnitPrice' have positive values


# In[14]:


data_cleaned = data_cleaned[(data_cleaned['Quantity'] > 0) & (data_cleaned['UnitPrice'] > 0)]


# In[15]:


# Verify the cleaned data


# In[16]:


print("\nCleaned Data Information:")
print(data_cleaned.info())


# ## Task 3: Explore Basic Statistics

# In[18]:


# Summary statistics
print("\nSummary Statistics:")
print(data_cleaned.describe())


# In[20]:


# Unique countries in the dataset
print("\nUnique Countries:")
print(data_cleaned['Country'].unique())


# ## Task 4: Sales Trends Analysis 

# In[21]:


# Convert InvoiceDate to datetime format
data_cleaned['InvoiceDate'] = pd.to_datetime(data_cleaned['InvoiceDate'])


# In[22]:


#Add a column for month and year
data_cleaned['MonthYear'] = data_cleaned['InvoiceDate'].dt.to_period('M')


# In[23]:


#Group by month to analyze trends
monthly_sales = data_cleaned.groupby('MonthYear')['Quantity'].sum()


# In[26]:


#Plot monthly sales trends
plt.figure(figsize=(12,6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month-Year')
plt.ylabel('Total Quantity Sold')
plt.grid()
plt.show()


# ## Task 5: Analyze top-selling products

# In[28]:


# Group by product description to find quantities sold
top_products = data_cleaned.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)


# In[33]:


# Plot the top 10 best-selling products
plt.figure(figsize=(10,6))
top_products.plot(kind='bar', color='aqua')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product Description')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.show()


# ## Task 6: Analyze Sales by country

# In[35]:


# Group by country to find total sales quantities
sales_by_country = data_cleaned.groupby('Country')['Quantity'].sum().sort_values(ascending=False)


# In[37]:


# Plot top 10 countries by sales

plt.figure(figsize=(10,6))
sales_by_country.head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Countries by Sales Quantity')
plt.xlabel('Country')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.show()


# ## Task 7: Identify Outliers

# In[39]:


# Boxplot for Unit Price
plt.figure(figsize=(8,6))
sns.boxplot(data_cleaned['UnitPrice'])
plt.title('Boxplot for Unit Price')
plt.show()


# In[40]:


# Boxplot for Quantity
plt.figure(figsize=(8,6))
sns.boxplot(data_cleaned['Quantity'])
plt.title('Boxplot for Quantity')
plt.show()


# ### The busiest sales months
# In the begining of the year, sales are largely volatile before stabilizing in the months of May to August.
# The sales tend to pick up with a spike seen in September and gradually increasing in the following months before peaking in November and falling back down in December.
# 
# 
# ### The top-selling products
# The United Kindgdom accounts for maority of the sales and accounts for majority of the combined marketshare. It is then followed by Netherlands, and the rest of the countries inclose range.
# 
# The top selling product is the 'Paper craft, little birdy,' closely followed by 'Medium ceramic top ceramic jar' with 80,000+ and 70,000+ units sold for each respectably. The 'Mini paint set vintage' has the lowest slaes volume.
# 
# ### Key customer insights
# While the majority of the order quantities fall below the 10,000units, there are two outliers with 75,000 and 80,000units. 

# In[ ]:




