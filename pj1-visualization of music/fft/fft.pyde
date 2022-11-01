add_library("minim")
minim = Minim(this)

pre_avg = 0.
circles = []

def setup():
    global player, fft, fftScale, cir_R
    size(1200, 800)
    player = minim.loadFile("tmusic.mp3")
    player.loop()
    fft = FFT(player.bufferSize(), player.sampleRate())
    fftScale = 30 #test 
    cir_R = 100
    frameRate(10)#test
    # colorMode(HSB)

def draw():
    # background(255)
    global pre_avg, circles
    fft.forward(player.mix)
    specLength = fft.specSize()/4*3
    specLength_drum = fft.specSize()/16*9
    avg = 0.0
    avg_drum = 0.0
    for i in range(specLength):
        ffti = sqrt(fft.getBand(i))*fftScale
        avg = avg + ffti
    avg /= specLength
    # for i in range(specLength_drum):
    #     ffti = sqrt(fft.getBand(i))*fftScale
    #     avg_drum = avg_drum + ffti
    # avg_drum /= specLength
    color_para = map(avg, 4,30, 100,200)
    pre_color_para = map(pre_avg, 4,30, 100,200)
    if abs(avg-pre_avg)>10 or pre_avg==0.0 or avg>40:
        background(color_para,10,10)
        pre_avg = avg
        if avg>40:
            cirx = random(3*cir_R, width-3*cir_R)
            ciry = random(3*cir_R, height-3*cir_R)
            circles.append([cirx, ciry, cir_R])
    else :
        background(pre_color_para,10,10)
        
    for cir in circles:
        if cir[2] <=0:
            continue
        fill(205,127,50)
        circle(cir[0], cir[1], cir[2])
        print(cir[0], cir[1], cir[2])
        cir[2] = cir[2] - cir_R/10
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
        # line(startX,startY, endXj,endYj)
        
        if i==0:
            point1x = endXi
            point1y = endYi
        elif i==specLength-2:
            pointnx = endXj
            pointny = endYj
    line(point1x,point1y, pointnx,pointny)
    # delay(1000)
