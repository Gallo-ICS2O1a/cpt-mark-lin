# use list to shoot multiple bullets and PVectors in list
Playerv1 = PVector(230, 600)
Playerv2 = PVector(250, 550)
Playerv3 = PVector(270, 600)
speedx = 0
speedy = 0
keysPressed = [False for _ in range(128)]
a = 135 
b = 206
c = 250
PlaySize = 30
HTPSize = 30
Menu = True
Play = False
HTP = False
img = None
img_2 = None
yimgA = 0
yimgB = -500
bs = PVector(Playerv2.x, Playerv2.y - 5)
bullet = [False for _ in range(128)]
def setup():
    global img, img_2
    size(500,700)
    img = None
    img = createGraphics(width, height)
    img.beginDraw()
    for i in range(10):
        x = random(img.width)
        y = random(img.width)
        diameter = random(5, 15)
        img.fill(255, 69, 0)
        img.ellipse(x, y, diameter, diameter)
    img.endDraw()
    img_2 = None
    img_2 = createGraphics(width, height)
    img_2.beginDraw()
    for i in range(10):
        x = random(img_2.width)
        y = random(img_2.width)
        diameter = random(5, 15)
        img_2.fill(255, 69, 0)
        img_2.ellipse(x, y, diameter, diameter)
    img_2.endDraw()
def draw():
    global speedx, speedy, Playerv1, Playerv2, Playerv3, keysPressed, a, b, c, PlaySize, HTPSize, HTP, img, yimgA, yimgB, bs, bullet
    # background
   
    if Play == True:
        if a > 0:
            a -= 0.25
        if b > 0:
            b -= 0.25
        if c > 100:
            c -= 0.25
    background(a, b, c)
    img.background(a, b, c)
    img_2.background(a, b, c)
    if Play == True:
        imgspeed = 1
        yimgA += imgspeed
        yimgB += imgspeed
        if yimgA >= img.height:
            yimgA = -height
        elif yimgB >= img.height:
            yimgB = -height
        image(img, 0, yimgA)
        image(img_2, 0, yimgB)

    # Player
    if Menu == True or Play == True:
        fill(50,200,10)
        strokeWeight(5)
        stroke(255)
        triangle(Playerv1.x, Playerv1.y, Playerv2.x, Playerv2.y, Playerv3.x, Playerv3.y)
    #menu screen
    if Menu == True:
        textSize(50)
        fill(34,139,34)
        text("<Retro Pew Pew>", 30, 100)
    
        textSize(HTPSize)
        fill(0,128,0)
        text("<HOW TO PLAY>", 20, 200)
        if mouseX >= 20 and mouseX <= 250 and mouseY >= 170 and mouseY <= 200:
            HTPSize = 40
        else: 
            HTPSize = 30
        
        textSize(PlaySize)
        fill(0,128,0)
        text("<PLAY>", 20, 250)
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 220 and mouseY <= 250:
            PlaySize = 40
        else:
            PlaySize = 30
    
        textSize(30)
        fill(0,128,0)
        text("<CUSTOMIZATION>", 20, 300)
    #How To Play
    if HTP == True:
        textSize(20)
        fill(0, 128, 0)
        text("ARROW KEYS - Up, Down, Left, Right", 20, 100)
        text("SPACE - Shoot", 20, 140)
        text("Avoid incoming enemy bullets and defeat the boss to win!!", 20, 160, 480, 300)
    #movement and shooting
    if Play == True:
        if keysPressed[37]:
            speedx = -3
        elif keysPressed[39]:
            speedx = 3
        if keysPressed[38]:
            speedy = -3
        elif keysPressed[40]:
            speedy = 3
        if bullet[32]:
            bs.y -= 4
            bs.x = bs.x
            fill(139, 0, 0)
            strokeWeight(0)
            rect(bs.x, bs.y, 5, 10)

    Playerv1.x += speedx
    Playerv2.x += speedx
    Playerv3.x += speedx
    Playerv1.y += speedy
    Playerv2.y += speedy
    Playerv3.y += speedy
    speedx = 0
    speedy = 0    
def keyPressed():
    keysPressed[keyCode] = True
    bullet[keyCode] = True
    
def keyReleased():
    keysPressed[keyCode] = False

def mouseClicked():
    global Menu, Play, HTP
    if Menu == True:
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 220 and mouseY <= 250:
            Play = True
            Menu = False
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 170 and mouseY <= 200:
            Menu = False
            HTP = True
