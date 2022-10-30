add_library("minim")
minim = Minim(this)

def setup():
    global player, fft, fftScale
    size(1200, 800)
    player = minim.loadFile("tmusic.mp3")
    player.loop()
    fft = FFT(player.bufferSize(), player.sampleRate())
    fftScale = 30 #test 
    frameRate(10)

def draw():
    background(255)
    fft.forward(player.mix)
    specLength = fft.specSize()/4*3
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
