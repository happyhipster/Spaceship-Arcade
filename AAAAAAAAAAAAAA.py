import arcade
import random
def stars():
    while True:
        pain_x = random.randint(0,1001)
        pain_y = random.randint(0,501)
        arcade.draw_circle_filled(pain_x,pain_y,1,arcade.color.WHITE,1)

def speed_lines():
    while True:
        x = random.randint(0,1001)
        y = random.randint(0,501)
        arcade.draw_line(x, y, x+50 ,y, arcade.color.WHITE_SMOKE, 2)

def spoceship():
    arcade.draw_rectangle_filled(400, 200, 200, 100, arcade.color.RED)
    arcade.draw_triangle_filled(400, 250, 250, 350, 300, 250, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(400, 150, 250, 50, 300, 150, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(500, 250, 600, 200, 500, 150, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(450,200,40,arcade.color.WHITE,1)
    arcade.draw_circle_filled(450,200,25,arcade.color.AQUA,1)

    fire_inside_point_list = ((300,250), (250,225), (270,210), (240,200), (260,185), (275,175), (280,165), (260,155), (300,150))
    arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)

def on_draw(delta_time):   
    arcade.start_render()
    stars()
    speed_lines()
    spoceship()
    #on_draw.x += 1




def main():
    arcade.open_window(1000, 500, "SPACESHIP")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1/60)  
    arcade.run()
    
    

main()

