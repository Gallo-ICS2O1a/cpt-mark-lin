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
    background(0)
    fill(50,200,10)
    strokeWeight(5)
    stroke(255)
    triangle(Playerv1.x, Playerv1.y, Playerv2.x, Playerv2.y, Playerv3.x, Playerv3.y)
    #menu screen
    # textSize(50)
    # fill(34,139,34)
    # text("<MAIN MENU>", 65, 100)
    
    # textSize(30)
    # fill(0,128,0)
    # text("<HOW TO PLAY>", 20, 200)
    
    # textSize(30)
    # fill(0,128,0)
    # text("<PLAY>", 20, 250)
    
    # textSize(30)
    # fill(0,128,0)
    # text("<CUSTOMIZATION>", 20, 300)
    
    #movement
    if keysPressed[37]:
        speedx = -3
    elif keysPressed[39]:
        speedx = 3
    if keysPressed[38]:
        speedy = -3
    elif keysPressed[40]:
        speedy = 3

    Playerv1.x += speedx
    Playerv2.x += speedx
    Playerv3.x += speedx
    Playerv1.y += speedy
    Playerv2.y += speedy
    Playerv3.y += speedy
    speedx = 0
    speedy = 0
    # background
    strokeWeight(1)
    fill(255,255,0)
    ellipse(350, 200, 120, 120)
    fill(255, 69, 0)
    ellipse(350, 200, 70, 70)
def keyPressed():
    keysPressed[keyCode] = True
    
def keyReleased():
    keysPressed[keyCode] = False
