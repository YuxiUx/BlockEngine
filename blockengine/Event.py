import threading
from collections import deque
class EventListener():
    """
      This file is part of blockengine
      Code by YuxiUx
    """
    def __init__(self):
        self._events = []
        self._queue = deque()
        super(EventListener, self).__init__()
    def AddEventListener(self, etype, callback, options=''):
        callback._evopt = options
        fn = ["Event",etype,callback]
        self._events[etype].append(fn)
        return fn
    def RemoveEventListener(self, event_ref):
        self._events[event_ref[1]].remove(event_ref)
    def Run(self): #TODO: thrd too?
        while len(self._queue)>0: 
            ev = self._queue.popleft()
            for i in range(len(self._events[ev.type])):
                self._call(self._events[ev.type][i])
    def _call(self, callback): #TODO: some threading magic here
        callback[2]()
        if(callback[2]._evopt=="once"):
            self.RemoveEventListener(callback)
    def EmmitEvent(self, event):
        self._queue.append(event)
        
class EventType:
    """
      List of event types
      This file is part of blockengine
      Code by YuxiUx
    """
    KEYUP    = 1
    KEYDOWN  = 2
    KEYPRESS = 3
    MOUSEBUTTONDOWN = 4 
    #qwertzuiopasdfghjklyxcvbnm
    #abcdefghijklmnopqxwyz
    #abcdefghijklmnouprstuvwxzy
    