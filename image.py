from PIL import Image

im = Image.open(r'f:\python\tset.bmp')

print(im.format, im.size,im.mode)


im.thumbnail((200,100))
im.save('thumb.jpg',"JPEG")