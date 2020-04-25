import random

def convert(iterable, pog=[1,2,3]):
    pog.append(3)
    print(pog)
    return list(map(str,iterable))

nums=[]
for _ in range(10):
    nums.append(random.randint(1,20))

print(convert(nums))