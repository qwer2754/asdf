import time
import random

# ANSI 색상 코드
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

sentences = [
    "아침에 일찍 일어나는 사람이 성공한다.",
    "노력은 배신하지 않는다.",
    "작은 습관이 큰 변화를 만든다.",
    "포기하지 않는 사람이 결국 이긴다.",
    "행복은 스스로 만드는 것이다.",
    "꿈을 이루기 위해서는 용기가 필요하다.",
    "천 리 길도 한 걸음부터 시작된다."
]

def highlight_errors(target, user):
    colored = ""
    max_len = max(len(target), len(user))

    for i in range(max_len):
        if i < len(target) and i < len(user):
            # 글자가 같으면 초록색
            if target[i] == user[i]:
                colored += GREEN + user[i] + RESET
            else:
                colored += RED + user[i] + RESET  # 오타
        elif i < len(target) and i >= len(user):
            colored += YELLOW + target[i] + RESET  # 입력 안한 글자
        else:
            colored += BLUE + user[i] + RESET  # 추가로 입력한 글자

    return colored


def typing_test():
    print("🎮 한국어 타자 속도 측정 게임 — 오타 강조 버전!\n")
    input("준비되면 Enter를 누르세요...")

    target = random.choice(sentences)

    print("\n👇 아래 문장을 입력하세요:\n")
    print(target)
    print()

    start_time = time.time()
    user_input = input("\n입력: ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    # CPM 계산
    cpm = len(user_input) / (elapsed_time / 60)

    # 정확도 계산
    correct = 0
    for t_c, u_c in zip(target, user_input):
        if t_c == u_c:
            correct += 1

    accuracy = correct / max(len(target), 1) * 100

    # 색 강조 문자열 생성
    highlighted = highlight_errors(target, user_input)

    print("\n--- 결과 ---")
    print(f"🕒 걸린 시간: {elapsed_time:.2f}초")
    print(f"⌨️ CPM(분당 글자 수): {cpm:.2f}")
    print(f"🎯 정확도: {accuracy:.2f}%")
    print("\n📌 오타 강조 결과:")
    print(highlighted)

typing_test()
