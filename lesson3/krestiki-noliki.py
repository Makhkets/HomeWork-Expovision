# Крестики нолики:


import os
from time import sleep

count = 0

board = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}


def output(board):
    os.system("cls")
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


def get_choice(row, width):
    choice = ""
    if row == 1 and width == 1:
        choice = "top-L"
    elif row == 1 and width == 2:
        choice = "top-M"
    elif row == 1 and width == 3:
        choice = "top-R"

    elif row == 2 and width == 1:
        choice = "mid-L"
    elif row == 2 and width == 2:
        choice = "mid-M"
    elif row == 2 and width == 3:
        choice = "mid-R"

    elif row == 3 and width == 1:
        choice = "low-L"
    elif row == 3 and width == 2:
        choice = "low-M"
    elif row == 3 and width == 3:
        choice = "low-R"

    return choice


def check_value(board, choice):
    if board[choice] != "X" and board[choice] != "O":
        return True
    else:
        return False


while True:
    try:
        while True:

            row = int(input("Выбирает игрок X\nВведите число ряда: "))
            width = int(input("Введите номер номер числа в ряду от 1 до 3: "))

            if count == 9:
                print("Игра закончена, создается новая...")
                sleep(3)
                count = 0
                board = {
                    "top-L": " ",
                    "top-M": " ",
                    "top-R": " ",
                    "mid-L": " ",
                    "mid-M": " ",
                    "mid-R": " ",
                    "low-L": " ",
                    "low-M": " ",
                    "low-R": " ",
                }
                continue

            if row != 1 and row != 2 and row != 3:
                print("Введите число от 1 до 3")
                continue

            if width != 1 and width != 2 and width != 3:
                print("Введите число от 1 до 3")
                continue

            choice = get_choice(row, width)
            check = check_value(board, choice)

            if check == True:
                board[choice] = "X"

                output(board)
                count += 1
                print(f"Count: {count}")
                break
            else:
                print("Это поле уже занято")
                continue

        while True:
            row = int(input("Выбирает игрок O\nВведите число ряда: "))
            width = int(input("Введите номер номер числа в ряду от 1 до 3: "))

            if count == 9:
                print("Игра закончена, создается новая...")
                sleep(3)
                count = 0
                board = {
                    "top-L": " ",
                    "top-M": " ",
                    "top-R": " ",
                    "mid-L": " ",
                    "mid-M": " ",
                    "mid-R": " ",
                    "low-L": " ",
                    "low-M": " ",
                    "low-R": " ",
                }
                continue

            if row != 1 and row != 2 and row != 3:
                print("Введите число от 1 до 3")
                continue

            if width != 1 and width != 2 and width != 3:
                print("Введите число от 1 до 3")
                continue

            choice = get_choice(row, width)
            check = check_value(board, choice)
            if check == True:
                board[choice] = "O"
                output(board)
                count += 1
                print(f"Count: {count}")
                break
            else:
                print("Это поле уже занято")
                continue
    except:
        os.system("cls")
        continue