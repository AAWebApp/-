from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import jieba

"""
# 简政
欢迎进入简政元空间！ :heart:

"""
xm = st.text_input('请在这里输入你真实姓名 ')
if st.button('确定'):
    if xm=="刘杨滢":
        st.write("知道吗，一个人几乎可以在任何他怀有无限热忱的事情上成功。")
    if xm=='朱冠源':
        st.write("如果不想做点事情，就不要想到达这个世界上的任何地方。")
    if xm=='卓靖东':
        st.write("人生舞台的大幕随时都可能拉开，关键是你愿意表演，还是选择躲避。")
    if xm=='金业成':
        st.write("失败是什么？没有什么，只是更走近成功一步；成功是什么？就是走过了所有通向失败的路，只剩下一条路，那就是成功的路。")
