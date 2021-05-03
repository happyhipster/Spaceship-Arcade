''' NOT GONNA WORK'''


import arcade
SPOOD = 10
SPEED = 5
WINDOW_HEIGHT = 750
WINDOW_LENGTH = 1500


class Pic:
    def __init__(self, pain_x, pain_y, x1, y1, x, y, SPOOD, SPEED):
        self.pain_x
        self.pain_y
        self.x1
        self.y1
        self.x
        self.y
        self.SPOOD
        self.SPEED

    def stars():
        for i in range(100):
            self.pain_x = random.randint(0,1501)
            self.pain_y = random.randint(0,751)
            arcade.draw_circle_filled(self.pain_x,self.pain_y,1,arcade.color.WHITE,1)
    
    def speed_lines():
        for i in range(120):
            self.x1 = random.randint(0,1501)
            self.y1 = random.randint(0,751)
            arcade.draw_line(self.x1, self.y1, self.x1+50 ,self.y1, arcade.color.WHITE_SMOKE, 2)

    def spoceship(, ):
        arcade.draw_rectangle_filled(self.x, self.y, 200, 100, arcade.color.RED)
        arcade.draw_triangle_filled(self.x, self.y+50, self.x-150, self.y+150, self.x-100, self.y+50, arcade.color.DARK_RED)
        arcade.draw_triangle_filled(self.x, self.y-50, self.x-150, self.y-150, self.x-100, self.y-50, arcade.color.DARK_RED)
        arcade.draw_triangle_filled(self.x+100, self.y+50, self.x+200, self.y, self.x+100, self.y-50, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_circle_filled(self.x+50,self.y,40,arcade.color.WHITE,1)
        arcade.draw_circle_filled(self.x+50,self.y,25,arcade.color.AQUA,1)

        fire_inside_point_list = ((self.x-100,self.y+50), (self.x-150,self.y+25), (self.x-130,self.y+10), (self.x-160,self.y), (self.x-140,self.y-15), (self.x-125,self.y-25), (self.x-120,self.y-35), (self.x-140,self.y-45), (self.x-100,self.y-50))
        arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)
    
    def on_draw(delta_time):
        global SPOOD
        global SPEED
        global WINDOW_HEIGHT
        global WINDOW_LENGTH
        arcade.start_render()
        stars()
        spoceship(on_draw.x, on_draw.y)      
        on_draw.x += SPEED
        on_draw.y += SPOOD
        if on_draw.x > WINDOW_LENGTH + 150:       
            on_draw.x = -250
            SPEED = SPEED * 1.5
            if SPEED > 500:
                SPEED = 500
                speed_lines()

        if on_draw.y == 600:
            SPOOD = -5

        if on_draw.y == 150:
            SPOOD = 5
        




class MyGame(arcade.Window):
    def __init__(self,width,height,title):

        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)
        
        def on_key_press(self, key, modifiers):
            if key == arcade.key.LEFT:
                print("POPOPOPOP")
        def on_key_release(self,key,modifiers):
            if key == arcade.key.LEFT:
                print("opopop")

def main():
    window = MyGame(WINDOW_LENGTH, WINDOW_HEIGHT, "SPOOCESHIP")
    arcade.schedule(on_draw, 1/5000)
    arcade.run()    

main()