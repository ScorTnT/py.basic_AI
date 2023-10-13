# hang man game!

# hang man 그림 구현
def hangmanD(temp) :
    DRAW = (
    '''
    +===+ 
    |   | 
    |   |  
    |   |   
    |
    |
    |
    |
    |
    |'''
    ,'''
    +===+ 
    |   | 
    |   |  
    |   |   
    |   o  
    |
    |
    |
    |
    |'''
    ,'''
    +===+ 
    |   | 
    |   |  
    |   |   
    |   o  
    |   |  
    |
    |
    |
    |'''
    ,'''
    +===+ 
    |   | 
    |   |  
    |   |   
    |   o
    |  /|
    |
    |
    |
    |'''
    ,'''
    +===+
    |   |
    |   |
    |   |
    |   o
    |  /|\ 
    |
    | 
    |
    |'''
    ,'''
    +===+ 
    |   | 
    |   |  
    |   |   
    |   o
    |  /|\ 
    |   |  
    | 
    |
    |'''
    ,'''
    +===+ 
    |   | 
    |   |  
    |   |   
    |   o  
    |  /|\ 
    |   |  
    |  /
    |
    |'''
    ,'''
    +===+ 
    |   | 
    |   |  
    |   |   
    |   o  
    |  /|\ 
    |   |     
    |  / \ 
    |
    |'''
    )
    print(DRAW[temp])

import random
words = ['apple','postoffice','depart', 'computer','science','commit', 'merge','google','github','manage','microsoft']
hangmanW = random.choice(words)             # 무작위 단어를 고르기.
letters=""                                  # 선택된 단어와 비교시에 밑줄표시와 글자표시를 하기 위함
temp=0

while True:
    hangmanD(temp)
    barcnt=0
    letter = input('Hmm.. What letter is included?... : ')
    temp += 1
    if letter not in letters:               
        letters += letter                   # 입력받은 글자를 모아서 비교하기 위함

    for l in hangmanW:                      # hangman에서 한글자씩 순차적으로 돌며 
        if l in letters:                    # 그 글자가 letters, 플레이어가 입력한 글자에서 있다면
            print(l, end=" ")               # 글자 표기와 띄어쓰기 1칸
        else :                              # 플레이어가 입력한 글자에 없다면
            print("_", end=" ")             # 밑줄로 표시, 띄어쓰기 1칸
            barcnt += 1                     # 밑줄 개수를 count하여 정답 여부 판단을 위함

    print()                                 # 단순 줄바꿈

    if barcnt == 0 :                        # 밑줄의 개수가 0일 경우 즉, 단어가 완성된 경우
        print("""SUCCESS!!\n
              \ o /
                |
                |
               / \ """)
        break
    if temp == 7 :                          # 시도 횟수가 7회, 그림이 다 그려졌을 경우
        hangmanD(temp)
        print("FAIL... TRY AGAIN")
        break