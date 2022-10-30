add_library("minim")
minim = Minim(this)

def setup():
    global player
    size(800, 400)
    player = minim.loadFile("tmusic.mp3")
    player.play()
    # frameRate(30)
    
def draw():
    background(255)
    music_left_size = player.left.size()
    music_right_size = player.right.size()
    for i in range(music_left_size-1):
        stroke(255,10,10)
        lx0 = map(i, 0,music_left_size-1, 0,width)
        ly0 = map(player.left.get(i), -1,1, 0,height)
        lx1 = map(i+1, 0,music_left_size-1, 0,width)
        ly1 = map(player.left.get(i+1), -1,1, 0,height)
        loudless = abs(player.left.get(i))
        sw = map(loudless, 0,1, 0.5,6)
        strokeWeight(sw)
        line(lx0,ly0, lx1,ly1)
        # point(lx,ly)
    for j in range(music_right_size-1):
        stroke(0,0,0)
        rx0 = map(j, 0,music_right_size-1, 0,width)
        ry0 = map(player.right.get(j), -1,1, 0,height)
        rx1 = map(j+1, 0,music_right_size-1, 0,width)
        ry1 = map(player.right.get(j+1), -1,1, 0,height)
        loudless = abs(player.left.get(j))
        sw = map(loudless, 0,1, 0.2,10)
        strokeWeight(sw)
        line(rx0,ry0, rx1,ry1)
        # point(rx,ry)
    # print(music_left_size, "----", music_right_size)
    return 
