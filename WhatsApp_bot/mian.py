from turtle import pos
import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(2) # time to go to open whatsapp
position1 = pt.locateOnScreen("WhatsApp/smiley_paperclip.png", confidence=0.6)
x = position1[0]
y = position1[1]

# gets messages
def get_message():
    
    global x,y
    position = pt.locateOnScreen("WhatsApp/smiley_paperclip.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y,duration=0.5) # this duratoin is for mac 
    
    pt.moveTo(x+70,y-40,duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print('message receievd: '+whatsapp_message)
    
    return whatsapp_message
    
    
# posts
def post_response(message):
    global x,y
    
    position = pt.locateOnScreen(
        "WhatsApp/smiley_paperclip.png", confidence=0.6)
    x = position[0]
    y = position[1]
    
    pt.moveTo(x+200,y+20,duration=0.5)
    pt.click()
    pt.typewrite(message, interval=0.1)
    
    pt.typewrite("\n", interval=0.1)
    
# process responses
def process_response(message):
    random_no = random.randomrange(3)
    
    if "?" in str(message).lower():
        return "Don't ask me any qusetions"
    else :
        if random_no == 0:
            return "thats cool"
        elif random_no == 1:
            return "Remember to subscribe"
        else:
            return "i want to eat something"
       
# check for new messages       
def check_for_new_messages():
    pt.moveTo(x+50,y-35,duration=0.5)
    while True:
        # check for green do and messages
        try:
            position = pt.locateOnScreen("WhatsApp/green_circle.png",confidence=0.7)
            
            if position is not None:
                pt.moveTo(position,duration=0.5)
                pt.moveRel(-100,0)
                pt.click()
                sleep(0.5)
                # get_message()
                # post_response(process_response(get_message()))
                # pt.moveTo(x+50,y-35,duration=0.5)
        except(Exception):
            print("no new messages")
    
        if pt.pixelMatchesColor(int(x+50),int(y-35),(255,255,255),tolerance=10):
            print("it is white")
            prccessed_message = process_response(get_message())
            post_response(prccessed_message)
        else:
            print("no new messages yet")
        sleep(5)
    
check_for_new_messages()        

