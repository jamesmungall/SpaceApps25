'''
Resizes image to a maximum of 2000 * 2000 and saves the image with a prefix "resized_"
Example usage: j_resize_image("NGC_2835.jpg") returns nothing but saves image to "resized_NGC_2835.jpg"
'''
from PIL import Image

def j_resize_image(filename):
    
    # Open image
    image = Image.open(filename)
    
    # Resize (width, height)
    image.thumbnail((2000, 2000))
    
    # Save it (overwrite or new file)
    image.save("resized_" + filename)
    