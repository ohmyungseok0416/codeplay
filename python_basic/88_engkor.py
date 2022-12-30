def enter(text):
    result = text + "\n"
    return result


e = open("eng.txt", "w", encoding = "UTF =-8")
k = open("kor.txt", "w", encoding = "UTF =-8")

while True:
    sel = input("단어이ㅂ력 - i / 끝내기 -q / 단어시험 - t")
    if sel == "i":
        word_E = input ("영어단어 입력")
        e.write(enter(word_E))

        word_K = input ("한글 뜻 입력")
        k.write(enter(word_K))

    elif sel == "q":
        break
    elif sel == "t":
        e = open("eng.txt" , "r", encoding = "UTF-8")
        k = open("kor.txt" , "r", encoding = "UTF-8")
        kors = k.readlines()
        engs = e.readlines()
        for i in range(len(kors)):
            answer = input(f"{kors[i]} 뜻을 가진 영어단어는? :")
            if answer == engs[i]:
                print("정답입니다")
            else:
                print(f"틀렸습니다. ㄷ정답아ㅡㄴ {engs[i]} 입니다")
        e.close()
        k.close()