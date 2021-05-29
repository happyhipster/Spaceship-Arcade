#Importing the 'arcade' package and 'random' package
import arcade
import random

#Function to change size of the spaceship and the planet
def smaller(c):
    global spooceship_l
    global spooceship_w
    global window_s
    global circle_size
    if c == True:
        spooceship_w -= 1
        spooceship_l -= 0.5
        window_s -= 0.3
        circle_size += 5
    else: 
        c = False

#Drawing stars in random coordinates
def stars():
    for i in range(100):
        ax = random.randint(0,1501)
        ay = random.randint(0,751)
        star_size = random.randint(0,4)
        arcade.draw_circle_filled(ax,ay,star_size,arcade.color.WHITE,1)


#Drawing the lines during the 'hyper space' process
def speed_lines(decider):
    if decider == 0:
        for i in range(100):
            x1 = random.randint(0,1501)
            y1 = random.randint(0,751)
            arcade.draw_line(x1, y1, x1+50 ,y1, arcade.color.WHITE_SMOKE, 2)

#Drawing of the planet
def planet():
    arcade.draw_circle_filled(1300,600,circle_size,arcade.color.RADICAL_RED,1)
    arcade.draw_text("Press down arrow", 100, 100, arcade.color.WHITE, 20, 1000, 'left', 'calibri', False, False, 'left', "baseline")



#Drawing the spaceship
def spoceship(x,y):
    arcade.draw_rectangle_filled(x, y, spooceship_w, spooceship_l, arcade.color.RED)
    arcade.draw_triangle_filled(x, y+spooceship_l/2, x-spooceship_w*0.75, y+spooceship_l*1.5, x-spooceship_w/2, y+spooceship_l/2, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x, y-spooceship_l/2, x-spooceship_w*0.75, y-spooceship_l*1.5, x-spooceship_w/2, y-spooceship_l/2, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x+spooceship_w/2, y+spooceship_l/2, x+spooceship_w, y, x+spooceship_w/2, y-spooceship_l/2, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(x+50,y,window_s,arcade.color.WHITE,1)
    arcade.draw_circle_filled(x+50,y,window_s-15,arcade.color.AQUA,1)

    fire_inside_point_list = ((x-spooceship_w * 0.5, y+spooceship_l * 0.5), (x-spooceship_w*0.75,y+spooceship_l *0.25), (x-spooceship_w *0.65,y+spooceship_l* 0.1), (x-spooceship_w*0.8,y), (x-spooceship_w*0.7,y-spooceship_l*0.15), (x-spooceship_w*0.625,y-spooceship_l*0.25), (x-spooceship_w*0.6,y-spooceship_l*0.35), (x-spooceship_w*0.7,y-spooceship_l*0.45), (x-spooceship_w*0.5,y-spooceship_l*0.5))
    arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)


#Declaring the variables
SPOOD = 1
SPEED = 5
SPOOD_change = 2
SPEED_change = 10
circle_size = 50

timer = 1


WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500

conditional = False

spooceship_w = 200
spooceship_l = 100
window_s = 40

#Function for animating
def on_draw(delta_time):
    #Access global variables in this function
    global SPEED
    global SPOOD
    global SPOOD_change
    global conditional
    global SPEED_change 
    global timer
    arcade.start_render()
    #Calling functions to draw the aspects of the animation
    stars()
    spoceship(on_draw.x, on_draw.y)

    #Conditions to carry out the animation
    if spooceship_w != 160:
        smaller(conditional)

    if SPEED >= 300:
        SPEED = 300
        speed_lines(0)
        timer += 1
        print(timer)
    if timer == 100:
        speed_lines(10)
        SPEED_change  = 1
        SPOOD = 0
        SPOOD_change = 0
        on_draw.y = 300
        timer = 0
        on_draw.x = 200
        SPEED = 0
    if timer == 0:
        planet()



    #Animating by adding value to the x and y
    on_draw.x += SPEED
    on_draw.y += SPOOD

    #conditional: if on_draw.x is more than the WINDOW_LENGTH+150 (once it reaches the end of the window, the spooceship goes back to the start again)
    if on_draw.x > WINDOW_LENGTH + 150:
        on_draw.x = -250
        SPEED *= SPEED_change 

    #conditional: if on_draw.y is more than WINDOW_HEIGHT-700, change SPOOD by -2
    if on_draw.y > WINDOW_HEIGHT-400:
        SPOOD -= SPOOD_change

    #conditional: else if on_draw.y is less than 700, change SPOOD by 2
    elif on_draw.y < 400:
        SPOOD += SPOOD_change


on_draw.x = -200
on_draw.y = 0


#class of the game window
class MyGame(arcade.Window):
    #Setting up the screen
    def __init__(self,width,height,title):

        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
    
    #Function to recognise user input
    def on_key_press(self, key, modifiers):
        global spooceship_l 
        global circle_size
        global spooceship_w
        global window_s
        global conditional
        if timer == 0:
            if spooceship_w != 160:
                if key == arcade.key.DOWN:
                    conditional = True
                
def main():
    #Set canvas then run
    MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/60)
    arcade.run()    


#Call main function to run
main()