import streamlit as st
import random
import time

# 문장 리스트
sentences = [
    "아침에 일찍 일어나는 사람이 성공한다.",
    "노력은 배신하지 않는다.",
    "작은 습관이 큰 변화를 만든다.",
    "포기하지 않는 사람이 결국 이긴다.",
    "행복은 스스로 만드는 것이다.",
    "꿈을 이루기 위해서는 용기가 필요하다.",
    "천 리 길도 한 걸음부터 시작된다."
]

# Streamlit 앱 타이틀
st.title("한국어 타자 연습 (Streamlit 버전)")

# 문장 랜덤 선택
if "target" not in st.session_state:
    st.session_state.target = random.choice(sentences)
if "start_time" not in st.session_state:
    st.session_state.start_time = None

st.subheader("아래 문장을 입력하세요:")
st.write(st.session_state.target)

# 사용자 입력
user_input = st.text_input("입력:")

# 타자 시작 시간 기록
if st.session_state.start_time is None and user_input != "":
    st.session_state.start_time = time.time()

# 제출 버튼
if st.button("제출"):
    if user_input == "":
        st.warning("먼저 문장을 입력하세요!")
    else:
        end_time = time.time()
        elapsed_time = end_time - st.session_state.start_time

        # CPM 계산
        cpm = len(user_input) / (elapsed_time / 60)

        # 정확도 계산
        correct = sum(1 for t, u in zip(st.session_state.target, user_input) if t == u)
        accuracy = correct / max(len(st.session_state.target), 1) * 100

        # 오타 강조
        def highlight_errors(target, user):
            result = ""
            max_len = max(len(target), len(user))
            for i in range(max_len):
                if i < len(target) and i < len(user):
                    if target[i] == user[i]:
                        result += f"<span style='color:green'>{user[i]}</span>"
                    else:
                        result += f"<span style='color:red'>{user[i]}</span>"
                elif i < len(target):
                    result += f"<span style='color:orange'>{target[i]}</span>"
                else:
                    result += f"<span style='color:blue'>{user[i]}</span>"
            return result

        highlighted_text = highlight_errors(st.session_state.target, user_input)

        st.markdown(f"**⏱ 걸린 시간:** {elapsed_time:.2f}초")
        st.markdown(f"**⌨️ CPM:** {cpm:.2f}")
        st.markdown(f"**🎯 정확도:** {accuracy:.2f}%")
        st.markdown("**📌 오타 강조 결과:**")
        st.markdown(highlighted_text, unsafe_allow_html=True)

        # 다음 라운드를 위해 초기화
        st.session_state.target = random.choice(sentences)
        st.session_state.start_time = None
