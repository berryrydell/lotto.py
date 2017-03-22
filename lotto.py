import random
import sys
import os

print "wygeneruje liste 8 losowych liczb z zakresu 1-49"

nums=(range(1,50))
lista=[]
for x in range(8):
    y=random.choice(nums)
    lista.append(y)
    nums.remove(y)
final=sorted(lista)
print final

