# bt-hid-proxy

Idea is to allow a bluetooth keyboard to communicate with a device that can't support native bluetooth due to hardware or software limitations.

The simple magic trick is to use a raspberry pi (4 or Zero) in gadget mode, meaninng it's physically plugged into the device via USB to do the keyboard emulation after getting instructions from the bluetooth keyboard thanks to `evdev`.

# Instructions

- Pair your keyboard to the pi
- Run `sudo ./setup.sh`
- Reboot your pi
- Enjoy your new "wired" keyboard


# Credit
Some helpful stuff I used for reference
- https://mtlynch.io/key-mime-pi/
- https://gitlab.com/dcro/quimby/-/blob/master/quimby-relay
- https://github.com/gvalkov/python-evdev
- https://github.com/mikerr/pihidproxy
- https://www.raspberrypi.org/forums/viewtopic.php?t=138578