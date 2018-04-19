import pygame
import datetime
import blockengine.key as key
class Window:
    """
      Main aplication window wraper
      This file is part of blockengine
      Code by YuxiUx
    """
    MAXIMIZED = [0,0]
    def __init__(self, size=[1280, 720], title="Block Engine window", FPS = 30, autoscreanshot=True):
        pygame.init()
        self._title = None
        self._shapes = None
        self.screen = None
        self.Fps = FPS
        self._fpslast = 0
        self.fpsClock = pygame.time.Clock()
        self._changes = True
        self._shotkey = None
        self.stop = False

        self.Shapes = size
        self.Title = title

        self._events = {
            "QUIT": [],
            "KEYUP": [],
            "KEYDOWN": [],
            "MOUSEBUTTONDOWN" : []
        }
        self._lops = []
        if autoscreanshot:
           self.AddEvent("KEYDOWN", self._autoshot)
    @property
    def Title(self):
        return self._title
    @Title.setter
    def Title(self, title):
        self._title = title
        pygame.display.set_caption(title)
    @property
    def Shapes(self):
        return self._shapes
    @Shapes.setter
    def Shapes(self, shape):
        self._shapes = shape
        self.screen = pygame.display.set_mode(shape)
    def getCurrFps(self):
        if self._fpslast == 0:
            return 0
        else:
            return 1000/self._fpslast 
    def handleQuit(self, event):
        if event.type == pygame.QUIT:
            self.Quit()
    def updateDisplay(self):
        if self._changes:
            pygame.display.update()
    def Quit(self):
        self.stop = True
    def main(self):
        while not self.stop:
            for event in pygame.event.get():
                self.handleQuit(event)
                if self.stop:
                    self.handleEvents(event, "QUIT")
                    pygame.display.quit()
                else:
                    if event.type == pygame.KEYUP:
                        self.handleEvents(event, "KEYUP")
                    else:
                        if event.type == pygame.KEYDOWN:
                            self.handleEvents(event, "KEYDOWN")
                        else:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                self.handleEvents(event, "MOUSEBUTTONDOWN")
            self.loopLoop(self._lops)
            self.updateDisplay()
            self._fpslast = self.fpsClock.tick(1000/self.Fps)
    def handleEvents(self, event, type):
        if type in self._events:
            for eve in self._events[type]:
                eve(event)
    def loopLoop(self, arr):
        for loo in arr:
            loo()
    def AddEvent(self, eventtype, fn):
        self._events[eventtype].append(fn)
    def AddLoop(self, fn):
        self._lops.append(fn)
    def SaveScrean(self, name=False, path="screenshots"):
        if name == False:
            name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        pat = path + "/" + name + ".jpeg"
        try:
            pygame.image.save(self.screen, pat)
            print("Screen saved as "+str(pat))
        except:
            print("Falied to save " + str(pat))
            print("First check your path above. All florder must be created first")
        
    def _autoshot(self, event):
        if event.key == key.PRINT:
            self.SaveScrean()
