def setup():
    size(1000,1000,P3D)
    background(0)
    noStroke()

def draw():
    background(0)
    camera(mouseX, height/2, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0)
    img = loadImage("t11.png")
    lights()
    translate(width/2,height/2,-200)
    rotateY(1.0)
    rotateZ(1.0)
    # rotateX(frameCount/30.0)
    for i in range(0,17):
        translate(0,220,0)
        ambient(modelX(0,0,0), modelY(0,0,0), 2*modelZ(0,0,0))
        # ambient(200)
        # sphere(40)
        s = createShape(SPHERE,43)
        s.setTexture(img)
        shininess(1.0)
        shape(s)
        translate(0,-220,0)
        rotateX(PI/8)


# def setup():
#     size(1000,1000,P3D)
#     background(0)
#     noStroke()

# def draw():
#     background(0)
#     camera(mouseX, height/2, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0)
#     img = loadImage("t11.png")
#     lights()
#     translate(width/2,height/2,-200)
#     # rotateY(1.0)
#     # rotateZ(1.0)
#     # rotateX(frameCount/30.0)
#     for i in range(0,17):
#         translate(0,220,0)
        
#         ambient(modelX(0,0,0), modelY(0,0,0), 2*modelZ(0,0,0))
#         # ambient(200)
#         sphere(40)
#         # s = createShape(SPHERE,40)
#         # s.setTexture(img)
#         # s.shininess(1.0)
#         # shape(s)
#         translate(0,-220,0)
#         rotateX(PI/8)


# def setup():
#     size(1000, 1000, P3D)
#     background(0)
#     # noStroke()
#     stroke(255)
#     # background(0)
#     # fill(0, 51, 102)
#     noFill()
# def draw():
#     # ambientLight(102, 102, 102)
#     # lightSpecular(204, 204, 204)
#     # directionalLight(102, 102, 102, 0, 0, -1)
#     # specular(255, 255, 255)
#     # translate(300, 300, 0)
#     # shininess(1.0)
#     # sphere(150)  # Left sphere
#     # translate(300, 0, 0)
#     # shininess(10)
#     # emissive(255, 10, 10)
#     # ambient(0,255,10)
#     # specular(255,100,150)
#     # # lights()
#     # if mousePressed:
#     #     directionalLight(255, 10, 21, 0, -1, 0)
#     # sphere(150)  # Right sphere
#     s = createShape()
#     s.beginShape()
#     s.vertex(10,10,10,0,0)
#     # vertex(100,100)
#     # vertex(150, 200)
#     s.bezierVertex(100,200,10, 600,200,10, width/4, height/2,-100)
#     s.bezierVertex(200,300,-100, 100,200,-100, 10,10,10)
#     s.endShape()
    
#     textureMode(NORMAL)
#     img = loadImage("t2.png")
#     # s.setTexture(img)
#     # s.setFill(img)
    
#     beginShape()
#     # s.setTexture(img)
#     texture(img)
#     vertex(0,0, 0,0)
#     vertex(100,0, 1,0)
#     vertex(100,100, 1,1)
#     vertex(0,100, 0,1)
#     endShape()
#     shape(s, 200,200)
#     # if mousePressed:
#     #     beginShape()
#     #     vertex(10,10)
#     #     # vertex(100,100)
#     #     # vertex(150, 200)
#     #     bezierVertex(100,200, 600,200, width/4, height/2)
#     #     # bezierVertex(200,300, 100,200, 10,10)
#     #     endShape(CLOSE)
#     # else:
#     #     beginShape()
#     #     curveVertex(10,10)
#     #     curveVertex(200,300)
#     #     curveVertex(600,100)
#     #     curveVertex(width/4, height/2)
#     #     endShape(CLOSE)
        
#     # beginShape()
#     # vertex(30, 20)
#     # vertex(85, 20)
#     # vertex(85, 75)
#     # vertex(30, 75)
#     # endShape()

# # String http = "http://";
# # global img 

# def setup():
#   size(400,400,P3D)
#   imageMode(CENTER)


