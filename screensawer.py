import random
#random testing shits
def example(event):
    for i in range(0,1000):
        backgre = Block(randomcolor(), eng.block, (random.randint(0,50),random.randint(0,28)), wi.screen)
        backgre.Render()
        #ramexploder.append(backgre)
    print("Sy debylni? nemackej tu klavesu")
def randomcolor():
    r = round(random.randint(0,255))
    g = round(random.randint(0,255))
    b = round(random.randint(0,255))
    return (r,g,b)

def example2(event):
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

def sporic():
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
########################################

from blockengine import Block
from blockengine import Window
from blockengine import key
from blockengine.colors import *

#from config.colors import *
from config.config import *
import config.engine as eng

wi = Window(title="HagridCraft in PYGame", size=Window.MAXIMIZED)
ramexploder = []

#wi.Shapes=(0,0)

backg = Block(Blue, eng.block, (0,0), wi.screen)
backg2 = Block(White, eng.block, (40,20), wi.screen)
backg3 = Block((0,127,255), eng.block, (30,30), wi.screen)

pl = Block(Red, eng.block, position=(0,0), screen=wi.screen, backg=backg, limit=(50,28))
pl2 = Block(Green, eng.block, position=(40,20), screen=wi.screen, backg=backg2, limit=(50,28))
pl3 = Block((75,75,75), eng.block, position=(30,30), screen=wi.screen, backg=backg3, limit=(50,28))

pl.MapKeyboard(up=key.w, down=key.s, left=key.a, right=key.d)
pl2.MapKeyboard(up=key.UP, down=key.DOWN, left=key.LEFT, right=key.RIGHT)



backg3 = Block(Blue, eng.block, (10,10), wi.screen)
backg3.Render()

wi.AddEvent("KEYDOWN", example)
wi.AddEvent("MOUSEBUTTONDOWN", example2)
wi.AddEvent("QUIT", bye)
wi.AddEvent("KEYDOWN", pl.lisner)
wi.AddEvent("KEYDOWN", pl2.lisner)

wi.AddLoop(sporic)
wi.AddLoop(frn)


wi.main()
