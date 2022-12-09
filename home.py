import streamlit as st
import matplotlib.pyplot as plt
from scipy import stats

st.header('Example streamlit')

fig = plt.figure()
plt.scatter(np.arange(0,10,1),np.arange(10,0,1))
plt.show()