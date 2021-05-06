import numpy as np
from variables import *
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()
class Brick:
    def __init__(self, x, y):
        self._x1 = 0
        self._y = 0
    


class Brick_U(Brick):
    def __init__(self):

        self.type = 'U'
        self._char = [' ', ' ', ' ', ' ']
        self._Y = 3
        self._X = 3

       
        # super().__init__(x, y)

    
    def print_brick(self,gamemap,x,y):
        self._Y = y
        self._X = x
        self
        j = x
        for i in self._char:
            gamemap[y][j] = Back.BLUE + i
            j = j + 1

    def break_brick(self,gamemap,thru):
        
        j = self._X
        y = self._Y
        for i in self._char:
            gamemap.grid[y][j] = Back.BLACK + i
            j = j + 1
        self._X = 0
        self._Y = 0
        self._char = []
     
    
class Brick_3(Brick):
    def __init__(self):

        self.type = '3'
        self._char = [' ', ' ', ' ', ' ']
        self._Y = 3
        self._X = 3
       
        # super().__init__(x, y)

    
    def print_brick(self,gamemap,x,y):
        self._Y = y
        self._X = x
        j = x
        for i in self._char:
            gamemap[y][j] = Back.YELLOW + i
            j = j + 1

    def break_brick(self,gamemap,thru):
        
        j = self._X
        y = self._Y
        for i in self._char:
            gamemap.grid[y][j] = Back.BLACK + i
            j = j + 1
        self._X = 0
        self._Y = 0
        self._char = []
     

class Brick_2(Brick):
    def __init__(self):

        self.type = '2'
        self._char = [' ', ' ', ' ', ' ']
        self._Y = 3
        self._X = 3
       
        # super().__init__(x, y)

    
    def print_brick(self,gamemap,x,y):
        self._Y = y
        self._X = x
        j = x
        if(self.type == '2'):
            for i in self._char:
                gamemap[y][j] = Back.GREEN + i
                j = j + 1
        if(self.type == '3'):
            for i in self._char:
                gamemap[y][j] = Back.YELLOW + i
                j = j + 1

    def break_brick(self,gamemap,thru):
        if thru == 1:
            j = self._X
            y = self._Y
            for i in self._char:
                gamemap.grid[y][j] = Back.BLACK + i
                j = j + 1
            self._X = 0
            self._Y = 0
            self._char = []
        else:    
            if self.type == '3' :
                j = self._X
                y = self._Y
                for i in self._char:
                    gamemap.grid[y][j] = Back.BLACK + i
                    j = j + 1
                self._X = 0
                self._Y = 0
                self._char = []
            j = self._X
            y = self._Y
            self.type = '3'
            for i in self._char:
                gamemap.grid[y][j] = Back.YELLOW + i
                j = j + 1
     
class Brick_explode(Brick):
    def __init__(self):

        self.type = 'E'
        self._char = [' ', ' ', ' ', ' ']
        self._Y = 3
        self._X = 3
       
        # super().__init__(x, y)

    
    def print_brick(self,gamemap,x,y):
        self._Y = y
        self._X = x
        j = x
        for i in self._char:
            gamemap[y][j] = Back.RED + i
            j = j + 1

    def break_brick(self,gamemap,bricks):
        
        j = self._X
        y = self._Y
        for i in self._char:
            gamemap.grid[y][j] = Back.BLACK + i
            j = j + 1
        _X = self._X
        _Y = self._Y
        self._X = 0
        self._Y = 0
        self._char = []
        for brick in bricks :
            if(_X < brick._X and  brick._X - _X <=5   and _Y == brick._Y):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)
            if(_X > brick._X and _X  - brick._X <= 5   and _Y == brick._Y):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)
            if(_X > brick._X and _X  - brick._X <= 5   and _Y == brick._Y + 1):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)
            if(_X < brick._X and  brick._X - _X <=5   and _Y == brick._Y + 1):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)
            if(  abs(brick._X - _X) <=1   and _Y == brick._Y + 1):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)
            if(_X > brick._X and _X  - brick._X <= 5   and _Y == brick._Y - 1):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)
            if(_X < brick._X and  brick._X - _X <=5   and _Y == brick._Y - 1):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)
            if(  abs(brick._X - _X) <=1   and _Y == brick._Y - 1):
                if(brick.type != 'E'):
                    brick.break_brick(gamemap,1)
                else:
                    brick.break_brick(gamemap,bricks)

class Brick_R(Brick):
    def __init__(self):

        self.type = 'R'
        self._char = [' ', ' ', ' ', ' ']
        self._Y = 3
        self._X = 3
    
        # super().__init__(x, y)

    
    def print_brick(self,gamemap,x,y):
        self._Y = y
        self._X = x
        j = x
        if(self.type =='R'):
            col = [Back.GREEN + ' ',Back.BLUE + ' ',Back.YELLOW + ' ']
            cur = col[random.randint(0,2)]
            for i in self._char:
                gamemap[y][j] = cur
                j = j + 1
        if(self.type == '3'):
            
            for i in self._char:
                gamemap[y][j] = Back.YELLOW + i
                j = j + 1
        if(self.type == '2'):
            
            for i in self._char:
                gamemap[y][j] = Back.GREEN + i
                j = j + 1
        if(self.type == 'U'):
            
            for i in self._char:
                gamemap[y][j] = Back.BLUE + i
                j = j + 1

    def break_brick(self,gamemap,thru):
        arr = ['U','3','2']
        if(self.type == '2'):
            if thru == 1:
                j = self._X
                y = self._Y
                for i in self._char:
                    gamemap.grid[y][j] = Back.BLACK + i
                    j = j + 1
                self._X = 0
                self._Y = 0
                self._char = []
            else:    
                
                j = self._X
                y = self._Y
                self.type = '3'
                for i in self._char:
                    gamemap.grid[y][j] = Back.YELLOW + i
                    j = j + 1     
        if self.type == '3' :
            j = self._X
            y = self._Y
            for i in self._char:
                gamemap.grid[y][j] = Back.BLACK + i
                j = j + 1
            self._X = 0
            self._Y = 0
            self._char = []
        if self.type == 'U' :
            if thru == 1:
                j = self._X
                y = self._Y
                for i in self._char:
                    gamemap.grid[y][j] = Back.BLACK + i
                    j = j + 1
                self._X = 0
                self._Y = 0
                self._char = []
        if self.type == 'R' :
            if thru == 1:
                j = self._X
                y = self._Y
                for i in self._char:
                    gamemap.grid[y][j] = Back.BLACK + i
                    j = j + 1
                self._X = 0
                self._Y = 0
                self._char = []
            else:
                self.type = arr[random.randint(0,2)]

        