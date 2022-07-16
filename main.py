import random
import time
import os

# ASCII CARS: https://www.asciiart.eu/vehicles/cars
# ASCII CARS2: https://textart.io/art/tag/car/1

print("\033[0;31m▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ 　 \033[0;34m▒█▀▀▀█ ▀█▀ ▒█▀▄▀█ ▒█░▒█ ▒█░░░ ░█▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█")
print("\033[0;31m▒█▄▄▀ ▒█▄▄█ ▒█░░░ ▒█▀▀▀ 　 \033[0;34m░▀▀▀▄▄ ▒█░ ▒█▒█▒█ ▒█░▒█ ▒█░░░ ▒█▄▄█ ░▒█░░ ▒█░░▒█ ▒█▄▄▀")
print("\033[0;31m▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ 　 \033[0;34m▒█▄▄▄█ ▄█▄ ▒█░░▒█ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ░▒█░░ ▒█▄▄▄█ ▒█░▒█")

print("")
print("")
input("\033[0;34mPress Enter To Continue\033[0;31: \033[1;37m")
print("")
print("")
print("\033[1;34mLoading\033[0;31m...")

time.sleep(1.5)

global breakdown
breakdown = 20

global energy
energy = 5

global race
race = 0

global money
money = 0

global level
level = 1

global luck
luck = 0





###CARS###


#ASCII, SPEED(placement chance), HANDLING(multiplier), PRICE(price to buy), CARLEVEL(level of car)
car1 = ["""
      __
  ____|~\_
  [____|_|-]
   (_)   (_)
  """, 1, 1, 0, 1 ]





car2 = "s"
























###CARS-END###

global yourcar
yourcar = car1


carpicture = yourcar[0]
carspeed = yourcar[1]
carhandling = yourcar[2]
carprice = yourcar[3]
carlevel = yourcar[4]



def mainmenu():
  clear = lambda: os.system('clear')
  clear()


  
  print("\033[0;31m▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ 　 \033[0;34m▒█▀▀▀█ ▀█▀ ▒█▀▄▀█ ▒█░▒█ ▒█░░░ ░█▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█")
  print("\033[0;31m▒█▄▄▀ ▒█▄▄█ ▒█░░░ ▒█▀▀▀ 　 \033[0;34m░▀▀▀▄▄ ▒█░ ▒█▒█▒█ ▒█░▒█ ▒█░░░ ▒█▄▄█ ░▒█░░ ▒█░░▒█ ▒█▄▄▀")
  print("\033[0;31m▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ 　 \033[0;34m▒█▄▄▄█ ▄█▄ ▒█░░▒█ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ░▒█░░ ▒█▄▄▄█ ▒█░▒█")
  
  print("")
  print("")


  print("Car Handling \033[0;31m: \033[0;34m" + str(carhandling))
  print("Car Speed \033[0;31m: \033[0;34m" + str(carspeed))
  print("Luck \033[0;31m: \033[0;34m" + str(luck))
  print("Car Level \033[0;31m: \033[0;34m" + str(carlevel))
  print("")
  print("Energy \033[0;31m : \033[1;33m" + str(energy))
  print("\033[0;34mMoney \033[0;31m : \033[1;32m" + str(round(money, 1)) + " $")
  
  print("\033[0;34m")
  
  print("              ",carpicture)


  print("""
    \033[1;34m[1] \033[0;31m- \033[0;34mRace

    \033[1;34m[2] \033[0;31m- \033[0;34mCar Shop

    \033[1;34m[3] \033[0;31m- \033[0;34mAbility Shop

    \033[1;34m[4] \033[0;31m- \033[0;34mMotel

        
    \033[1;34m[5] \033[0;31m- \033[0;34mCredits


    
       
  """)

  choose = input("\033[1;34mEnter Option Here\033[1;31m: \033[1;37m")

  if choose == "1":
    if energy > 0:
      Startrace()
    else:
      print("")
      print("Not Enough Energy!")
      mainmenu()

  elif choose == "2":
    Carshop()

  elif choose == "3":
    Abilityshop()

  elif choose == "4":
    Motel()
  
  elif choose == "5":
    gameCredits()



def Startrace():
  global energy
  global money
  global race
  
  #Start Race

  print("")
  print("Starting Race\033[1;31m...")
  print("")
  race += 1
  print("\033[1;34mRace \033[1;31m" + str(race))
  print("")
  print()
  #print(("random 0,5-",race+3), "*",level,"-", luck,"-",energy/10)
  difficulty = round((random.uniform(0.5, race+3) * level - luck - (energy / 10)), 1)

  print("\033[1;34mCurrent Difficulty\033[1;31m: \033[1;34m" + str(difficulty))

  #race

  if carspeed > difficulty:
    victory = True
    placement = 1
  elif carspeed > difficulty*0.66:
    victory = False
    placement = 2
  elif carspeed > difficulty*0.33:
    victory = False
    placement = 3

  elif carspeed > difficulty*0.165:
    victory = False
    placement = 4

  elif carspeed <= difficulty*0.165:
    victory = False
    placement = 5


  moneygained = 10/placement*carhandling

  if victory == True:
    print("Victory!")
    moneygained = moneygained*1.25




  time.sleep(3)

  moneygained = round(moneygained, 1)
  energy -= 1
  money += moneygained
  print("Placement: ", placement)
  print("Money Gained:", moneygained)
  time.sleep(3)

