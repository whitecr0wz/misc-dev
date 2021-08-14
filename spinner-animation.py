import os
from time import sleep

def loader(phrase):

 og = phrase
 animation = og

 z = 0

 while True:

      os.system("clear")
      print (animation)

      if (z == 5):
         return None

      animation = og

      if z == 0:

              animation = animation + "\\"
              z = z + 1

      elif z == 1:

              animation = animation + "|"
              z = z + 1

      elif z == 2:

              animation = animation + "/"
              z = z + 1

      elif z == 3:

              animation = animation + "-"
              z = z + 1

      elif z == 4:

              animation = og 
              z = z + 1

      sleep (0.1)

for x in range(6):
    loader("[+] Loading...")
