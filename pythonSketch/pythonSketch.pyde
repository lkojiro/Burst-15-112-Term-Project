#Logan Kojiro-112 term project
#Spring 2017

add_library('minim')
from ddf.minim import *
from ddf.minim.analysis import *
import random
import math
import os
from listSongs import *


song = None
songStr = None
fft = None


time=0
colorBox=0
mode='menu'
isLive=False
    

def setup():
    #Width=1024
    #Height=600
    global mode
    size(1024,600,P3D)
    if mode == 'menu':
        setupMenu()
    elif mode == 'vis':
        setupVisualizer()
    elif mode == 'settings':
        setupSettings()
    elif mode == 'live':
        setupLive()
    elif mode == 'help':
        setupHelp()

def draw():
    global mode
    if mode == 'vis':
        drawVisualizer()
    elif mode=='menu':
        drawMenu()
    elif mode == 'settings':
        drawSettings()
    elif mode == 'live':
        drawLive()
    elif mode =='help':
        drawHelp()

    keyPressed()
    mousePressed()
        
def keyPressed():
    global mode
    if mode == 'vis':
        keyPressedVisualizer()
    elif mode=='menu':
        keyPressedMenu()
    elif mode == 'settings':
        keyPressedSettings()
    elif mode == 'live':
        keyPressedLive()
    elif mode == 'help':
        keyPressedHelp()

        

    
    
def mousePressed():
    global mode
    if mode == 'vis':
        mousePressedVisualizer()
    elif mode=='menu':
        mousePressedMenu()
    elif mode == 'settings':
        mousePressedSettings()
    elif mode == 'live':
        mousePressedLive()
    elif mode == 'help':
        mousePressedHelp()

        
 ####### MENU ####### 
 
visualizeButtonColor = 255
settingsButtonColor = 255
liveButtonColor = 255
helpButtonColor = 255


def setupMenu():
    clear()
    if song!=None:
        song.close()
    
    
def updateMenu():
    global visualizeButtonColor
    global settingsButtonColor
    global liveButtonColor
    global helpButtonColor
    
    #Visualize Button
    if (mouseY<height/4+100 and mouseY>height/4+50 and mouseX<width/4+width/2 
        and mouseX>width/4):
        visualizeButtonColor=150
    else:
        visualizeButtonColor=255
    
    #Settings Button
    if (mouseY<height/4+200 and mouseY>height/4+150 and mouseX<width/4+width/2 
        and mouseX>width/4):
        settingsButtonColor=150
    else:
        settingsButtonColor=255
        
    #Live Button
    if (mouseY<height/4+300 and mouseY>height/4+250 and mouseX<width/4+width/2 
        and mouseX>width/4):
        liveButtonColor=150
    else:
        liveButtonColor=255
        
    #Help Button
    if (mouseY<height and mouseY>height-55 and mouseX>5 and mouseX<5+width/5):
        helpButtonColor = 150
    else:
        helpButtonColor = 255
        
        
    
def drawMenu():
    global visualizeButtonColor
    global settingsButtonColor
    global liveButtonColor
    global helpButtonColor
    updateMenu()
    
    photo = loadImage('background.jpg')
    #http://interfacelift.com/wallpaper/Dbc402ac/01936_bluetiles_1024x600.jpg
    image(photo,0,0)
    
    #Title Text
    stroke(0)
    fill(255)
    textAlign(CENTER)
    textSize(150)
    text(' B U R S T ',width/2,height/4)
    textSize(15)
    text("Logan Kojiro Spring '17 15-112 Term Project",width/2,height-20)

    #Visualize Button
    fill(visualizeButtonColor)
    rect(width/4,height/4+50,width/2,50,25)
    fill(0)
    textSize(45)
    text('Visualize',width/2,height/4+90)
    
    #Settings Button
    fill(settingsButtonColor)
    rect(width/4,height/4+150,width/2,50,25)
    fill(0)
    text('Choose Song',width/2,height/4+190)
    
    #Live Button
    fill(liveButtonColor)
    rect(width/4,height/4+250,width/2,50,25)
    fill(0)
    text('Do it Live!',width/2,height/4+290)
    
    #Help Button
    fill(helpButtonColor)
    rect(5,height-55,width/5,50,25)
    fill(0)
    textAlign(LEFT)
    text('Help',35,height-15)
    
