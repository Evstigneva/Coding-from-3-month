for i in range(20):
    a1 = int('302010001', 19) + i*19**1 + i*19**3 + i*19**5 + i*19**7
    a2 = int('02024', 19) + i*19**4
    a3 = int('10077', 19) + i*19**3

    sum = a1+a2+a3
    
    if sum%18==0:
        print(sum/18)

