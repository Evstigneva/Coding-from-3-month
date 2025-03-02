import sys

sys.setrecursionlimit(10000000)

def func(i):
    if i==1:
        return 1
    
    elif i==2:
        return 2
    
    elif i>2:
        l = i * (i-1) + func(i-1) - func(i-2)
        return l
    
sum = func(2024) + func(2020) - func(2019)
print(sum)