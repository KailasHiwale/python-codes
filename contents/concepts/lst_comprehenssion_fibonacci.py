>>> l=[]
>>> l.append(1)
>>> l.append(1)
>>> tmp=(l[i-1]+l[i-2] for i in range(2, 10))
>>> l += tmp
>>> l
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]