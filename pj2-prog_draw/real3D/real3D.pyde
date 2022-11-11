def setup():
    size(1000,1000,P3D)
    background(0)
    noStroke()

def draw():
    background(0)
    camera(mouseX, height/2, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0)
    img = [] 
    # tint(10,255,10,150)
    img.append(loadImage("t1.png"))
    img.append(loadImage("t2.png"))
    img.append(loadImage("t3.png"))
    # if mousePressed:
    dirY = (mouseY / float(height) - 0.5) * 2;
    dirX = (mouseX / float(width) - 0.5) * 2;
    directionalLight(255, 100, 100, -dirX, -dirY, -1); 
    # directionalLight(255,100,100,1,1,-1)
    # else:
        # lights()
    translate(width/2,height/2,-200)
    rotateY(1.0)
    rotateZ(1.0)
    # rotateX(frameCount/30.0)
    numrandom = [1,0,2,1,2,0,0,2,1,1,0,2,1,2,0,1,2]
    
    for i in range(0,17):
        translate(0,220,0)
        ambient(modelX(0,0,0), modelY(0,0,0), 2*modelZ(0,0,0))
        # ambient(10,10,255)
        # ambient(200)
        # sphere(40)
        s = createShape(SPHERE,43)
        s.setTexture(img[numrandom[i]])
        s.tint(10,255,10,150)
        shininess(5.0*i/10)
        shape(s)
        translate(0,-220,0)
        rotateX(PI/8)
