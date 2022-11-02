add_library("minim")
minim = Minim(this)

pre_avg = 0.
pre_avg_drum = 0.
circles = []
img = []
# Plmage img 

def setup():
    global player, fft, fftScale, cir_R, img
    size(1200, 800)
    player = minim.loadFile("tmusic.mp3")
    # player = minim.loadFile("2.mp3")
    # player = minim.loadFile("Hey Jude.mp3")
    # player = minim.loadFile("Be Here Now.mp3")
    # player.loop()
    player.play()
    img.append(loadImage("0.png"))
    img.append(loadImage("1.png"))
    img.append(loadImage("2.png"))
    fft = FFT(player.bufferSize(), player.sampleRate())
    fftScale = 30 #test 
    cir_R = 100
    frameRate(20)#test
    # colorMode(HSB)

def draw():
    # background(255)
    global pre_avg, circles, pre_avg_drum,img
    
    fft.forward(player.mix)
    specLength = fft.specSize()/4*3
    specLength_drum = fft.specSize()/2
    avg = 0.0
    avg_drum = 0.0
    for i in range(specLength):
        ffti = sqrt(fft.getBand(i))*fftScale
        avg = avg + ffti
    avg /= specLength
    for j in range(specLength_drum, specLength):
        fftj = sqrt(fft.getBand(j))*fftScale
        avg_drum = avg_drum + fftj
    avg_drum /= specLength-specLength_drum+1
    # avg = avg_drum
    print(avg_drum)
    color_para = map(avg, 4,30, 100,200)
    pre_color_para = map(pre_avg, 4,30, 100,200)
    
    if avg_drum>20 or abs(pre_avg_drum-avg_drum)>10:
        pre_avg_drum = avg_drum
        p1 = random(0,1)
        if p1<0.5:
            cirx = random(2*cir_R, width/3)
        else :
            cirx = random(width/3*2, width-2*cir_R)
        
        p2 = random(0,1)
        if p2<0.5:
            ciry = random(2*cir_R, height/3)    
        else :
            ciry = random(height/3*2, height-2*cir_R)
        
        randid = random(0,6)
        if randid < 2:
            randid = 0
        elif randid < 4:
            randid = 1
        else: 
            randid = 2
        circles.append([cirx, ciry, cir_R, 1, randid])
    
    if abs(avg-pre_avg)>10 or pre_avg==0.0 or avg>40:
        background(color_para,10,10)
        pre_avg = avg
    else :
        background(pre_color_para,10,10)
    # image(img,10,10,100,100)
        
    for cir in circles:
        if cir[2] <=0 or cir[3]<=0:
            continue
        # fill(205,127,50)
        # circle(cir[0], cir[1], cir[2])
        image(img[cir[4]],cir[0],cir[1],100*cir[3],100*cir[3])
        # print(cir[0], cir[1], cir[2])
        cir[2] = cir[2] - cir_R/10
        cir[3] = cir[3]-0.05
    # changeable parm:30
    
    point1x, point1y, pointnx, pointny = [0., 0., 0., 0.]
    for i in range(specLength-1):
        # x = map(i, 0,specLength-1, 0,width)
        # y = height - 
        ffti = sqrt(fft.getBand(i))*fftScale
        angle = map(i, 0,specLength-1, -0.5*PI, 1.5*PI)
        startX = width/2
        startY = height/2
        endXi = width/2 + cos(angle)*ffti
        endYi = height/2 + sin(angle)*ffti
        # line(startX,startY, endXi,endYi)
        
        fftj = sqrt(fft.getBand(i+1))*fftScale
        angle = map(i+1, 0,specLength-1, -0.5*PI, 1.5*PI)
        endXj = width/2 + cos(angle)*fftj
        endYj = height/2 + sin(angle)*fftj
        line(endXi,endYi, endXj,endYj)
        line(startX,startY, endXj,endYj)
        
        if i==0:
            point1x = endXi
            point1y = endYi
        elif i==specLength-2:
            pointnx = endXj
            pointny = endYj
    line(point1x,point1y, pointnx,pointny)
    # if player.isPlaying():
    #     # saveFrame("/save1/music1-########.png")
    #     print("Saving")
    # else :
    #     print("Finish")
    # delay(1000)
