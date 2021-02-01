import os
import time
from evdev import InputDevice, categorize, ecodes
from enum import Enum
from keycodes import scan_to_hid, modifiers

# The virtual device to listen input from
device_path = os.environ.get('DEVICE_PATH', '/dev/input/event0')

# auto connect
device =  None
while device is None:
  try:
    device = InputDevice(device_path)
    print(device)
  except:
    print('No keyboard - waiting...')
    time.sleep(1)

# Location of HID file handle in which to write keyboard HID input.
hid_path = os.environ.get('HID_PATH', '/dev/hidg0')

modifier_state = 0
keys_down = set()

# keep input
device.grab()

def send_keys(packet):  
  with open(hid_path, 'wb+') as hid_handle:
    assert(len(packet) == 8)
    hid_handle.write(bytearray(packet))

for event in device.read_loop():
  if event.type != ecodes.EV_KEY:
    continue

  data = categorize(event)

  modifier = modifiers.get(data.scancode, None)
  if modifier:
    if data.keystate == data.key_down:
      modifier_state |= modifier
    if data.keystate == data.key_up:
      modifier_state &= ~modifier
  else:
    code = scan_to_hid.get(data.scancode, None)
    if code is None:
      print('Ignoring unknown key', data)
      continue

    if data.keystate == data.key_down:
      if len(keys_down) >= 6:
        print('Ignoring key due to rollover')
        continue
      keys_down.add(code)

    if data.keystate == data.key_up:
      keys_down.remove(code)

  # Build the packet
  packet = [modifier_state, 0] + [k for k in keys_down]
  packet += [0] * (8 - len(packet))

  # print(packet, bytes(packet))
  send_keys(packet)
