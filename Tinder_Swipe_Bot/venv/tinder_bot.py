from time import sleep
import pyautogui as pt
class Tinder:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def navigate_to_heart(self,speed):
        position = pt.locateOnScreen('images/heart.png',confidence=0.8) # locate the heart icon
        self.x = position[0]+20
        self.y = position[1]+20
        pt.moveTo(self.x,self.y,duration=speed) # move to the heart icon
        print("moving to heart")
        sleep(0.5)
        
    def navigate_to_x(self, speed):
        position = pt.locateOnScreen(
            'images/x.png', confidence=0.8)  # locate the heart icon
        self.x = position[0]+20
        self.y = position[1]+20
        pt.moveTo(self.x, self.y, duration=speed)  # move to the heart icon
        print("moving to x")
        sleep(0.5)
        
    def navigate_to_info(self, speed):
        position = pt.locateOnScreen(
            'images/heart.png', confidence=0.8)  # locate the heart icon
        self.x = position[0]
        self.y = position[1]-55
        pt.moveTo(self.x, self.y, duration=speed)  # move to the heart icon
        print("moving to info")
        sleep(0.5)
        
    def navigate_to_down(self, speed):
        position = pt.locateOnScreen(
            'images/down_arrow.png', confidence=0.8)  # locate the heart icon
        self.x = position[0]
        self.y = position[1]-55
        pt.moveTo(self.x, self.y, duration=speed)  # move to the heart icon
        print("moving to down button")
        sleep(0.5)

    def navigate_to_next_picture(self, speed):
        position = pt.locateOnScreen(
            'images/profile.png', confidence=0.8)  # locate the heart icon
        self.x = position[0]+20
        self.y = position[1]+200
        pt.moveTo(self.x, self.y, duration=speed)  # move to the heart icon
        print("moving to new picture")
        sleep(0.5)
