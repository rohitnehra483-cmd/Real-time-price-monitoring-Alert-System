import streamlit as  st
from PIL import Image as image
import pandas as pd
import requests
import plotly.express as px


img = image.open("logo.png")
img = img.resize((1000, 300))
st.image(img)

st.set_page_config(page_title="Fake Store Insights", page_icon="🏬", layout="wide")
st.title("🏬Fake Store API - Interactive DASHBOARD")
API ="https://fakestoreapi.com/products"
@st.cache_data
def load_data():
    response = requests.get(API)
    data = response.json()
    DF = pd.DataFrame(data)
    return DF
df = load_data()
st.subheader("🏬 Dataset Overview")
st.dataframe(df,use_container_width=True)

#basic cleaning
df['price'] = df['price'].astype(float)
df['category'] = df['category'].astype(str)

# slider

st.sidebar.header("🗞️Filter ")
categories = st.sidebar.multiselect("Select Categories", 
                                    df['category'].unique(), default=df['category'].unique())
filtered_df = df[df['category'].isin(categories)]

# kpis

st.header("📊 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Products", len(filtered_df))
col2.metric("Average Price", f"${filtered_df['price'].mean():.2f}")
col3.metric("Highest Price", f"${filtered_df['price'].min():.2f} ")

# visuals

st.header("📈 Key Performance Indicators ")

# bar chart

cate_count = filtered_df['category'].value_counts().reset_index()
fig_bar = px.bar(cate_count, x='category', y='count',  title="Product Count by Category")
st.plotly_chart(fig_bar, use_container_width=True)

# price distribution

fig_hist = px.histogram(filtered_df, x='price', nbins=20, title="Price Distribution", color_discrete_sequence=['#636EFA'])
st.plotly_chart(fig_hist, use_container_width=True)

#sacatter price vs id

fig_scatter = px.scatter(filtered_df, x='id', y='price', title="Price by Product ID", color_discrete_sequence=['#EF553B'])
st.plotly_chart(fig_scatter, use_container_width=True)

# table view
st.header("Filtered products")
st.dataframe(filtered_df, use_container_width=True)

# download button
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_products.csv',
    mime='text/csv',
)

