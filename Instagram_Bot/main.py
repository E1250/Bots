import pyautogui as pt
from time import sleep

class GuiCommands:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def navigate_to_heart(self,speed):
        position = pt.locateOnScreen("Instagram_Bot/images/book_mark.png",confidence=0.8)
        self.x = position[0]-510
        self.y = position[1]+10
        pt.moveTo(self.x,self.y,duration = speed)
        print("Naviageting To Heart!")
        sleep(0.3)


sleep(2)
commands = GuiCommands(0,0)

for i in range(5):
    try:
        commands.navigate_to_heart(1)
        if pt.pixelMatchesColor(pt.position().x,pt.position().y,(237,73,86),tolerance = 10):
            pt.scroll(-1000)
            sleep(0.3)
        else:
            pt.click()
            sleep(0.3)
            
    except Exception as e:
        print(e)
        pt.scroll(5000)   
        sleep(0.3)     
        