def keyPressedMenu():
    global mode
    if key =='w':
        mode = 'vis'
        setup()
    elif key == 's':
        mode = 'settings'
        setup()

def mousePressedMenu():
    global visualizeButtonColor
    global settingsButtonColor
    global liveButtonColor
    global helpButtonColor
    global mode
    if (mouseY<height/4+100 and mouseY>height/4+50 and mouseX<width/4+width/2 
        and mouseX>width/4 and visualizeButtonColor==150 and mousePressed and songStr!=None):
        mode='vis'
        setup()
    elif (mouseY<height/4+200 and mouseY>height/4+150 and mouseX<width/4+width/2 
        and mouseX>width/4 and settingsButtonColor==150 and mousePressed):
        mode='settings'
        setup()
    elif (mouseY<height/4+300 and mouseY>height/4+250 and mouseX<width/4+width/2 
        and mouseX>width/4 and liveButtonColor==150 and mousePressed):
        mode='live'
        setup()
    elif (mouseY<height and mouseY>height-55 and mouseX>5 and mouseX<5+width/5
              and helpButtonColor==150 and mousePressed):
        mode='help'
        setup()
        

 ####### SETTINGS #######
 

quitButtonColor = 255  
 
class songButton(object):
    def __init__(self,file,x,y,h):
        self.buttonWidth=350
        self.song=file
        self.x=x
        self.y=y
        self.h=h
    def isOver(self):
        if (mouseX>self.x and mouseX<self.x+self.buttonWidth and 
                mouseY>self.y and mouseY<self.y+self.h):
            return True
    def isPressed(self):
        if (mouseX>self.x and mouseX<self.x+self.buttonWidth and 
                mouseY>self.y and mouseY<self.y+self.h and mousePressed):
            return True
 
songList=[]
buttonList=[]

def setupSettings():
    clear()
    global songList
    songList=getSongs()
    
def updateSettings():
    global quitButtonColor
    if mouseX<200 and mouseY<55:
        quitButtonColor=155
    else:
        quitButtonColor=255
    
def drawSettings():
    updateSettings()
    photo = loadImage('background.jpg')
    image(photo,0,0)
    
    #Title Text
    stroke(0)
    fill(255)
    textAlign(CENTER)
    textSize(50)
    text('Click to Select A Song',width/2,height/4)
    
    
    #Make Buttons
    drawButtons()
    
    #Quit Button
    textSize(45)
    fill(quitButtonColor)
    rect(5,5,width/5,50,25)
    fill(0)
    text('Menu',50,50)
    
def drawButtons():
    global songList,buttonList
    buttons=len(songList)
    #fit inside height/4 to height
    #width range is 100 to width-100
    buttonMargin=50
    buttonRows=len(songList)//2
    buttonHeight=(height-height/2)/buttonRows
    for i in range(len(songList)):
        song=songList[i]
        if i%2==0:
            x=100
        else:
            x=550
        if i%2 == 0:
            y=200+ i*buttonHeight/1.5
        else:
            y=200+ (i-1)*buttonHeight/1.5
        button=songButton(song,x,y,buttonHeight)
        buttonList.append(button)
        if button.isOver():
            fill(150)
        else:
            fill(255)
        rect(button.x,button.y,button.buttonWidth,button.h,20)
        textAlign(LEFT)
        textSize(buttonHeight/2)
        fill(0)
        text(button.song,button.x+5,button.y+buttonHeight/2)
    
def keyPressedSettings():
    global mode
    if key == 'm':
        mode = 'menu'
        setup()
    
def mousePressedSettings():
    global songStr,buttonlist,quitButtonColor,mode
    for button in buttonList:
        if button.isPressed():
            songStr=button.song
            mode='menu'
            setup()
    if mouseX<200 and mouseY<55 and quitButtonColor==155 and mousePressed:
        mode='menu'
        setup()
    
    
    
    
 ####### VISUALIZER #######
 
 
intensityAvg = 0
intensityList = []
listAvg = 0
isBeat = False
 
