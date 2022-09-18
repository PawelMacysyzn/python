# <!-- https://micropython.org/unicorn/

# https://docs.micropython.org/en/latest/pyboard/quickref.html#

# Ustaw na zadaną lokaliację serwo

# Zapal diodę na 3 sekundy

# Optionalnie - wyśliwtlić na LCD "Boom!" -->

import machine
import pyb
import time
import framebuf
#prepare io
servo = pyb.Servo(1)
y12 = machine.Pin('Y12')
scl = machine.Pin('X9')
sda = machine.Pin('X10')
i2c = machine.I2C(scl=scl, sda=sda)
y4 = machine.Pin('Y4')
#prepare bmp buffs
fbuf = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)
logo = framebuf.FrameBuffer(bytearray(36 * 10 // 8), 36, 10, framebuf.MONO_HLSB)
#screen clear
fbuf.fill(0)
i2c.writeto(8, fbuf)
#fill screen buf
logo.fill(0)
logo.text('BOOM!', 0, 0, 0xffff)
logo.hline(0, 9, 96, 0xffff)
fbuf.fill(0)
fbuf.blit(logo, 14, 10)
adc_angle = pyb.ADC(y4).read()
#main event
servo.angle(adc_angle-127, 1500)
#wait for servo
time.sleep_ms(1500)
#led on
y12(1)
#screen on
i2c.writeto(8, fbuf)
#wait 3 sec
time.sleep(3)
#led off
y12(0)
#screen clear
fbuf.fill(0)
i2c.writeto(8, fbuf)