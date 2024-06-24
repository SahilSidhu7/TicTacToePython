def Move(Places):
    run = 'True'
    Move = ''
    while run:
        try:
            Input = int(input("Player 2 Turn\nEnter the place num: "))
        except ValueError:
            print("Invalid Command")
            Input = ''
        if type(Input) == int and Input <= 9 and Input >= 0 and Places[Input - 1] != 'X' and Places[Input - 1] != 'O':
            Move = Input
            run = False
        else:
            print("Invalid Input")
    return Move