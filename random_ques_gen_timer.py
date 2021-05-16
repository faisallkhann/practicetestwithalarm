from os import sep
import random
import time
import winsound
from colorama import Fore, Back, Style
from colorama import init
import colorama

init()

print(Fore.YELLOW +'''

██████  ██████   █████   ██████ ████████ ██  ██████ ███████     ████████ ███████ ███████ ████████     ██     ██ ██ ████████ ██   ██     ████████ ██ ███    ███ ███████ ██████  
██   ██ ██   ██ ██   ██ ██         ██    ██ ██      ██             ██    ██      ██         ██        ██     ██ ██    ██    ██   ██        ██    ██ ████  ████ ██      ██   ██ 
██████  ██████  ███████ ██         ██    ██ ██      █████          ██    █████   ███████    ██        ██  █  ██ ██    ██    ███████        ██    ██ ██ ████ ██ █████   ██████  
██      ██   ██ ██   ██ ██         ██    ██ ██      ██             ██    ██           ██    ██        ██ ███ ██ ██    ██    ██   ██        ██    ██ ██  ██  ██ ██      ██   ██ 
██      ██   ██ ██   ██  ██████    ██    ██  ██████ ███████        ██    ███████ ███████    ██         ███ ███  ██    ██    ██   ██        ██    ██ ██      ██ ███████ ██   ██ 
                                                                   By - Faisal Khan
                                                                   Date - May 16, 2021                                         
                                                                                                                                                                               

''')

fname = open('questions.txt', 'r')
ques = fname.readlines()
numb = input("How many questions do you want to practice?: ")
dura_sec = input("Enter the time duration (in Minutes): ")
dura_sec = float(dura_sec)
dura_min = dura_sec * 60

lst = random.sample(ques, int(numb))

print(Fore.GREEN + "_______________________________Start____________________________________ \n")

print(*lst, sep = "\n")

print(Fore.GREEN + "________________________________End____________________________________ \n")

print(Fore.RESET +" ")

time.sleep(dura_min)

beepdura = 5000
freq = 700
winsound.Beep(freq, beepdura)





