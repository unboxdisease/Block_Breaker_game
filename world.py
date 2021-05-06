import numpy as np
from variables import *
import colorama
from colorama import Fore, Back, Style
from bricks import *
colorama.init()
import time

class World :
    def __init__(self):
        self.rows = rows
        self.columns = columns
        self.grid = []
        self.bric = []
        with open("b.txt", 'rb') as f:
            for line in f:
                self.bric.append(line)
        f.close()
        self.brick_list = []
        self.score = 0
        self.time = 0
        self.lives = 5
        self.pregame = 1
        self.endgame = 0
        self.level = 1
        self.t = time.perf_counter()
        self.boss = 0
        self.youwin = 0
    def fill_grid(self):
        self.grid = []
        
        

        for i in range(self.rows):
            arr = []
            for j in range(self.columns):
                if j == 0 or j == self.columns - 1 or i==2 or i==self.rows -1:     
                    arr.append(Back.WHITE + Fore.RED + " ")
                elif i <=1:
                    arr.append(Back.YELLOW + Fore.RED + " ")
                else:
                    
                    arr.append(Back.BLACK + Fore.RED + " ")
            self.grid.append(arr)
        # print(str(self.grid[0][0]))
        
        height = len(self.bric)
        count = 0
        for i in range(height):
            for j in range(len(self.bric[i])-1):
                if(chr(self.bric[i][j]) == 'U'):
                    self.brick_list.append( Brick_U() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == '3'):
                    self.brick_list.append( Brick_3() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == '2'):
                    self.brick_list.append( Brick_2() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == 'E'):
                    self.brick_list.append( Brick_explode() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == 'R'):
                    self.brick_list.append( Brick_R() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1

    def update_score(self , powerups):
        self.time =  (time.perf_counter() - self.t )
        scoree = ["S","C","O","R","E", ":" , str(self.score)," "," "," "," ","T",'I','M','E',':',str(int(int(self.time)/10)),str(int(self.time)%10)," "," "," ","L","E",'V','E','L',':',str(self.level) ]
        k = 0
        for i in scoree:
            self.grid[0][k+42] = Back.YELLOW + i
            k+=1
        k =0 
        for i in  range(30):
            self.grid[1][i+40] = Back.YELLOW + ' '
        for i in range(self.lives):
            self.grid[1][k+42] = Back.YELLOW + 'o'
            self.grid[1][k+43] = Back.YELLOW + ' '
            self.grid[1][k+44] = Back.YELLOW + ' '
            k+=3
        k = 0
        for i in powerups:
            if(i.active == 1):
                self.grid[1][k+62] = Back.YELLOW + 'P'
                self.grid[1][k+63] = Back.YELLOW + ' '
                self.grid[1][k+64] = Back.YELLOW + ' '
                k+=3
        

    def change_level(self,ball):
        
        self.grid = []
        self.level += 1
        self.t = time.perf_counter()
        ball.powerups = []
        #new grid
        for i in range(self.rows):
            arr = []
            for j in range(self.columns):
                if j == 0 or j == self.columns - 1 or i==2 or i==self.rows -1:     
                    arr.append(Back.WHITE + Fore.RED + " ")
                elif i <=1:
                    arr.append(Back.YELLOW + Fore.RED + " ")
                else:
                    
                    arr.append(Back.BLACK + Fore.RED + " ")
            self.grid.append(arr)
        
        
        self.bric = []
        self.brick_list = []
        if(self.level == 2):
            with open("c.txt", 'rb') as f:
                for line in f:
                    self.bric.append(line)
        if(self.level == 3):
            self.boss = 1
            with open("final.txt", 'rb') as f:
                for line in f:
                    self.bric.append(line)
        height = len(self.bric)
        count = 0
        for i in range(height):
            for j in range(len(self.bric[i])-1):
                if(chr(self.bric[i][j]) == 'U'):
                    self.brick_list.append( Brick_U() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == '3'):
                    self.brick_list.append( Brick_3() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == '2'):
                    self.brick_list.append( Brick_2() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == 'E'):
                    self.brick_list.append( Brick_explode() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
                if(chr(self.bric[i][j]) == 'R'):
                    self.brick_list.append( Brick_R() )
                    self.brick_list[count].print_brick(self.grid,3+j,5+i)
                    count += 1
        self.pregame = 1
        


                    
    
    def print_grid(self):
        for i in range(self.rows):
            arr = []
            for j in range(self.columns):
                if j == 0 or j == self.columns - 1 or i==2 or i==self.rows -1:     
                    self.grid[i][j] = Back.WHITE + " "
        
        #update bricks
        for b in self.brick_list:
            
            b.print_brick(self.grid,b._X,b._Y)
            

        stri = ""
        # print(self.grid[0][0])
        for i in range(self.rows):
            for j in range(self.columns):
                # print(self.grid[0][0])
                stri += self.grid[i][j]
            stri += "\n"
        print("\033[H" + stri , end="" )
    