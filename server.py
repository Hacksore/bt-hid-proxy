import os
import time
from evdev import InputDevice, categorize, ecodes
from enum import Enum

# The virtual device to listen input from
device_path = os.environ.get('DEVICE_PATH', '/dev/input/event0')

# auto connect
device =  None
while device is None:
  try:
    device = InputDevice(device_path)
    print(device)
  except:
    print "No keyboard - waiting..."
    time.sleep(1)

# Location of HID file handle in which to write keyboard HID input.
hid_path = os.environ.get('HID_PATH', '/dev/hidg0')

scan_to_hid = {
  # Reserved: 0
  # ErrorRollOver: 1
  # POSTFail: 2
  # ErrorUndefined: 3

  ecodes.KEY_A: 0x04,
  ecodes.KEY_B: 0x05,
  ecodes.KEY_C: 0x06,
  ecodes.KEY_D: 0x07,
  ecodes.KEY_E: 0x08,
  ecodes.KEY_F: 0x09,
  ecodes.KEY_G: 0x0a,
  ecodes.KEY_H: 0x0b,
  ecodes.KEY_I: 0x0c,
  ecodes.KEY_J: 0x0d,
  ecodes.KEY_K: 0x0e,
  ecodes.KEY_L: 0x0f,
  ecodes.KEY_M: 0x10,
  ecodes.KEY_N: 0x11,
  ecodes.KEY_O: 0x12,
  ecodes.KEY_P: 0x13,
  ecodes.KEY_Q: 0x14,
  ecodes.KEY_R: 0x15,
  ecodes.KEY_S: 0x16,
  ecodes.KEY_T: 0x17,
  ecodes.KEY_U: 0x18,
  ecodes.KEY_V: 0x19,
  ecodes.KEY_W: 0x1a,
  ecodes.KEY_X: 0x1b,
  ecodes.KEY_Y: 0x1c,
  ecodes.KEY_Z: 0x1d,

  ecodes.KEY_1: 0x1e,
  ecodes.KEY_2: 0x1f,
  ecodes.KEY_3: 0x20,
  ecodes.KEY_4: 0x21,
  ecodes.KEY_5: 0x22,
  ecodes.KEY_6: 0x23,
  ecodes.KEY_7: 0x24,
  ecodes.KEY_8: 0x25,
  ecodes.KEY_9: 0x26,
  ecodes.KEY_0: 0x27,

  ecodes.KEY_ENTER: 0x28,
  ecodes.KEY_ESC: 0x29,
  ecodes.KEY_BACKSPACE: 0x2a,
  ecodes.KEY_TAB: 0x2b,
  ecodes.KEY_SPACE: 0x2c,

  ecodes.KEY_MINUS: 0x2d,
  ecodes.KEY_EQUAL: 0x2e,
  ecodes.KEY_LEFTBRACE: 0x2f,
  ecodes.KEY_RIGHTBRACE: 0x30,
  ecodes.KEY_BACKSLASH: 0x31,
  # Non-US # and ~: 0x32,
  ecodes.KEY_SEMICOLON: 0x33,
  ecodes.KEY_APOSTROPHE: 0x34,
  ecodes.KEY_GRAVE: 0x35,
  ecodes.KEY_COMMA: 0x36,
  ecodes.KEY_DOT: 0x37,
  ecodes.KEY_SLASH: 0x38,

  ecodes.KEY_CAPSLOCK: 0x39,

  ecodes.KEY_F1: 0x3a,
  ecodes.KEY_F2: 0x3b,
  ecodes.KEY_F3: 0x3c,
  ecodes.KEY_F4: 0x3d,
  ecodes.KEY_F5: 0x3e,
  ecodes.KEY_F6: 0x3f,
  ecodes.KEY_F7: 0x40,
  ecodes.KEY_F8: 0x41,
  ecodes.KEY_F9: 0x42,
  ecodes.KEY_F10: 0x43,
  ecodes.KEY_F11: 0x44,
  ecodes.KEY_F12: 0x45,

  ecodes.KEY_PRINT: 0x46,
  ecodes.KEY_SCROLLLOCK: 0x47,
  ecodes.KEY_PAUSE: 0x48,
  ecodes.KEY_INSERT: 0x49,
  ecodes.KEY_HOME: 0x4a,
  ecodes.KEY_PAGEUP: 0x4b,
  ecodes.KEY_DELETE: 0x4c,
  ecodes.KEY_END: 0x4d,
  ecodes.KEY_PAGEDOWN: 0x4e,

  ecodes.KEY_RIGHT: 0x4f,
  ecodes.KEY_LEFT: 0x50,
  ecodes.KEY_DOWN: 0x51,
  ecodes.KEY_UP: 0x52,
  ecodes.KEY_NUMLOCK: 0x53,
  ecodes.KEY_KPSLASH: 0x54,
  ecodes.KEY_KPASTERISK: 0x55,
  ecodes.KEY_KPMINUS: 0x56,
  ecodes.KEY_KPPLUS: 0x57,
  ecodes.KEY_KPENTER: 0x58,

  ecodes.KEY_KP1: 0x59,
  ecodes.KEY_KP2: 0x5a,
  ecodes.KEY_KP3: 0x5b,
  ecodes.KEY_KP4: 0x5c,
  ecodes.KEY_KP5: 0x5d,
  ecodes.KEY_KP6: 0x5e,
  ecodes.KEY_KP7: 0x5f,
  ecodes.KEY_KP8: 0x60,
  ecodes.KEY_KP9: 0x61,
  ecodes.KEY_KP0: 0x62,

  ecodes.KEY_KPDOT: 0x63,
  # non-us / and |: 0x64,
  ecodes.KEY_APPSELECT: 0x65,
  ecodes.KEY_POWER: 0x66,
  ecodes.KEY_KPEQUAL: 0x67,

  ecodes.KEY_F13: 0x68,
  ecodes.KEY_F14: 0x69,
  ecodes.KEY_F15: 0x6a,
  ecodes.KEY_F16: 0x6b,
  ecodes.KEY_F17: 0x6c,
  ecodes.KEY_F18: 0x6d,
  ecodes.KEY_F19: 0x6e,
  ecodes.KEY_F20: 0x6f,
  ecodes.KEY_F21: 0x70,
  ecodes.KEY_F22: 0x71,
  ecodes.KEY_F23: 0x72,
  ecodes.KEY_F24: 0x73,

  # execute
  ecodes.KEY_HELP: 0x75,
  ecodes.KEY_MENU: 0x76,
  ecodes.KEY_SELECT: 0x77,
  ecodes.KEY_STOP: 0x78,
  ecodes.KEY_AGAIN: 0x79,
  ecodes.KEY_UNDO: 0x7a,
  ecodes.KEY_CUT: 0x7b,
  ecodes.KEY_COPY: 0x7c,
  ecodes.KEY_PASTE: 0x7d,
  ecodes.KEY_FIND: 0x7e,

  ecodes.KEY_MUTE: 0x7f,
  ecodes.KEY_VOLUMEUP: 0x80,
  ecodes.KEY_VOLUMEDOWN: 0x81,
  ecodes.KEY_KPCOMMA: 0x85,
  ecodes.KEY_KPEQUAL: 0x86,
  ecodes.KEY_SYSRQ: 0x9a,
}


modifier_state = 0
keys_down = set()

modifiers = {
  ecodes.KEY_LEFTCTRL: 1 << 0,
  ecodes.KEY_LEFTSHIFT: 1 << 1,
  ecodes.KEY_LEFTALT: 1 << 2,
  ecodes.KEY_LEFTMETA: 1 << 3,

  ecodes.KEY_RIGHTCTRL: 1 << 4,
  ecodes.KEY_RIGHTSHIFT: 1 << 5,
  ecodes.KEY_RIGHTALT: 1 << 6,
  ecodes.KEY_RIGHTMETA: 1 << 7,
}

# keep input guarded
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
