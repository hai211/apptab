import streamlit as st
import pandas as pd 
import numpy as np

st.title("Ứng dụng với Tabs")
tab1, tab2, tab3 = st.tabs(["Giới thiệu", "Phân tích Dữ liệu", "Thiết lập"])
with tab1:
    st.header("Chào mừng!")
    
    st.write("Đây là trang giới thiệu về ứng dụng của chúng tôi.")
    
    st.image("https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgbt9ucwaihedns96canw.jpg", width=100)

with tab2:  
    st.header("Phân tích Dữ liệu")
    
    st.write("Bạn có thể thực hiện các phân tích ở đây.")

    st.bar_chart({"Data": [10, 20, 15, 25]})
    st.line_chart({"Data": [10, 20, 15, 25]})    
    st.area_chart({"Data": [10, 20, 15, 25]})    

with tab3:
    st.header("Thiết lập")
    
    st.write("Điều chỉnh các cài đặt cho ứng dụng.")
    
    st.checkbox("Bật chế độ nâng cao")
