import turtle

def main():
    ## passing the draw function as a callback
    ## b/c exitonclick caused lockups if done before draw
    run_window(draw)

def draw():
    scrawly = turtle.Turtle()
    scrawly.forward(100)

def run_window(func):
    window = turtle.Screen()
    window.bgcolor("gray")
    func()
    window.exitonclick()

main()
