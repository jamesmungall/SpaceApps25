'''
Saves the image in the url to the local computer and save it as the file name given.

'''
import urllib.request
url = "https://assets.science.nasa.gov/dynamicimage/assets/science/missions/hubble/galaxies/interacting/Hubble_Arp105_WFC3_mstr_flat_cont_FINAL2.jpg"
urllib.request.urlretrieve(url, "Hubble_Arp105.jpg")
