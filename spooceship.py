#NOTES MAKE THE GAME MECHANIC COLLECTABLES DURING CLASS OR SMTHN IDK MAAAAAN
#importing the 'arcade' package and 'random' package
import arcade
import random

#Drawing stars in random coordinates
def stars():
    for i in range(100):
        ax = random.randint(0,1501)
        ay = random.randint(0,751)
        arcade.draw_circle_filled(ax,ay,1,arcade.color.WHITE,1)


#Lines during the 'warp phase'
def speed_lines(wow):
        if wow == 1:
            for i in range(100):
                x1 = random.randint(0,1501)
                y1 = random.randint(0,751)
                arcade.draw_line(x1, y1, x1+50 ,y1, arcade.color.WHITE_SMOKE, 2)
        else:
            arcade.draw_line(900, 900, 900 ,900, arcade.color.BLACK, 1)


#Drawing the spooceship
def spoceship(x,y):
    arcade.draw_rectangle_filled(x, y, 200, 100, arcade.color.RED)
    arcade.draw_triangle_filled(x, y+50, x-150, y+150, x-100, y+50, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x, y-50, x-150, y-150, x-100, y-50, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x+100, y+50, x+200, y, x+100, y-50, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(x+50,y,40,arcade.color.WHITE,1)
    arcade.draw_circle_filled(x+50,y,25,arcade.color.AQUA,1)

    fire_inside_point_list = ((x-100,y+50), (x-150,y+25), (x-130,y+10), (x-160,y), (x-140,y-15), (x-125,y-25), (x-120,y-35), (x-140,y-45), (x-100,y-50))
    arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)


#Drawing the explosion
def explosion():
    arcade.draw_circle_filled(on_draw.x, on_draw.y, 300, arcade.color.RED, 10)
    arcade.draw_circle_filled(on_draw.x, on_draw.y, 150, arcade.color.YELLOW, 10)

def objective(obj_x, obj_y):
    arcade.draw_circle_filled(obj_x,obj_y,20, arcade.color.RED,1)



#Declaring the variables
SPOOD = 0
SPEED = 5
b = 0
a = 1
space = 2
boom = 0


WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500


#Function for animating
def on_draw(delta_time):
    #access global variables in this function
    global SPEED
    global boom
    arcade.start_render()
    #Calling functions to draw scenery
    stars()
    spoceship(on_draw.x, on_draw.y)
    objective(on_draw.obj_x, on_draw.obj_y)

    #Animating by adding value to the x and y
    on_draw.x += SPEED
    on_draw.y += SPOOD
    on_draw.obj_x -= SPEED

    #conditional: when the speed of the ship is more than 300, the speed_lines function is called.
    #If the speed of the ship is lower than 300, then the speed_lines are gone.
    if SPEED > 300:
        speed_lines(1)
    else:
        speed_lines(0)


    #conditionals: if a (counter of key 'o') is divisible by 10, cover screen with black circle and add text, "hehe spooceship go brr" then set speed to 700
    if a%10 == 0:
        arcade.draw_circle_filled(0,0,1000000000000,arcade.color.BLACK,1)
        arcade.draw_text("hehe spooceship go brr", 600, 400, arcade.color.WHITE, 50, width=750, align="center", anchor_x="center", anchor_y="center")
        SPEED = 700
    
    #conditionals: if boom (counter of key 'e') if on_draw.x is bigger than 50, set speed to 75 then call explosion function. 
    if boom == 15:
        if on_draw.x >50:
            SPEED = 75
            explosion()
    else:
        if on_draw.x > WINDOW_LENGTH + 150:       
            on_draw.x = -250

        if on_draw.y > WINDOW_HEIGHT-100:
            on_draw.y = WINDOW_HEIGHT-100

        if on_draw.y < 100:
            on_draw.y = 100
        
        if on_draw.obj_x <= 10:
            on_draw.obj_x = 1500
            on_draw.obj_y = random.randint(0,751)


on_draw.x = -200
on_draw.y = 0
on_draw.obj_x = 1500
on_draw.obj_y = random.randint(0,751)

class MyGame(arcade.Window):
    #setting the screen
    def __init__(self,width,height,title):

        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    
    #function for user input
    def on_key_press(self, key, modifiers):
        global b
        global SPEED
        global speed_lines
        global a
        global boom
        global space

        #this code speaks for itself (?)
        if key == arcade.key.UP or key == arcade.key.W:
            on_draw.y += 20

        elif key == arcade.key.DOWN or key == arcade.key.S:
            on_draw.y += -20

        if key == arcade.key.RIGHT or key == arcade.key.D:
            SPEED *= 1.5
            if SPEED > 700:
                SPEED = 700

        elif key == arcade.key.LEFT or key == arcade.key.A:
            SPEED /= 1.3

        if key == arcade.key.O:
            a += 1
            print(a)
        
        if key == arcade.key.E:
            boom += 1
            print(boom)

        if key == arcade.key.SPACE:
            space += 1
            if space%2 == 1:
                SPEED = 0
            elif space%2 == 0:
                SPEED = 10

def main():
    #Set canvas then run
    MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/60)
    arcade.run()    


#Call main function to run
main()