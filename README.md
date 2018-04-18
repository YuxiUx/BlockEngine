# BlockEngine
### Simple 2D engine in python.
_Originally created for HagridCraft_

Powerful grid&block system.

Features:
* automatic grid
* virtual position/size units. (you don't need to count pixels)
* callback based Event Listeners
* callback based "ticks". (given fn is called every render loop)
* Block - implements all basic features you may need.
  * absolute positioning
  * relative positioning
  * simple mapping keyboard to movement (just setup keys and register listener) for basic player.
  * automatic keep block in window. this function don't let block move out of window or configued area. When block collide with border return `"TOP","BOTTOM","LEFT","RIGHT"` status
  * etc.
* map
  * 3 layers (background color, background blocks(with textures), active layer(player, walls, etc.. go here))
  * optimized rendering
  * your own block types
* and more

Works great on old and lowend computers. Requires about 30MB RAM for fullHD
window and less than 1MB/5000 independent Blocks.  
_Our test - laptop: 1GB ram, Intel Atom x32, 1024x768 => 66>FPS>120)_.  
Good stability - when you render really much blocks at one time
(about `n * 100 000`) it's may take while (depends on computer), but OS or
game don't freeze, all interaction with game is stored in event queue.
Queue is processed imidetly after computation(render) is finished.  
(we noticed that many engines in this situation freeze and only thing you
 can do is force kill application before your computer freeze too.
 So we're trying make it better.)
_Our test with same hw - 1,000,000 of blocks with size 25x25px (it's like 33k image)._
 1 6
 3 20
 5 30

## Installation
Dependencies:
* python3
* pygame (actual version)
* numpy

Current best way to use BlockEngine:
1. fork this project
2. install dependence's
3. (remove examples - not necessary)
4. edit/update config as you need
5. now everything is ready

This is still prealpha version. Since first stable release is recommended way installation via pip

## About
Main part of this engine was created at one friendly dev night with some alcohol,
so theres can be some issues and strange code. But we believe there is no
bigger problem here because it works fine.