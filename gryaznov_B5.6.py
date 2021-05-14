def greetings():
    print("-------------------")
    print("   Добро пожаловать")
    print("      в игру       ")
    print("  Крестики-нолики  ")
    print("-------------------")
    print("  формат ввода: x y")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print("-------------------")


def field_show():
    print()
    print(f"    | 0 | 1 | 2 | ")
    print(f"  --------------- ")
    for i, row in enumerate(field):
        row_info = f"  {i} | {' | '.join(row)} | "
        print(row_info)
        print("  --------------- ")


def ask_turn():
    while True:
        cords = input("          Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print(f" Выиграли {field[a[0]][a[1]]}!")
            return True
    return False


greetings()
field = [[" "] * 3 for i in range(3)]
turnNum = 0
while True:
    turnNum += 1
    field_show()

    if turnNum % 2 == 1:
        print(" Ходят крестики ")
    else:
        print(" Ходят нолики ")

    x, y = ask_turn()

    if turnNum % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        field_show()
        break

    if turnNum == 9:
        print(" Ничья! ")
        field_show()
        break
