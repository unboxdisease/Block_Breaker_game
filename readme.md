# BRICK SMASHER
##### kushal Jain 2019111001
## Introduction 

It is an arcade brick samshing game built in Python3 without any major external libraries using only ascii characters. The player will be using paddle with a bouncing ball to smash bricks and increase scores.You loose a life when the ball touches the ground below the paddle.

## Screenshots
![brick smasher](https://user-images.githubusercontent.com/56218470/175813080-95d88be9-0738-433e-83a8-7fdd5450e8cf.png)

## OOPS CONCEPTS 

#### Inheritence 
There is one main brick class and different types of bricks which have different colours are inherited from it similarly for objects and powerups.

### Polymorphism
All the child classes of the Brick class have functions with same names Break_Brick() and print_brick(),similarly all powerups have spawn_catch() and delete_catch().

### Encapsulation 
Class and Object based approach is used for all the functionalities implemented in the game  

### Abstraction 
Intitutive Functionality is used where required , such as break_brick(), delete_powerup() , .

## Quick - Game Guide 
### Paddle :
- Press 'a' and 'd' to move the paddle horizontally 
- Press 'w' to release the ball
### Bricks :
There are 4 different types of bricks, here is the color guide:
- yellow  - Bricks with health 1
- Green - Bricks with health 2
- Blue - Unbreakable Bricks
- Red - Exploding Bricks

### Score and Time :
 - 1 Score is added on every time the ball collides with bricks/not when bricks explode (since that requires no skill)
 - Time is calculated from the start of the game
 - There are initially 5 lives , you loose a life when ball touches the ground.

 ### Powerups :
 - There are 5 types of powerups ('Catch','expand','shrink','fast ball','thru ball'), there is a 50% chance of a random powerup falling after brick breaks . They last for 15 seconds and are not lost with a loss of a life . Game quits when all lives are finished. (or when q is pressed)
