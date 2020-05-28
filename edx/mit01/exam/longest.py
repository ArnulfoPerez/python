def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    def decr(a, b):
        """
        decreasing order
        """
        return not a < b
    def incr(a, b):
        """
        increasing order
        """
        return not a > b
    size = len(L)
    longest_sequence = []
    ll = 0
    for i in range(size):
        def longest(order):
            sequence = [L[i]]
            for j in range(i+1, size):
                if order(L[j-1], L[j]):
                    sequence.append(L[j])
                else:
                    break
            return sequence
        sequence = longest(decr)
        ls = len(sequence)
        if ls > ll:
            longest_sequence = sequence[:]
            ll = ls
        sequence = longest(incr)
        ls = len(sequence)
        if ls > ll:
            longest_sequence = sequence[:]
            ll = ls
    return sum(longest_sequence)
    
assert(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])==26)
assert(longest_run([5, 4, 10])==9)
print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
print(longest_run([5, 4, 10]))
    