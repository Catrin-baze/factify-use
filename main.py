# This is a sample Python script.
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title('多模态虚假新闻检测算法')
 
# 设置侧边栏     Tips:所有侧边栏的元素都必须在前面加上 sidebar，不然会在主页显示
st.sidebar.expander('')     # expander必须接受一个 label参数，我这里留了一个空白
st.sidebar.subheader('新闻案例选择')       # 副标题
# st.selectbox:创造一个下拉选择框的单选题，接收参数: (题目名称， 题目选项)
cluster_class = st.sidebar.selectbox('1.案例选择:', list(range(1, 6)))     
midpro = st.sidebar.radio('2.是否显示中间过程:', ['是', '否'])        
ifdetect = st.sidebar.button('输出检测结果')
image = Image.open('image/claim1.jpg')
st.image(image, caption='Sunrise by the mountains',use_column_width=True)

