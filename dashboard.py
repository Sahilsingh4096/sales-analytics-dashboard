import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Sales Data Dashboard")

# Load dataset
data = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Show dataset
st.subheader("Dataset Preview")
st.write(data.head())

# Sales by Category
st.subheader("Sales by Category")
category_sales = data.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots()
category_sales.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Sales by Region
st.subheader("Sales by Region")
region_sales = data.groupby("Region")["Sales"].sum()

fig, ax = plt.subplots()
region_sales.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Top 10 Products
st.subheader("Top 10 Products by Sales")
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
top_products.plot(kind="barh", ax=ax)
st.pyplot(fig)
st.subheader("Key Metrics")

total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_orders = data["Order ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", data["Region"].unique())

filtered_data = data[data["Region"] == region]
category_sales = filtered_data.groupby("Category")["Sales"].sum()
st.title("Sales Analytics Dashboard")
st.write("Interactive dashboard built with Streamlit")