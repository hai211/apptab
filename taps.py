import streamlit as st
import pandas as pd 
import numpy as np

st.title("Ứng dụng với Tabs")
tab1, tab2, tab3, tap4, tap5 = st.tabs(["Giới thiệu", "Phân tích Dữ liệu", "Thiết lập", "Đăng nhập", "Đăng ký"])
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

with tap4:
    
    st.header("Đăng nhập")

    container = st.container(border=True)

    container.header("Đăng nhập hệ thống học viên")

    container.write("Nhập tài khoản được cấp để đăng nhập vào hệ thống")

    container.write()

    container.write("**Tên đăng nhập**")

    user = container.text_input(label=" ",placeholder="Vui long nhap ten tai khoan")

    container.write("**Mật khẩu**")

    password1 = container.text_input(label=" ",placeholder="Vui long nhap mat khau")

    widget = container.button("Dang nhap")


def add_bg_from_url():
   st.markdown(
       f"""
       <style>
       .stApp {{
           background-image: url("https://images.pexels.com/photos/632280/pexels-photo-632280.jpeg");
           background-size: cover;
       }}
       </style>
       """,
       unsafe_allow_html=True
   )
add_bg_from_url()


account = "admin"
password = "1234"

if widget:
    
    if user == account and password == password1:
        
        st.success("success!!")
    
    else:
        
        st.error("error!!")

else:
    
    user=""
    password1=""


with tap5:
    
    st.title("Tạo Tài Khoản Mới Của Bạn")
    container2 = st.container(border=True)
    container2.subheader("Vui lòng điền thông tin vào đây:")
    username = container2.text_input("Tên người dùng", placeholder="Nhập tên của bạn")
    password = container2.text_input("Mật khẩu", type="password", placeholder="Nhập mật khẩu")
    confirm_password = container2.text_input("Xác nhận mật khẩu", type="password", placeholder="Nhập lại mật khẩu")
    widget2 = container2.button("Đăng ký")
    container2.markdown("---")
    container2.write("Cảm ơn bạn đã ghé thăm ứng dụng đơn giản này!")
    
    if not username or not password or not confirm_password:
        st.warning("Vui lòng điền đầy đủ tất cả các trường.")
    elif password != confirm_password:
        st.error("Mật khẩu và xác nhận mật khẩu không khớp.")
    else:
        st.success("Đăng ký thành công! Chào mừng bạn.")
        st.info("Lưu ý: Thông tin này chỉ để hiển thị, không được lưu trữ.")


