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

camera.focus_mode("earth")

# End script neatly
base.settings_backup()
base.sleep(20.0)



ui.remove_all_objects()
base.settings_restore()
# Remember to shut down the connection before exiting
gateway.shutdown()