class shootingStar(object):
    def __init__(self,velocity,r=255,g=255,b=255):
        self.x=random.randint(400,600)
        self.y=random.randint(200,400)
        self.z=random.randint(-1200,-400)
        self.dz=velocity
        self.time=0
        self.RED=r
        self.GREEN=g
        self.BLUE=b
        #UP,DOWN,LEFT,RIGHT 0,1,2,3
        self.direction=random.randint(0,3)


 
 
def keyPressedVisualizer():
    global mode
    if key=='r':
        song.close()
        mode = 'menu'
        setup()

def mousePressedVisualizer():
    pass

def setupVisualizer():
    global song,songStr
    global fft
    minim=Minim(this)
    
    #if you get the 'NoneType' object has no attribute play error,
    #change the string in listSongs.py to match the location of 
        #your song directory
        
    if mode=='vis':
        song=minim.loadFile('songs/%s'%songStr,1024)
        song.play()
        song.loop()
    else:
        song=minim.getLineIn()
    fft=FFT(song.bufferSize(),song.sampleRate())

    
isBeat=False
wait=0
    
def updateVisualizer():
    global intensityAvg,intensityList,listAvg,fft
    intensitySum=0
    #gets average energy levels for sample
    for i in range(0,fft.specSize()):
        intensitySum+=fft.getBand(i)
    intensityAvg=intensitySum/fft.specSize()
    intensityList.append(intensityAvg)
    detectBeats()
    
    
def detectBeats():
    #algorithm from 
    #http://archive.gamedev.net/archive/reference/programming/features/beatdetection/index.html
    
    global intensityAvg,intensityList,listAvg,isBeat,wait
    if len(intensityList)>43:
        intensityList.pop(0)
    sum=0
    for level in intensityList:
        sum+=level
    listAvg=sum/len(intensityList)
    wait+=1
    C=getEnergyVariance()
    if intensityAvg>C*listAvg: 
        if wait<=10:
            isBeat=False
        elif wait>=10:
            wait=0
            isBeat=True
    else:
        isBeat=False

    
def getEnergyVariance(): 
    global intensityAvg, listAvg, intensityList
    #len intensityList=32
    V=0 #total variance in energy levels
    for E in intensityList:
        diff=(E-intensityAvg)**2
        V+=diff
    return (-0.0025714*V)+1.6142857


    
    
    
def drawVisualizer():
    global isBeat,time,colorBox
    updateVisualizer()
    colorBox+=1
    time+=1
    avg=((1.5*fft.getBand(2)+fft.getBand(4)+fft.getBand(6)+
         fft.getBand(8)+fft.getBand(10)+fft.getBand(12)+fft.getBand(14)+fft.getBand(16))/8)
    background(0.35*avg)
    drawBackground()
    drawFFT()
    drawBox(colorBox)
    
    
stars=[]
for i in range(1,5):
    stars.append(shootingStar(100))
    
    
def drawBackground():
    global intensityAvg,stars,prevX,isBeat
    drawTimeDomain()
    drawBars()
    fill(255)
    translate(0,0,-1000)
    
    if isBeat:
        for i in range(1,int(intensityAvg*50)):
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            stars.append(shootingStar(intensityAvg,r,g,b))
            
    starsToKeep=[]
    for i in range(len(stars)):
        star=stars[i]
        star.time+=1
        noStroke()
        if star.z>-1400:
            starsToKeep.append(star)
            pass
        star.z=star.z-0.5-2*star.dz
        
        if star.direction==0:
            star.y+=0.15
        elif star.direction==1:
            star.y-=0.15
        elif star.direction==2:
            star.x-=0.15
        else:
            star.x+=0.15
    
        
        translate(0,0,-star.z)
        fill(star.RED,star.GREEN,star.BLUE)
        ellipse(star.x,star.y,intensityAvg/2,intensityAvg/2)
        translate(0,0,star.z)
    stars=starsToKeep
    translate(0,0,1000)

prevX = 0

class bar(object):
    def __init__(self,energy):
        self.z=-1000
        self.y=420 #height/2
        self.w=30
        self.x=512-self.w/2 #width/2
        
barsList=[]

