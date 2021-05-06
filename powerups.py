import numpy as np
from variables import *
import colorama
from colorama import Fore, Back, Style
import time
colorama.init()
class Power:
    def __init__(self, x, y):
        self._x1 = 0
        self._y = 0
        



class catch(Power):
    def __init__(self,x,y,xs,ys):

        self.type = 'catch'
        self._char = Fore.RED + Back.CYAN + 'C'
        self.inity = y+1
        self._Y = y+1
        self._X = x
        self.active = 0
        self.temp = Back.BLACK + ' '
        self.t = 10000000
        self.spawned = 1
        self.xspeed = xs/2
        self.yspeed = ys
        self.tt = time.perf_counter()
    def spawn_catch(self,gamemap,paddle):
        
        if(self.spawned == 1 and self._Y <= rows-2):
            if((self._X + self.xspeed <= 1) or (self._X + self.xspeed >= 98) ):
                self.xspeed = -self.xspeed
         
            gamemap.grid[int(self._Y)][int(self._X)] = self.temp
            
            if(self._Y < rows-2 and self.spawned == 1):
                self._X += self.xspeed
                self._Y = self.inity - ((self.yspeed - 3*(time.perf_counter() - self.tt))*(time.perf_counter() - self.tt))
            self._X = int(self._X)
            self._Y = int(self._Y)
                
            
            self.temp = gamemap.grid[self._Y][self._X]
            gamemap.grid[self._Y][self._X] = self._char
            
            
            if(self._Y == rows - 2):
                gamemap.grid[self._Y][self._X] = Back.BLACK + " "
                self.delete_catch()
                
            if((self._Y == rows-3 or self._Y == rows-2) and self._X >=paddle.current_col and self._X <= paddle.current_col+11):
                self.active = 1
                self.t = gamemap.time
                self.delete_catch()
            
            
            
    def delete_catch(self):
        self.spawned = 0
        self._char = Back.YELLOW + " "
        self._X = 0
        self._Y = 0

class Shrink(Power):
    def __init__(self,x,y,xs,ys):

        self.type = 'shrink'
        self._char = Fore.GREEN + Back.RED + 'S'
        self._Y = y+1
        self._X = x
        self.active = 0
        self.temp = Back.BLACK + ' '
        self.t = 1000000
        self.spawned = 1
        self.shrunk = 0
        self.xspeed = xs/2
        self.yspeed = ys
        self.tt = time.perf_counter()
        self.inity = y+1
    def spawn_catch(self,gamemap,paddle):
        if(self.spawned == 1 and self._Y <= rows-2):
            if((self._X + self.xspeed <= 1) or (self._X + self.xspeed >= 98) ):
                self.xspeed = -self.xspeed
         
            gamemap.grid[int(self._Y)][int(self._X)] = self.temp
            
            if(self._Y < rows-2 and self.spawned == 1):
                self._X += self.xspeed
                self._Y = self.inity - ((self.yspeed - 3*(time.perf_counter() - self.tt))*(time.perf_counter() - self.tt))
            self._X = int(self._X)
            self._Y = int(self._Y)
                
            
            self.temp = gamemap.grid[self._Y][self._X]
            gamemap.grid[self._Y][self._X] = self._char
            
            
            if(self._Y == rows - 2):
                gamemap.grid[self._Y][self._X] = Back.BLACK + " "
                self.delete_catch()
                
            if((self._Y == rows-3 or self._Y == rows-2) and self._X >=paddle.current_col and self._X <= paddle.current_col+11):
                self.active = 1
                self.t = gamemap.time
                self.delete_catch()
            
            
    def delete_catch(self):
        self.spawned = 0
        self._char = Back.YELLOW + " "
        self._X = 0
        self._Y = 0    

class Expand(Power):
    def __init__(self,x,y,xs,ys):

        self.type = 'expand'
        self._char = Fore.GREEN + Back.WHITE + 'E'
        self._Y = y+1
        self._X = x
        self.active = 0
        self.temp = Back.BLACK + ' '
        self.t = 1000000
        self.spawned = 1
        self.expanded = 0
        self.xspeed = xs/2
        self.yspeed = ys
        self.tt = time.perf_counter()
        self.inity = y+1
    def spawn_catch(self,gamemap,paddle):
        if(self.spawned == 1 and self._Y <= rows-2):
            if((self._X + self.xspeed <= 1) or (self._X + self.xspeed >= 98) ):
                self.xspeed = -self.xspeed
         
            gamemap.grid[int(self._Y)][int(self._X)] = self.temp
            
            if(self._Y < rows-2 and self.spawned == 1):
                self._X += self.xspeed
                self._Y = self.inity - ((self.yspeed - 3*(time.perf_counter() - self.tt))*(time.perf_counter() - self.tt))
            self._X = int(self._X)
            self._Y = int(self._Y)
                
            
            self.temp = gamemap.grid[self._Y][self._X]
            gamemap.grid[self._Y][self._X] = self._char
            
            
            if(self._Y == rows - 2):
                gamemap.grid[self._Y][self._X] = Back.BLACK + " "
                self.delete_catch()
                
            if((self._Y == rows-3 or self._Y == rows-2) and self._X >=paddle.current_col and self._X <= paddle.current_col+11):
                self.active = 1
                self.t = gamemap.time
                self.delete_catch()
            
            
    def delete_catch(self):
        self.spawned = 0
        self._char = Back.YELLOW + " "
        self._X = 0
        self._Y = 0    


