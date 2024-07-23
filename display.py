# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time
import subprocess

from PIL import Image, ImageDraw, ImageFont
import random



# image = Image.new("1", (width, height))
clock = Image.open("images/clock-icon.png").convert('1')
clock.save("out.png")
input()
dice = Image.open("images/dice_3d.png").convert('1')

randlist = { i: Image.open(f"images/output_dice_{i}.png").convert('1') for i in range(1,7) }
print(randlist)
#randlist = {1: one, 2: two, 3: three, 4: four, 5: five,6:six}
indexes = []
lastindex = -1
dice.save("out.png")

input()
random.shuffle(indexes)

n_images = random.randint(5,10)
print(n_images,"interations")
for _ in range(n_images):
    roll = random.randint(1,6)
    if roll == lastindex:
        print("same roll twice")
        continue
    lastindex = roll
    indexes.append(roll)


for i in indexes:
    randlist[i].save("out.png")
    time.sleep(0.2)
print(indexes[-1])