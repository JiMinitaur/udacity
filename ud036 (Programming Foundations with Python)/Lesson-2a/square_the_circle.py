import turtle

def main():
    ## passing the draw function as a callback
    ## b/c exitonclick caused lockups if done before draw
    run_window(draw)

def draw(window):
    t = build_turtle()
    length = 100
    for i in xrange(0,5):
      for x in xrange(0,4):
        t.forward(length)
        t.left(90)
        swap_color(t)

def swap_color(turtle):
    colors = ['black', 'red','blue','green','white']

    cur_color = turtle.pencolor()
    cur_index = colors.index(cur_color)

    if cur_index + 1 == len(colors):
        turtle.pencolor(colors[0])
    else:
        turtle.pencolor(colors[cur_index + 1])

def build_turtle():
    """ Pity the fool """
    mr_t = turtle.Turtle()
    mr_t.shape("blank")
    mr_t.width(3)
    return mr_t

def run_window(func):
    window = turtle.Screen()
    window.bgcolor("gray")
    func(window) 
    window.exitonclick()

main()
