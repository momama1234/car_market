import streamlit as st
from cars_data import CARS

# 1) ลองอ่านจาก query string ก่อน
car_id = st.query_params.get("id")

# 2) ถ้าไม่มี ให้ลองอ่านจาก session_state (ที่ตั้งมาจากหน้า home)
if not car_id:
    car_id = st.session_state.get("detail_id")

# 3) ถ้าได้ค่าแล้ว อัพเดต URL ให้มี ?id=... (รองรับ Streamlit เวอร์ชันเก่า/ใหม่)
try:
    # API ใหม่
    st.query_params.clear()
    if car_id:
        st.query_params["id"] = car_id
except Exception:
    # เผื่อเวอร์ชันที่ยังใช้ experimental_* อยู่
    try:
        st.experimental_set_query_params(id=car_id)
    except Exception:
        pass

car = next((c for c in CARS if c["id"] == car_id), None)

if not car:
    st.error("ไม่พบรถที่คุณเลือก (พารามิเตอร์ id ไม่ถูกต้อง)")
    st.page_link("pages/home.py", label="กลับหน้าแรก", icon="🏠")
else:
    st.page_link("pages/home.py", label="← กลับหน้าแรก", icon="🏠")
    st.title(car["name"])
    st.image(car["image"], use_container_width=True)
    st.markdown(f"**ราคา:** {car['price']:,} บาท  \n**ปี:** {car['year']}")
    st.divider()
    st.subheader("รายละเอียด")
    st.write(car["desc"])
    st.subheader("สเปก")
    for k, v in car["specs"].items():
        st.write(f"- **{k}**: {v}")
    st.page_link("pages/company.py", label="ข้อมูลบริษัท", icon="🏢")
