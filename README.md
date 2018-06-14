# APN-Project
Piloter un ou plusieurs APN avec une RaspberryPI

## Setup
Raspberry PY with raspbian

### Gphoto2 and libgphoto2
http://gphoto.org/

https://github.com/jim-easterbrook/python-gphoto2

Installation de gphoto2
* sudo apt-get install gphoto2
Update de gphoto2 en 2.5.17 pour utilisation de libgphoto2
* wget https://raw.githubusercontent.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh && chmod +x gphoto2-updater.sh && sudo ./gphoto2-updater.sh

Python interface to libgphoto2
* sudo apt-get install python-dev
* sudo pip3 install gphoto2
