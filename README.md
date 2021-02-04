# bt-hid-proxy

Idea is to allow a bluetooth keyboard to communicate with a device that can't support native bluetooth due to hardware or software limitations.

The simple magic trick is to use a raspberry pi (4 or Zero) in gadget mode, meaninng it's physically plugged into the device via USB to do the keyboard emulation after getting instructions from the bluetooth keyboard thanks to `evdev`.

## Instructions
- Run `git clone https://github.com/Hacksore/bt-hid-proxy.git` in the `pi` home directory
- Pair your keyboard to the pi
- Run `cd bt-hid-proxy`
- Run `sudo apt-get install -y ansible && ./setup.yaml`
- Enjoy your new "wired" keyboard


## Pairing your keyboard

Ensure you have enabled entryption for your device. Replace `BD_ADDR` with your keyboard's mac address as well as the name with the correct name.

```
device BD_ADDR {
    name "some_name";
    auth enable;
    encrypt enable;
}
```

`sudo bluetoothctl`


Scan for a keyboard

`scan on`


Once found 

`scan off`


Now attempt to pair to your keyboard

`pair <mac>`

Once you see the prompt for the pin code type it on your wireless keyboard and hit enter.

`trust <mac>`

Now trust for future connecftions

`connect <mac>`

Connect to the ketboard


## Credit
Some helpful stuff I used for reference
- https://mtlynch.io/key-mime-pi/
- https://gitlab.com/dcro/quimby/-/blob/master/quimby-relay
- https://github.com/gvalkov/python-evdev
- https://github.com/mikerr/pihidproxy
- https://www.raspberrypi.org/forums/viewtopic.php?t=138578