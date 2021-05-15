# BUBBLE SORT
BubbleSortArray = [69,42,11,1,61,12,65,2]
for i in range(len(BubbleSortArray)):
    for index in range(len(BubbleSortArray)-1):
        print(BubbleSortArray)
        if BubbleSortArray[index] > BubbleSortArray[index+1]:
            BubbleSortArray[index], BubbleSortArray[index+1] = BubbleSortArray[index+1], BubbleSortArray[index]

print(BubbleSortArray)