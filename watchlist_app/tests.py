from django.test import TestCase

# Create your tests here.
import time
from random import randint


print("on the count of")
for i in reversed(range(1,3)):
    print(i)

s = ''
for i in range(1,1000):
    count = randint(1,1000)
    while (count > 0):
        s += " "
        count -= 1
    if (i%10 == 0):
        print(s+"HAPPY NEW YEAR 2023")
        print(s+"From __Asad_Raza__XD")
    else:
        print(s + "*")
    
    s=""
    time.sleep(0.3)