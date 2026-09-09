def calculate_total_price(price):
    vat_rate = 0.07       # ภาษี 7%
    discount_rate = 0.05  # ส่วนลด 5%

    # คำนวณภาษีมูลค่าเพิ่ม 7% จากราคาสินค้า
    vat = price * vat_rate

    # ตรวจสอบเงื่อนไขส่วนลด (ตั้งแต่ 2,000 บาทขึ้นไป ได้รับส่วนลด 5%)
    if price >= 2000:
        discount = price * discount_rate
    else:
        discount = 0.0

    # คำนวณราคารวมสุทธิ (ราคาเดิม + ภาษี - ส่วนลด)
    total_price = price + vat - discount

    return vat, discount, total_price


# --- ส่วนการทำงานหลัก (รับค่าและแสดงผล) ---
if __name__ == "__main__":
    try:
        bag_price = float(input("กรุณากรอกราคากระเป๋า (บาท): "))

        if bag_price < 0:
            print("กรุณากรอกราคาที่มากกว่าหรือเท่ากับ 0")
        else:
            vat, discount, total = calculate_total_price(bag_price)

            print("\n" + "=" * 30)
            print("      รายละเอียดการคำนวณ")
            print("=" * 30)
            print(f"ราคากระเป๋า:     {bag_price:>10,.2f} บาท")
            print(f"ภาษี (7%):        {vat:>10,.2f} บาท")
            print(f"ส่วนลด (5%):      {discount:>10,.2f} บาท")
            print("-" * 30)
            print(f"ราคารวมสุทธิ:    {total:>10,.2f} บาท")
            print("=" * 30)

    except ValueError:
        print("ข้อผิดพลาด: กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น")
