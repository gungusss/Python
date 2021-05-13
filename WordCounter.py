f = open("message.txt", "r")
data = f.read()
words = data.split()
print(len(words))