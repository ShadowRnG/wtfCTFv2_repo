from PIL import Image
import random

def newImg():
    img = Image.new('RGB', (300, 256))
    i = 0
    j = 0
    for i in range(300):
        for j in range(256):
            img.putpixel((i, j), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    img.save('sqr.png')

    return img

wallpaper = newImg()
wallpaper.show()
