import streamlit as st

st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

# สร้างช่องกรอกราคากระเป๋า/สินค้า
price = st.number_input(
    "กรุณากรอกราคากระเป๋า (บาท):",
    min_value=0.0,
    value=0.0,
    step=100.0,
    format="%.2f"
)

# ปุ่มคำนวณราคา
if st.button("คำนวณราคา"):
    vat_rate = 0.07       # ภาษี 7%
    discount_rate = 0.05  # ส่วนลด 5%

    # คำนวณภาษีมูลค่าเพิ่ม 7% จากราคาสินค้า
    vat = price * vat_rate

    # ตรวจสอบเงื่อนไขส่วนลด (ตั้งแต่ 2,000 บาทขึ้นไป ได้รับส่วนลด 5%)
    if price >= 2000:
        discount = price * discount_rate
    else:
        discount = 0.0

    # คำนวณราคารวมสุทธิ (ราคา + ภาษี - ส่วนลด)
    total_price = price + vat - discount

    # แสดงผลลัพธ์
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

    # แสดงข้อความสรุปส่วนลด
    if discount > 0:
        st.success(f"🎉 คุณได้รับส่วนลดพิเศษ 5% เป็นจำนวนเงิน {discount:,.2f} บาท!")
    else:
        st.info("💡 ซื้อครบ 2,000 บาทขึ้นไป เพื่อรับส่วนลดพิเศษ 5%")
