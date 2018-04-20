from blockengine import Block
from blockengine import Window
from blockengine import key
from blockengine import DirectDebugConsole
from blockengine.colors import *
from config.config import *
import config.engine as eng

'''
   1. Start this example
   2. On graphic window press K (pause game and open terminal input)
   3. Open terminal window
   4. just try to write something
   examples:
      s = 1		> increase speed
      cl = Green	> change color of left direction
      cr = Black	> change color of right direction
      pl1.Boost *= -1	> invert direction of top block (for bottom just use pl2)
      example()		> run example function
      pl1.Move(2,2)	> manualy move top block to position 2,2 on grid
      Or try anithing else include multiline input, but remember you still write python code so if you write
      $$: def MyNewFunction():
      $$: pl1.Boost *= -1
      $$: pl2.Boost *= -1
      $$: 
      you get only error(ident block), but 
      $$: def MyNewFunction():
      $$:    pl1.Boost *= -1
      $$:    pl2.Boost *= -1
      $$: 
      declare new function MyNewFunction that's invert direction of both blocks. this function can be caled like this
      $: MyNewFunction()      
      before writing another command press K on graphic window again.
      If you want to copy some code to console: 
         1) enable multiline mode 
         1) code can't start with blank line
         2) code can't contain blank line
       after blank line is code executed in singleline mode that means you need repeatly press K untill last line is processed.
       in future we try fix this
       
      console can interact with anithing inside of this file
      
'''

wi = Window(title="Debug example - press K", size=(900,700)) # create window


debug = DirectDebugConsole(key.k, locals(), locals()) # create debug console instance
# key - hotkey for open console input
# specify content - use of locals() give full access to everithing in this scope

# Register debug listener
wi.AddEvent("KEYDOWN", debug.Listener)

#==== example app ====
cl = Red
cr = Blue
s  = 0

pl1 = Block(Green, eng.block, position=(0,0), screen=wi.screen, limit=(35,27))
pl2 = Block(Green, eng.block, position=(35,27), screen=wi.screen, limit=(35,27))

def colise(border, obj):
    if border[0] == "RIGHT":
        obj.color = cl
        obj.Boost = -1
    else:
        obj.color = cr
        obj.Boost = 1
    # or you can simply change direction only using obj.Boost *= -1

def example():
    print("Hello")
    print("pl1: "+str(pl1))
        
pl1.OnColision = colise
pl2.OnColision = colise

def loop():
    pl1.Movr(1+s)
    pl1.Render()
    pl2.Movr(1+s)
    pl2.Render()
    
wi.AddLoop(loop)

wi.main()
