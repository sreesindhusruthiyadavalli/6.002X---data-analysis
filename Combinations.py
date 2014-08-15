def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        
#import itertools
#x =  itertools.combinations('1234567', 3) 

combinations('1234567', 3)
       def lotsOfParameters2(1,2,3,4,5):
    print a
    print b
    print c
    print d
    print e
    
#lotsOfParameters2()
lotsOfParameters2(1, 2)
#lotsOfParameters2(1, c=2)

#lotsOfParameters2(1, e= 20,b = 3)
#lotsOfParameters2(e=5,d=4,c=3,b=2, 1)
#lotsOfParameters2(e=5,a=1,d=4,b=2,c=3)
#lotsOfParameters2(a=5,b=1,c=4,d=2,3)
