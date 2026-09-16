import streamlit as st

st.title("เป๋านี้ราคาเท่าไหร่🛒")

# กำหนดรายการกระเป๋าและราคา
item_options = {
    "เลือกกระเป๋า หรือ กรอกราคาเอง": 0.0,
    "กระเป๋าสะพายข้าง (2,850 บาท)": 2850.0,
    "กระเป๋าเป้ (2,550 บาท)": 2550.0,
    "กระเป๋าตัง (1,500 บาท)": 1500.0,
    "กระเป๋าใส่บัตร (1,200 บาท)": 1200.0,
}

# ให้ผู้ใช้เลือกรุ่นกระเป๋า
selected_item = st.selectbox("เลือกประเภทกระเป๋า:", list(item_options.keys()))
default_price = item_options[selected_item]

# รับค่าราคากระเป๋า (หากเลือกรุ่นจะดึงราคาให้อัตโนมัติ แต่ยังสามารถแก้ไขตัวเลขได้)
price = st.number_input(
    "กรอกราคากระเป๋า (บาท)",
    min_value=0.0,
    value=default_price,
    step=100.0,
    format="%.2f",
)

# คำนวณผลลัพธ์ทันทีเมื่อกรอกตัวเลข
vat_rate = 0.07  # ภาษี 7%
discount_rate = 0.05  # ส่วนลด 5%

vat = price * vat_rate

if price >= 2000:
    discount = price * discount_rate
else:
    discount = 0.0

total_price = price + vat - discount

# แสดงผลลัพธ์
st.write("---")
st.subheader("📊 รายละเอียดการคำนวณ")

col1, col2 = st.columns(2)
with col1:
    st.write("ราคากระเป๋า:")
    st.write("ภาษี VAT (7%):")
    st.write("ส่วนลด (5%):")
    st.markdown("**ราคารวมสุทธิ:**")

with col2:
    st.write(f"{price:,.2f} บาท")
    st.write(f"{vat:,.2f} บาท")
    st.write(f"{discount:,.2f} บาท")
    st.markdown(f"**{total_price:,.2f} บาท**")

if price > 0:
    if discount > 0:
        st.success(
            f"🎉 คุณได้รับส่วนลดพิเศษ 5% เป็นจำนวนเงิน {discount:,.2f} บาท!"
        )
    else:
        st.info("💡 ซื้อครบ 2,000 บาทขึ้นไป เพื่อรับส่วนลดพิเศษ 5%")
