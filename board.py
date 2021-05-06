import random
import numpy as np
from variables import *
import colorama
from colorama import Fore, Back, Style
from powerups import *
colorama.init()

def prob():
    a = random.randint(1,100)
    if(a > 0):
        return 1
    else:
        return 0
# Inheritence : Board , ball , brick are  inherited from object Class

class Object:
    def __init__(self, x, y):
        self._pos_x = 0
        self._pos_y = 0
        


class Board(Object):
    def __init__(self,gamemap):

       
        self._char = [' ', ' ', ' ', ' ',' ', ' ',' ',' ',' ',' ',' ']
        self.current_row = rows - 3
        self.current_col = 40
        self._lives = 3
        self._score = 0
        self._time = 100
        self._info = " "
       
        # super().__init__(x, y)

    
    def print_board(self,gamemap):
        for i in range(1,98):
            gamemap.grid[rows - 3][i] = Back.BLACK + ' '
        j = self.current_col
        for i in self._char:
            gamemap.grid[self.current_row][j] = Back.BLUE + i
            j = j + 1
    
    def change_vel(self, val):
        if(val == 'a' or val == 'A'):
            if(self.current_col > 2):
                self.current_col -= 2
        elif(val == 'd' or val == 'D'):
            if(self.current_col < columns - 13) :
                self.current_col += 2

class Board_small(Object):
    def __init__(self,gamemap):

       
        self._char = [' ', ' ', ' ', ' ',' ', ' ']
        self.current_row = rows - 3
        self.current_col = 40
        
        
        self._lives = 3
        self._score = 0
        self._time = 100
        self._info = " "
       
        # super().__init__(x, y)

    
    def print_board(self,gamemap):
        for i in range(1,98):
            gamemap.grid[rows - 3][i] = Back.BLACK + ' '
        j = self.current_col
        for i in self._char:
            gamemap.grid[self.current_row][j] = Back.BLUE + i
            j = j + 1
    
    def change_vel(self, val):
        if(val == 'a' or val == 'A'):
            if(self.current_col > 2):
                self.current_col -= 2
        elif(val == 'd' or val == 'D'):
            if(self.current_col < columns - 8) :
                self.current_col += 2

