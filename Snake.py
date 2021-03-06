from pygame.locals import *
from random import randint
import pygame
import time

black = (0, 0, 0)
white = (255, 255, 255)
 
class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
           
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
    def collision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
 
class App:
 
    display_width = 800
    display_height = 600
    player = 0
    apple = 0
 
    def __init__(self):
        self.running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3) 
        self.apple = Apple(5,5)
 
    def initiation(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.display_width,self.display_height), pygame.HWSURFACE)
 
        pygame.display.set_caption('Snake')
        self.running = True
        self._image_surf = pygame.image.load("pygame.png")
        self._apple_surf = pygame.image.load("apple.png")
 
    def event(self, event):
        if event.type == QUIT:
            self.running = False

    
         
 
    def loop(self):
        
        self.player.update()
 
        
        for i in range(0,self.player.length):
            if self.game.collision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1
               
                
 
 
        for i in range(2,self.player.length):
            if self.game.collision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                print("You lose! Collision: ")
                exit(0)
        pass
 
    def render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()
 
    def cleanup(self):
        pygame.quit()
 
    def execute(self):
        if self.initiation() == False:
            self.running = False
 
        while(self.running):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self.running = False
 
            self.loop()
            self.render()
 
            time.sleep (50.0 / 1000.0);
        self.cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.execute()
