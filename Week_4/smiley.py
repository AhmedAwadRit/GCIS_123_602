"""

This module uses turtle to draw a smiley face

"""


from turtle import Turtle, Screen

def draw_circle(turta, x, y, color, radius):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()

def draw_centered_circle(turta, x, y, color, radius):
    new_y = y-radius
    draw_circle(turta, x, new_y, color, radius)
    turta.up()
    turta.goto(x, y)

def draw_eye(turta, new_x, new_y, lens_color, iris_color, cornea_color, radius):
  
    draw_centered_circle(turta, new_x, new_y, cornea_color, radius*0.2)
    draw_centered_circle(turta, new_x, new_y, iris_color, radius*0.15)
    draw_centered_circle(turta, new_x, new_y, lens_color, radius*0.1)

def draw_smiley(turta, x, y, base_color, nose_color, radius):
    draw_centered_circle(turta, x, y, base_color, radius)
    draw_centered_circle(turta, x, y, nose_color, radius*0.1)

def draw_smile(turta, x, y, base_color, smile_color):
    pass

def main():
    base_color = input("What is the base color: ")
    nose_color = input("What is the nose color: ")

    lens_color = "Black"
    iris_color = "Blue"
    cornea_color = "White"

    wind = Screen()
    turta = Turtle()

    base_x = 100
    base_y = 100
    radius = 180

    # draw_centered_circle(turta, Base_x, Base_y, Base_color, radius)
    # draw_nose(turta, Base_x, Base_y, Nose_color, radius)
    
    draw_smiley(turta, base_x, base_y, base_color, nose_color, radius)

    eye1_x = base_x + (-radius*0.25)
    eye2_x = base_x + (radius*0.25)
    eye_y = base_y + (radius*0.35)

    draw_eye(turta, eye1_x, eye_y, lens_color, iris_color, cornea_color, radius)
    draw_eye(turta, eye2_x, eye_y, lens_color, iris_color, cornea_color, radius)
    

    wind.exitonclick()

main()