import pyautogui as pt
import pyperclip as pc  # for copying pasting text
from time import sleep

pt.FAILSAFE = True

# nov to any images
def nav_to_image(image,clicks,off_x = 0 ,off_y = 0):
    position = pt.locateCenterOnScreen(image, confidence=0.7)
    if position is None:
        print("image not found")
        return 0
    else:
        pt.moveTo(position,duration=0.5)
        pt.moveRel(off_x,off_y,duration=0.2)
        pt.click(clicks=clicks,interval=0.1)
        
def get_message():
    nav_to_image("WhatsApp_Bot_last\images\paper_clib.png", clicks=1, off_y=-100,off_x=90)
    pt.click(clicks=3, interval=0.1)
    pt.rightClick()
    copy = nav_to_image('WhatsApp_Bot_last\images\copy.png', clicks=1)
    sleep(0.5)
    pt.click(clicks=1, interval=0.1)
    
    return pc.paste() if copy != 0 else 0

def send_message(msg):
    nav_to_image("WhatsApp_Bot_last\images\paper_clib.png", clicks=1,off_x=100)
    pt.typewrite(msg, interval=0.1) 
    # pt.typewrite("\n", interval=0.1) // enter key
    
def close_reply_box():
       nav_to_image("WhatsApp_Bot_last\images\close.png", clicks=2)
       pt.click(clicks=1, interval=0.1)
       
def process_message(msg):
    raw_message =msg.lower()
    
    if raw_message == 'hello':
        return "Hey there!"
    elif raw_message =="yes":
        return " BOT says you wrote yes"
    elif raw_message =="ok":
        return "OK!!!"
    elif "hey" in raw_message:
        return "What's up?"
    else:
        return "I don't understand"
         
sleep(2)

# Loop the codec
delay = 10 #check message every 10 seconds
last_message = ''

while True:
    # check for new messages
    nav_to_image("WhatsApp_Bot_last\images\green_dot.png", clicks=1,off_x=-100) # selecting new messages
    close_reply_box()
    message = get_message()
    
    if message !=  0 and message != last_message:
        last_message = message
        send_message(process_message(message))
    else:
        print("No new message")   
        
    sleep(10)    
    
    
  
