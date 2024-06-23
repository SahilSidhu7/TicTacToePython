import random
import EasyAI, LocalPlay


def main():
    GameMode = 'Select'
    GameMode = SelectGameMode()
    print("GameMode: " + GameMode)
    print('''Welcome to Tic-Tac-Toe,\nEnter the num to place your mark.\nYour mark is X.''')
    print(' 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 ')
    Places = [1,2,3,4,5,6,7,8,9]
    playing = True
    State = 'Continue'

    FunctionList = [VL1, VL2,VL3,HL1,HL2,HL3,D1,D2]

    CurrentFunction = 11;
    
    HardAIDraw = "Continue"

    while playing:
        try:
            Input = int(input("Player 1 Turn\nEnter the place num: "))
        except ValueError:
            Input = ''
        if type(Input) == int and Input <= 9 and Input >= 0 and Places[Input - 1] != 'X' and Places[Input - 1] != 'O':
            Places[Input - 1] = 'X'
            State = Check_Win(Places, State)
            if State != 'Continue':
                print(State)
                print(f''' {Places[0]} | {Places[1]} | {Places[2]}\n {Places[3]} | {Places[4]} | {Places[5]}\n {Places[6]} | {Places[7]} | {Places[8]}''')
                break
            else:
                print(f''' {Places[0]} | {Places[1]} | {Places[2]}\n {Places[3]} | {Places[4]} | {Places[5]}\n {Places[6]} | {Places[7]} | {Places[8]}''')
               
            
            if GameMode == 'EasyAI':
                Move = EasyAI.My_Move(Places)
            elif GameMode == 'HardAI':
                Move,FunctionList,CurrentFunction,HardAIDraw = My_Move(Places,FunctionList,CurrentFunction)
                if(HardAIDraw == "Draw"):
                    print("Draw")
                    break
                elif(HardAIDraw == "Lost"):
                    print("Lost")
                    break
            elif GameMode == 'LocalPlay':
                Move = LocalPlay.Move(Places)
            else:
                print("GameMode not detected")
            try:
                Places[int(Move) - 1] = 'O'
            except ValueError:
                print("Draw")
                break
            State = Check_Win(Places, State)
            if State != 'Continue':
                print(f''' {Places[0]} | {Places[1]} | {Places[2]}\n {Places[3]} | {Places[4]} | {Places[5]}\n {Places[6]} | {Places[7]} | {Places[8]}''')
                break
            print("Player 2 Move")
            print(f''' {Places[0]} | {Places[1]} | {Places[2]}\n {Places[3]} | {Places[4]} | {Places[5]}\n {Places[6]} | {Places[7]} | {Places[8]}''')
            
        else:
            print("Invalid Command")


def Check_Win(Places, State):
    AvailablePos = list()
    a = 1


    if Places[0] == Places[1] == Places[2] == 'X' or Places[3] == Places[4] == Places[5] == 'X'or Places[6] == Places[7] == Places[8]== 'X':
        State = 'Won'
        print("Won")
    elif Places[0] == Places[3] == Places[6] == 'X' or Places[1] == Places[4] == Places[7] == 'X'or Places[2] == Places[5] == Places[8]== 'X':
        State = 'Won'
        print("Won")
    elif Places[0] == Places[4] == Places[8] == 'X' or Places[2] == Places[4] == Places[6] == 'X':
        State = 'Won'
        print("Won")
    elif Places[0] == Places[1] == Places[2] == 'O' or Places[3] == Places[4] == Places[5] == 'O'or Places[6] == Places[7] == Places[8]== 'O':
        State = 'Lost'
        print("Lost")
    elif Places[0] == Places[3] == Places[6] == 'O' or Places[1] == Places[4] == Places[7] == 'O'or Places[2] == Places[5] == Places[8]== 'O':
        State = 'Lost'
        print("Lost")
    elif Places[0] == Places[4] == Places[8] == 'O' or Places[2] == Places[4] == Places[6] == 'O':
        State = 'Lost'
        print("Lost")
    else:
        for i in range(0,len(Places)):
            try:
                Places[i] = int(Places[i])
            except ValueError:
                continue
            if type(Places[i]) == type(a):
                AvailablePos.append(i)
            else:
                continue
        if len(AvailablePos) == 0:
            State = 'Draw'
        else:
            State = 'Continue'
    return State

def SelectGameMode():
    print('Select Game Mode\n1.Easy AI\n2.Hard AI\n3.Local Play')
    GameModes = ('EasyAI', 'HardAI', 'LocalPlay')
    Input = 'Null'
    run = True
    while run:
        try:
            Input = int(input('GameMode Serial No. ')) - 1
        except ValueError:
            print("Invalid Input")
        if (Input == 0 or Input == 1 or Input == 2):
            run = False
        else:
            print("Invalid Input")
    GameMode = str(GameModes[Input])
    return GameMode

def My_Move(Places,FunctionList,CurrentFunction):
    PosibleMoves = list()
    Move = 0
    Functions = FunctionList
    HardAIDraw = "Continue"
    if (CurrentFunction == 11):
        try:
            CurrentFunction = random.randint(0,len(Functions)-1)
            Move = Functions[CurrentFunction](Places)
        except ValueError:
            HardAIDraw = "Lost"
    else:
        Move = Functions[CurrentFunction](Places)

    if (type(Move) == type(23)):
        return Move,FunctionList,CurrentFunction,HardAIDraw
    elif(Move == "Lost"):
        HardAIDraw = "Lost"
        return Move,FunctionList,CurrentFunction,HardAIDraw
    else:     
        while(type(Move) != type(23)):
            try:
                if(len(Functions) != 0):
                    Functions.pop(CurrentFunction)
                    if(len(Functions) != 0):
                        CurrentFunction = random.randint(0,len(Functions)-1)
                        Move = Functions[CurrentFunction](Places)
                    else:
                        for i in Places:
                            if (i != "X" and i != "O"):
                                PosibleMoves.append(i)
                        random.shuffle(PosibleMoves)
                        return PosibleMoves[0],FunctionList,CurrentFunction,HardAIDraw
            except ValueError:
                HardAIDraw = "Lost"
            FunctionList = Functions
        return Move,FunctionList,CurrentFunction,HardAIDraw

def VL1(Places):
    Pos = list()
    K = "O"
    for i in [0,3,6]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [0,3,6]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"
    
def VL2(Places):
    Pos = list()
    K = "O"
    for i in [1,4,7]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [1,4,7]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"
    
def VL3(Places):
    Pos = list()
    K = "O"
    for i in [2,5,8]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [2,5,8]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"


def HL1(Places):
    Pos = list()
    K = "O"
    for i in [0,1,2]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [0,1,2]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"
    
def HL2(Places):
    Pos = list()
    K = "O"
    for i in [3,4,5]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [3,4,5]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"
    
def HL3(Places):
    Pos = list()
    K = "O"
    for i in [6,7,8]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [6,7,8]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"
    
def D1(Places):
    Pos = list()
    K = "O"
    for i in [0,4,8]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [0,4,8]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"
    
def D2(Places):
    Pos = list()
    K = "O"
    for i in [2,4,6]:
        if (Places[i] != 'X'):
            Pos.append(Places[i])
    if(len(Pos) == 3):
        for i in [2,4,6]:
            if(Places[i] == 'O'):
                for K in Pos:
                    Pos.remove(K)
        random.shuffle(Pos)
        print(Pos)
        if (len(Pos) != 0):
            return Pos[0]
        else:
            return "Lost"
    else:
        return "Null"

main()