 
def setup():
    size(1000,1000,P3D)
    background(0)
    noStroke()

def draw():
    img = loadImage("t11.png")
    lights()
    translate(width/2,height/2,-200)
    rotateY(1.0)
    rotateZ(1.0)
    # rotateX(frameCount/30.0)
    for i in range(0,17):
        translate(0,220,0)
        # ambient(modelX(0,0,0), modelY(0,0,0), 2*modelZ(0,0,0))
        # ambient(200)
        # sphere(40)
        s = createShape(SPHERE,40)
        s.setTexture(img)
        # s.shininess(1.0)
        shape(s)
        translate(0,-220,0)
        rotateX(PI/8)
