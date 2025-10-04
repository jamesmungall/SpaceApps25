import os
from PIL import Image
from py4j.clientserver import ClientServer, JavaParameters
import numpy as np
import csv

from j_resize_image_file import j_resize_image
from j_read_csv_file import j_read_csv
from j_get_image_file import j_get_image

# region gaia_utilities

def j_display_image(filename):
    ui.remove_all_objects()
    if os.path.exists(filename):
        print("File exists!")
    else:
        print("File does not exist.")
    ui.preload_texture(os.path.abspath(filename))
    ui.display_image(1, os.path.abspath(filename), 0.0, 0.0)

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

rows = j_read_csv("CelestialData.csv")

name = rows[3][0]
url = rows[3][1]
ra = float(rows[3][2])
dec = float(rows[3][3])

j_get_image(url, name + ".jpg")

j_resize_image(name + ".jpg")

j_orientate_to_ra_then_dec(ra, dec)

j_display_image("resized_" + name + ".jpg")

# region endup
base.settings_backup()
base.sleep(5.0)
ui.remove_all_objects()
base.settings_restore()

# Remember to shut down the connection before exiting
gateway.shutdown()
# endregion