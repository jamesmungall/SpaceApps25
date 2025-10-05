'''

'''
from PIL import Image, ImageOps
def j_border_image(filename):
    img = Image.open(filename)
    bordered = ImageOps.expand(img, border=20, fill='red')
    bordered.save(filename)
    