import os
import urllib.request
from PIL import Image
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


# We can now use the modules

def j_orientate_to_ra_then_dec(final_ra, final_dec):
    camera.set_fov(100.0)
    time_for_transition = 1.0
    sleep_transition_factor = 1.5
    camera_position = [0.0, 0.0, 0.0]
    sync = False

    def j_do_transition():
        dirn = np.array(refsys.equatorial_to_cartesian(ra, dec, 1.0E9))
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

j_orientate_to_ra_then_dec(290.0, 30.0)

# End script neatly
base.settings_backup()
base.sleep(20.0)
ui.remove_all_objects()
base.settings_restore()
# Remember to shut down the connection before exiting
gateway.shutdown()
