'''
Gets image from url and saves it to the name of the image
Example usage: j_get_image(url, name + ".jpg")
'''
import urllib.request
def j_get_image(url, name):
    urllib.request.urlretrieve(url, name)