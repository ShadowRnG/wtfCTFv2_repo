from PIL import Image
 
img = Image.open('pixelwtfctf.png')
pix = img.load()
 
for h in range(img.size[1]):
  for w in range(img.size[0]):
    p = pix[w,h]
    print(p)
