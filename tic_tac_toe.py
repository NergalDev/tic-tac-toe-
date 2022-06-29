# Зададим поле
maps = list(range(1,10))

def draw_board(maps):
    print ("-" * 13)
    for i in range(3):
        print ("|", maps[0+i*3], "|", maps[1+i*3], "|", maps[2+i*3], "|")
        print ("-" * 13)


win_combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

# Сделаем ход
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Текущий результат игры
def get_result():
    win = ""

    for i in win_combination:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O, sum_X):
    step = ""
    for line in win_combination:
        o = 0
        x = 0

        for j in range(0, 3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]

    return step


# Выбор хода компьютера
def AI():
    step = ""

    # если на какой либо из победных линий 2 свои фигуры и 0 чужих
    step = check_line(2, 0)

    # если на какой либо из победных линий 2 чужие фигуры и 0 своих
    if step == "":
        step = check_line(0, 2)

        # если 1 фигура своя и 0 чужих
    if step == "":
        step = check_line(1, 0)

        # центр пуст, то занимаем центр
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5

            # если центр занят, то занимаем первую ячейку
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1

    return step

# Основная программа
valid = False
player = True

while valid == False:

    # Показываем карту
    draw_board(maps)

    # Спросим у играющего куда делать ход
    if player == True:
        symbol = "X"
        step = int(input("Player, your turn: "))
    else:
        print("Computer's turn: ")
        symbol = "O"
        step = AI()

    # Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
    if step != "":
        step_maps(step, symbol)  # делаем ход в указанную ячейку
        win = get_result()  # определим победителя
        if win != "":
            valid = True
        else:
            valid = False
    else:
        print("Draw!")
        valid = True
        win = "Friendship"

    player = not (player)

print(win, "won!")