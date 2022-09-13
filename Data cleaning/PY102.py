# 3
a = [3,6,9]
import numpy as np
while True:
    b = eval(input())
    try:
        print(np.inner(a,b))
        break
    except:
        continue
    