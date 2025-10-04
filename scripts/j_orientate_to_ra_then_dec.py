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
