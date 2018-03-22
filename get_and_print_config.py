import gphoto2 as gp

def main():
    # use Python logging
    #logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    #gp.check_result(gp.use_python_logging())
    
    # open camera connection
    camera = gp.check_result(gp.gp_camera_new())
    context = gp.gp_context_new()
    gp.check_result(gp.gp_camera_init(camera, context))
    
    # get configuration tree
    config = gp.check_result(gp.gp_camera_get_config(camera, context))
    # find the capture target config item
    iso = gp.check_result(gp.gp_widget_get_child_by_name(config, 'iso'))
    imageformat = gp.check_result(gp.gp_widget_get_child_by_name(config, 'imageformat'))
    whitebalance = gp.check_result(gp.gp_widget_get_child_by_name(config, 'whitebalance'))
    shutterspeed = gp.check_result(gp.gp_widget_get_child_by_name(config, 'shutterspeed'))
    aperture = gp.check_result(gp.gp_widget_get_child_by_name(config, 'aperture'))
    capturetarget = gp.check_result(gp.gp_widget_get_child_by_name(config, 'capturetarget'))
    
    confIso = gp.check_result(gp.gp_widget_get_value(iso))
    confImageformat = gp.check_result(gp.gp_widget_get_value(imageformat))
    confWhitebalance = gp.check_result(gp.gp_widget_get_value(whitebalance))
    confShutterspeed = gp.check_result(gp.gp_widget_get_value(shutterspeed))
    confAperture = gp.check_result(gp.gp_widget_get_value(aperture))
    confCapturetarget = gp.check_result(gp.gp_widget_get_value(capturetarget))

    # Print Info
    print(">>>> Vitesse {} Ouverture {} ISO {} ".format(confShutterspeed, confAperture, confIso))
    print(">>>> Balance {} Format {} Destination {} ".format(confWhitebalance, confImageformat, confCapturetarget))

    # clean up
    gp.check_result(gp.gp_camera_exit(camera, context))
    return 0

if __name__ == "__main__":
    sys.exit(main())