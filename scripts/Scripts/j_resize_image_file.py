'''
Resizes image to a maximum of 2000 * 2000 and saves the image with a prefix "resized_"
Example usage: j_resize_image("NGC_2835.jpg") returns nothing but saves image to "resized_NGC_2835.jpg"
'''
from PIL import Image, ImageDraw

def j_resize_image(filename):
    
    # Open image
    image = Image.open(filename)
    
    # Resize (width, height)
    image.thumbnail((100, 100))
    
    # Save it (overwrite or new file)
    image.save("resized_" + filename)

'''
Crops image to a circle and saves the image with a prefix cropped_
Example usage: j_crop_image(name + ".jpg")
'''
def j_crop_image(filename):
    # Open image and ensure RGBA mode
    img = Image.open(filename).convert("RGBA")

    # Create same-size mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

    # Apply mask to image
    img.putalpha(mask)

    # Save as PNG to preserve transparency
    img.save("cropped_" + filename, format="PNG")