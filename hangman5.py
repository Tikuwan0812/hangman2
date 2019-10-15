import random

def hangman():
    wrong = 0
    stages = ['',
              '________        ',
              '|               ',
              '|       |       ',
              '|       0       ',
              r'|      /|\      ',
              r'|      / \      ',
              '|               '
              ]
    word_list = ['pikachu', 'penchan', 'kumachan', 'iru', 'mogumogu']
    word = random.choice(word_list)
    board = ['_'] * len(word)
    rletters = list(word)
    win = False
    print('ハングマンへようこそ！')

    while wrong < len(stages)-1:
        print('\n')
        ans = input('１文字を予想してね：')
        if ans in rletters:
            index = rletters.index(ans)
            rletters[index] = '$'
            board[index] = ans
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち！')
            print('{}'.format(word))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！正解は {}.'.format(word))

hangman()