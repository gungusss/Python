row1 = "1|2|3"
row2 = "4|5|6"
row3 = "7|8|9"
player = 1

selected = ""

while True:
    x = input("Where do you want to mark?")
    if x == "1" or "2" or "3"and player == 1:
        row1 = row1.replace(x,"X")
        player = 1
        print(row1)
        print(row2)
        print(row3)

    if x == "4" or "5" or "6"and player == 1:
        row2 = row2.replace(x,"X")
        player = 1
        print(row1)
        print(row2)
        print(row3)

    if x == "7" or "8" or "9"and player == 1:
        row3 = row3.replace(x,"X")
        player = 1
        print(row1)
        print(row2)
        print(row3)

    x = input("Where do you want to mark?")
    if x == "1" or "2" or "3"and player == 2:
        row1 = row1.replace(x,"O")
        player = 1
        print(row1)
        print(row2)
        print(row3)

    if x == "4" or "5" or "6"and player == 2:
        row2 = row2.replace(x,"O")
        player = 1
        print(row1)
        print(row2)
        print(row3)

    if x == "7" or "8" or "9"and player == 2:
        row3 = row3.replace(x,"O")
        player = 1
        print(row1)
        print(row2)
        print(row3)



print(row1)
print(row2)
print(row3)

# def game():
    


# if input() = "start":
#     game()


    


