from random import random
import pyautogui as pt
from time import sleep
import random

from scipy import rand

from tinder_bot import Tinder

print("Strarting Tinder Bot...")
sleep(3)

heart_swibes = 0
x_swibes = 0

tn = Tinder(0,0)

for i in range(10):
    random_no = random.randrange(1,5)
    random_no_swibe = random.randrange(10)
    
    # Preforms simulated tinder swipes
    pt.navigate_to_next_picture(.5)
    pt.click(clicks=random_no, interval=0.3)
    tn.naviagate_to_information(0.3)
    pt.click()
    sleep(2)
    tn.navigate_to_down(0.3)
    pt.click()
    
    # swipw away rate = 1/10
    if random_no_swibe == 5:
        tn.navigate_to_x(0.3)
        pt.click()
        x_swibes += 1
    else: 
        tn.navigate_to_heart(0.3)
        pt.click()
        heart_swibes += 1
        
    print("""
          ------------------------------
          Total Swipes:
          Heart = {heart_swibes}
          X = {x_swibes}
          """)
    
    # Delays
    sleep(random_no)
