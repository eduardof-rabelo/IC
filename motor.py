#import nidaqmx
import keyboard, time, sys
from threading import Thread

class Motor:
    def __init__(self, bit1, bit2, porta='Dev1/port0/line0:7', pos = 0, pulso = 1e-4):
        self.bit1 = bit1
        self.bit2 = bit2
        self.porta = porta
        self.pos = pos
        self.pulso = pulso
        self.exit = False
        self.continuar = 0

    def andar(self, steps, sentido):
        self.steps = steps
        self.sentido = sentido

        def monitorKey():
            while True:
                if keyboard.is_pressed('esc'):
                    self.continuar += 1
                    break

        Thread(target = monitorKey).start() 

        for i in range(steps):
            if self.exit == False:
                print(1)
                time.sleep(self.pulso)
                print(0)
                time.sleep(self.pulso)

                if(self.continuar != 0):
                    self.exit = True
                    break

                self.pos += 1
                print(self.pos)
            
            
'''
        with nidaqmx.Task() as task:
    	    task.do_channels.add_do_chan('Dev1/port0/line0:7')
    	    task.start()
            task.write([bit1])
    		time.sleep(pulso)
    		task.write([bit2])
    		time.sleep(pulso)
'''
