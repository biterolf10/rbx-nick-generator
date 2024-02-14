import win32api, win32con
import keyboard as kb
import pyautogui as pag
import random as rng
import time as t

pag.useImageNotFoundException()

def checkButton():   
  try:
    if pag.locateOnScreen("./press_button.png"):
      return True
  except pag.ImageNotFoundException:
    return False

def register():
  if checkButton()==True:
    win32api.SetCursorPos((int(pag.locateOnScreen("./press_button.png").left+(pag.locateOnScreen("./press_button.png").width/2)), int(pag.locateOnScreen("./press_button.png").top+(pag.locateOnScreen("./press_button.png").height/2))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
  
def main():
  letters = "1234567890qwertyuiopasdfghjklzxcvbnm_"

  nicklen = int(input("Nick length: "))
  attemps = int(input("Attemps: "))
  autoreg = bool(int(input("Auto registration ( 1 - Yes / 0 - No ): ")))
  
  print("You have 10 second to go in roblox web page and click on nickname entry field")
  t.sleep(10)
  
  for i in range(attemps):
    nick = ""
    
    for count in range(nicklen):
      rngletter = None
      if count==0:
        rngletter = letters[rng.randint(0, len(letters))-2]
      else:
        rngletter = letters[rng.randint(0, len(letters))-1]
      
      nick += rngletter
        
        
    kb.write(nick)
    
    t.sleep(.5)    
    
    if autoreg==True:
      register()
    
    if checkButton()==False:
      for _ in range(nicklen):
        kb.write("\b")
    else:
      break

main()