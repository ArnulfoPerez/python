import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    count = 0;
    for i in range(numTrials):
        box = [0,0,0,0,1,1,1,1]
        random.shuffle(box)
        draw= [box.pop()]
        random.shuffle(box)
        draw.append(box.pop())
        random.shuffle(box)
        draw.append(box.pop())
        check = draw[0] + draw[1] + draw[2]
        if check == 0 or check == 3:
            count += 1
    return float(count)/numTrials   
numTrials = 100000
print (drawing_without_replacement_sim(numTrials))
        
        