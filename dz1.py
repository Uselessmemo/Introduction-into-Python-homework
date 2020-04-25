import sys

num = sys.argv[1]
num =int(num)

s = [' ']*num

for i in range(num):
    s[-(i+1)] = '#'
    print(*s,sep='')