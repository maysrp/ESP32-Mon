from machine import I2C,Pin
import _thread,json,time
i2c=I2C(sda=Pin(5), scl=Pin(4), freq=40000000)
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c) 
WIDTH, HEIGHT=128,64
from writer import Writer
import freesans20


rhs = WIDTH -1
wri = Writer(oled, freesans20)

def cpu(b,d,e):
    oled.fill(0)
    Writer.set_textpos(oled, 0, 0) 
    wri.printstring('CPU')
    Writer.set_textpos(oled, 0, 50) 
    wri.printstring(' '+b,True)
    Writer.set_textpos(oled, 22, 0) 
    wri.printstring('MEM')
    Writer.set_textpos(oled, 22, 50) 
    wri.printstring(' '+d,True)
    Writer.set_textpos(oled, 44, 0) 
    wri.printstring('GPU')
    Writer.set_textpos(oled, 44, 50) 
    wri.printstring(' '+e,True)
    oled.show()

def nonv(b,d):
    oled.fill(0)
    Writer.set_textpos(oled, 10, 0) 
    wri.printstring('CPU')
    Writer.set_textpos(oled, 10, 50) 
    wri.printstring(' '+b,True)
    Writer.set_textpos(oled, 42, 0) 
    wri.printstring('MEM')
    Writer.set_textpos(oled, 42, 50) 
    wri.printstring(' '+d,True)
    oled.show()



    
# cpu('50.5%','50.5%','66.4%')
# nonv('50.5%','66.4%')