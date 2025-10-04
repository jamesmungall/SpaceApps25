def j_message_demos():
    text_1 = "Elliptical galaxy NGC 3561B (upper left) and spiral galaxy NGC 3561A (lower right) form a shimmering guitar " \
             "shape in the ongoing merger known collectively as Arp 105."
    text_2 = "NASA, ESA and M. West (Lowell Observatory); " \
             "Processing: Gladys Kober (NASA/Catholic University of America) "

    # ui.display_message(0, text, 0.2, 0.0, 1.0, 0.0, 0.0, 1.0, 20)
    ui.display_text(0,
                    text_1 + text_2,
                    0.1,  # x position on a scale 0.0 to 1.0
                    0.1,  # y position on a scale 0.0 to 1.0
                    0.2,  # max_w. Use 0.0 to let the system decide
                    0.4,  # max_h. Use 0.0 to let the system decide
                    1.0,  # red
                    0.0,  # green
                    0.0,  # blue
                    1.0,  # alpha
                    20.0)  # size
    #
    ui.display_popup_notification(text_1, 15.0)
    ui.display_popup_notification(text_2, 15.0)
