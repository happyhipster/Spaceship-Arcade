''' COOMMENTS, this code is looped. The process is the spaceship getting gradually faster then entering 'hyperspace' and then flashing back to normal speed.
After this process the code continues looping. :3 
Also don't mind the variable names 
'''
import arcade
import random
def stars():
    for i in range(100):
        ax = random.randint(0,1501)
        ay = random.randint(0,751)
        arcade.draw_circle_filled(ax,ay,1,arcade.color.WHITE,1)

def speed_lines(wow):
        if wow == 1:
            for i in range(100):
                x1 = random.randint(0,1501)
                y1 = random.randint(0,751)
                arcade.draw_line(x1, y1, x1+50 ,y1, arcade.color.WHITE_SMOKE, 2)
        else:
            arcade.draw_line(900, 900, 900 ,900, arcade.color.BLACK, 1)



def spoceship(x,y):
    arcade.draw_rectangle_filled(x, y, 200, 100, arcade.color.RED)
    arcade.draw_triangle_filled(x, y+50, x-150, y+150, x-100, y+50, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x, y-50, x-150, y-150, x-100, y-50, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x+100, y+50, x+200, y, x+100, y-50, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(x+50,y,40,arcade.color.WHITE,1)
    arcade.draw_circle_filled(x+50,y,25,arcade.color.AQUA,1)

    fire_inside_point_list = ((x-100,y+50), (x-150,y+25), (x-130,y+10), (x-160,y), (x-140,y-15), (x-125,y-25), (x-120,y-35), (x-140,y-45), (x-100,y-50))
    arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)

def flash(hm):
    if hm == 1:
        arcade.draw_circle_filled(0,0,1000000000000,arcade.color.WHITE,1)
    elif hm == 0:
        arcade.draw_circle_filled(0,0,0,arcade.color.WHITE,1)


SPOOD = 0
SPEED = 5
b = 0



WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500
def on_draw(delta_time):
    global SPOOD
    global SPEED
    global b
    global WINDOW_HEIGHT
    global WINDOW_LENGTH
    arcade.start_render()
    stars()
    spoceship(on_draw.x, on_draw.y)

    on_draw.x += SPEED
    on_draw.y += SPOOD

    if SPEED == 700:
        speed_lines(1)
    elif SPEED < 500:
        speed_lines(0)

    if on_draw.x > WINDOW_LENGTH + 150:       
        on_draw.x = -250
        

on_draw.x = -200
on_draw.y = 0

class MyGame(arcade.Window):
    def __init__(self,width,height,title):

        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    

    def on_key_press(self, key, modifiers):
        global b
        global SPEED
        global speed_lines
        if key == arcade.key.UP or key == arcade.key.W:
            on_draw.y += 20

        elif key == arcade.key.DOWN or key == arcade.key.S:
            on_draw.y += -20

        if key == arcade.key.RIGHT or key == arcade.key.D:
            SPEED *= 1.5
            if SPEED > 700:
                SPEED = 700

        elif key == arcade.key.LEFT or key == arcade.key.A:
            SPEED /= 1.5
            

def main():
    window = MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/60)
    arcade.run()    



main()