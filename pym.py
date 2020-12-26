import psutil
import serial
import time
import GPUtil




def connect(com):
    try:
        ser=serial.Serial(com,115200,timeout=0.5)
    except Exception as e:
        return False
    return ser

#自动从COM号中连接
for i in range(30):
    ser=connect("com"+str(i))
    if ser:
        break

#手动连接
# ser=serial.Serial("COM3",115200,timeout=0.5)



def x(cv):
    if cv<1024*1024*1024:
        return str(cv//(1024*1024))+"MB"
    else:
        return str(round(cv/(1024*1024*1024)))+"GB"
def le(st):
    if len(st)<5:
        return "  "+st
    elif len(st)>5:
        return " 100%"
    else:
        return st
while True:
    b=psutil.cpu_percent()
    c=psutil.virtual_memory()
    while b==0:
        b=psutil.cpu_percent()
    aa=str(b)+"%"
    cc=str(c.percent)+"%"
    if GPUtil.getGPUs():
        try:
            ee=str(round(100*GPUtil.getGPUs()[0].load,1))+"%"
        except Exception as e:
            ee="0.0%"
        aa,cc,ee=le(aa),le(cc),le(ee)
        q="cpu('%s','%s','%s')\r" % (aa,cc,ee)
    else:
        q="nonv('%s','%s')\r" % (aa,cc)
    ser.write(q.encode())
    time.sleep(1)
