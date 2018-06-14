#!/usr/bin/env python3
# -*- coding: utf8 -*-
#Liste les APN détectés et récupère leur configuration
#Récupère la configuration des paramètres de la liste

from __future__ import print_function

import logging
import sys

import gphoto2 as gp

logFile = sys.argv[0]
listeParametres = ('cameramodel', 'iso', 'imageformat', 'whitebalance', 'shutterspeed', 'aperture', 'capturetarget')
listeApn = ()

def main():
    # use Python logging
    logging.basicConfig(filename= logFile + '.log',
        format='%(asctime)s: %(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    gp.check_result(gp.use_python_logging())
    # find cameras
    cameras = gp.check_result(gp.gp_camera_autodetect())
    

    # détecte les APN connecté et pour chacun créé un dictionnaire de paramètre
    #>>> print(ListeApn)
    #{'APN4': {}, 'APN1': {'A': 1, 'C': 'pigeon', 'B': 2}, 'APN2': {'A': 3, 'C': 'coucou', 'B': 125}, 'APN3': {}}
    #>>> i = 'APN2'
    #>>> j = 'C'
    #>>> print(ListeApn.get(i).get(j))
    #coucou

    # pour chaque dictionnaire ouvre le connexion, charge les paramètres, ferme la connexion

    # affiche en colonne APN les lignes paramétres


if __name__ == "__main__":
    sys.exit(main())