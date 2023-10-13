# hang man game!

# hang man 그림 구현
def hangmanD(temp) :
    DRAW = [
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
    ]
    print(DRAW[temp])

import random
words = ['apple','postoffice','depart', 'computer','science','commit', 'merge','google','github','manage','microsoft']
hangmanW = random.choice(words)
letters=""
temp=0

while True:
    hangmanD(temp)
    barcnt=0
    letter = input('Hmm.. What letter is included?... : ')
    temp += 1
    if letter not in letters:               
        letters += letter                   # 입력받은 글자를 모아서 비교하기 위함

    for l in hangmanW:                      
        if l in letters:                    
            print(l, end=" ")               
        else :                              
            print("_", end=" ")             
            barcnt += 1

    print()                                 # 단순 줄바꿈

    if barcnt == 0 :                        # 밑줄의 개수가 0일 경우 즉, 단어가 완성된 경우
        print("SUCCESS!!")
        break
    if temp == 7 :                          # 시도 횟수가 7회, 그림이 다 그려졌을 경우
        hangmanD(temp)
        print("FAIL... TRY AGAIN")
        break