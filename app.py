# ============================================
# 🔐 비밀번호 강도 검사기 (Google Colab용)
# 반복 실행 기능 추가 버전
# ============================================

import re

def check_password(password):
    score = 0
    feedback = []

    # 길이 검사
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ 최소 8자 이상 입력하세요.")

    # 대문자 포함
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ 대문자를 포함하세요.")

    # 소문자 포함
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ 소문자를 포함하세요.")

    # 숫자 포함
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ 숫자를 포함하세요.")

    # 특수문자 포함
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ 특수문자를 포함하세요.")

    # 결과 출력
    print("\n🔍 검사 결과")

    if score == 5:
        print("🟢 매우 강함")
    elif score >= 4:
        print("🟡 강함")
    elif score >= 3:
        print("🟠 보통")
    else:
        print("🔴 약함")

    print(f"점수: {score}/5\n")

    if feedback:
        print("💡 개선 방법:")
        for tip in feedback:
            print(tip)

# 반복 실행
while True:
    pw = input("비밀번호를 입력하세요: ")
    check_password(pw)

    retry = input("\n다시 입력하시겠습니까? (y/n): ").lower()

    if retry != 'y':
        print("프로그램을 종료합니다. 🔐")
        break
