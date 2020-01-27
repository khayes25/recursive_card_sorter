import random 
  
def randomize(list, n) : 
    for i in range(n - 1, 0, -1): 
        j = random.randint(0, i + 1) 
  
        list[i], list[j] = list[j], list[i] 
    return list 
