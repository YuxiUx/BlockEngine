from blockengine import Block
from blockengine import Window
from blockengine import key
from blockengine import color as c

import config.engine as eng


wi = Window(title="Example window - pres ASWD or <v^>", size=(900,700))


backg1 = Block(c.Blue, eng.block, (0,0), wi.screen)
backg2 = Block(c.White, eng.block, (35,27), wi.screen)

pl1 = Block(c.Red, eng.block, position=(0,0), screen=wi.screen, backg=backg1, limit=(35,27))
pl2 = Block(c.Green, eng.block, position=(35,27), screen=wi.screen, backg=backg2, limit=(35,27))

pl1.MapKeyboard(up=key.w, down=key.s, left=key.a, right=key.d) #or just (key.w, key.s, key.a, key.d)
pl2.MapKeyboard(up=key.UP, down=key.DOWN, left=key.LEFT, right=key.RIGHT)

wi.AddEvent("KEYDOWN", pl1.lisner)
wi.AddEvent("KEYDOWN", pl2.lisner)

wi.main()