class Thru(Power):
    def __init__(self,x,y,xs,ys):

        self.type = 'thru'
        self._char = Fore.BLACK + Back.BLUE + 'T'
        self._Y = y+1
        self._X = x
        self.active = 0
        self.temp = Back.BLACK + ' '
        self.t = 1000000
        self.spawned = 1
        self.expanded = 0
        self.xspeed = xs/2
        self.yspeed = ys
        self.tt = time.perf_counter()
        self.inity = y+1
    def spawn_catch(self,gamemap,paddle):
       if(self.spawned == 1 and self._Y <= rows-2):
            if((self._X + self.xspeed <= 1) or (self._X + self.xspeed >= 98) ):
                self.xspeed = -self.xspeed
         
            gamemap.grid[int(self._Y)][int(self._X)] = self.temp
            
            if(self._Y < rows-2 and self.spawned == 1):
                self._X += self.xspeed
                self._Y = self.inity - ((self.yspeed - 3*(time.perf_counter() - self.tt))*(time.perf_counter() - self.tt))
            self._X = int(self._X)
            self._Y = int(self._Y)
                
            
            self.temp = gamemap.grid[self._Y][self._X]
            gamemap.grid[self._Y][self._X] = self._char
            
            
            if(self._Y == rows - 2):
                gamemap.grid[self._Y][self._X] = Back.BLACK + " "
                self.delete_catch()
                
            if((self._Y == rows-3 or self._Y == rows-2) and self._X >=paddle.current_col and self._X <= paddle.current_col+11):
                self.active = 1
                self.t = gamemap.time
                self.delete_catch()
            
            
    def delete_catch(self):
        self.spawned = 0
        self._char = Back.YELLOW + " "
        self._X = 0
        self._Y = 0

class Fast(Power):
    def __init__(self,x,y,xs,ys):

        self.type = 'fast'
        self._char = Fore.BLUE + Back.YELLOW + 'F'
        self._Y = y+1
        self._X = x
        self.active = 0
        self.temp = Back.BLACK + ' '
        self.t = 1000000
        self.spawned = 1
        self.expanded = 0
        self.xspeed = xs/2
        self.yspeed = ys
        self.tt = time.perf_counter()
        self.inity = y+1
    def spawn_catch(self,gamemap,paddle):
        if(self.spawned == 1 and self._Y <= rows-2):
            if((self._X + self.xspeed <= 1) or (self._X + self.xspeed >= 98) ):
                self.xspeed = -self.xspeed
         
            gamemap.grid[int(self._Y)][int(self._X)] = self.temp
            
            if(self._Y < rows-2 and self.spawned == 1):
                self._X += self.xspeed
                self._Y = self.inity - ((self.yspeed - 3*(time.perf_counter() - self.tt))*(time.perf_counter() - self.tt))
            self._X = int(self._X)
            self._Y = int(self._Y)
                
            
            self.temp = gamemap.grid[self._Y][self._X]
            gamemap.grid[self._Y][self._X] = self._char
            
            
            if(self._Y == rows - 2):
                gamemap.grid[self._Y][self._X] = Back.BLACK + " "
                self.delete_catch()
                
            if((self._Y == rows-3 or self._Y == rows-2) and self._X >=paddle.current_col and self._X <= paddle.current_col+11):
                self.active = 1
                self.t = gamemap.time
                self.delete_catch()
            
            
    def delete_catch(self):
        self.spawned = 0
        self._char = Back.YELLOW + " "
        self._X = 0
        self._Y = 0

class Gun(Power):
    def __init__(self,x,y,xs,ys):

        self.type = 'bullet'
        self._char = Fore.BLUE + Back.WHITE + 'G'
        self._Y = y+1
        self._X = x
        self.active = 0
        self.temp = Back.BLACK + ' '
        self.t = 1000000
        self.spawned = 1
        self.expanded = 0
        self.xspeed = xs/2
        self.yspeed = ys
        self.tt = time.perf_counter()
        self.inity = y+1
        self.tt
    def spawn_catch(self,gamemap,paddle):
        if(self.spawned == 1 and self._Y <= rows-2):
            if((self._X + self.xspeed <= 1) or (self._X + self.xspeed >= 98) ):
                self.xspeed = -self.xspeed
         
            gamemap.grid[int(self._Y)][int(self._X)] = self.temp
            
            if(self._Y < rows-2 and self.spawned == 1):
                self._X += self.xspeed
                self._Y = self.inity - ((self.yspeed - 3*(time.perf_counter() - self.tt))*(time.perf_counter() - self.tt))
            self._X = int(self._X)
            self._Y = int(self._Y)
               
            
            self.temp = gamemap.grid[self._Y][self._X]
            gamemap.grid[self._Y][self._X] = self._char
            
            
            if(self._Y == rows - 2):
                gamemap.grid[self._Y][self._X] = Back.BLACK + " "
                self.delete_catch()
                
            if((self._Y == rows-3 or self._Y == rows-2) and self._X >=paddle.current_col and self._X <= paddle.current_col+11):
                self.active = 1
                self.t = gamemap.time
                self.tt = gamemap.time
                self.delete_catch()
            
            
    def delete_catch(self):
        self.spawned = 0
        self._char = Back.YELLOW + " "
        self._X = 0
        self._Y = 0




            

