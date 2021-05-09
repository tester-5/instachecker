import os
import time
import random
import requests

ani="""

- INFORMATION ✅
- Owner : @Hideable
- Languages : VB NET ,  C# , PYTHON



-----------------



"""
def cheker_insta():
	os.system("clear")
	global ani
	print(ani)
	file = open('userinsta.txt', 'r').readlines()
	for x in file:
	 u = x.strip()
	 url = "https://m.facebook.com/{}/".format(u)
	# print(url)
	 ss = requests.get(url)
	 chk = ss.status_code
#	 print(chk)
	 if chk==200:
	   print("==== USER ====")
	   print("User : "+u)
	   print("status  : Haya")
	   print("=============")
	   print(" ")
	 elif chk==404:
	   print("==== USER ====")
	   print("User : "+u)
	   print("status : Nya")
	   print("=============")
	   print(" ")


def user():
	   global ani
	   os.system("clear")
	   print(ani)
	   four=open("userinsta.txt","w")
	  
	   url=int(input("USER CHAND PET BE : :"))
	   for x in range(300):
	   	text='bagd4563oq91083_.k1pd._..1038dncl_.'
	   	word=''.join(random.choice(text) for x in range (url))
	   	four.write(word+"\n")
	   time.sleep(3)
	   print("")
	   print("> ALL USER SAVED IN FILE USERINSTA.TXT")
	   time.sleep(2)
user()
cheker_insta()
	   	
	   
