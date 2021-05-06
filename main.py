from variables import *
import colorama
from colorama import Fore, Back, Style
import world
from input import *
from board import *
# from objects import shoot
# from game_over import *
import termios
# from check import *
import subprocess as sp
import time
import tty
import sys
import os
def clear():
    _ = os.system('clear')
timeout = 0.07
colorama.init()
gg = []
with open("win.txt", 'rb') as f:
    
    cnt = 0
    mx = -1
    for line in f:
        gg.append(line)
        mx = max(mx, len(gg[cnt]))
if __name__ == "__main__":
    
    clear()
    
    var = 1
    getch = Get()
    gamemap = world.World()
    gamemap.fill_grid()
    ufo = UFO(gamemap)
    board1 = Board(gamemap)
    temp = board1
    ball1 = Ball(gamemap)

    board_s = Board_small(gamemap)
    board_b = Board_Big(gamemap)
    bul = []
    prelaunch = 1
    os.system('stty -echo')
    t = time.perf_counter()
    while(1):
        sys.stdout.write("\033c")
        inputch = input_to(getch , timeout)
        if(gamemap.endgame == 1):
            break
        next_spawn = random.randint(0,len(board1._char))
        while(gamemap.pregame):
            sys.stdout.write("\033c")
            inputch1 = input_to(getch,timeout)
            
            gamemap.update_score(ball1.powerups)
            gamemap.print_grid()
            board1.print_board(gamemap)
            

            if(gamemap.boss == 1):
                ufo.print_ufo(gamemap,board1,ball1)
            j = 0
            for i in ball1.powerups:
                i.spawn_catch(gamemap,board1)
                # if(i.type == 'catch' and i.active == 1 ):
                    # next_spawn = ball1.spawn
                
                timeout = 0.07
                if(i.type == 'fast' and i.active == 1 ):
                    timeout = 0.03
                if(i.type == 'bullet' and i.active == 1 ):
                
                    if(time.perf_counter()- i.tt > 1):    
                        bul.append(Bullet(gamemap,board1))
                        i.tt = time.perf_counter()
                    for l in bul:
                        l.print_bullet(gamemap,board1)
                if(i.type == 'shrink' and i.active == 1 and i.shrunk == 0):
                    i.shrunk = 1
                    board_s.current_col = board1.current_col
                    board1 = board_s
                if(i.type == 'expand' and i.active == 1 and i.expanded == 0):
                    i.expanded = 1
                    board_b.current_col = board1.current_col
                    board1 = board_b
                if int(gamemap.time - i.t) >= 15 and i.type == 'shrink' :
                    temp.current_col = board1.current_col
                    board1 = temp
                if int(gamemap.time - i.t) >= 15 and i.type == 'expand' :
                    temp.current_col = board1.current_col
                    board1 = temp   

                if int(gamemap.time - i.t) >= 15:
                    if(i.type == 'bullet'):
                        for k in bul:
                            k.delete(gamemap) 
                        bul = []
                    i.active = 0
                    del(ball1.powerups[j])
                j+=1

            ball1.update_ball_pre(gamemap,board1,next_spawn)
            if inputch1 : 
               
                if inputch1 == "w" or inputch1 == "W" :
                    ball1.launch_ball(board1)
                    gamemap.pregame = 0
                if inputch1 == "n" or inputch1 == "N" :
                    gamemap.grid[ball1.current_row ][ball1.current_col] = Back.BLACK + ' '
                    gamemap.change_level(ball1)
                else :
                    board1.change_vel(inputch1) 
                    if(gamemap.boss == 1):
                        ufo.change_vel(inputch1)
                       
                
            
        while(gamemap.youwin == 1):

            gamemap.bric = []
            gamemap.brick_list = []
            gamemap.grid = []
            gamemap.fill_grid()
            while(1):    
                gamemap.print_grid()

                for i in range(len(gg)):
                    for j in range(len(gg[i])):
                        gamemap.grid[16 + i][1+ j] = chr(gg[i][j])
            

        if inputch : 
            if inputch == "q" or inputch == "Q" :
                break
            if inputch == "n" or inputch == "N" :
                gamemap.grid[ball1.current_row ][ball1.current_col] = Back.BLACK + ' '
                gamemap.change_level(ball1)
            
            else :
                board1.change_vel(inputch)
                if(gamemap.boss == 1):
                    ufo.change_vel(inputch)

        
        j = 0
        for i in ball1.powerups:
            i.spawn_catch(gamemap,board1)
            if(i.type == 'shrink' and i.active == 1 and i.shrunk == 0):
                i.shrunk = 1
                board_s.current_col = board1.current_col
                board1 = board_s
            
            timeout = 0.07
            if(i.type == 'fast' and i.active == 1 ):
                timeout = 0.03
            if(i.type == 'bullet' and i.active == 1 ):
                
                if(time.perf_counter()- i.tt > 1):    
                    bul.append(Bullet(gamemap,board1))
                    i.tt = time.perf_counter()
                for l in bul:
                    l.print_bullet(gamemap,board1)
                
            if(i.type == 'expand' and i.active == 1 and i.expanded == 0):
                i.expanded = 1
                board_b.current_col = board1.current_col
                board1 = board_b
            if int(gamemap.time - i.t) >= 15 and i.type == 'shrink' :
                temp.current_col = board1.current_col
                board1 = temp
            if int(gamemap.time - i.t) >= 15 and i.type == 'expand' :
                temp.current_col = board1.current_col
                board1 = temp   

            if int(gamemap.time - i.t) >= 15:
                if(i.type == 'bullet'):
                    for k in bul:
                        k.delete(gamemap) 
                    bul = []           
                i.active = 0
                del(ball1.powerups[j])
            j+=1
        #falling bricks
        if(int(gamemap.time) > 20 ):
            ball1.drop_bricks = 1
        else:
            ball1.drop_bricks = 0
        # //boss
        if(gamemap.boss == 1):
            ufo.print_ufo(gamemap,board1,ball1)
            

        gamemap.update_score(ball1.powerups)
        gamemap.print_grid()
        board1.print_board(gamemap)
        ball1.update_ball(gamemap,board1)
        # time.sleep(0.1)
os.system('stty echo')   
        
        

