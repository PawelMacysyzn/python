from PIL import Image

from math import tan, pi
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def set_alfa_S(alpha_x, beta_z):
    sizeX, sizeY, sizeZ = 40, 50, 30

    image = Image.open(
        r'C:\Users\pmacyszyn_adm\Documents\python\python\Szkolenie_embedded\project\squid_game.png')
    x, z = image.size
    fig, ax = plt.subplots()
    im = ax.imshow(image)

    if 0 < alpha_x < 180 and 0 < beta_z < 180:
        x1 = sizeX/2 - (sizeY/2)/tan(alpha_x * pi / 180)
        z1 = sizeZ/2 - (sizeY/2)/tan(beta_z * pi / 180)
        if (0 <= x1 <= sizeX) and (0 <= z1 <= sizeZ):
            x1 = translate(x1, 0, sizeX, 0, x)
            z1 = translate(z1, 0, sizeZ, 0, z)
            #circle = patches.Circle((x1, z1), radius=20, linewidth=2, edgecolor="r")
            # ax.add_patch(circle)
            ax.add_patch(patches.FancyArrow(x1, z1 - 40, 0, 30, edgecolor="r"))
            ax.add_patch(patches.FancyArrow(x1 - 40, z1, 30, 0, edgecolor="r"))
            ax.add_patch(patches.FancyArrow(
                x1, z1 + 40, 0, -30, edgecolor="r"))
            ax.add_patch(patches.FancyArrow(
                x1 + 40, z1, -30, 0, edgecolor="r"))
        
        return x1, z1


alpha_x, beta_z = (90, 90)
print(set_alfa_S(alpha_x, beta_z))

plt.show()
