# pages/company.py
import streamlit as st

st.title("🏢 เกี่ยวกับบริษัท")
st.write("""
**PKRU Car Market Co., Ltd.**  
ซื้อ–ขายรถมือสองคุณภาพ ตรวจสภาพทุกคันก่อนขาย  
- ที่อยู่: 123 มหาวิทยาลัยราชภัฏภูเก็ต, เมืองภูเก็ต  
- โทร: 08x-xxx-xxxx  
- อีเมล: sales@pkru-carmarket.example
""")

with st.expander("นโยบายการรับประกัน"):
    st.write("- รับประกันเครื่อง+เกียร์ 6 เดือน\n- เปลี่ยนถ่ายของเหลวก่อนส่งมอบ\n- มีบริการไฟแนนซ์หลายธนาคาร")

st.page_link("pages/home.py", label="← กลับหน้าแรก", icon="🏠")
