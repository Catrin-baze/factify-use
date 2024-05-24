# This is a sample Python script.
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title('多模态虚假新闻检测算法')
st.title('                    ')
 
# 设置侧边栏     Tips:所有侧边栏的元素都必须在前面加上 sidebar，不然会在主页显示
st.sidebar.expander('')     # expander必须接受一个 label参数，我这里留了一个空白
st.sidebar.subheader('新闻案例选择')       # 副标题
# st.selectbox:创造一个下拉选择框的单选题，接收参数: (题目名称， 题目选项)
news_class = st.sidebar.selectbox('1.案例选择:', ['案例一','案例二','案例三','案例四','案例五'],index = 1)     

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

elif news_class == '案例二':
 st.subheader('待检测新闻')
 image1 = Image.open('image/claim2.jpg')
 st.image(image1, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：Madhya Pradesh: A 90-year-old woman casts her vote at polling booth number 153 in Shahdol.')
 st.subheader('参考证据')
 image2 = Image.open('image/doc2.jpg')
 st.image(image2, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：Seventy-two seats across nine states are voting in the fourth phase of 2019 general elections on Monday. This phase will see the end of polling in Maharashtra and Odisha, while the process will start in Rajasthan, Madhya Pradesh and Jharkhand. Twenty-six seats in Bihar, Uttar Pradesh and West Bengal are also scheduled to vote in this phase. These three states have seats going to polls in each of the seven phases in the 2019 elections.Also Read | BJP-Sena hope to repeat thumping win in MaharashtraThe Bharatiya Janata Party (BJP) has high stakes in this phase. Of the 72 seats going to polls, it won 45 in 2014. Its allies won another 11 seats. The Congress’s tally was just two. In 2009, the BJP-Congress breakup in these seats was 9-29.Follow highlights here: 64% voter turnout in Phase 4 of Lok Sabha elections 2019A voter turnout of 64 percent was recorded in the fourth phase of Lok Sabha polls on Monday, the Election Commission said.Voting was held in 72 parliamentary constituencies spread across nine states in this phase.Nearly 66 per cent turnout was recorded in the third phase of Lok Sabha polls in which voting was held in 116 seats. In the first two phases, polling was conducted in 91 and 95 seats on April 11 and April 18 respectively.Election to 543 seats across the country is being held in seven phases. The counting of votes will take place on May 23. The poll percentage in Bihar was 58.92%, 9.79% in Jammu and Kashmir, 63.77% in Jharkhand, 66.52% in Madhya Pradesh, 55.88% in Maharashtra, 64.05% in Odisha, 66.44% in Rajasthan, 55.57% in Uttar Pradesh, and 76.59% in West Bengal.')

elif news_class == '案例三':
 st.subheader('待检测新闻')
 image1 = Image.open('image/claim3.png')
 st.image(image1, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：PM Narendra Modi to lay the foundation stone of AIIMS at Rajkot in Gujarat via video conferencing today.')
 st.subheader('参考证据')
 image2 = Image.open('image/doc3.jpg')
 st.image(image2, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：3.77% in Jharkhand, 66.52% in Madhya Pradesh, 55.88% in Maharashtra, 64.05% in Odisha, 66.44% in Rajasthan, 55.57% in Uttar Pradesh, and 76.59% in West Bengal. 1.91 first time voters: ECThe total number of first-time voters in the seven phases of 2019 Lok Sabha elections is 1.91 crore., which is 20% more than that it in 2014, said EC while addressing a press conference after the fourth phase of polling. Mumbai’s first-time voters seek to make ‘indelible’ markA large number of first-time voters came out to cast their ballots Monday in Mumbai, marking their formal participation in choosing the next government in the world’s largest democracy.According to the Election Commission (EC) data, Maharashtra has over 1.19 crore voters who fall in the age group of 18-19 years and are eligible to exercise their franchise in the Lok Sabha polls for the first time.Enthusiasm was palpable among first-time electors, who openly expressed their views about candidates in the fray and whom they voted for.At 6 pm, 60% voter turnout in Phase 4Till 6 pm, the voter turnout in the fourth phase of Lok Sabha elections 2019 was 59.62%.The poll percentage in Bihar was 53.67%, 9.79% in Jammu and Kashmir, 63.77% in Jharkhand, 65.86% in Madhya Pradesh, 52.03% in Maharashtra, 64.05% in Odisha, 63.58% in Rajasthan, 53.34% in Uttar Pradesh, and 76.59% in West Bengal. Congress approaches EC over EVM snags, NCP says something fishyThe Congress Monday made 30 complaints to the Election Commission about alleged glitches in EVMs across the 17 Lok Sabha constituencies in Maharashtra where polling is underway.A majority of the complaints came in from Dhule and Nandurbar, the party said, prompting ally NCP’s state chief Jayant Patil to claim that something was “fishy” in the two seats.“Complaints have been made to Election Commissioner, Chief Electoral Officer and other authorities concerned via e-mail,” the Congress said in a statement.Patil too said that complaints were coming in from several seats where election is being held, and questioned if the Electronic Voting Machine glitches were being caused deliberately.')

elif news_class == '案例四':
 st.subheader('待检测新闻')
 image1 = Image.open('image/claim4.png')
 st.image(image1, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：UPDATE Blackbuck poaching case: The next date of hearing is 27th September. The Court directed Salman Khan to be present before it on that date. He did not appear before the court today.')
 st.subheader('参考证据')
 image2 = Image.open('image/doc4.jpg')
 st.image(image2, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：The International Court of Justice will, on July 17, pronounce its verdict on India’s appeal on Indian national Kulbhushan Jadhav, who is on death row in Pakistan.“A public sitting will take place at 3 p.m. at the Peace Palace in The Hague, during which Judge Abdulqawi Ahmed Yusuf, President of the Court, will read the Court’s decision,” the ICJ, or the UN Court announced on Thursday.India had approached the World Court to direct Pakistan to revoke the death sentence awarded to Kulbhushan Jadhav on allegations of espionage. India has argued that Islamabad had breached the Vienna Convention on consular access and the process of resolution and stressed that the death penalty ruling delivered by a Pakistani military court was based on a farcical case.A Pakistani military court sentenced Jadhav, in a closed hearing, to death in April 2017 on charges of spying and terrorism.Pakistan claimed that Jadhav was arrested from its restive province Baluchistan in March 2016. India, on the other hand, alleges that the former Navy officer had gone to Iran on a business trip when he was kidnapped.The last hearing coincided with a sharp spike in tensions after the Pulwama suicide bombing in Kashmir.Following his conviction, India moved the ICJ seeking a stay on the death sentence awarded to Jadhav by the military court of Pakistan. In May 2017, the ICJ ordered stay on execution of the death sentence till final adjudication of the case at the UN top court.')

elif news_class == '案例五':
 st.subheader('待检测新闻')
 image1 = Image.open('image/claim5.jpg')
 st.image(image1, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：‘DAWN’ news article about a Pakistan Pilot pissing in the cockpit of PAF F-16 fighter jet.')
 st.subheader('参考证据')
 image2 = Image.open('image/doc5.jpg')
 st.image(image2, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 st.markdown(' **text** ：A screenshot of a news article purportedly published in the Pakistani daily ‘Dawn’ is being shared on social media claiming that a Pakistan Pilot was caught pissing in the cockpit of PAF F-16 fighter jet. The headline of this news report claims that Pilot had done this act following Allah’s advise in his dream. Let’s verify the claim made in the post. The news article shared in the post is a photoshopped one. No such report about a Pakistan Pilot pissing in F-16 fighter jet is published on Pakistani news websites. Hence, the claim made in the post is FALSE. When we searched for this news report using the keywords and time filters in Google, it is found that the Pakistan based ‘DAWN’ news did not report any such incident in their newspaper published on ‘10 June 2020’. Misspelt words like ‘efficiancy’ instead of ‘efficiency’ and the usage of randomly capitalized words in the headline indicate that the news report shared in the post could have been a morphed one. On comparing the news report shared in the post with the regular news report published in ‘DAWN’ newspaper, we could find a few differences between them. The regular header below the ‘DAWN’ Logo in the news report is missing in the one shared in the post. A full stop was used at the ending of this news report headline which is not found in the regular format. Also, there is no byline between the headline and the details of the article shared in the post which is present in the regular news reports published on ‘DAWN’ news. On ‘10 June 2020’, ‘DAWN’ news website published an article about misusing their news website to spread false news on social media. In the article, they shared a similar morphed image of another fake news report claimed to be published on their website. From all these pieces of evidence, it is concluded that the screenshot of a news report shared in the article is a photoshopped one. To sum it up, a morphed news report is being shared as Pakistan Pilot caught pissing inside F-16 fighter jet on the advice of Allah.')

midpro = st.sidebar.radio('2.是否显示中间过程:', ['是', '否'])        
ifdetect = st.sidebar.button('输出检测结果')
if midpro == '是':
 if st.sidebar.button('输出检测结果'):
  st.write('1')
