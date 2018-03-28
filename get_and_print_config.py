#!/usr/bin/env python3
# -*- coding: utf8 -*-
#Liste les APN détectés et propose le choix
#Récupère la configuration de celui sélectionné

from __future__ import print_function

import logging
import sys

import gphoto2 as gp

logFile = "get_and_print_config"

def main():
    # use Python logging
    logging.basicConfig(filename= logFile + '.log',
        format='%(asctime)s: %(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    gp.check_result(gp.use_python_logging())

    # choose camera
    camera_list = []
    for name, addr in gp.check_result(gp.gp_camera_autodetect()):
        camera_list.append((name, addr))
    if not camera_list:
        print('Err 1 : Pas d\'APN détecté !')
        return 1
    # sort by first item
    camera_list.sort(key=lambda x: x[0])
    # ask user to choose one
    for index, (name, addr) in enumerate(camera_list):
        print('{:d}:  {:s}  {:s}'.format(index, addr, name))
    choice = input('Indiquez le n° d\'APN choisi : ')
    # test answer
    try:
        choice = int(choice)
    except ValueError:
        print('Err 2 : Veuillez saisir un nombre !')
        return 2
    if choice < 0 or choice >= len(camera_list):
        print('Err 3 : Veuillez saisir une des valeurs proposée !')
        return 3
    # initialise chosen camera
    name, addr = camera_list[choice]
    camera = gp.Camera()
    context = gp.Context()
    # search ports for camera port name
    port_info_list = gp.PortInfoList()
    port_info_list.load()
    idx = port_info_list.lookup_path(addr)
    camera.set_port_info(port_info_list[idx])
    
    # init connection
    try:
        camera.init(context)
    except:
        print('Err 4 : Erreur à l\'ouverture de la connexion')
        return 4
    
    # get configuration tree
    config = gp.check_result(gp.gp_camera_get_config(camera, context))
    # find the capture target config item
    cameramodel = gp.check_result(gp.gp_widget_get_child_by_name(config, 'cameramodel'))
    iso = gp.check_result(gp.gp_widget_get_child_by_name(config, 'iso'))
    imageformat = gp.check_result(gp.gp_widget_get_child_by_name(config, 'imageformat'))
    whitebalance = gp.check_result(gp.gp_widget_get_child_by_name(config, 'whitebalance'))
    shutterspeed = gp.check_result(gp.gp_widget_get_child_by_name(config, 'shutterspeed'))
    aperture = gp.check_result(gp.gp_widget_get_child_by_name(config, 'aperture'))
    capturetarget = gp.check_result(gp.gp_widget_get_child_by_name(config, 'capturetarget'))
    
    confName = gp.check_result(gp.gp_widget_get_value(cameramodel))
    confIso = gp.check_result(gp.gp_widget_get_value(iso))
    confImageformat = gp.check_result(gp.gp_widget_get_value(imageformat))
    confWhitebalance = gp.check_result(gp.gp_widget_get_value(whitebalance))
    confShutterspeed = gp.check_result(gp.gp_widget_get_value(shutterspeed))
    confAperture = gp.check_result(gp.gp_widget_get_value(aperture))
    confCapturetarget = gp.check_result(gp.gp_widget_get_value(capturetarget))

    # Print Info
    print("====", confName, "====")
    print(">>>> Vitesse {}s - Ouverture f/{} - ISO {} ".format(confShutterspeed, confAperture, confIso))
    print(">>>> Balance {} - Format {} - Destination {} ".format(confWhitebalance, confImageformat, confCapturetarget))

    # clean up
    gp.check_result(gp.gp_camera_exit(camera, context))
    return 0

if __name__ == "__main__":
    sys.exit(main())
