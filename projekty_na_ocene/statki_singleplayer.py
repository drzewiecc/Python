rzad1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad3=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad4=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad5=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad6=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad7=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad8=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad9=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rzad10=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#orientacja ---> poziom-1, pion-2
import random

# losowanie czworki
orientacja=random.randint(1,2)
if orientacja==1:
    #tu rzedy
    rzad=random.randint(1,10)
    miejsce=random.randint(1,10)
    
else:
    #tu kolumny