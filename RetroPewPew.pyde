Playerv1 = PVector(230, 600)
Playerv2 = PVector(250, 550)
Playerv3 = PVector(270, 600)
speedx = 0
speedy = 0
keysPressed = [False for _ in range(128)]

def setup():
    size(500,700)
def draw():
    global speedx, speedy, Playerv1, Playerv2, Playerv3, keysPressed
    Playerv1.x += speedx
    Playerv2.x += speedx
    Playerv3.x += speedx
    Playerv1.y += speedy
    Playerv2.y += speedy
    Playerv3.y += speedy
    background(255)
    fill(50,200,10)
    strokeWeight(5)
    triangle(Playerv1.x, Playerv1.y, Playerv2.x, Playerv2.y, Playerv3.x, Playerv3.y)
    if keyPressed:
        if keysPressed[37]:
            speedx = -3
        elif keysPressed[38]:
            speedy = -3
        elif keysPressed[39]:
            speedx = 3
        elif keysPressed[40]:
            speedy = 3
    else:
        speedx = 0
        speedy = 0    
  
def keyPressed():
    keysPressed[keyCode] = True
    
def keyReleased():
    keysPressed[keyCode] = False
