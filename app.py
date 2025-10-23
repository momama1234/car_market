# app.py
import streamlit as st

st.set_page_config(page_title="Car Market", page_icon="🚗", layout="wide")

# ใช้ Multipage API แบบใหม่
# หน้า default = home, และตั้ง url_path ให้หน้า details ใช้ทางลัด /car
home = st.Page("pages/home.py", title="หน้าหลัก", icon=":material/directions_car:", default=True)
details = st.Page("pages/details.py", title="รายละเอียดรถ", icon=":material/description:", url_path="car")
company = st.Page("pages/company.py", title="ข้อมูลบริษัท", icon=":material/apartment:")

pg = st.navigation([home, details, company])
pg.run()
