from m5stack import *
from m5ui import *
from uiflow import *
lcd.setRotation(1)

setScreenColor(0x111111)

def buttonA_wasPressed():
  # global params
  lcd.print('Led is ON!', 50, 50, 0xffffff)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonA_wasReleased():
  # global params
  lcd.print('Led Off :(', 50, 50, 0xffffff)
  pass
btnA.wasReleased(buttonA_wasReleased)


setScreenColor(0x33ccff)
