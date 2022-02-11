from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import jieba

"""
# 简政
欢迎进入简政元空间！ :heart:
以下可以忽略[documentation](https://docs.streamlit.io) ，[community
forums](https://discuss.streamlit.io).

"""
st.write("""# 我的第一个网站""")
t = st.text_input('分词器', '输入一段文字')
if st.button('确定'):
    import jieba
    j=jieba.cut(t)
    st.write("输出结果是")
    for i in j:
        st.write(i)
    
else:
    st.write('我哈哈大笑')
st.write("词典输出功能的试用")
cidian={"功能1":"分词器","功能2":"哈哈大笑"}
st.write(cidian)

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
