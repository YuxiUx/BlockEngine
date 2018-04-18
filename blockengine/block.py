import pygame
class Block:
    """ Code by YuxiUx for HagridCraft
    """
    def __init__(self,color,size,position, screen, limit=(False,False), backg=False):
        self.ox, self.oy = position
        self.x, self.y = position
        self.w, self.h = size
        self.color = color
        self.backg = backg
        self.screen = screen
        self.rek=pygame.rect.Rect((self.x*self.w,self.y*self.h,self.w,self.h))
        self.maxX, self.maxY = limit
        self.ColidStat = []
        self.Boost = 1
        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False
    def Move(self,x=0,y=0):
        self.x = x
        self.y = y
        self.validPos()
    def Movr(self,x=0,y=0):
        self.x += x
        self.y += y
        self.validPos()
    def recountPos(self):
        x = self.x - self.ox
        y = self.y - self.oy
        self.ox, self.oy = self.x, self.y
        x = x*self.w
        y = y*self.h
        return x,y
    def Render(self, replacement=False):
        self.Replace(replacement)
        self.rek.move_ip(self.recountPos())
        pygame.draw.rect(self.screen, self.color, self.rek)
    def Replace(self, obj=False):
        if(obj==False):
            obj = self.backg
        if(obj!=False):
            obj.Move(self.ox,self.oy)
            obj.Render()
    def __str__(self):
        return "X:"+str(self.x)+"Y:"+str(self.y)+str(self.ColidStat)
    def validPos(self):
        stat = []
        if(self.x<0):
            self.x = 0
            stat.append("LEFT")
        if(self.y<0):
            self.y = 0
            stat.append("TOP")
        if(self.maxX!=False):
            if(self.x>self.maxX):
                self.x = self.maxX
                stat.append("RIGHT")
        if(self.maxY!=False):
            if(self.y>self.maxY):
                self.y = self.maxY
                stat.append("BOTTOM")
        self.ColidStat = stat
    def MapKeyboard(self, up=False, down=False, left=False, right=False):
        self.key_up = up
        self.key_down = down
        self.key_left = left
        self.key_right = right
    def lisner(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_right:
                self.Movr(1*self.Boost)
            if event.key == self.key_down:
                self.Movr(0,1*self.Boost)
            if event.key == self.key_left:
                self.Movr(-1*self.Boost)
            if event.key == self.key_up:
                self.Movr(0,-1*self.Boost)
            self.Render()
