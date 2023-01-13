def tlqkf(word_in):

    word_poem = []
    words = word_in("3글자 단어 입력 ")
    poem = 0

    for w in words:
        while True:
            print(w)
            poem = input(" => ")
            word_poem.append(poem)
            if w == poem[0]:
                break
            else:
                print ("첫글자 확인")
                continue
        print(word_poem)
    for i in word_poem:
        print(f"{i[0]}: {i}")

tlqkf(input("삼행시를 짓기위한 3글자 단어를 입력해 : "))
