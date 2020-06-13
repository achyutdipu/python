w = "the quick brown fox jumps over the lazy dog ".split()
print(w)
i = w.index('fox')
print(i)
print w[i]
print w.count('the')
print 37 in [1, 78, 9, 37, 34, 53]
print 78 not in [1, 78, 9, 37, 34, 53]
u = "jackdaws love my big sphinx of quartz".split()
print u
del u[3]
print u
u.remove('jackdaws')
print u
del u[u.index('quartz')]
print u
del u[3]
print u
m = [2, 1, 3]
n = [4, 7, 11]
k = m + n
print k
k += [18, 29, 47]
print k
k.extend([76, 129, 199])
print k
