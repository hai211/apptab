import streamlit as st


st.title("Ứng dụng với Sidebar")


with st.sidebar:
    st.header("Cài đặt")
    ten_nguoi_dung = st.text_input("Nhập tên của bạn:")
    muc_do_phuc_tap = st.slider("Chọn mức độ phức tạp", 1, 10, 5)
    st.info("Đây là thông tin bổ sung trong sidebar.")

st.write(f"Chào mừng, **{ten_nguoi_dung if ten_nguoi_dung else 'khách'}**!")

st.write(f"Mức độ phức tạp đã chọn: **{muc_do_phuc_tap}**")

st.write("Nội dung chính của ứng dụng nằm ở đây.")
