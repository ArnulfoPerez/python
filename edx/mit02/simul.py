import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    count = 0
    for i in range(numTrials):
        balls = [0,0,0,1,1,1]
        one = balls.pop(random.randrange(6))
        two = balls.pop(random.randrange(5))
        three = balls.pop(random.randrange(4))
        same= one + two + three
        if same == 3 or same == 0:
            count +=1
    return count/numTrials
numTrials = 1
for i in range(5):
    numTrials *= 10
    print(noReplacementSimulation(numTrials))