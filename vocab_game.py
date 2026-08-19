import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
 if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog

# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1,ans2,ans3,ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans2 = ans3.strip().lower()
    u_ans2 = ans4.strip().lower()

    # ตรวจข้อ 1 
    if u_ans1 == "banana":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2 
    if u_ans2 == "mango":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
        
    # ตรวจข้อ 3
    if u_ans3 == "lemon":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
      
    # ตรวจข้อ 4
    if u_ans4 == "cherry":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")

# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.is_ended:
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ
ans1 = st.text_input(
    "ข้อ 1: Monkey eating `b _ n a _ _ `. 🍌",
    value=st.session_state.ans1_val,
    key="input_ans1",
)
ans2 = st.text_input(
    "ข้อ 2: Noey peels the `m _ _ g o`. 🥭",
    value=st.session_state.ans2_val,
    key="input_ans2",
)
ans2 = st.text_input(
    "ข้อ 2: `_ e m _ n` have a sour taste . 🍋 ",
    value=st.session_state.ans3_val,
    key="input_ans3",
)
    ans2 = st.text_input(
    "ข้อ 2: `c h _ r r _` is sweet . 🍒 ",
    value=st.session_state.ans4_val,
    key="input_ans4",
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.is_ended:
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1,ans2,ans3,ans4)

st.divider()
st.write("นางสาวพัชรมัย มโนชัย เลขที่ 17 ม.4/2")
