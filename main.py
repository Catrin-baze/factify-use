# This is a sample Python script.
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title('多模态虚假新闻检测算法')
st.title('--------------------')
 
# 设置侧边栏     Tips:所有侧边栏的元素都必须在前面加上 sidebar，不然会在主页显示
st.sidebar.expander('')     # expander必须接受一个 label参数，我这里留了一个空白
st.sidebar.subheader('新闻案例选择')       # 副标题
# st.selectbox:创造一个下拉选择框的单选题，接收参数: (题目名称， 题目选项)
news_class = st.sidebar.selectbox('1.案例选择:', ['案例一','案例二','案例三','案例四','案例五'],index = 1)     

midpro = st.sidebar.radio('2.是否显示中间过程:', ['是', '否'])        
ifdetect = st.sidebar.button('输出检测结果')
#image = Image.open('image/claim1.jpg')
#st.image(image, caption='Sunrise by the mountains',use_column_width=True)
if news_class == '案例一':
 st.subheader('待检测新闻')
 image1 = Image.open('image/claim1.jpg')
 st.image(image1, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：Mumbai: Actors Amitabh Bachchan, Jaya Bachchan, Abhishek Bachchan &amp; Aishwarya Rai Bachchan cast their vote at a polling booth in Juhu.')
 st.subheader('参考证据')
 image2 = Image.open('image/doc1.jpg')
 st.image(image2, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：Seventy-two seats across nine states are voting in the fourth phase of 2019 general elections on Monday. This phase will see the end of polling in Maharashtra and Odisha, while the process will start in Rajasthan, Madhya Pradesh and Jharkhand. Twenty-six seats in Bihar, Uttar Pradesh and West Bengal are also scheduled to vote in this phase. These three states have seats going to polls in each of the seven phases in the 2019 elections.Also Read | BJP-Sena hope to repeat thumping win in MaharashtraThe Bharatiya Janata Party (BJP) has high stakes in this phase. Of the 72 seats going to polls, it won 45 in 2014. Its allies won another 11 seats. The Congress’s tally was just two. In 2009, the BJP-Congress breakup in these seats was 9-29.Follow highlights here: 64% voter turnout in Phase 4 of Lok Sabha elections 2019A voter turnout of 64 percent was recorded in the fourth phase of Lok Sabha polls on Monday, the Election Commission said.Voting was held in 72 parliamentary constituencies spread across nine states in this phase.Nearly 66 per cent turnout was recorded in the third phase of Lok Sabha polls in which voting was held in 116 seats. In the first two phases, polling was conducted in 91 and 95 seats on April 11 and April 18 respectively.Election to 543 seats across the country is being held in seven phases. The counting of votes will take place on May 23. The poll percentage in Bihar was 58.92%, 9.79% in Jammu and Kashmir, 63.77% in Jharkhand, 66.52% in Madhya Pradesh, 55.88% in Maharashtra, 64.05% in Odisha, 66.44% in Rajasthan, 55.57% in Uttar Pradesh, and 76.59% in West Bengal. ')

 



