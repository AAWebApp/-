import streamlit as st
"""# 我的第一个网站"""
with t = st.text_input('分词器', '输入一段文字')
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


    st.markdown('Streamlit is **_really_ cool**.')
    #st.write('输出是', title)

   
