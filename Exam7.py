def player_1():
    pk1 = str(input('Nhap skill_pk1: '))
    return pk1

def player_2():
    pk2 = str(input('Nhap skill_pk2: '))
    return pk2

def handle_result():
    pk1 = player_1()
    pk2 = player_2()
    if pk1 == 'Rock' and pk2 == 'Rock':
        print('Player 1 hoa Player 2')
    elif pk1 == 'Rock' and pk2 == 'Scissors':
        print('Player 1 Win')
    elif pk1 == 'Rock' and pk2 == 'Paper':
        print('Player 2 Win')
    elif pk1 == 'Scissors' and pk2 == 'Rock':
        print('Player 1 Lose')
    elif pk1 == 'Scissors' and pk2 == 'Scissors':
        print('Player 1 hoa Player 2')
    elif pk1 == 'Scissors' and pk2 == 'Paper':
        print('Player 1 Win')
    elif pk1 == 'Paper' and pk2 == 'Rock':
        print('Player 1 Win')
    elif pk1 == 'Paper' and pk2 == 'Scissors':
        print('Player 1 Lose')
    else:
        print('Player 1 hoa Player 2')
handle_result()