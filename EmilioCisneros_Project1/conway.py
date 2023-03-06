"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

from datetime import date
import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def addPoint(i,j,grid):
    grid[i,j] = ON

block = np.array([  [0,0,0,0], 
                    [0,255,255,0], 
                    [0,255,255,0],
                    [0,0,0,0]])

beehive = np.array([[0,0,0,0,0,0], 
                    [0,0,255,255,0,0], 
                    [0,255,0,0,255,0],
                    [0,0,255,255,0,0],
                    [0,0,0,0,0,0]])

loaf = np.array([   [0,0,0,0,0,0], 
                    [0,0,255,255,0,0],
                    [0,255,0,0,255,0],
                    [0,0,255,0,255,0],
                    [0,0,0,255,0,0],
                    [0,0,0,0,0,0]])

boat = np.array([   [0,0,0,0,0], 
                    [0,255,255,0,0],
                    [0,255,0,255,0],
                    [0,0,255,0,0],
                    [0,0,0,0,0]])

tub = np.array([    [0,0,0,0,0], 
                    [0,0,255,0,0],
                    [0,255,0,255,0],
                    [0,0,255,0,0],
                    [0,0,0,0,0]])

blinker1 = np.array([[0,0,0], 
                     [0,255,0],
                     [0,255,0],
                     [0,255,0],
                     [0,0,0]])

blinker2 = np.array([[0,0,0,0,0],
                     [0,255,255,255,0],
                     [0,0,0,0,0]])

toad1 = np.array([   [0,0,0,0,0,0], 
                    [0,0,0,255,0,0],
                    [0,255,0,0,255,0],
                    [0,255,0,0,255,0],
                    [0,0,255,0,0,0],
                    [0,0,0,0,0,0]])

toad2 = np.array([  [0,0,0,0,0,0],
                    [0,0,255,255,255,0],
                    [0,255,255,255,0,0],
                    [0,0,0,0,0,0]])

beacon1 = np.array([ [0,0,0,0,0,0],
                    [0,255,255,0,0,0],
                    [0,255,255,0,0,0],
                    [0,0,0,255,255,0],
                    [0,0,0,255,255,0],
                    [0,0,0,0,0,0]])

beacon2 = np.array([[0,0,0,0,0,0],
                    [0,255,255,0,0,0],
                    [0,255,0,0,0,0],
                    [0,0,0,0,255,0],
                    [0,0,0,255,255,0],
                    [0,0,0,0,0,0]])

glider1 = np.array([[0,0,0,0,0],
                    [0,0,255,0,0],
                    [0,0,0,255,0],
                    [0,255,255,255,0],
                    [0,0,0,0,0]])

glider2 = np.array([[0,0,0,0,0],
                    [0,255,0,255,0],
                    [0,0,255,255,0],
                    [0,0,255,0,0],
                    [0,0,0,0,0]])

glider3 = np.array([[0,0,0,0,0],
                    [0,0,0,255,0],
                    [0,255,0,255,0],
                    [0,0,255,255,0],
                    [0,0,0,0,0]])

glider4 = np.array([[0,0,0,0,0],
                    [0,255,0,0,0],
                    [0,0,255,255,0],
                    [0,255,255,0,0],
                    [0,0,0,0,0]])

lws1 = np.array([   [0,0,0,0,0,0,0],
                    [0,255,0,0,255,0,0],
                    [0,0,0,0,0,255,0],
                    [0,255,0,0,0,255,0],
                    [0,0,255,255,255,255,0],
                    [0,0,0,0,0,0,0]])

lws2 = np.array([   [0,0,0,0,0,0,0],
                    [0,0,0,255,255,0,0],
                    [0,255,255,0,255,255,0],
                    [0,255,255,255,255,0,0],
                    [0,0,255,255,0,0,0],
                    [0,0,0,0,0,0,0]])

lws3 = np.array([   [0,0,0,0,0,0,0],
                    [0,0,255,255,255,255,0],
                    [0,255,0,0,0,255,0],
                    [0,0,0,0,0,255,0],
                    [0,255,0,0,255,0,0],
                    [0,0,0,0,0,0,0]])

lws4 = np.array([   [0,0,0,0,0,0,0],
                    [0,0,255,255,0,0,0],
                    [0,255,255,255,255,0,0],
                    [0,255,255,0,255,255,0],
                    [0,0,0,255,255,0,0],
                    [0,0,0,0,0,0,0]]) 

def checkFigure(i,j,N,M,grid,figure):
    check=True
    if(i+len(figure)-1 < N and j+len(figure[0])-1<M):
        for h in range(len(figure)):
            for k in range(len(figure[0])):      
                    if(grid[i+h,j+k]!=figure[h,k]):
                        check=False
    else: check = False
    return check

