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
def speed_lines():
        for i in range(100):
            x1 = random.randint(0,1501)
            y1 = random.randint(0,751)
            arcade.draw_line(x1, y1, x1+50 ,y1, arcade.color.WHITE_SMOKE, 2)


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


#Declaring the variables
SPOOD = 0
SPEED = 5


WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500


#Function for animaring
def on_draw(delta_time):
    #access global variables in this function
    global SPEED
    global SPOOD
    arcade.start_render()
    #Calling functions to draw scenery
    stars()
    spoceship(on_draw.x, on_draw.y)

    #Animating by adding value to the x and y
    on_draw.x += SPEED
    on_draw.y += SPOOD

    #conditional: when the speed of the ship is more than 300, the speed_lines function is called.
    if SPEED >= 300:
        speed_lines()
        SPEED = 300

    #conditional: if on_draw.x is more than the WINDOW_LENGTH+150, set on_draw.x to -250 then times SPEED by 1.5 (once it reaches the end of the window, the spooceship goes back to the start again)
    if on_draw.x > WINDOW_LENGTH + 150:
        on_draw.x = -250
        SPEED *= 1.5

    #conditional: if on_draw.y is more than WINDOW_HEIGHT-700, change SPOOD by -2
    if on_draw.y > WINDOW_HEIGHT-700:
        SPOOD += -2

    #conditional: else if on_draw.y is less than 700, change SPOOD by 2
    elif on_draw.y < 700:
        SPOOD += 2


on_draw.x = -200
on_draw.y = 0


class MyGame(arcade.Window):
    #setting the screen
    def __init__(self,width,height,title):

        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    
    
def main():
    #Set canvas then run
    MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/60)
    arcade.run()    


#Call main function to run
main()