from urllib.request import urlopen
import os

print("""   ____                           _                   _   _                  _    
  / ___|   ___    _   _   _ __   | |_    ___   _ __  | | | |   __ _    ___  | | __
 | |      / _ \  | | | | | '_ \  | __|  / _ \ | '__| | |_| |  / _` |  / __| | |/ /
 | |___  | (_) | | |_| | | | | | | |_  |  __/ | |    |  _  | | (_| | | (__  |   < 
  \____|  \___/   \__,_| |_| |_|  \__|  \___| |_|    |_| |_|  \__,_|  \___| |_|\_\
                                                                                  

""")

url = input("Paste your url, you want to hack: ")
freq = int(input("Write amount of views: "))


def success():
   print("Done, thanks! Kuczi$")

try:  
  for i in range (freq):
      response = urlopen(url)
  success()
except:
  print("Try url with https://")

os.system("pause")


 


