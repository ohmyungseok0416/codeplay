import os
from text_data_01 import questions_01
from text_data_02 import questions_02
from text_data_03 import questions_03
from ending import *


clear = lambda: os.system('cls')

#3명의 인물 선택지
women = ["선배", "동갑", "후배", "끝"]

#인물도전 진행상황 변수
success = [0, 0, 0]

score1 = 0 #인물별 연애점수
score2 = 0 #인물별 연애점수
score3 = 0 #인물별 연애점수
success = [score1, score2, score3]

#10개의 반복질문 함수

def line():
    print("-" * 30)

def question10(woman):
    score = 0
    for question in woman:
        clear()
        for i in question [0]:
            print(i)
            num = 1
        line()
        for answer in question[1]:
            print(f"{num}.  {answer}")
            num += 1
        line()
        
        sel = int(input("1~4 중 하나를 선택 :"))
        print(f"주인공 : {question[1][sel-1]}")
        print(f"상대방 : {question[2][sel-1]}")
        score+= question[3][sel-1]
        input("(다음으로 넘어가려면 엔터를 치세요...)")

    if chosen_woman == "선배":
        if score >= 12:
            score1 = 1
        else:
            score1 = 0
        clear()
        print(personal_ending1[score1])

    elif chosen_woman == "동갑":
        if score >= 12:
            score2 = 1
        else:
            score2 = 0
        clear()
        print(personal_ending2[score2])
        
    elif chosen_woman == "후배":
        if score >= 12:
            score3 = 1
        else:
            score3 = 0
        clear()
        print(personal_ending3[score3])
    
    
    input("(다음으로 넘어가려면 엔터를 치세요...")


running =True

while running:
    #누구와 연애를 할 지 선택
    if len(women) > 0:
        print("이성의 눈에 뜬 주인공, 여자친구를 만들고싶다")
        line()
        name_list = 1
        for name in women:
            print(f"{name_list}. {name}")  
            name_list += 1
        line()
        choice = int(input("누구와 연애를 시작하시겠습니까? : "))
        chosen_woman = women.pop(choice-1)
        if chosen_woman == "선배":
            question10(questions_01)
        elif chosen_woman == "동갑":
            question10(questions_02)
        elif chosen_woman == "후배":
            question10(questions_03)
        elif chosen_woman == "끝":
            running = False
    else:
        print("세 명의 여자와 모두 사귀게 된 홍식, 그는 쓰레기로 낙인찍혀 영원히 사회에서 격리된다...")
        running = False




clear()
if success[0] == 1 and success[1] == 1 and success[2] == 1:
    print(real_ending111)
elif success[0] == 0 and success[1] == 0 and success[2] == 0:
    print(real_ending000)
elif success[0] == 0 and success[1] == 0 and success[2] == 1:
    print(real_ending001)
elif success[0] == 0 and success[1] == 1 and success[2] == 1:
    print(real_ending011)
elif success[0] == 1 and success[1] == 1 and success[2] == 0:
    print(real_ending110)
elif success[0] == 1 and success[1] == 0 and success[2] == 1:
    print(real_ending101)
elif success[0] == 1 and success[1] == 0 and success[2] == 0:
    print(real_ending100)
elif success[0] == 0 and success[1] == 1 and success[2] == 0:
    print(real_ending010)



    # print(score)

# 인물별 엔딩
#연애를 더한다 / 여기서 마친다
#while 반복문 끝.
#최종엔딩.