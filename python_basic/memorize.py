import random
import os
clear = lambda: os.system('cls')


eng = ["car", "hat", "rat", "bat", "cat", "hen", "day", "bad", "way", "dog"]
kor = ["자동차", "모자", "쥐", "박쥐", "고양이", "암탉", "하루", "나쁜", "길", "개"]
select = 0
answer = 0
mode = 0





while True:
    clear()
    print("*" * 20)
    print("oms 깜지봇 III")
    print("*" * 20)
    print(f"수록 영단어 갯수 : {len(eng)}")
    mode = input("원하는 작업 선택: 단어시험 / 단어입력 / 종료")
    print("*" * 20)

    if mode == "단어시험":    
        while len(kor) != 0:
            clear()
            select = random.randint(0, len(eng)) - 1
            answer = input(f"{kor[select]} - 이 단어를 영어로 하면? :")
            if answer == eng[select]:
                print("정답입니다 {kor[select]} = {eng[select]} 이죠")
                eng.pop(select)
                kor.pop(select)
            else:
                print("틀렸어요. 빡빡인가")

        print("열개의 준비된 단어를 모두 맞추셨습니다.")
    elif mode == "종료":
        print("종료합니다 뻐큐맨")
        break

    elif mode == "단어입력":
        while True:
            eng.append(input("영어단어를 입력하세요 :"))
            kor.append(input("한글단어를 입력하세요 :"))
            if "아니요" == input("입력을 더 하시겠습니까? (예 / 아니요)"):
                print("단어입력을 완료했다")
                break




























































































































































































































































































































































































































































































































































































































