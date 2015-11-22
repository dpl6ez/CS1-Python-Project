import math
import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# Initialize world
name = "Orbit Simulation. Click the Mouse to Set the Center of the Orbit"
width = 1000
height = 1000
rw.newDisplay(width, height, name)
################################################################

# Display the state by drawing a cat at that x coordinate
background = dw.loadImage("background.jpg")
myimage = dw.loadImage("rsz_planet.jpg")
star = dw.loadImage("star.jpg")

# state -> image (IO)
#draws a star field as the background
#draws the planet at the x and y coordinates given by state[0] and state[1]
#draws the star at the coordinates given by state[6] and state [7] -25
#pixels to center the star on the mouse as opposed to drawing it off center
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(background, (0,0,))
    dw.draw(myimage, (state[0]-10, state[1]-10))
    dw.draw(star, (state[6]-25, state[7]-25))

################################################################

# Update state is contorlled based on whether or not an r value other
# than zero has been assigned. If r is zero, update state keeps the
# state the same as it is initially, outside of updating state[0] and
# state[1] using the values in state[2] and state[3]. This moves the
# planet across the screen at a constant velocity. However, if
# handleEvent assigns a non-zero r value, update state now uses the
# first set of state values. Now the position of the star is set by the
# position of the mouse click, state[6] and state[7]. The position of
# the planet is determined by the radious of the orbit (state[5])
# multiplied by cos[theta + t]. t is detrmined by state[2] and
# state[3], which both increase at a constant rate. This causes the
# cos and sin values to return to values that give the planet a
# circular motion
#
# state -> state
def updateState(state):
    if (state[5] != 0):
        return(state[6] + state[5]*math.cos(-1*state[2]),state[7] + state[5]*math.sin(-1*state[3]),state[2]+state[4],state[3]+state[4],state[4],state[5],state[6],state[7])
    else:
        return((state[0]+state[2],state[1]+state[3],state[2],state[3],state[4],0,2000,2000))

################################################################

# Terminate the program when the x in the top corner is pressed
def endState(state):
    if pg.event.EventType == pg.QUIT:
        return True
    else:
        return False

    
################################################################

# When the mouse button is pressed, a number of variables are
# calculated. The Position of the moouse assigns the Cpoint, which is
# where the sun is drawn. The current x and y location of the planet
# is assigned to x and y for further calculations. The xdis and ydis
# are calculated from the Cpoint and x and y values, giving the
# distance from the sun to planet. These values are used to calculated
# r, the radius of the planets orbit. Finally, theta, the initial
# point on the circle the planet should be drawn at is calcualted
# using the x distance and the y distance. All of these values are
# stores in state so they can be used in updateState
#
# state -> event -> state
#
def handleEvent(state, event):    
    if (event.type == pg.MOUSEBUTTONDOWN):
        Cpoint = pg.mouse.get_pos()
        x = state[0]
        y = state[1]
        xdis = (Cpoint[0]-x)
        ydis = (Cpoint[1]-y)
        theta = math.atan(xdis/ydis)
        r = (((xdis)**2 + (ydis)**2)**(1/2.0))
        return (state[0],state[1],theta,theta,state[4],r,Cpoint[0],Cpoint[1])
    else:
        return(state)

################################################################

# The planet starts at 500,500 and start moving in a random
# direction. The T value is .01, there r value is zero and the initial
# position of the star is offscreen
initState = (500,500,randint(-2,2),randint(-2,2),.01,0,2000,2000)

# Run the simulation no faster than 60 frames per second
frameRate = 60
# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
