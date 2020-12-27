# ESP32-Mon
ESP32 结合SSD1306 OLED 监控CPU 内存 GPU的使用(仅支持英伟达的GPU，若无英伟达的显卡则不显示GPU栏)

## ESP32

### 连线
|ESP32|OLED（IIC）|
|---|---|
|G4  |SCL|
|G5  |SDA|
|3v3 |Vdd|
|GND |GND|

### 上传
上传freesans20.py , ssd1306.py ,writer.py ,main.py 到你的ESP32 上。  
测试：cpu('10%','10%','10%','10%')  
若oled现在显示  
CPU 10%  
MEM 10%  
GPU 10%  
即表示上传完成。



## PC端

### 执行pym.py  
首先在安装python3，使用pip安装pyserial,GPUtil,psutil，这三个模块  
如果你知道你的com号，请把注释的 手动连接 取消注释，并且修改其中的COM号，然后再把自动从COM号中连接。  
若不知道COM请不用修改。

在PC上执行pym.py

### 自动运行pym.exe
点击pym.exe即可运行。 
可以使用pyinstaller 自己打包exe程序，目前的pym.exe为win10 64bit  
打包命令  
`pyinstaller -i f.ico -F pym.py`


## 外壳
文件中的3d打印的外壳，或者下载：
https://www.thingiverse.com/thing:2993338  
（目前我就是下载这个打印的外壳）

## 视频教程

https://www.bilibili.com/video/BV1b54y1t7DW  

https://www.acfun.cn/v/ac21105834



## 原理
python 通过psutil和GPUtil获取 计算器的CPU GPU 内存信息 通过pyserial 串口连接并发送给esp32然后在oled上显示数据。
