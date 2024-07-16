import pandas as pd
import numpy as np
import streamlit as st

st.title("Khoshal Ram's First Webpage")
st.header("The Beginning")
st.write("Khoshal Ram - Tech Journey")
st.write("Who's gonna carry the boats and the logs ?")
st.subheader("The first Area chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

st.subheader("The first Bar chart")
st.bar_chart(chart_data)

st.subheader("The first Line chart")
st.line_chart(chart_data)

st.subheader("A Population map around San Fransisco')
             
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)
