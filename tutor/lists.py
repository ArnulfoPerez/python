import time

n= 100000

start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print('+: ' + str(time.time() - start_time))

start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print('+=: ' +str(time.time() - start_time))

start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print('append: '+str(time.time() - start_time))

def timing(fun,label):
    start_time = time.time()
    fun()
    end_time = time.time()
    print(label + str(end_time - start_time))
    
def concat():
    l = []
    for i in range(n):
        l = l + [i * 2]
        
def accum():
    l = []
    for i in range(n):
        l += [i * 2]
        
def app():
    l = []
    for i in range(n):
        l.append(i * 2)
        
timing(concat,'+: ')
timing(accum,'+=: ')
timing(app,'append: ')
        
