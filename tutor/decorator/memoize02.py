class Memoize:
    '''
    Memoization decorator class
    '''
    def __init__(self, func):
        self.func = func
        self.memo = {}
    def __call__(self, *args):
        '''
        As we are using a dictionary, we can't use mutable arguments,
        i.e. the arguments have to be immutable.
        '''
        if args not in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]
    
@Memoize
def fib(n):
    '''
    Fibonnaci number generator
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(161))
