''' COOMMENTS, this code is looped. The process is the spaceship getting gradually faster then entering 'hyperspace' and then flashing back to normal speed.
After this process the code continues looping. :3 
Also don't mind the variable names 
'''
import arcade
import random

#Drawing stars in random coordinates
def stars():
    for i in range(100):
        ax = random.randint(0,1501)
        ay = random.randint(0,751)
        arcade.draw_circle_filled(ax,ay,1,arcade.color.WHITE,1)

#Lines during the warp phase
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

#Drawing explosions
def explosion():
    arcade.draw_circle_filled(on_draw.x, on_draw.y, 300, arcade.color.RED, 10)
    arcade.draw_circle_filled(on_draw.x, on_draw.y, 150, arcade.color.YELLOW, 10)

''' Not needed 
def flash(hm):
    if hm == 1:
        arcade.draw_circle_filled(0,0,1000000000000,arcade.color.WHITE,1)
    elif hm == 0:
        arcade.draw_circle_filled(0,0,0,arcade.color.WHITE,1)
'''

#Declaring the variables
SPOOD = 0
SPEED = 5
b = 0
a = 1
space = 2
boom = 0

WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500

#Function to animate
def on_draw(delta_time):
    global SPEED
    global boom
    arcade.start_render()
    #Calling functions to draw scenery
    stars()
    spoceship(on_draw.x, on_draw.y)

    #Animating by adding a value to the x and y
    on_draw.x += SPEED
    on_draw.y += SPOOD

    #When the speed of the ship is more than 300, the speed lines function is called. If the speed of the ship is lower than 300, then the 'speed lines' go away.
    if SPEED > 300:
        speed_lines(1)
    elif SPEED < 300:
        speed_lines(0)


    if a%10 == 0:
        arcade.draw_circle_filled(0,0,1000000000000,arcade.color.BLACK,1)
        arcade.draw_text("hehe spooceship go brr", 600, 400, arcade.color.WHITE, 50, width=750, align="center", anchor_x="center", anchor_y="center")
        SPEED = 700
    
    if boom == 15:
        if on_draw.x >50:
            SPEED = 75
            explosion()
    elif boom != 15:
        if on_draw.x > WINDOW_LENGTH + 150:       
            on_draw.x = -250

        if on_draw.y > WINDOW_HEIGHT-100:
            on_draw.y = WINDOW_HEIGHT-100

        if on_draw.y < 100:
            on_draw.y = 100





on_draw.x = -200
on_draw.y = 0

class MyGame(arcade.Window):
    def __init__(self,width,height,title):

        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    
    #Function to detect the keyboard input
    def on_key_press(self, key, modifiers):
        global b
        global SPEED
        global speed_lines
        global a
        global boom
        global space

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
    MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/60)
    arcade.run()    



main()