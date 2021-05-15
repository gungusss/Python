import random, time

inv = open("inv.txt", "r+")
inv.write("Sex Has OPEND!")
listOfLines = inv.readlines()
print(listOfLines)
inv.close()

# def commoncrateopen():
#     global r_crates_opened
#     for i in range(5):
#         time.sleep(i/5)
#         temp = str(random.choice(c_list))
#         item = " ".join(temp)
#         print(random.choice(item))
#     loot = random.choice(c_list)
#     print(f"You got, {loot}")
#     c_crates_opened =+  1
#     print(f'You have opened {c_crates_opened} common crates')

# def rarecrateopen():
#     global r_crates_opened
#     for i in range(5):
#         time.sleep(i/5)
#         print(random.choice(r_list))
#     loot = random.choice(r_list)
#     print(f"You got, {loot}")
#     r_crates_opened = r_crates_opened + 1

# def legendarycrateopen():
#     global l_crates_opened
#     for i in range(5):
#         time.sleep(i/5)
#         print(random.choice(l_list))
#     loot = random.choice(l_list)
#     print(f"You got, {loot}")
#     l_crates_opened = l_crates_opened + 1

# money, c_crates, r_crates, l_crates, c_crates_opened, r_crates_opened, l_crates_opened = 0,0,0,0,0,0,0

# c_list = ["knife1","knife2","knife3","knife4","knife5"]
# r_list = ["knife1a", "knife2a", "knife3a", "knife4a", "knife5a"]
# l_list = ["knife1b", "knife2b", "knife3b", "knife4b", "knife5b"]

# print("1) Open Common Crate - £10")
# print("2) Open Rare Crate - £50")
# print("3) Open Legendary Crate - £100")
# print("4) Check Cash Balance")
# print("5) Add Cash Balance")
# input = int(input("Please type one of the above commands\n"))

# if input == 1:
#     if money >= 10:
#         money -= 10
#         commoncrateopen()
# elif input == 2:
#      if money >= 50:
#         money -= 50
#         rarecrateopen()    
# elif input == 3:
#     if money >= 100:
#         money -= 100
#         legendarycrateopen()
# elif input == 4:
#     print(f"You have £{money}")
# elif input == 5:
#     moneyAdd = int(input("How much do you want to add?"))
#     money =+ moneyAdd
#     print(f"You now have £{money}")

# Start at random number and print as you are going
# By each item so like
# Knife 1
# Gun 1
# etc etc
# Sticker 1
# You Opened : Knife 1!

    







