'''
Once the file exists on the local machine (in this case "Hubble_Arp105.jpg"), you display it in GaiaSky by running the function j_display_image.

'''
import os
from py4j.clientserver import ClientServer, JavaParameters
import numpy as np

gateway = ClientServer(java_parameters=JavaParameters(auto_convert=True, auto_field=True))
apiv2 = gateway.entry_point.apiv2
# Base module
base = apiv2.base
# Time module
time = apiv2.time
# Camera module
camera = apiv2.camera
# Interactive camera module (sub-module of camera)
icam = camera.interactive
# UserInterface module
ui = apiv2.ui
# Scene
scene = apiv2.scene
# input
gaia_input = apiv2.input
# reference system
refsys = apiv2.refsys


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
ui.remove_all_objects()
    # j_display_image("Hubble_Arp105.jpg")
gateway.shutdown()


