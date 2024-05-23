# This is a sample Python script.
import streamlit as st
import pandas as pd
import numpy as np
st.title('多模态虚假新闻检测算法')
 
# 设置侧边栏     Tips:所有侧边栏的元素都必须在前面加上 sidebar，不然会在主页显示
st.sidebar.expander('')     # expander必须接受一个 label参数，我这里留了一个空白
st.sidebar.subheader('在下方调节你的参数')       # 副标题
# st.selectbox:创造一个下拉选择框的单选题，接收参数: (题目名称， 题目选项)
cluster_class = st.sidebar.selectbox('1.聚类数量:', list(range(2, 10)))     # 选择聚类中心，并赋值
minmaxscaler = st.sidebar.radio('2.是否归一化:', ['是', '否'])         # 选择是否标准化
