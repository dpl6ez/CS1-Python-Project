from random import randint

def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
         newState = print(randint(1,5))
        return((state[0],state[1],newState,newState))
    else:
        return(state)
