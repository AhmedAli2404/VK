import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
#from pynput.keyboard import Controller



cap=cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)

detector=HandDetector(detectionCon=0.8)

keys=[["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L",";"],
    ["Z","X","C","V","B","N","M",",",".","/"],
        ["1","2","3","4","5","6","7","8","9","0"],
        ['[',']','{','}','(',')','*','&','^','%'],
        ['#','$','@','!','`','~','-','_','=','+'],
        ['Space']
        ]


finaltext=""

        # keyboard=Controller()

def draw_all(img,butttonlist):
    for button in buttonlist:
        
        x,y=button.pos
        w,h=button.size
        if button.text=="Space":
            cv2.rectangle(img,(x,y),(x+w+135,y+h),(0,0,0),cv2.FILLED)
        else:

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),cv2.FILLED)
        cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,
                        4,(255,255,255),4
                    )
    return img

class Button():

    def __init__(self,pos,text,size=[85,85]):
        self.pos=pos
        self.size=size
        self.text=text

buttonlist=[]
for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonlist.append(Button([100*j+50,100*i+50],key))


run=True
try:
    while run:
        success,img=cap.read()
        #img1=detector.findHands(img)
        allhands,img=detector.findHands(img)
        img=draw_all(img,buttonlist)
        
        
        lmList=allhands[0]["lmList"]
    
        if lmList:
            for button in buttonlist:
                x,y=button.pos
                w,h=button.size

                if x< lmList[8][0]<x+w and y< lmList[8][1]<y+h :
                    cv2.rectangle(img,(x,y),(x,y+h),(192,192,192),cv2.FILLED)
                    cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,
                                4,(255,255,255),4
                                )
                    l,info,img=detector.findDistance((lmList[8][0],lmList[8][1]),(lmList[12][0],lmList[12][1]),img)

                    if l<35:
                        
                        # keyboard.press("button.text")
                        cv2.rectangle(img,(x-10,y-10),(x+w+5,y+h+5),(128,128,128),cv2.FILLED)
                        cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,
                                    4,(255,255,255),4
                                    )
                        finaltext+=button.text
                        sleep(0.3)

                            
                    
        cv2.rectangle(img,(350,1100),(1300,630),(255,255,255),cv2.FILLED)
        cv2.putText(img,finaltext,(400,700),cv2.FONT_HERSHEY_PLAIN,
                                    5,(0,0,0),5
                                    )  
        
        cv2.imshow("Image",img)
        cv2.waitKey(1)    
except Exception as e:
    print(finaltext)
    run=False 


