import numpy as np
import time

file = np.load('ann_all.npy', allow_pickle = True)
a1 = 1
for i in file:
    print(i)
    #if file[a1]==None:
    #    file = file[:a1+1]
    #    np.save('ann_all.npy', file)
    #    a1-=1
    #a1+=1

#file = file[1:]
#file = file[:-1]


np.save('ann_all.npy', file)
