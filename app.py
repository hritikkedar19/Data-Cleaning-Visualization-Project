import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Data Cleaning Dashboard", layout="wide")

st.title("Data Cleaning & Visualization Dashboard")

df = pd.read_csv("data/cleaned_sales_data.csv")

st.subheader("Cleaned Dataset")
st.dataframe(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", len(df))
col2.metric("Total Sales", f"₹{df['Sales'].sum():,.0f}")
col3.metric("Total Profit", f"₹{df['Profit'].sum():,.0f}")
col4.metric("Average Discount", f"{df['Discount'].mean():.1f}%")

st.subheader("Sales by Category")
fig1 = px.bar(df.groupby("Category", as_index=False)["Sales"].sum(),
              x="Category", y="Sales", title="Total Sales by Category")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Profit by Region")
fig2 = px.bar(df.groupby("Region", as_index=False)["Profit"].sum(),
              x="Region", y="Profit", title="Total Profit by Region")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Sales Distribution")
fig3 = px.histogram(df, x="Sales", nbins=30, title="Sales Distribution")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Category vs Profit")
fig4 = px.box(df, x="Category", y="Profit", title="Profit Distribution by Category")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Key Insights")
st.write("""
- Electronics and Furniture usually generate higher total sales.
- Some raw records had missing values, duplicates, and outliers.
- After cleaning, the dataset became ready for analysis and dashboard creation.
- Region-wise profit helps identify strong and weak business areas.
""")