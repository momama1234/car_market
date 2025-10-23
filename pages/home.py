import streamlit as st
from cars_data import CARS

st.title("🚗 ตลาดรถมือสอง")
st.caption("คลิกที่รถเพื่อดูรายละเอียดเพิ่มเติม")

cols = st.columns(3, gap="large")

# ... โค้ดด้านบนคงเดิม
for i, car in enumerate(CARS):
    with cols[i % 3]:
        st.image(car["image"], use_container_width=True)
        st.subheader(car["name"])
        st.write(f"ปี {car['year']} · ราคา: **{car['price']:,} บาท**")

        if st.button("ดูรายละเอียด", key=f"btn_{car['id']}"):
            st.session_state["detail_id"] = car["id"]
            st.switch_page("pages/details.py")



