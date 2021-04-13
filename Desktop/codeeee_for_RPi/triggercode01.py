##this bad b is for all polulu all the time 
import maestro
import numpy as np
import time
polo = maestro.Controller()
def ckeckList(lst): 
  
    ele = lst[0] 
    chk = True
    chan = 2 
    # Comparing each element with first item  
    for item in lst: 
        if ele != item: 
            chk = False
            break; 
             
    if (chk == True): runno = polo.setTarget(chan,6000) 
    else: polo.setTarget(chan,4500) 

merp=[]
#runno = polo.setTarget(chan,6000)
#stoppo = polo.setTarget(chan,5000)
#inpval = polo.getPosition(5)
while True:
    merp.append(polo.getPosition(5))
    perp = merp[-20:]
    ckeckList(perp)
    time.sleep(0.01)
    