def Carshop():

  clear = lambda: os.system('clear')
  clear()

  print("""
  \033[0;31m▒█▀▀█ ░█▀▀█ ▒█▀▀█ 　 \033[1;34m▒█▀▀▀█ ▒█░▒█ ▒█▀▀▀█ ▒█▀▀█ 
  \033[0;31m▒█░░░ ▒█▄▄█ ▒█▄▄▀ 　 \033[1;34m░▀▀▀▄▄ ▒█▀▀█ ▒█░░▒█ ▒█▄▄█ 
  \033[0;31m▒█▄▄█ ▒█░▒█ ▒█░▒█ 　 \033[1;34m▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄█ ▒█░░░

  """)
  
  print("\033[1;34m[1] \033[0;31m- \033[0;34mUpgrade Handing \033[1;35m| Current Level\033[0;31m: \033[1;34m" + str(carhandling))

  print("")
  
  print("\033[1;34m[2] \033[0;31m- \033[0;34mUpgrade Speed   \033[1;35m| Current Level\033[0;31m: \033[1;34m" + str(carspeed))

  print("")
  
  input("\033[1;34mEnter Option Here\033[1;31m: \033[1;37m")


















def Abilityshop():

  clear = lambda: os.system('clear')
  clear()
  
  print("ABILITY SHOP")
  
  print("\033[1;34m[4] \033[0;31m- \033[0;34mUpgrade Luck    \033[1;35m| Current Level\033[0;31m: \033[1;34m" + str(carhealth))

  print("")
  
  print("\033[1;34m[4] \033[0;31m- \033[0;34mUpgrade Luck    \033[1;35m| Current Level\033[0;31m: \033[1;34m" + str(luck))

def Motel():
  global energy
  
  clear = lambda: os.system('clear')
  clear()

  print("""
  \033[1;31m▒█▀▄▀█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█░░░ 
  ▒█▒█▒█ ▒█░░▒█ ░▒█░░ ▒█▀▀▀ ▒█░░░ 
  ▒█░░▒█ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█▄▄█
  """)
  
  print("\033[1;34m[1] \033[0;31m- \033[0;34mSleep In Motel",str(round((2+race), 1))+"$","\033[1;35m| \033[1;34mCurrent Energy\033[0;31m: \033[1;34m" + str(energy))

  print("")
  
  print("\033[1;34m[2] \033[0;31m- \033[0;34mExit To Menu")
  
  print("")
  
  motelchoose = input("\033[1;34mEnter Option Here\033[1;31m: \033[1;37m")


  if motelchoose == "1":
    if money >= 2:
      sleeping()
      energy += 5

    else:
      print("Not Enough Money")
      mainmenu()

  if motelchoose == "2":
    mainmenu()





def sleeping():
  for i in range(15):
      clear = lambda: os.system('clear')
      clear()
  
      print("""                   z                     
                               z                        
                                Z                       
                      .--.  Z Z                         
                     / _(c\   .-.     __                
                    | / /  '-;   \'-'`  `\______        
                    \_\/'/ __/ )  /  )   |      \--,    
                    | \`""`__-/ .'--/   /--------\  \   
                     \\`  ///-\/   /   /---;-.    '-'   
                                  (________\  \         
                                            '-'         
  """)
      
  
      time.sleep(0.3)
      clear = lambda: os.system('clear')
      clear()
  
      print("""              z                        
                              z                        
                            Z                         
                  .--.    Z                           
                 / _(c\   .-.     __                  
                | / /  '-;   \'-'`  `\______          
                \_\/'/ __/ )  /  )   |      \--,      
                | \`""`__-/ .'--/   /--------\  \     
                 \\`  ///-\/   /   /---;-.    '-'     
                              (________\  \          
                                        '-'          
  """)
  
  
  
  
      time.sleep(0.3)
      clear = lambda: os.system('clear')
      clear()
  
      print("""                z             
                             z                         
                           Z                        
                  .--.   Z                           
                 / _(c\   .-.     __                
                | / /  '-;   \'-'`  `\______        
                \_\/'/ __/ )  /  )   |      \--,    
                | \`""`__-/ .'--/   /--------\  \   
                 \\`  ///-\/   /   /---;-.    '-'   
                              (________\  \        
                                        '-'        
  """)
  
      time.sleep(0.3)  


def gameCredits():

  clear = lambda: os.system('clear')
  clear()
  
  print("\033[0;31mMade By\033[0;34m: \033[1;35mOtsoBear \033[0;34mAnd \033[1;35mKolmio")
  time.sleep(5)
  mainmenu()

while True:

  mainmenu()







  #print("""\033[1;35m                                                                                
#        _______       
#       //  ||\ \      
# _____//___||_\ \___  
# )  _          _    \  
# |_/ \________/ \___|  
#   \_/        \_/      
#  
#""")