def drawBars():
    global isBeat,intensityAvg,barsList
    if isBeat:
        barsList.append(bar(intensityAvg))
    keep=[]
    for it in barsList:
        if it.z<0:
            keep.append(it)
        it.z+=intensityAvg*100
        it.y+=3+intensityAvg/2
        it.w+=13+intensityAvg*1.5
        it.x=512-it.w/2
    stroke(0)
    for it in barsList:
        fill(intensityAvg*150)
        rect(it.x,it.y,it.w,2)
        rect(it.x,height-it.y,it.w,2)
    

def drawTimeDomain():
    global fft,song
    stroke(255)
    translate(0,0,-1000)
    for i in range(fft.specSize()-1):
        line(-width+3*i,height/2+song.left.get(i)*150,-width+3*i+1,height/2+song.left.get(i+1)*150)
        line(2*width-3*i,height/2+song.right.get(i)*150,2*width-3*i+1,height/2+song.right.get(i+1)*150)
    translate(0,0,1000)
        

def drawBox(time):
    stroke(255)
    global intensityAvg,prevX
    translate(0,height/2+song.left.get(1000)*20,0)
    rotateX(prevX+0.015*intensityAvg)
    prevX+=0.015*intensityAvg
    rotateY(0.2)
    rotateZ(0.6)
    fill((fft.getBand(2))%255,fft.getBand(4)%255,fft.getBand(6)%255)
    avg=(1.5*fft.getBand(2)+fft.getBand(4)+fft.getBand(6))/3
    box(250+avg)

    
def drawFFT():
    stroke(146, 167, 181)
    fft.forward(song.mix)
    rotateY(math.pi/3)
    #Left Side
    for i in range(0,fft.specSize()-20):
        r=255/(i+1)*4
        g=255/(i+1)*8
        b=255/(i+1)*32
        stroke(r,g,b)
        fill(b,g,r)
        triangle(2*i-25,height,2*i,height-fft.getBand(i)*2,2*i+25,height)
        triangle(2*i-25,0,2*i,fft.getBand(i)*2,2*i+25,0)
        


    
    
    
    translate(width-1,0,0)
    rotateY(-math.pi/3)
    rotateY(-math.pi/3)
    
    #Right Side
    for i in range(0,fft.specSize()):
        r=255/(i+1)*4
        g=255/(i+1)*8
        b=255/(i+1)*32
        stroke(r,g,b)
        fill(b,g,r)
        triangle(width-2*i-25,height,width-2*i,height-fft.getBand(i)*2,width-2*i+25,height)
        triangle(width-2*i-25,0,width-2*i,fft.getBand(i)*2,width-2*i+25,0)
        
        
        
        
def drawInfo():
    global fft,intensityAvg,intensityList,ListAvg
    C=getEnergyVariance()
    intensityAvg>C*listAvg
        
        
        
####### LIVE #######
audio = None

def setupLive():
    setupVisualizer()
    
def keyPressedLive():
    global mode
    if key=='r':
        mode='menu'
        setup()

    
def mousePressedLive():
    pass

def drawLive():
    drawVisualizer()
    
    
####### HELP #######

def setupHelp():
    pass

def drawHelp():
    photo = loadImage('background.jpg')
    image(photo,0,0)
    fill(255)
    rect(15,15,width-30,height-30,10)
    #Title Text
    stroke(0)
    fill(0)
    textAlign(CENTER)
    textSize(50)
    text('Help',width/2,height/4)
    
    textAlign(LEFT)
    textSize(25)
    text('Visualize:   after selecting a song sit back and watch it come to life on screen',
         width/8,height/4+50)
    text('\n     press r at anytime to return to home screen',width/8,height/4+50)
    text('Choose a song: click to select a song to visualize \n     drag mp3 files into the songs folder to add to the list',
         width/8,height/4+150)
    text('Do it Live: opens a chanel to computers mic \n     try singing or clapping! \n     hit r to return to home screen',
         width/8,height/4+250)
    textAlign(CENTER)
    text('hit m to return to the home screen',width/2,height/4+400)
    
    

def keyPressedHelp():
    global mode 
    if key == 'm':
        mode = 'menu'
        setup()
    
def mousePressedHelp():
    pass