class Board_Big(Object):
    def __init__(self,gamemap):

       
        self._char = [' ', ' ', ' ', ' ',' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.current_row = rows - 3
        self.current_col = 40
        
        
        self._lives = 3
        self._score = 0
        self._time = 100
        self._info = " "
       
        # super().__init__(x, y)

    
    def print_board(self,gamemap):
        for i in range(1,98):
            gamemap.grid[rows - 3][i] = Back.BLACK + ' '
        j = self.current_col
        for i in self._char:
            gamemap.grid[self.current_row][j] = Back.BLUE + i
            j = j + 1
    
    def change_vel(self, val):
        if(val == 'a' or val == 'A'):
            if(self.current_col > 2):
                self.current_col -= 2
        elif(val == 'd' or val == 'D'):
            if(self.current_col < columns - 17) :
                self.current_col += 2



class Ball(Object):
    def __init__(self,gamemap):

       
        self._char = 'o'
        self.current_row = rows - 4
        self.current_col = 45
        
        gamemap.grid[self.current_row][self.current_col] = Fore.WHITE + self._char
        self.velx = 0
        self.vely = 0
        self.powerups = []
        self.thru = 0
        self.spawn = 0
        self.drop_bricks = 0
    def update_ball(self,gamemap,board):
        self.thru = 0
        for i in self.powerups:
                if(i.type == 'thru' and i.active == 1):
                    self.thru = 1
        for brick in gamemap.brick_list:
            if(self.current_col + self.velx >= brick._X and self.current_col + self.velx < brick._X + 4 and self.current_row + self.vely == brick._Y):
                if(self.thru == 0):
                    self.vely = -self.vely
                

                if(brick.type == 'U' and self.thru == 1):
                    brick.break_brick(gamemap,self.thru)

                if(brick.type != 'U'):
                    if(brick.type == '3' and prob()):
                        # pups = [Thru(brick._X+2,brick._Y,self.velx,self.vely),Shrink(brick._X+2,brick._Y,self.velx,self.vely),Expand(brick._X+2,brick._Y,self.velx,self.vely),catch(brick._X+2,brick._Y,self.velx,self.vely),Fast(brick._X +2,brick._Y,self.velx,self.vely),Gun(brick._X +2,brick._Y,self.velx,self.vely)]
                        v = random.randint(0,5)
                        # p = pups[v]
                        p = Gun(brick._X +2,brick._Y,self.velx,self.vely)
                        self.powerups.append(p)
                    if(brick.type != 'E'):
                        brick.break_brick(gamemap,self.thru)
                    else:
                        brick.break_brick(gamemap,gamemap.brick_list)
                    gamemap.score += 1
            
            if(( self.current_col + self.velx == brick._X or self.current_col + self.velx == brick._X + 4 )  and self.current_row  == brick._Y):
                if(self.thru == 0):
                    self.velx = -self.velx
                

                if(brick.type == 'U' and self.thru == 1):
                    brick.break_brick(gamemap,self.thru)

                if(brick.type != 'U'):
                    if(brick.type == '3' and prob()):
                        pups = [Thru(brick._X+2,brick._Y,self.velx,self.vely),Shrink(brick._X+2,brick._Y,self.velx,self.vely),Expand(brick._X+2,brick._Y,self.velx,self.vely),catch(brick._X+2,brick._Y,self.velx,self.vely),Fast(brick._X +2,brick._Y,self.velx,self.vely),Gun(brick._X +2,brick._Y,self.velx,self.vely)]
                        v = random.randint(0,5)
                        p = pups[v]
                        self.powerups.append(p)
                    if(brick.type != 'E'):
                        brick.break_brick(gamemap,self.thru)
                    else:
                        brick.break_brick(gamemap,gamemap.brick_list)
                    gamemap.score += 1
        
        if((self.current_col + self.velx <= 0) or (self.current_col + self.velx >= 98) ):
            self.velx = -self.velx
        if(self.current_row + self.vely <= 2):
            self.vely = -self.vely
        if((self.current_row + self.vely == rows - 3)  and (self.current_col + self.velx >= board.current_col) and (self.current_col + self.velx <= board.current_col + len(board._char))):
            if(self.current_col + self.velx - (board.current_col + int(len(board._char)/2)) == 2 ):
                self.velx = 1
            if(self.current_col + self.velx - (board.current_col + int(len(board._char)/2)) >= 5 ):
                self.velx = 2
            if(abs(self.current_col + self.velx - (board.current_col + int(len(board._char)/2))) == 3 ):
                self.velx = 1
            if(abs(self.current_col + self.velx - (board.current_col + int(len(board._char)/2))) == 4 ):
                self.velx = 1
            if(abs(self.current_col + self.velx - (board.current_col + int(len(board._char)/2))) == -1 ):
                self.velx = -1
            if(abs(self.current_col + self.velx - (board.current_col + int(len(board._char)/2))) < 2 ):
                self.velx = 0
            if(self.current_col + self.velx - (board.current_col + int(len(board._char)/2)) == -2 ):
                self.velx  = -1
            if(self.current_col + self.velx - (board.current_col + int(len(board._char)/2)) == -3 ):
                self.velx  = -1
            if(self.current_col + self.velx - (board.current_col + int(len(board._char)/2)) == -4 ):
                self.velx  = -1
            if(self.current_col + self.velx - (board.current_col + int(len(board._char)/2)) <= -5 ):
                self.velx  = -2
            for i in self.powerups:
                if(i.type == 'catch' and i.active == 1):
                    self.spawn = self.current_col
                    self.vely = 0
                    self.velx = 0 
                    gamemap.pregame = 1
        #fallinyg bricks
            self.vely = -self.vely
            if self.drop_bricks == 1:
                
                for b in gamemap.brick_list:
                    if(b._Y + 1 == rows -3):
                        gamemap.endgame = 1
                    j = b._X
                    for i in b._char:
                        gamemap.grid[b._Y ][j] = Back.BLACK + i
                        j = j + 1
                    b._Y = b._Y + 1
        
        #move the ball
        gamemap.grid[self.current_row][self.current_col] = Back.BLACK + " "     
        self.current_col = self.current_col + self.velx
        self.current_row = self.current_row + self.vely
        gamemap.grid[self.current_row][self.current_col] = Fore.WHITE + self._char
        
        #lost life
        if(self.current_row == rows - 1):
            gamemap.lives += -1
            if(gamemap.lives == 0):
                gamemap.endgame = 1
            gamemap.pregame = 1
            self.current_col = 5 + board.current_col
            self.current_row = rows -4
        
    
    
    
    def update_ball_pre(self,gamemap,board,x):
        
        gamemap.grid[self.current_row][self.current_col] = Back.BLACK + " "   
        self.current_row  = rows - 4  
        self.current_col =  board.current_col + x
        
        gamemap.grid[self.current_row][self.current_col] = Fore.WHITE + self._char
    
    def launch_ball(self,board):
        self.vely = -1
        if(self.current_col  - (board.current_col + 5) == 2 ):
            self.velx = 1
        if(self.current_col  - (board.current_col + 5) == 5 ):
            self.velx = 2
        if(abs(self.current_col  - (board.current_col + 5)) == 3 ):
            self.velx = 1
        if(abs(self.current_col  - (board.current_col + 5)) == 4 ):
            self.velx = 1
        if(abs(self.current_col  - (board.current_col + 5)) == -1 ):
            self.velx = -1
        if(abs(self.current_col  - (board.current_col + 5)) < 2 ):
            self.velx = 0
        if(self.current_col  - (board.current_col + 5) == -2 ):
            self.velx  = -1
        if(self.current_col  - (board.current_col + 5) == -3 ):
            self.velx  = -1
        if(self.current_col  - (board.current_col + 5) == -4 ):
            self.velx  = -1
        if(self.current_col  - (board.current_col + 5) == -5 ):
            self.velx  = -2
    



class Bullet(Object):
    def __init__(self,gamemap,board):

       
        self._char = ['^']
        self.current_row = rows - 4
        self.current_col = int(board.current_col+(len(board._char)/2))
        self.vel = 1
        self.temp = Back.BLACK + " "
       
       
        # super().__init__(x, y)

    
    def print_bullet(self,gamemap,board):
        for brick in gamemap.brick_list:
            if(self.current_col  >= brick._X and self.current_col < brick._X + 4 and self.current_row - 1 == brick._Y):
                if(brick.type != 'U'):
                    
                    if(brick.type != 'E'):
                        brick.break_brick(gamemap,0)
                    else:
                        brick.break_brick(gamemap,gamemap.brick_list)
                    gamemap.score += 1
                gamemap.grid[self.current_row][self.current_col] = self.temp
                self._char = [' ']
                self.vel = 0
                self.current_col = 0
    
        if(self.current_row  < 4 ):
            gamemap.grid[self.current_row][self.current_col] = self.temp
            self._char = [' ']
            self.vel = 0
            self.current_col = 0
        else:
            gamemap.grid[self.current_row][self.current_col] = self.temp

            self.current_row -= self.vel

        self.temp =  gamemap.grid[self.current_row][self.current_col]
        j = self.current_col
        for i in self._char:
            gamemap.grid[self.current_row][j] = Back.WHITE + Fore.BLUE + i
            j = j + 1
    def delete(self,gamemap):
        gamemap.grid[self.current_row][self.current_col] = self.temp
        self._char = [' ']
        self.vel = 0
        self.current_col = 0

class UFO(Object):
    def __init__(self,gamemap):
        self._char = []
        
       
        self._health = 9
        a = [' ', ' ', ' ', '.','-', '-','-','.',' ',' ',' ']
        b = [' ', '_', '/', '_','_', '~','0','_','\\','_',' ']
        c = ['(', '_', '_', '_','_', '_','_','_','_','_',')',' ']
        self._char.append(a)
        self._char.append(b)
        self._char.append(c)
        self.current_row =  5
        self.current_col = 40
        
        
        
        self._score = 0
        self._time = 100
        self._info = " "
        self.t = 0
        self.bombs = []
        # super().__init__(x, y)

    
    def print_ufo(self,gamemap,board,ball):
        self.current_col = board.current_col
        self._char[0][10] = str(self._health)
        for k in range(3):    
            for i in range(len(self._char[0]) + 4):
                gamemap.grid[k + 5][self.current_col + i - 2] = Back.BLACK + ' '
        j = self.current_col
        for i in range(len(self._char)):
            for j in range(len(self._char[i])):
                gamemap.grid[self.current_row + i][self.current_col + j] = Back.BLACK + self._char[i][j]
        if(gamemap.time - self.t > 3):
            self.bombs.append(Bomb(gamemap,board))
            self.t = gamemap.time
        for b in self.bombs:
            b.print_bomb(gamemap,board)
        if((ball.current_row + ball.vely <=  7)  and (ball.current_col + ball.velx >= board.current_col) and (ball.current_col + ball.velx <= board.current_col + len(board._char))):
            ball.vely = -ball.vely
            self._health -= 1
            if self._health == 0:
                gamemap.youwin = 1

        
        # coll


            
    
    def change_vel(self, val):
        x = 1
        # if(val == 'a' or val == 'A'):
        #     if(self.current_col > 2):
        #         self.current_col -= 2
        # elif(val == 'd' or val == 'D'):
        #     if(self.current_col < columns - 17) :
        #         self.current_col += 2


class Bomb(Object):
    def __init__(self,gamemap,board):

       
        self._char = ['O']
        self.current_row = 6
        self.current_col = int(board.current_col+(len(board._char)/2))
        self.vel = -1
        self.temp = Back.BLACK + " "
       
       
        # super().__init__(x, y)

    
    def print_bomb(self,gamemap,board):
        
        if(self.current_col  >= board.current_col and self.current_col < board.current_col + len(board._char) and self.current_row + 1 == rows-3):
            gamemap.lives -= 1
            gamemap.grid[self.current_row][self.current_col] = self.temp
            self._char = [' ']
            self.vel = 0
            self.current_col = 0
    
        if(self.current_row  > rows-3 ):
            gamemap.grid[self.current_row][self.current_col] = self.temp
            self._char = [' ']
            self.vel = 0
            self.current_col = 0
        else:
            gamemap.grid[self.current_row][self.current_col] = self.temp

            self.current_row -= self.vel

        self.temp =  gamemap.grid[self.current_row][self.current_col]
        j = self.current_col
        for i in self._char:
            gamemap.grid[self.current_row][j] =  Fore.RED + i
            j = j + 1
    def delete(self,gamemap):
        gamemap.grid[self.current_row][self.current_col] = self.temp
        self._char = [' ']
        self.vel = 0
        self.current_col = 0