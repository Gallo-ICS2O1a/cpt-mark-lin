Playerv1 = PVector(230, 600)
Playerv2 = PVector(250, 550)
Playerv3 = PVector(270, 600)
speedx = 0
speedy = 0

def setup():
    size(500,700)
def draw():
    global speedx, speedy, Playerv1, Playerv2, Playerv3
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
        if keyCode == LEFT:    
            speedx = -3
        if keyCode == RIGHT:
            speedx = 3
        if keyCode == UP:
            speedy = -3
        if keyCode == DOWN:
            speedy = 3
    elif keyPressed == False:
        speedx = 0
        speedy = 0
        
keysPressed = [False for _ in range(128)]

def setup():
    size(200, 200)
    
def draw():
    if keysPressed[37]:
        print("left")
    elif keysPressed[38]:
        print("up")
    elif keysPressed[39]:
        print("down")
    elif keysPressed[40]:
        print("right")
def keyPressed():
    keysPressed[keyCode] = True
    
def keyReleased():
    keysPressed[keyCode] = False