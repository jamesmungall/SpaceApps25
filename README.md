## Hubble Sky Viewer
We have created scripts in Python which run on the Gaia Sky application to help visualise the Hubble Space Telescope's high resolution images.

Our python scripts create a walkthough from earth, zooming in on low resolution textures and overlaying them with much higher resolution images taken from NASA's Hubble image archive.

This gives you a sense of perspective as to where these amazing images fit into the cosmos around us allowing the large image files from Hubble to be fully appreciated. We have included the detailed captions provided by NASA to help give more context for what you are seeing.

-------------
Find the main scripts in scripts>j_scripts:
main.py -> sets up the connection with the Gaia Sky application and executes our functions

j_resize_image_file.py -> resizes the image so that if it is too large to fit on the screen, it is compressed

j_border_image_file.py -> creates a border around the given image

j_get_image_file.py -> gets the image from the given url

j_read_csv_file.py -> parses a csv into rows getting the image name,url,ra,dec and 3 captions


A test csv file is called CelestialData.csv with 3 rows for the Triangulum Galaxy (M33), the Horsehead Nebula (B33) and the Whirlpool Galaxy (M51).

--------------
Go to https://jamesmungall.github.io/SpaceApps25/ for more information.



