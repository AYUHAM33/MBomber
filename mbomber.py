import os
import random as r
import time as t

def banner():
  print("""
  
  ██████   ██████    ███████████                           █████                       
░░██████ ██████    ░░███░░░░░███                         ░░███                        
 ░███░█████░███     ░███    ░███  ██████  █████████████   ░███████   ██████  ████████ 
 ░███░░███ ░███     ░██████████  ███░░███░░███░░███░░███  ░███░░███ ███░░███░░███░░███
 ░███ ░░░  ░███     ░███░░░░░███░███ ░███ ░███ ░███ ░███  ░███ ░███░███████  ░███ ░░░ 
 ░███      ░███     ░███    ░███░███ ░███ ░███ ░███ ░███  ░███ ░███░███░░░   ░███     
 █████     █████    ███████████ ░░██████  █████░███ █████ ████████ ░░██████  █████    
░░░░░     ░░░░░    ░░░░░░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░ ░░░░░░░░   ░░░░░░  ░░░░░     
                                                                                      
                                                                            - by IMKutta  
                                                                                      """)
banner()

def ins_bomb():
  bombs = ['https://github.com/iMro0t/bomb3r.git' , 'https://github.com/Nikait/ni_bomber.git' , 'https://github.com/Bhai4You/otpbomber.git' , 'https://github.com/TheSpeedX/TBomb.git' , 'https://github.com/anubhavanonymous/XLR8_BOMBER.git' , 'https://github.com/un1cum/Beast_Bomber.git']
  i = 0
  for i in range(5):
    os.system("git clone " + bombs[i])
  #os.system("clear")
  #banner()
  #print("INSTALLATION SUCCESFUL")

c = input("ARE YOU SURE WANT TO INSTALL THE BOMBERS ??? (Y/N) \n I am not responsible for any harm caused by this script. -->")
if c == "Y" or c == "Yes" or c == "yes":
  ins_bomb()
else:
  print("Quitting...........")
  t.sleep(2)
  exit()
