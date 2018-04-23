from blockengine import Block
from blockengine import Window
from blockengine.color import *

import config.engine as eng


wi = Window(title="Example - just render one block", size=(900,700))

bloc = Block(Blue, eng.block, (10,10), wi.screen)
bloc.Render()


wi.main() #or anorher type of loop

