import turtle as tur

#Settings
tur.pencolor("pink")
tur.bgcolor("violet")

def CurveHeart():
    for i in range(200):
        tur.right(1)
        tur.forward(1)

def ShowHeart():
    tur.fillcolor("red")
    tur.begin_fill()
    tur.left(140)
    tur.forward(113)
    CurveHeart()
    tur.left(120)
    CurveHeart()
    tur.forward(112)
    tur.end_fill()

ShowHeart()
tur.ht()

# Keep window
tur.done()