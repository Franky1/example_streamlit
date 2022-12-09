import streamlit as st
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

st.header('Example streamlit')

fig = plt.figure()
plt.scatter(np.arange(0,10,1),np.arange(0,10,1))
st.pyplot(fig=fig)