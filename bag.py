import streamlit as st

st.title("เป๋านี้ราคาเท่าไหร่🛒")

# แสดงรายการกระเป๋าและราคาเป็นข้อความ
st.markdown("""
**🛍️ รายการกระเป๋า:**
1. กระเป๋าสะพายข้าง - **2,850** บาท
2. กระเป๋าเป้ - **2,550** บาท
3. กระเป๋าตัง - **1,500** บาท
4. กระเป๋าใส่บัตร - **1,200** บาท
""")

st.write("---")

# รับค่าราคากระเป๋า/สินค้า
price = st.number_input(
    "กรอกราคากระเป๋า (บาท)",
    min_value=0.0,
    value=0.0,
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
