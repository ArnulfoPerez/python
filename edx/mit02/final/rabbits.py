import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300
PROBABILITYDYING = 0.90

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    if CURRENTRABBITPOP < 10:
        return
    p_rep = 1 - (float(CURRENTRABBITPOP)/MAXRABBITPOP)
    current = CURRENTRABBITPOP
    for i in range(current):
        if (random.random() < p_rep) and CURRENTRABBITPOP <MAXRABBITPOP :
            CURRENTRABBITPOP += 1
        
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    if CURRENTRABBITPOP > 10:
        p_eating = CURRENTRABBITPOP/MAXRABBITPOP
        current = CURRENTFOXPOP
        for i in range(current):
            if random.random() < p_eating and CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1
                if random.random() < 1/3:
                    CURRENTFOXPOP += 1
            else:
                if random.random() < PROBABILITYDYING:
                    CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations=[]
    fox_populations=[]
    for i in range(numSteps):
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
        rabbitGrowth()
        foxGrowth()
    return (rabbit_populations, fox_populations)
        
numSteps = 200
(rabbits,foxes) = runSimulation(numSteps)
time = range(len(rabbits))
rcoeff = pylab.polyfit(time,rabbits,2)
fcoeff = pylab.polyfit(time,foxes,2)
pylab.plot(pylab.polyval(rcoeff,time))
pylab.plot(pylab.polyval(fcoeff,time))