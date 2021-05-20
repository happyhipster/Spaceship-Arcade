#NOTES MAKE THE GAME MECHANIC COLLECTABLES DURING CLASS OR SMTHN IDK MAAAAAN
#importing the 'arcade' package and 'random' package
import arcade
import random

def target():
    arcade.draw_circle_filled(200,100,40,(235,64,64),1)
    arcade.draw_circle_filled(200,300,40,(235,64,64),1)
    arcade.draw_circle_filled(200,500,40,(235,64,64),1)
    arcade.draw_circle_filled(200,700,40,(235,64,64),1)

#Drawing stars in random coordinates
def stars():
    for i in range(100):
        ax = random.randint(0,1501)
        ay = random.randint(0,751)
        arcade.draw_circle_filled(ax,ay,1,arcade.color.WHITE,1)


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

def speed_lines(decider):
    if decider == 0:
        for i in range(100):
            x1 = random.randint(0,1501)
            y1 = random.randint(0,751)
            arcade.draw_line(x1, y1, x1+50 ,y1, arcade.color.WHITE_SMOKE, 2)

def hit(hit_x, hit_y):
    arcade.draw_circle_filled(hit_x,hit_y,radius, r,1)        

def victory():
    arcade.draw_circle_filled(0, 0, 1000, arcade.color.BLACK,1)
    arcade.draw_text("YOU WIN! :3", 100, 200, arcade.color.WHITE, 20, 100, "left", "calibri", True, False)

#Declaring the variables
SPOOD = 0
SPEED = 5
r = arcade.color.WHITE
score = 0
hit_speed = 15
t = 0
radius = 20

avoid_y_list = [100, 300, 500, 700]

WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500


#Function for animating
def on_draw(delta_time):
    #access global variables in this function
    global SPEED
    global t
    global score
    global hit_speed
    global radius
    global r
    arcade.start_render()
    #Calling functions to draw scenery
    stars()
    spoceship(on_draw.x, on_draw.y)
    hit(on_draw.hit_x, on_draw.hit_y)
    on_draw.hit_x -= hit_speed
    target()
    arcade.draw_text(str(score), 100, 200, arcade.color.WHITE, 20, 100, "left", "calibri", True, False)

    if on_draw.hit_x <= 10:
        print(score)
        t = 0
        if r == arcade.color.WHITE:
            score -= 1
        on_draw.hit_x = 1500
        g = random.randint(0,3)
        on_draw.hit_y = avoid_y_list[g]
        r = arcade.color.WHITE

        if score %5:
            hit_speed+=1

    if score == 40:
        hit_speed = 0
        victory()
        spoceship(200,400)
        speed_lines(0)
        stars()


on_draw.x = 700
on_draw.y = 400
on_draw.hit_x = 1500
g = random.randint(0,3)
on_draw.hit_y = avoid_y_list[g]

class MyGame(arcade.Window):
    #setting the screen
    def __init__(self,width,height,title):

        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    
    #function for user input
    def on_key_press(self, key, modifiers):
        global score
        global t
        global hit_speed
        global radius
        global r
        #this code speaks for itself (?)
        if t == 0:
            if key == arcade.key.UP or key == arcade.key.W:
                t += 1
                if on_draw.hit_y == 700:
                    if on_draw.hit_x < 400:
                        score += 1
                        print(score)
                        r = arcade.color.GREEN
                else: 
                    score -= 1
                    print(score)
                    r = arcade.color.RED_DEVIL
                    
        if t == 0:
            if key == arcade.key.LEFT or key == arcade.key.A:
                t += 1
                if on_draw.hit_y == 500:
                    if on_draw.hit_x < 400:
                        score  += 1
                        print(score)
                        r = arcade.color.GREEN
                else: 
                    score -= 1
                    print(score)
                    r = arcade.color.RED_DEVIL

        if t == 0:
            if key == arcade.key.RIGHT or key == arcade.key.D:
                t += 1
                if on_draw.hit_y == 300:
                    if on_draw.hit_x < 400:
                        score += 1
                        print(score)
                        r = arcade.color.GREEN
                else: 
                    score -= 1
                    print(score)
                    r = arcade.color.RED_DEVIL

        if t == 0:
            if key == arcade.key.DOWN or key == arcade.key.S:
                t += 1 
                if on_draw.hit_y == 100:
                    if on_draw.hit_x < 400:
                        score += 1
                        print(score)
                        r = arcade.color.GREEN
                else: 
                    score -= 1
                    print(score)
                    r = arcade.color.RED_DEVIL

            

def main():
    #Set canvas then run
    MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/60)
    arcade.run()    


#Call main function to run
main()