import turtle

def main():
    ## passing the draw function as a callback
    ## b/c exitonclick caused lockups if done before draw
    run_window(draw)

def draw(window):
    t = build_turtle()
    length = 100
    for x in xrange(0,4):
        t.forward(length)
        t.left(90)

def build_turtle():
    """ Pity the fool """
    mr_t = turtle.Turtle()
    return mr_t

def run_window(func):
    window = turtle.Screen()
    window.bgcolor("gray")
    func(window) 
    window.exitonclick()

main()
