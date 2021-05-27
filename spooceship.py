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
    arcade.draw_rectangle_filled(x, y, spooceship_w, spooceship_l, arcade.color.RED)
    arcade.draw_triangle_filled(x, y+spooceship_l/2, x-spooceship_w*0.75, y+spooceship_l*1.5, x-spooceship_w/2, y+spooceship_l/2, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x, y-spooceship_l/2, x-spooceship_w*0.75, y-spooceship_l*1.5, x-spooceship_w/2, y-spooceship_l/2, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(x+spooceship_w/2, y+spooceship_l/2, x+spooceship_w, y, x+spooceship_w/2, y-spooceship_l/2, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(x+50,y,window_s,arcade.color.WHITE,1)
    arcade.draw_circle_filled(x+50,y,window_s-15,arcade.color.AQUA,1)

    fire_inside_point_list = ((x-spooceship_w * 0.5, y+spooceship_l * 0.5), (x-spooceship_w*0.75,y+spooceship_l *0.25), (x-spooceship_w *0.65,y+spooceship_l* 0.1), (x-spooceship_w*0.8,y), (x-spooceship_w*0.7,y-spooceship_l*0.15), (x-spooceship_w*0.625,y-spooceship_l*0.25), (x-spooceship_w*0.6,y-spooceship_l*0.35), (x-spooceship_w*0.7,y-spooceship_l*0.45), (x-spooceship_w*0.5,y-spooceship_l*0.5))
    arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)

def speed_lines(decider):
    if decider == 0:
        for i in range(100):
            x1 = random.randint(0,1501)
            y1 = random.randint(0,751)
            arcade.draw_line(x1, y1, x1+50 ,y1, arcade.color.WHITE_SMOKE, 2)
    else:
        arcade.draw_line(100000, 1000000, 10000+50 ,1000000, arcade.color.WHITE_SMOKE, 2)

def hit(hit_x, hit_y):
    arcade.draw_circle_filled(hit_x,hit_y,radius, projectile_colour,1)        

def end(hm):
    global accuracy 
    if hm == True:
        arcade.draw_circle_filled(0, 0, 1000, arcade.color.BLACK,1)
        arcade.draw_text("YOU WIN! :3", 100, 200, arcade.color.WHITE, 20, 100, "left", "calibri", True, False)
        total = (misses + hits)
        accuracy = hits/total *100
        arcade.draw_text("Accuracy is " + str(accuracy) + "%", 100, 75, arcade.color.WHITE, 20, 500, "left", "calibri", True, False)
    if hm == False:
        arcade.draw_circle_filled(0, 0, 100000, arcade.color.BLACK,1)
        arcade.draw_text("YOU LOST! ;-;", 100, 200, arcade.color.WHITE, 20, 100, "left", "calibri", True, False)

#Declaring the variables
SPOOD = 0
SPEED = 5
projectile_colour = arcade.color.WHITE
score = 0
hit_speed = 15
space_count = 0
radius = 20

avoid_y_list = [100, 300, 500, 700]

WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500

spooceship_w = 200
spooceship_l = 100
window_s = 40
misses = 0
hits = 0
accuracy = 0

#Function for animating
def on_draw(delta_time):
    #access global variables in this function
    global SPEED
    global space_count
    global score
    global hit_speed
    global radius
    global projectile_colour
    global misses
    global spooceship_l
    global spooceship_w
    global window_s
    arcade.start_render()
    #Calling functions to draw scenery
    stars()
    spoceship(on_draw.x, on_draw.y)
    hit(on_draw.hit_x, on_draw.hit_y)
    on_draw.hit_x -= hit_speed
    target()
    
    arcade.draw_text(str(score), 100, 200, arcade.color.WHITE, 20, 100, "left", "calibri", True, False)

    if on_draw.hit_x <= 10:
        space_count = 0
        if projectile_colour == arcade.color.WHITE:
            score -= 1
            misses += 1
            spooceship_l -= 2
            spooceship_w -= 4
            window_s -= 1.2
            if spooceship_l <= 80:
                spooceship_l = 80
                spooceship_w = 180
                window_s = 20
                

        on_draw.hit_x = 1500
        place_generator = random.randint(0,3)
        on_draw.hit_y = avoid_y_list[place_generator]
        projectile_colour = arcade.color.WHITE

        if score %5:
            hit_speed+=1

    if score == 40:
        hit_speed = 0
        space_count = 100
        end(True)
        spoceship(200,400)
        speed_lines(0)
        stars()
        on_draw.hit_x = 20000

    if score == -5:
        space_count = 100
        hit_speed = 0
        end(False)


on_draw.x = 700
on_draw.y = 400
on_draw.hit_x = 1500
place_generator = random.randint(0,3)
on_draw.hit_y = avoid_y_list[place_generator]

class MyGame(arcade.Window):
    #setting the screen
    def __init__(self,width,height,title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    
    #function for user input
    def on_key_press(self, key, modifiers):
        global score
        global space_count
        global hit_speed
        global radius
        global projectile_colour
        global spooceship_w
        global spooceship_l
        global window_s
        global misses
        global hits
        #this code speaks for itself (?)
        if space_count == 0:
            if key == arcade.key.UP or key == arcade.key.W:
                space_count += 1
                if on_draw.hit_y == 700:
                    if on_draw.hit_x > 100 and on_draw.hit_x < 300:
                        score += 1
                        projectile_colour = arcade.color.GREEN
                        spooceship_l += 0.5
                        spooceship_w += 1
                        window_s += 0.3
                        hits += 1
                    else: 
                        score -= 1
                        projectile_colour = arcade.color.RED_DEVIL
                        spooceship_l -= 2
                        spooceship_w -= 4
                        window_s -= 1.2
                        misses += 1
                else: 
                    score -= 1
                    projectile_colour = arcade.color.RED_DEVIL
                    spooceship_l -= 2
                    spooceship_w -= 4
                    window_s -= 1.2
                    misses += 1
                    
            if key == arcade.key.LEFT or key == arcade.key.A:
                space_count += 1
                if on_draw.hit_y == 500:
                    if on_draw.hit_x > 100 and on_draw.hit_x < 300:
                        score  += 1
                        projectile_colour = arcade.color.GREEN
                        spooceship_l += 0.5
                        spooceship_w += 1
                        window_s += 0.3
                        hits += 1
                    else: 
                        score -= 1
                        projectile_colour = arcade.color.RED_DEVIL
                        spooceship_l -= 2
                        spooceship_w -= 4
                        window_s -= 1.2
                        misses += 1
                else: 
                    score -= 1
                    projectile_colour = arcade.color.RED_DEVIL
                    spooceship_l -= 2
                    spooceship_w -= 4
                    window_s -= 1.2
                    misses += 1

            if key == arcade.key.RIGHT or key == arcade.key.D:
                space_count += 1
                if on_draw.hit_y == 300:
                    if on_draw.hit_x > 100 and on_draw.hit_x < 300:
                        score += 1
                        projectile_colour = arcade.color.GREEN
                        spooceship_l += 0.5
                        spooceship_w += 1
                        window_s += 0.3
                        hits += 1
                    else: 
                        score -= 1
                        projectile_colour= arcade.color.RED_DEVIL
                        spooceship_l -= 2
                        spooceship_w -= 4
                        window_s -= 1.2
                        misses += 1

                else: 
                    score -= 1
                    projectile_colour= arcade.color.RED_DEVIL
                    spooceship_l -= 2
                    spooceship_w -= 4
                    window_s -= 1.2
                    misses += 1

            if key == arcade.key.DOWN or key == arcade.key.S:
                space_count += 1 
                if on_draw.hit_y == 100:
                    if on_draw.hit_x > 100 and on_draw.hit_x < 300:
                        score += 1
                        projectile_colour = arcade.color.GREEN
                        spooceship_l += 0.5
                        spooceship_w += 1
                        window_s += 0.3
                        hits += 1
                    else: 
                        score -= 1
                        projectile_colour = arcade.color.RED_DEVIL
                        spooceship_l -= 2
                        spooceship_w -= 4
                        window_s -= 1.2
                        misses += 1
                else: 
                    score -= 1
                    projectile_colour = arcade.color.RED_DEVIL
                    spooceship_l -= 2
                    spooceship_w -= 4
                    window_s -= 1.2
                    misses += 1

            if key == arcade.key.SPACE:
                score = 40

            if key == arcade.key.P:
                score = -5

            

def main():
    #Set canvas then run
    MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/60)
    arcade.run()    


#Call main function to run
main()