from tkinter import HORIZONTAL
from turtle import circle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
# my
from matplotlib.widgets import Cursor, Button
import math


image = mpimg.imread(r'Szkolenie_embedded\project\squid_game.png')

fig, ax = plt.subplots()
im = ax.imshow(image)  # 1920 x 960 p


# my
cursor = Cursor(ax, horizOn=True, vertOn=True, color='green', linewidth=2.0)
height, width = im.get_size()
camera_height = 32  # in meters, height at which the camera is suspended from the ground
# triangle_2 = alfa_2 + beta_2 + 90° = 180° and alfa_2 + beta_2 = 90°


def oneclick(event):
    x1, y1 = event.xdata, event.ydata
    # for x1
    if x1 > width/2:
        alfa_1 = ((70*x1)/width) - 35  # -35° - +35°
    elif x1 < width/2:
        alfa_1 = ((70*x1)/width) - 35  # -35° - +35°
    else:
        alfa_1 = 0                     # -35° - +35°

    # for y1
    # alfa_2 + beta_2 = 90° => alfa_2 = 90° - beta_2
    alfa_2 = 90 - ((90*y1)/height)  # 0° - 90° really is beta
    
    print('-'*35)
    print('{:6.1f} x {:<5.1f} px'.format(x1, y1))
    print('{:5.1f}° x {:<5.1f}°'.format(alfa_1, alfa_2))

    ctg_alfa_2 = math.cos(math.radians(alfa_2))/math.sin(math.radians(alfa_2))
    tract_y = alfa_2_b = camera_height/ctg_alfa_2

    tract_x = alfa_2_b / math.tan(math.radians(90 - abs(alfa_1)))

    print('{:6.1f} x {:<4.1f} m'.format(tract_x, tract_y))
    tract_x_y = math.sqrt(math.pow(tract_x, 2) + math.pow(tract_y, 2))
    print('Total:  {:<5.1f} m'.format(tract_x_y))

# my
fig.canvas.mpl_connect('button_press_event', oneclick)




# x, y = 100, 100
# circle = patches.Circle((x, y), radius=20, linewidth=2, edgecolor='r')
# ax.add_patch(circle)


plt.show()
