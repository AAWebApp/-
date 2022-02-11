from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import jieba

"""
# 简政
欢迎进入简政元空间！ :heart:
这两个东西可以忽略[不要点我](https://docs.streamlit.io) ，[不要点我](https://discuss.streamlit.io).

"""
xm = st.text_input('请在这里输入你的姓名 :heart:')
if st.button('确定'):
    if xm=="刘杨滢":
        st.write("知道吗，一个人几乎可以在任何他怀有无限热忱的事情上成功。")
    if xm=='朱冠源':
        st.write("如果不想做点事情，就不要想到达这个世界上的任何地方。")
    if xm=='卓靖东':
        st.write("人生舞台的大幕随时都可能拉开，关键是你愿意表演，还是选择躲避。")
    if xm=='金业成':
        st.write("失败是什么？没有什么，只是更走近成功一步；成功是什么？就是走过了所有通向失败的路，只剩下一条路，那就是成功的路。")

t = st.text_input('分词器', '请输入一段文字')
if st.button('确定'):
    import jieba
    j=jieba.cut(t)
    st.write("输出结果是")
    for i in j:
        st.write(i)

    
from jieba import posseg
import jieba
#h=input("粘贴输入长文本：")
h=open("大实验1.txt","r",encoding='utf-8').read()
c=posseg.cut(h)
d={}
e={}
for i1,i2 in c:
    i3=i1+i2#将元组合并为字符串
    if len(i1)==1:
        continue
    if i2!="v"and"vn":
        continue
        
    a=d.get(i3,0)
    d[i3]=a+1
#print(d)
n=list(d.items())#将词典中的键值对转换成元组构成的列表
#print(n)
n.sort(key=lambda x:x[1],reverse=True)#降序排列
#print(n)
st.write(len(n))
for i in range(5):
    q,w=n[i]
    st.write("{0: <20}{1: >20}".format(q,w))


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
