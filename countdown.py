import time

x = int(input('How long do you want to countdown to be'))

for i in range(x):
  print(x)
  x=x-1
  time.sleep(1)

print('GO')
