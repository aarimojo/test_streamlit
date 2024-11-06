import streamlit as st
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame

st.title('Example dataset')
st.header('Iris Dataset')
st.subheader('Iris dataset subheader')
st.write('asdasodam')

st.dataframe(df)