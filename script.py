def greetings():#приветствие
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
def field():#Поле
    print("__________________")
    print (f"   | 0 | 1 | 2 |")
    print("----------------")
    for i in range(3):
        row_info = " | ".join(cell[i])
        print(f" {i} | {row_info} | ")
        print("----------------")

def ask():#Проверка ввода пользователя
    while True:
        coords = input("Ваш ход:").split()

        if len(coords) != 2:
            print("Введите 2 значения!")
            continue

        x, y = coords

        if not(x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне диапазона!")
            continue

        if cell[x][y] != ' ':
            print("Клетка занята!")
            continue

        return x,y

def win():#Проверка выйгрыша
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        cell_sym = []
        for c in coord:
            cell_sym.append(cell[c[0]][c[1]])
        if cell_sym == ["X", "X", "X"]:
            print("Выйграл X!!!")
            return True
        if cell_sym == ["0", "0", "0"]:
            print("Выйграл 0!!!")
            return True
        return False

greetings()
cell = [[' '] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    field()
    if num % 2 == 1:
        print("Ходит крестик.")
    else:
        print("Ходит нолик.")

    x, y = ask()

    if num % 2 == 1:
        cell[x][y] = "X"
    else:
        cell[x][y] = "0"

    if win():
        break

    if num == 9:
        field()
        print("НИЧЬЯ!!!")
        break