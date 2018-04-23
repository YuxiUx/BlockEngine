import random
from blockengine import Block
from blockengine import Window
from blockengine import key
from blockengine.color import *

from config.config import *
import config.engine as eng

#create window
wi = Window(title="'Screensawer' - random move - press mouse button or any key", size=Window.MAXIMIZED)

#define blocks 
backg = Block(Blue, eng.block, (0,0), wi.screen)
backg2 = Block(White, eng.block, (40,20), wi.screen)
backg3 = Block((0,127,255), eng.block, (30,30), wi.screen)

pl = Block(Red, eng.block, position=(0,0), screen=wi.screen, backg=backg, limit=(50,28))
pl2 = Block(Green, eng.block, position=(40,20), screen=wi.screen, backg=backg2, limit=(50,28))
pl3 = Block((75,75,75), eng.block, position=(30,30), screen=wi.screen, backg=backg3, limit=(50,28))

#============ "SCREENSAVER" ============
def sawer():
    r = round(random.randint(-3,3))
    u = round(random.randint(-2,2))
    pl.Movr(r,u)
    pl.Render()
    b = round(random.randint(-2,2))
    i = round(random.randint(-4,4))
    pl2.Movr(b,i)
    pl2.Render()
    b = round(random.randint(-2,2))
    i = round(random.randint(-3,3))
    pl3.Movr(b,i)
    pl3.Render()

wi.AddLoop(sawer)


#helper
def randomcolor():
    r = round(random.randint(0,255))
    g = round(random.randint(0,255))
    b = round(random.randint(0,255))
    return (r,g,b)

#========= SOME EXAMPLE EVENTS =========
def Boooom(event): #render 1000 blocks on random position with random color.
    #Can be used as preformance test. change to bigger number 
    if event.key != key.PRINT:
        for i in range(0,1000):
            backgre = Block(randomcolor(), eng.block, (random.randint(0,50),random.randint(0,28)), wi.screen)
            backgre.Render()
        #just sample output. In memmory to our teacher. (read with russian/ucraine accent)
        print("Sy debylni? nemackej tu klavesu")  

def changeColors(event): 
    pl.color = randomcolor()
    pl2.color = randomcolor()
    pl3.color = randomcolor()
    backg.color = randomcolor()
    backg2.color = randomcolor()
    backg3.color = randomcolor()

def bye(event):
    print("do svidania")

def frn():
    print("Actual FPS: "+str(wi.getCurrFps()))


wi.AddEvent("KEYDOWN", Boooom)
wi.AddEvent("MOUSEBUTTONDOWN", changeColors)
wi.AddEvent("QUIT", bye)
#wi.AddLoop(frn)



wi.main()
