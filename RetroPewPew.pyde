Playerv1 = PVector(230, 600)
Playerv2 = PVector(250, 550)
Playerv3 = PVector(270, 600)
speedx = 0
speedy = 0
keysPressed = [False for _ in range(128)]
bgcoloura = 135
bgcolourb = 206
bgcolourc = 250
PlaySize = 30
HTPSize = 30
Menu = True
Play = False
HTP = False
img = None
img_2 = None
yimgA = 0
yimgB = -500
bs = [PVector(Playerv2.x - 2.5, Playerv2.y - 5) for _ in range(100)]
bullets = [False for _ in range(128)]
backSize = 30
i = 0


def setup():
    global img, img_2
    size(500, 700)
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
    global speedx, speedy, Playerv1, Playerv2, Playerv3
    global keysPressed, bs, bullets
    global bgcoloura, bgcolourb, bgcolourc,
    global PlaySize, HTPSize, HTP, Menu, Play
    global img, yimgA, yimgB, backSize, i
    # background
    if Play:
        if bgcoloura > 0:
            bgcoloura -= 0.25
        if bgcolourb > 0:
            bgcolourb -= 0.25
        if bgcolourc > 100:
            bgcolourc -= 0.25
    background(bgcoloura, bgcolourb, bgcolourc)
    img.background(bgcoloura, bgcolourb, bgcolourc)
    img_2.background(bgcoloura, bgcolourb, bgcolourc)
    if Play:
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
    if Menu or Play:
        fill(50, 200, 10)
        strokeWeight(5)
        stroke(255)
        triangle(Playerv1.x, Playerv1.y, Playerv2.x, Playerv2.y, Playerv3.x, Playerv3.y)
    # menu screen
    if Menu:
        textSize(50)
        fill(34, 139, 34)
        text("<Retro Pew Pew>", 30, 100)

        textSize(HTPSize)
        fill(0, 128, 0)
        text("<HOW TO PLAY>", 20, 200)
        if mouseX >= 20 and mouseX <= 250 and mouseY >= 170 and mouseY <= 200:
            HTPSize = 40
        else:
            HTPSize = 30

        textSize(PlaySize)
        fill(0, 128, 0)
        text("<PLAY>", 20, 250)
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 220 and mouseY <= 250:
            PlaySize = 40
        else:
            PlaySize = 30

        textSize(30)
        fill(0, 128, 0)
        text("<CUSTOMIZATION>", 20, 300)
    # How To Play
    if HTP:
        textSize(20)
        fill(0, 128, 0)
        text("ARROW KEYS - Up, Down, Left, Right", 20, 100)
        text("SPACE - Shoot", 20, 140)
        text("Avoid incoming enemy bullets and defeat the boss to win!!", 20, 160, 480, 300)
        textSize(backSize)
        text("<BACK>", 20, 650)
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 620 and mouseY <= 650:
            backSize = 40
        else:
            backSize = 30

    # movement and shooting
    if Play:
        if keysPressed[37]:
            speedx = -3
        elif keysPressed[39]:
            speedx = 3
        if keysPressed[38]:
            speedy = -3
        elif keysPressed[40]:
            speedy = 3
        if keysPressed[32]:
            bs[i].y -= 4
            fill(139, 0, 0)
            strokeWeight(0)
            rect(bs[i].x, bs[i].y, 5, 10)
            i += 1

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


def keyReleased():
    keysPressed[keyCode] = False


def mouseClicked():
    global Menu, Play, HTP
    if Menu:
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 220 and mouseY <= 250:
            Play = True
            Menu = False
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 170 and mouseY <= 200:
            Menu = False
            HTP = True
    if HTP:
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 620 and mouseY <= 650:
            HTP = False
            Menu = True
