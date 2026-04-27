import streamlit as  st
from PIL import Image as image

img = image.open("logo.png")
st.image(img, width=600)

st.title("Real-time-price-monitoring-Alert-System")
st.header("Daily Price  Traking")
st.header("Daily Price  Storage")
st.header("Daily Price  Comparison")
st.header("Alert  System for Price  Change")
st.header("Autamated pipline")

st.markdown("### Database connective")
   
st.success("Proceed Successfully")
st.info("Find the Formal information")
st.warning("You are going to high risk scenario")
st.error("Accunt is Bloced for 24 hours") 