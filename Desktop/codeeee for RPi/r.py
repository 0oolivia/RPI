import maestro
import numpy as np
import time
def ckeckList(lst): 
  
    ele = lst[0] 
    chk = True
      
    # Comparing each element with first item  
    for item in lst: 
        if ele != item: 
            chk = False
            break; 
              
    if (chk == True): runno = polo.setTarget(0,6000) 
    else: polo.setTarget(0,4500) 
polo = maestro.Controller()
merp=[]
#runno = polo.setTarget(3,6000)
#stoppo = polo.setTarget(3,0000)
#inpval = polo.getPosition(5)
while True:
    merp.append(polo.getPosition(5))
    perp = merp[-20:]
    ckeckList(perp)
    time.sleep(0.1)
    