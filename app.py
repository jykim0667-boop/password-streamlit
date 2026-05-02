import streamlit as st
import re

st.set_page_config(page_title="비밀번호 강도 검사기", page_icon="🔐")

st.title("🔐 비밀번호 강도 검사기")
st.write("비밀번호를 입력하면 강도를 분석해드립니다.")

password = st.text_input("비밀번호 입력", type="password")

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ 최소 8자 이상 입력하세요.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ 대문자를 포함하세요.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ 소문자를 포함하세요.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ 숫자를 포함하세요.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ 특수문자를 포함하세요.")

    return score, feedback

if st.button("검사하기"):
    if password:
        score, feedback = check_password(password)

        st.subheader("🔍 검사 결과")

        if score == 5:
            st.success("🟢 매우 강함")
        elif score >= 4:
            st.warning("🟡 강함")
        elif score >= 3:
            st.info("🟠 보통")
        else:
            st.error("🔴 약함")

        st.write(f"점수: {score}/5")

        if feedback:
            st.subheader("💡 개선 방법")
            for tip in feedback:
                st.write(tip)
    else:
        st.warning("비밀번호를 입력하세요.")
