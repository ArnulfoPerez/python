import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    def find(l,t,s):
        if t == 0 or l == []:
            return s
        for i in l:
            if i == t:
                s[i]=1
                return s
        x = find(l[1:],t,s)
        tx = test(x)
        y = s.copy()
        y[l[0]]=1
        z = find(l[1:],t-l[0],y)
        tz = test(z)
        if (tz == total and tx != total) or (tz > tx and tz < total) or (tz == tx and sum(z) < sum(x)):
            return z
        else:
            return x
        
    def test(x):
        size = len(x)
        t = 0
        for i in range(size):
            t += x[i] * choices[i]
        return t

    size = len(choices)
    subset = np.zeros(size, dtype=int)
    l = []
    for i in range(size):
        element = choices[i]
        if element == total:
            subset[i] = 1
            return subset
        if element < total:
            l.append(i)
    return find(l,total,subset)
#    l_len = len(l)
#    for i in range(l_len):
#        y = subset.copy()
#        y[l[i]]=1
#        x = find(l[i+1:],total-choices[l[i]],y)
#        print(x,i,l[i+1:],total-choices[l[i]],y,subset)
#        if test(x):
#            return x
#    return find_combination(choices, total-1)
#    
            
print(find_combination([1,2,2,3], 4))
print(find_combination([1,1,3,5,3], 5))
print(find_combination([1,1,1,9], 4))
print(find_combination([3, 10, 2, 1, 5], 12))
print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171))
print(find_combination([4, 6, 3, 5, 2], 10))