import os
from time import sleep

og = "[+] Loading..."
animation = og

z = 0

while True:

      os.system("clear")
      print (animation)

      if (z > 3):

            z = 0

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

      sleep (0.1)
