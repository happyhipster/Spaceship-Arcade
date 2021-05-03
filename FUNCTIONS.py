def stars():
    pain_x = random.randint(0,1001)
    pain_y = random.randint(0,501)
    arcade.draw_circle_filled(pain_x,pain_y,1,arcade.color.WHITE,1)

def speed_lines():
    AAA_x = random.randint(0,1001)
    y = random.randint(0,501)
    BBB_x = AAA_x + 50
    arcade.draw_line(AAA_x, y, BBB_x,y, arcade.color.WHITE_SMOKE, 2)

def spoceship():
    arcade.draw_rectangle_filled(400, 200, 200, 100, arcade.color.RED)
    arcade.draw_triangle_filled(400, 250, 250, 350, 300, 250, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(400, 150, 250, 50, 300, 150, arcade.color.DARK_RED)
    arcade.draw_triangle_filled(500, 250, 600, 200, 500, 150, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(450,200,40,arcade.color.WHITE,1)
    arcade.draw_circle_filled(450,200,25,arcade.color.AQUA,1)

    fire_inside_point_list = ((300,250), (250,225), (270,210), (240,200), (260,185), (275,175), (280,165), (260,155), (300,150))
    arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)

    '''
    for i in range(1000):
        pain_x = random.randint(0,1001)
        pain_y = random.randint(0,501)
        arcade.draw_circle_filled(pain_x,pain_y,1,arcade.color.WHITE,1)

    for i in range(75):
        AAA_x = random.randint(0,1001)
        y = random.randint(0,501)
        BBB_x = AAA_x + 50
        arcade.draw_line(AAA_x, y, BBB_x,y, arcade.color.WHITE_SMOKE, 2)


        arcade.draw_rectangle_filled(400, 200, 200, 100, arcade.color.RED)
        arcade.draw_triangle_filled(400, 250, 250, 350, 300, 250, arcade.color.DARK_RED)
        arcade.draw_triangle_filled(400, 150, 250, 50, 300, 150, arcade.color.DARK_RED)
        arcade.draw_triangle_filled(500, 250, 600, 200, 500, 150, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_circle_filled(450,200,40,arcade.color.WHITE,1)
        arcade.draw_circle_filled(450,200,25,arcade.color.AQUA,1)

        fire_inside_point_list = ((300,250), (250,225), (270,210), (240,200), (260,185), (275,175), (280,165), (260,155), (300,150))
        arcade.draw_polygon_filled(fire_inside_point_list, arcade.color.YELLOW)
        this not needed code'''