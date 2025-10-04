import os
from PIL import Image
from py4j.clientserver import ClientServer, JavaParameters
import numpy as np
import csv
import time

from j_resize_image_file import j_resize_image, j_crop_image
from j_read_csv_file import j_read_csv
from j_get_image_file import j_get_image

# region gaia_utilities
def j_display_image(filename):
    
    if os.path.exists(filename):
        print("File exists!")
    else:
        print("File does not exist.")
        
    gaia_input.wait_input()
    
    ui.remove_all_objects()
    print(os.path.abspath(filename))
    ui.preload_texture(os.path.abspath(filename))
    ui.display_image(0, os.path.abspath(filename), 0.0, 0.0)

def j_orientate_to_ra_then_dec(final_ra, final_dec):
    camera.set_fov(100.0)
    time_for_transition = 1.0
    sleep_transition_factor = 1.5
    camera_position = [0.0, 0.0, 0.0]
    sync = False

    def j_do_transition():
        dirn = refsys.equatorial_to_cartesian(ra, dec, 1.0E9)
        dirn = [dirn[0], dirn[1], dirn[2]]
        camera.transition(camera_position, dirn, up_vector, time_for_transition, sync)
        base.sleep(time_for_transition * sleep_transition_factor)

    ra = 0.0
    dec = 0.0
    up_vector = [0.0, 1.0, 0.0]
    j_do_transition()

    ra = final_ra
    j_do_transition()

    dec = final_dec
    j_do_transition()

def j_set_component_visibility():
    # this didnt work in gaia sky
    scene.set_component_type_visibility("stars", True)
    scene.set_component_type_visibility("planets", False)
    scene.set_component_type_visibility("moons", False)
    scene.set_component_type_visibility("satellites", False)
    scene.set_component_type_visibility("asteroids", False)
    scene.set_component_type_visibility("clusters", True)
    scene.set_component_type_visibility("milkyway", True)
    scene.set_component_type_visibility("galaxies", True)
    scene.set_component_type_visibility("nebulae", True)
    scene.set_component_type_visibility("meshes", False)
    scene.set_component_type_visibility("systems", False)
    scene.set_component_type_visibility("labels", True)
    scene.set_component_type_visibility("orbits", False)
    scene.set_component_type_visibility("locations", False)
    scene.set_component_type_visibility("countries", False)
    scene.set_component_type_visibility("ruler", False)
    scene.set_component_type_visibility("equatorial", True)
    scene.set_component_type_visibility("ecliptic", False)
    scene.set_component_type_visibility("galactic", False)
    scene.set_component_type_visibility("recursivegrid", False)
    scene.set_component_type_visibility("constellatios", False)
    scene.set_component_type_visibility("boundaries", False)
    scene.set_component_type_visibility("atmospheres", False)
    scene.set_component_type_visibility("clouds", False)
    scene.set_component_type_visibility("effects", True)
    scene.set_component_type_visibility("axes", False)
    scene.set_component_type_visibility("velocityvectors", False)
    scene.set_component_type_visibility("keyframes", False)
    scene.set_component_type_visibility("others", False)

def j_set_start_position():
    camera.set_fov(100.0)
    ui.remove_all_objects()
    base.sleep(2.0)
    
    scene.set_component_type_visibility("element.planets", True)
    # go to earth
    camera.go_to_object_instant("earth")
    gaia_input.wait_input()
    # toggle visibility of planets off
    scene.set_component_type_visibility("element.planets", False)

# endregion

# region setup
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
# endregion


j_set_start_position()

rows = j_read_csv("CelestialData.csv")

i = 2
name = rows[i][0]
url = rows[i][1]
ra = float(rows[i][2])
dec = float(rows[i][3])
text1 = rows[i][4]
text2 = rows[i][5]
text3 = rows[i][6]

#j_get_image(url, name + ".jpg")

#j_resize_image(name + ".jpg")

#j_crop_image("resized_" + name + ".jpg")


#j_orientate_to_ra_then_dec(ra, dec)

#camera.transition_fov(5.0, 2.5)

j_display_image("cropped_resized_" + name + ".jpg")

gaia_input.wait_input()
ui.display_text(0,text1,0.1,0.1,0.4,0.4,1.0,0.0,0.0,1.0,40.0)
gaia_input.wait_input()
ui.display_text(0,text2,0.1,0.1,0.4,0.4,1.0,0.0,0.0,1.0,40.0)
gaia_input.wait_input()
ui.display_text(1,text3,0.1,0.1,0.4,0.2,1.0,0.0,0.0,1.0,40.0)
gaia_input.wait_input()


# region endup
base.settings_backup()
base.sleep(2.0)
#gaia_input.wait_input()
ui.remove_all_objects()
base.settings_restore()

# Remember to shut down the connection before exiting
gateway.shutdown()
# endregion