# def draw():
#   background(128)
#   global img
#   img = loadImage("t1.png")
#   translate(width/2,height/2,0)
#   rotateY(map(mouseX,0,width,-PI,PI))
#   translate(100,0,0)
#   rotateY(-map(mouseX,0,width,-PI,PI))
#   image(img,0,0,200,200)



# global globe

# def setup():
#     size(600, 600, P3D)
#     background(0) 
#     noStroke()
#     # String http = "http://"
#     # earth = loadImage( http + "previewcf.turbosquid.com/Preview/2014/08/01__15_41_30/Earth.JPG5a55ca7f-1d7c-41d7-b161-80501e00d095Larger.jpg");
#     earth = loadImage("t2.png")
#     global globe
#     globe = createShape(SPHERE, 100)
#     globe.setTexture(earth)

# def draw():
#     global globe
#     translate(width/2, height/2, 0) 
#     if mousePressed:
#         # lights()
#         directionalLight(255, 255, 255, 1, 1, -1)
    
#     shape(globe)



# def setup():
#     size(1000, 1000, P3D)
#     # noStroke()
#     stroke(255)
#     background(0)
    
# def draw():
#     img = loadImage("t2.png")
#     textureMode(NORMAL)
#     # textureWrap(REPEAT)
#     textureWrap(CLAMP)
#     beginShape()
#     texture(img)
#     vertex(0, 0, 0, 0)
#     vertex(1000, 0, 3, 0)
#     vertex(1000, 1000, 3, 3)
#     vertex(0, 1000, 0, 3)
#     endShape()
#     # translate(width/2, height/2, 0)
#     # sphere(200)


# def setup():
#   size(1000, 800, P3D)
#   noStroke()
#   fill(204)

# def draw() :
#   noStroke() 
#   background(0) 
#   dirY = (mouseY / float(height) - 0.5) * 2
#   dirX = (mouseX / float(width) - 0.5) * 2
#   if mousePressed:
#       directionalLight(255, 204, 204, -1,-1,-1)
#   else :
#     directionalLight(255, 204, 204, -1, -1, -1) 
#   translate(width/2 - 100, height/2, 0) 
#   sphere(80)
#   translate(200, 0, 0) 
#   sphere(80)

# def setup():
#       size(200, 200, P3D)

# def draw():
#     background(0)
#     translate(100, 100, 0)
#     # camera(mouseX, height/2, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0)
#     # spotLight(255, 0, 0, width/2, height/2, 400, 0, 0, -1, PI/2, 2)
#     spotLight(255,0,0, -100,-100,0, 1,1,0, PI/2, 0)
#     if (mousePressed):
#         # lights()
#         # ambientLight(0,0,255)
#         # directionalLight(255,0, 0, 0, 0, 1)
#         # spotLight(255, 0, 0, width/2, height/2, 400, 0, 0, -1, PI/6, 2)
#         spotLight(255,0,0, -100,-100,0, 1,1,0, PI, 0)

#     noStroke()
#     fill(255)
#     sphere(50)


# def setup():
#     size(640, 360, P3D)

# def draw():
#     background(0)
#     camera(mouseX, mouseY, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0)
#     translate(width/2, height/2, -100)
#     # translate(200,200,-200)
#     # translate(0, 0, -100)
#     stroke(255)
#     # fill(255)
#     noFill()
#     # box(200)
#     pointLight(255,0,0, 0,0,0)
#     sphere(200)
#     # translate(100, 0, 0)
#     # sphere(50)
#     # lights()
#     # directionalLight(0, 255, 0, 0, -1, 0)
    
    
# def setup():
#     size(600, 600, P3D)

# def draw():
#     background(0,0,0)
#     pushMatrix()
#     translate(400,300,-mouseX)
#     fill(255,255,255)
#     noStroke()
#     directionalLight(255,0,0,1,1,0) # 从左上角打入的红光
#     directionalLight(0,255,0,1,0,0) # 从左侧打入的绿光
#     directionalLight(0,255,255,-1,0,0) # 从右侧打入的青蓝光
#     sphere(150.0)
#     popMatrix() 
