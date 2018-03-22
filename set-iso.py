#!/usr/bin/env python3

# python-gphoto2 - Python interface to libgphoto2
# http://github.com/jim-easterbrook/python-gphoto2
# Copyright (C) 2015  Jim Easterbrook  jim@jim-easterbrook.me.uk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import logging
import sys

import gphoto2 as gp

def main():
    # use Python logging
    logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    gp.check_result(gp.use_python_logging())
    
    # open camera connection
    camera = gp.check_result(gp.gp_camera_new())
    context = gp.gp_context_new()
    gp.check_result(gp.gp_camera_init(camera, context))
    #
    valIso = 1                 # 1=100, 25=25600 
    valImageformat = 32        # 32=RAW, 33=mRAW, 34=sRAW
    valWhitebalance = 1        # 1=Natural
    valShutterspeed = 20       # 15=1s
    valAperture = 0            # 0=min
    valCapturetarget = 1       # 1=Carte memoire
    
    # get configuration tree
    config = gp.check_result(gp.gp_camera_get_config(camera, context))
    # find the capture target config item
    iso = gp.check_result(gp.gp_widget_get_child_by_name(config, 'iso'))
    imageformat = gp.check_result(gp.gp_widget_get_child_by_name(config, 'imageformat'))
    whitebalance = gp.check_result(gp.gp_widget_get_child_by_name(config, 'whitebalance'))
    shutterspeed = gp.check_result(gp.gp_widget_get_child_by_name(config, 'shutterspeed'))
    aperture = gp.check_result(gp.gp_widget_get_child_by_name(config, 'aperture'))
    capturetarget = gp.check_result(gp.gp_widget_get_child_by_name(config, 'capturetarget'))
    # check value in range
    count = gp.check_result(gp.gp_widget_count_choices(iso))
    if valIso < 0 or valIso >= count:
        print('Parameter out of range')
        return 1
    # set value
    valIso = gp.check_result(gp.gp_widget_get_choice(iso, valIso))
    gp.check_result(gp.gp_widget_set_value(iso, valIso))
    valImageformat = gp.check_result(gp.gp_widget_get_choice(imageformat, valImageformat))
    gp.check_result(gp.gp_widget_set_value(imageformat, valImageformat))
    valWhitebalance = gp.check_result(gp.gp_widget_get_choice(whitebalance, valWhitebalance))
    gp.check_result(gp.gp_widget_set_value(whitebalance, valWhitebalance))
    valShutterspeed = gp.check_result(gp.gp_widget_get_choice(shutterspeed, valShutterspeed))
    gp.check_result(gp.gp_widget_set_value(shutterspeed, valShutterspeed))
    valAperture = gp.check_result(gp.gp_widget_get_choice(aperture, valAperture))
    gp.check_result(gp.gp_widget_set_value(aperture, valAperture))
    valCapturetarget = gp.check_result(gp.gp_widget_get_choice(capturetarget, valCapturetarget))
    gp.check_result(gp.gp_widget_set_value(capturetarget, valCapturetarget))
    # set config
    gp.check_result(gp.gp_camera_set_config(camera, config, context))
    # Shoot
    capture = gp.check_result(gp.gp_camera_capture(camera, 0, context))

    # Print Info
    print(capture.name)
    print(valAperture, valShutterspeed, valIso, valImageformat, valWhitebalance, valCapturetarget)
    # clean up
    gp.check_result(gp.gp_camera_exit(camera, context))
    return 0

if __name__ == "__main__":
    sys.exit(main())