generations=0
first = True
def update(frameNum, img, grid, N,M):
    global first
    if(first == True): 
        first = False
        return 
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    auxGrid = grid.copy()
    auxGrid = np.pad(auxGrid,1,mode="constant")
    # TODO: Implement the rules of Conway's Game of Life
    numBlocks=0
    numBeehive=0
    numLoaf=0
    numBoat=0
    numBlinker=0
    numToad=0
    numBeacon=0
    numTub=0
    numGlider=0
    numLWS=0
    for i in range(N):
        for j in range(M):
            #Block
            if(checkFigure(i-1,j-1,N,M,auxGrid,block)): numBlocks +=1
            #Beehive
            if(checkFigure(i-1,j-1,N,M,auxGrid,beehive)): numBeehive +=1
            #Loaf
            if(checkFigure(i-1,j-1,N,M,auxGrid,loaf)): numLoaf +=1
            #Boat
            if(checkFigure(i-1,j-1,N,M,auxGrid,boat)): numBoat +=1
            #Tub
            if(checkFigure(i-1,j-1,N,M,auxGrid,tub)): numTub +=1
            #Blinker
            if(checkFigure(i-1,j-1,N,M,auxGrid,blinker1)): numBlinker +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,blinker2)): numBlinker +=1
            #Toad
            if(checkFigure(i-1,j-1,N,M,auxGrid,toad1)): numToad +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,toad2)): numToad +=1
            #Beacon
            if(checkFigure(i-1,j-1,N,M,auxGrid,beacon1)): numBeacon +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,beacon2)): numBeacon +=1
            #Glider
            if(checkFigure(i-1,j-1,N,M,auxGrid,glider1)): numGlider +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,glider2)): numGlider +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,glider3)): numGlider +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,glider4)): numGlider +=1
            #Light-weight spaceship
            if(checkFigure(i-1,j-1,N,M,auxGrid,lws1)): numLWS +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,lws2)): numLWS +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,lws3)): numLWS +=1
            if(checkFigure(i-1,j-1,N,M,auxGrid,lws4)): numLWS +=1
    sumTotal = numBlocks+numBeehive+numLoaf+numBoat+numBlinker+numToad+numBeacon+numTub+numGlider+numLWS
    f = open("output.txt","a")
    f.write("######################################### \n")
    f.write("Iteration:"+ str(frameNum)+ "\n\n")
    f.write("Block: "+ str(numBlocks) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numBlocks/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Beehive: "+ str(numBeehive) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numBeehive/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Loaf: "+ str(numLoaf) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numLoaf/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Boat: "+ str(numBoat) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numBoat/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Tub: "+ str(numTub) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numTub/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Blinker: "+ str(numBlinker) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numBlinker/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Toad: "+ str(numToad) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numToad/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Beacon: "+ str(numBeacon) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numBeacon/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Glider: "+ str(numGlider) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numGlider/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("LWS: "+ str(numLWS) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(numLWS/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Total: "+ str(sumTotal)+"\n")

    for i in range(N):
        for j in range(M):
            neighbors = 0
            for h in range(-1,2):
                for k in range(-1,2):
                    #check if im in bounds
                    if(i+h>= 0 and i+h <N and j+k>= 0 and j+k <M):
                        if(h!= 0 or k!= 0):
                            if(grid[i+h,j+k]==ON): neighbors +=1 
            if(grid[i,j]==ON):
                if(neighbors<2): newGrid[i,j]=OFF
                if(neighbors==2 or neighbors == 3): newGrid[i,j]=ON
                if(neighbors>3): newGrid[i,j]=OFF
            if(grid[i,j]==OFF):
                if(neighbors==3): newGrid[i,j]=ON
    
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments

    # set animation update interval
    updateInterval = 50

    with open('input5.txt', 'r') as file:
        input_lines = [line.strip() for line in file]
    x,y= input_lines.pop(0).split()
    x= int(x)
    y= int(y)
    global generations
    generations = input_lines.pop(0)
    generations = int(generations)
    # declare grid
    grid = np.array([])
    grid = np.zeros(x*y).reshape(x, y)

    #Put the initial settings
    for lines in input_lines:
        i,j = lines.split()
        i = int(i)
        j = int(j)
        addPoint(i,j,grid)
    
    ###############################
    # Output file
    f = open("output.txt","w")
    f.write("Simulation at "+ str(date.today())+ "\n")
    f.write("Universe size "+ str(x)+ " x "+ str(y)+"\n")
    f.close()

    #####################################################################
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, x, y),frames = generations, interval=updateInterval, save_count=50,repeat=False)
    plt.show()
    ####################################################################$$

# call main
if __name__ == '__main__':
    main()