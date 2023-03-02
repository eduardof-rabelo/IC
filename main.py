from motor import Motor
import keyboard, time, sys
from threading import Thread
import tkinter as tk

'''
#PINOS DE COMUNICAÇÃO EM BINÁRIO
#[0,1,2,3, 4, 5, 6,  7] - BITS DA PLACA
#[1,2,4,8,16,32,64,128] - SINAL DE COMUNICAÇÃO CORRESPONDENTE
'''   

mx = Motor(4, 8)
my = Motor(16, 32)

dx, dy = 2700, 270

while(my.pos <= 2700):
    mx.andar(dx, 1)
    if(mx.exit == True):
        break
    my.andar(dy, 1)
    if(my.exit == True):
        break
    mx.andar(dx, 0)
    if(mx.exit == True):
        break
    my.andar(dy, 1)
    if(my.exit == True):
        break
    
print(mx.pos, my.pos)
print('cabou')