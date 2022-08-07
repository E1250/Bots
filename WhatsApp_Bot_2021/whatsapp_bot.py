import pyautogui as pt
import pyperclip as pc
from time import sleep
from whatsapp_responses import responses
# Mouce Click for mac
# mouce = Controller()

# instructions for our both
class WhatsApp:
    def __inti__(self,speed=0.5,click_speed =0.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
        
    # navigate to green dotes for new messages    
    def nav_green_dot(self):    
        try:
            position = pt.locateOnScreen("WhatsApp/green_dot.png", confidence=0.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,0,self.speed)
            pt.doubleClick(internal = self.click_speed)

            
        except Exception as e:
            print("Error: Image not found :ERROR " , e)


    def nav_input_box(self):
        try:
            position = pt.locateOnScreen(
                "WhatsApp/paper_clip.png", confidence=0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10,duration =self.speed)
            pt.doubleClick(internal=self.click_speed)

        except Exception as e:
            print("Error: Image not found :ERROR " , e)

    def nav_message(self):
        try:
            position = pt.locateOnScreen(
                "WhatsApp/paper_clip.png", confidence=0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, -50, duraion =self.speed)
        except Exception as e:
            print("Error: Image not found :ERROR ", e)

    def get_message(self):
        pt.doubleClick(internal=self.click_speed)
        sleep(self.speed)
        pt.rightClick(internal=self.click_speed)
        sleep(self.speed)
        pt.moveRel(10,10,duration=self.speed)
        sleep(self.speed)
        
        self.message = pc.paste()
        print(self.message)

    def send_message(self):
        try:
            # check last message is the same as the
            if self.message != self.last_message:
                bot_response = responses(self.message)
                print('you say: ',bot_response)
                pt.typewrite(bot_response, interval=0.1)
                pt.typewrite("\n", interval=0.1) # enter key
                
                self.last_message = self.message
            else:
                print('no messages')
        except Exception as e:
            print("some error ",str(e))

    def nav_x(self):
        try:
            position = pt.locateOnScreen(
                "WhatsApp/x.png", confidence=0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 10, duraion =self.speed)
            pt.click()
        except Exception as e:
            print("Error: Image not found :ERROR ", e)

wa_bot = WhatsApp(speed=0.5,click_speed=0.4)
sleep(2)

while True:
    wa_bot.nav_green_dot()
    wa_bot.nav_x()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()
    sleep(10)