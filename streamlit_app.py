import cartopy
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy import stats

st.header('Example streamlit')

fig = plt.figure()
plt.scatter(np.arange(0,10,1),np.arange(0,10,1))
st.pyplot(fig=fig)
