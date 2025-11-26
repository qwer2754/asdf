import streamlit as st
import time
import random

sentences = [
    "아침에 일찍 일어나는 사람이 성공한다.",
    "노력은 배신하지 않는다.",
    "작은 습관이 큰 변화를 만든다."
]

st.title("한국어 타자 연습 (Streamlit)")

target = random.choice(sentences)
st.write("아래 문장을 입력하세요:")
st.write(target)

user_input = st.text_input("입력:")

if st.button("제출"):
    start_time = time.time()  # 실제 구현 시엔 입력 시작 시점 기록
    end_time = time.time()    # 입력 후 시간 계산
    elapsed_time = 10  # 테스트용 임시 값

    cpm = len(user_input) / (elapsed_time / 60)
    st.write(f"CPM: {cpm:.2f}")
