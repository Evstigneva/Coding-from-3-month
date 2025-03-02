import time

def ss(num, ss):
    string = ''
    while num>0:
        string+=str(num%ss)
        num = num//ss

    return string[::-1]


def chet(i):
    i4 = ss(i, 4)

    i4st = str(i4)

    if i%4==0:
        i4st+=i4st[-2:]

    elif i%4!=0:
        ost = (i%4) * 2

        ost = ss(ost, 4)

        i4st+=ost

    a = int(i4st, 4)
    return a

for i in range(1, 10000):
    if chet(i)>=1088:
        print(chet(i), i)
        time.sleep(1000)