import turtle 
trtl = turtle.Screen()
trtl.bgcolor("light blue")
trtl.title("Turtle")
pen = turtle.Turtle()
size = 0 
while True:
    for i in range(4):
        pen.fd(size + 1)
        pen.lt(90)
        size = size - 5
    size = size + 1