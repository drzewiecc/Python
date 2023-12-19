#wyswietlamy
f=open("text.txt", "r")
print(f.read())
f.close()

#edytujemy
f=open("text.txt", "a")
f.write("\neee\n")

for i in f:
    print("Linijka: ", i)

f.close()

import os
import time
time.sleep(5)
os.system('clear')

print("\ngithub")