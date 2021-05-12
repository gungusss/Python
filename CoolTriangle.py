# numberOfLines= 7
# size = int(numberOfLines)

# if size < 2 and size > 9:
#     print("This number is not between 2 and 9");
# if size >= 2 and size <= 9:
#     m = (2 * size) - 2
#     for i in range(0, size):
#         for j in range(0, m):
#             print(end=" ")
#         m = m - 1
#         for j in range(0, i):
#             print(i , end=' ')
#         print(" ")

size= int(input("Enter a number between 2-9"))

if size < 2 or size > 9:
    print("Number between 1-9")
 
if size >= 2 and size <= 9:
    m = (2 * size) - 2
    for i in range(0, size):
        for j in range(0, m):
            print(end=" ")
        m = m - 1
        for j in range(0, i + 1):
            print(i+1 , end=' ')
        print(" ")