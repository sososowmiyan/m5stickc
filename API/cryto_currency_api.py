from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import json


def setFont():
  lcd.clear()
  setScreenColor(0x006600)
  lcd.setRotation(1)
  lcd.font(lcd.FONT_Small)
  lcd.setTextColor(0xffffff,0x006600)




def getAPI():
  try:
    req = urequests.request(method='GET', url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC,ETH,LTC', headers={'X-CMC_PRO_API_KEY':'insertapihere','Accept':'application/json'})
    setFont()
    BTCviewCount = json.loads((req.text))["data"]["BTC"]["quote"]["USD"]["price"]
    ETHviewCount = json.loads((req.text))["data"]["ETH"]["quote"]["USD"]["price"]
    LTCviewCount = json.loads((req.text))["data"]["LTC"]["quote"]["USD"]["price"]
    lcd.print("BTC: $" + str(BTCviewCount), 5, 10)
    lcd.print("ETH: $" + str(ETHviewCount), 5, 30)
    lcd.print("LTC: $" + str(LTCviewCount), 5, 50)
  except:
    setScreenColor(0xff0000)
    
while True:
  getAPI()
  wait(300)

