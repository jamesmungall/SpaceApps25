'''
Once the file exists on the local machine (in this case "Hubble_Arp105.jpg"), you display it in GaiaSky by running this function.

'''
import os
def j_display_image(filename):
    # url = "https://assets.science.nasa.gov/dynamicimage/assets/science/missions/hubble/galaxies/interacting/Hubble_Arp105_WFC3_mstr_flat_cont_FINAL2.jpg"
    # urllib.request.urlretrieve(url, "Hubble_Arp105.jpg")
    if os.path.exists(filename):
        print("File exists!")
    else:
        print("File does not exist.")
    ui.preload_texture(os.path.abspath(filename))
    ui.display_image(1, os.path.abspath(filename), 0.0, 0.0)

  # Example usage
    # j_display_image("Hubble_Arp105.jpg")
