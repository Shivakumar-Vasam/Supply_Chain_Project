import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page config
st.set_page_config(page_title="📦 Supply Chain Dashboard", layout="wide")

# Load data
if (
    os.path.exists('./data/orders.csv') and 
    os.path.exists('./data/inventory.csv') and 
    os.path.exists('./data/returns.csv') and 
    os.path.exists('./data/people.csv')
):
    orders = pd.read_csv('./data/orders.csv', parse_dates=['Order Date', 'Ship Date'], dayfirst=True)
    inventory = pd.read_csv('./data/inventory.csv', parse_dates=['date'])
    returns = pd.read_csv('./data/returns.csv')
    people = pd.read_csv('./data/people.csv')

    # ---------------- Section 1: KPIs ----------------
    st.title("Supply Chain Dashboard")

    st.header(" Key Metrics")

    total_orders = len(orders)
    total_sales = orders['Sales'].sum()
    avg_lead_time = (orders['Ship Date'] - orders['Order Date']).dt.days.mean()
    unique_products = orders['Product Name'].nunique() if 'Product Name' in orders.columns else 0
    return_rate = len(returns) / len(orders) * 100 if len(orders) > 0 else 0
    employee_count = people['Name'].nunique() if 'Name' in people.columns else len(people)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Orders", total_orders)
    col2.metric("Total Sales", f"${total_sales:,.2f}")
    col3.metric("Avg Lead Time (Days)", round(avg_lead_time, 2))
    col4.metric("Unique Products", unique_products)

    col5, col6 = st.columns(2)
    col5.metric("Return Rate", f"{return_rate:.2f}%")
    col6.metric("Employees", employee_count)

    # ---------------- Section 2: Sales Trend ----------------
    st.header(" Sales Over Time")
    daily_sales = orders.groupby('Order Date')['Sales'].sum().reset_index()
    fig_sales = px.line(daily_sales, x='Order Date', y='Sales', title='Daily Sales Trend')
    st.plotly_chart(fig_sales)

    # ---------------- Section 3: Inventory Overview ----------------
    st.header(" Inventory Trend")
    inventory_over_time = inventory.groupby('date')['inventory_level'].sum().reset_index()
    fig_inventory = px.line(inventory_over_time, x='date', y='inventory_level', title='Total Inventory Over Time')
    st.plotly_chart(fig_inventory)

    # ---------------- Section 4: Inventory by Product ----------------
    st.header(" Product-wise Inventory")

    selected_product = st.selectbox("Choose a product", inventory['product_name'].unique())
    product_data = inventory[inventory['product_name'] == selected_product]

    fig_product = px.line(product_data, x='date', y='inventory_level', title=f"Inventory for {selected_product}")
    st.plotly_chart(fig_product)

    # ---------------- Section 5: Restock Days ----------------
    st.subheader("Restock Events")
    restocks = product_data[product_data['restock'] == 1]
    st.dataframe(restocks[['date', 'inventory_level']])

    # ---------------- Section 6: Category View ----------------
    st.header("Category-wise Inventory")

    category_counts = inventory['category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']

    col7, col8 = st.columns(2)

    with col7:
        st.subheader("Bar Chart")
        st.bar_chart(category_counts.set_index('Category'))

    with col8:
        st.subheader("Pie Chart")
        fig_pie = px.pie(category_counts, names='Category', values='Count', title='Inventory Share by Category')
        st.plotly_chart(fig_pie)

else:
    st.error("Required files not found. Please run the ETL script to generate 'orders.csv', 'inventory.csv', 'returns.csv', and 'people.csv'.")
