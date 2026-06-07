import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import the dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

#Understanding the dataset
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

#Data Cleaning
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

df['YEAR'] = df['ORDERDATE'].dt.year
df['MONTH'] = df['ORDERDATE'].dt.month_name()

df.drop_duplicates(inplace=True)

#Analyze and plot the graph(EDA)

#Total sales and line graph
print("Total Sales =", df['SALES'].sum())

sales_product = df.groupby('PRODUCTLINE')['SALES'].sum()

sales_product.sort_values().plot(
    kind='barh',
    figsize=(10,6)
)

plt.title("Sales by Product Line")
plt.show()

#Sales by country and barplot
country_sales = df.groupby('COUNTRY')['SALES'].sum()

country_sales.sort_values(ascending=False).head(10)
country_sales.sort_values(ascending=False).head(10).plot(
    kind='bar'
)
plt.show()

#Monthly sales trend
monthly_sales = df.groupby(
    ['YEAR','MONTH_ID']
)['SALES'].sum()

monthly_sales.plot(figsize=(12,6))
plt.title("Monthly Sales Trend")
plt.show()

#Sales by deal
deal_sales = df.groupby('DEALSIZE')['SALES'].sum()

deal_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)
plt.show()

#Top 10 cust
top_customers = df.groupby(
    'CUSTOMERNAME'
)['SALES'].sum()

top_customers.sort_values(
    ascending=False
).head(10)

#Sales by territory
territory_sales = df.groupby(
    'TERRITORY'
)['SALES'].sum()

territory_sales.plot(
    kind='bar'
)
plt.show()

#other insights

year_sales = df.groupby(
    'YEAR'
)['SALES'].sum()

print(year_sales)

aov = df['SALES'].sum() / df['ORDERNUMBER'].nunique()

print(aov)

top_products = df.groupby(
    'PRODUCTCODE'
)['SALES'].sum()

top_products.sort_values(
    ascending=False
).head(10)

#Export cleansed dataset
df.to_csv(
    "sales_dashboard_data.csv",
    index=False
)

