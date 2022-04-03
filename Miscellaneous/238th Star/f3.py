from re import A
from PIL import Image
import random
 
img = Image.open('pixelwtfctf.png')
pix = img.load()
 
x = 200
y = 12
a = 2
b = 23
pix[x, y] = (888, 888, 1, 254)

x = x + a
y = y + b
pix[x, y] = (1, 888, 888, 254)

x = x + a
y = y + b
pix[x, y] = (888, 1, 888, 254)

x = x + a
y = y + b
pix[x, y] = (888, 1, 888, 254)

x = x + a
y = y + b
pix[x, y] = (1, 888, 888, 254)

x = x + a
y = y + b
pix[x, y] = (888, 0, 888, 254)

x = x + 1
y = y + 0
pix[x, y] = (888, 1, 888, 254)

img.save('pixelwtfctf.png')
