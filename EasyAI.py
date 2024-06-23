import random

def My_Move(Places):
    Possible_Pos = list()
    for i in range(0,len(Places)):
        if Places[i] != 'X' and Places[i] != 'O':
            Possible_Pos.append(Places[i])
    random.shuffle(Possible_Pos)
    if not Possible_Pos:
        return 'Draw'
    else:
        return Possible_Pos[0]
