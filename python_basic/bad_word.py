bad_words = ["병신", "븅신", "코딩쌤", "코드플레이", "느금마", "민재", "씨발", "지랄",  "시발"]
bad_word = []
answer = 0
add_word = 0


while True:
    answer = input("말 해라 ㅎ병 신아 : ")
    bad_word = [] #홍석이 바구니
    for word in bad_words:
        if word in answer:
            bad_word.append(word)

    
    if len(bad_word) > 0:
         print(f"{word}<- ㅄ쉑 ㅋㅋ ㅋㅋ ㅋㅋ 병신 ㅋㅋ ㄱㅋㅋㅋㅋㅋ 개병신 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
         continue
    else:
        if answer == "꺼져":
            print("안녕히 가라 병 신아")
            break
        elif answer == "추가":
            add_word = input("어떤 단어를 추가하냐 병신 아")
            bad_words.append(add_word)
            print(f"{add_word} 단어가 금치겅에 추가 댓다 ㅄ아")
            print(f"지금까지 등ㅀㄱ단 단겅다 ㅄ아")
            print("=" * 50)
            print(bad_words)
            print("=" * 50)
            continue
        else:
            print(f"{answer} (이) 라구요? 옳은 ㅁ랄 씀이다 병 신아")

