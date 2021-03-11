import interfascia.*;
grid = [[9]*8 for n in range(10)]
w = 50

def setup():
    size(800,600)
def draw():
    x,y = 0,0
    for row in grid:
        for col in grid:
            rect(x,y, w, w)
            x = x + w
        y = y + w
