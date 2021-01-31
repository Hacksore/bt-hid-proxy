import os
from evdev import InputDevice, categorize, ecodes
from enum import Enum

# TODO: make some kind of config or something for this?
device = InputDevice("/dev/input/event2")
print(device)

# Location of HID file handle in which to write keyboard HID input.
hid_path = os.environ.get('HID_PATH', '/dev/hidg0')

KEY_CODE_TO_HID = {
    # 3: 0x48,  # Pause / Break
    14: 0x2a,  # Backspace / Delete
    15: 0x2b,  # Tab
    # 12: 0x53,  # Clear
    28: 0x28,  # Enter
    42: 0xe1,  # Shift (Left)
    29: 0xe0,  # Ctrl (left)
    56: 0xe1,  # Alt (left)
    # 19: 0x48,  # Pause / Break
    58: 0x39,  # Caps Lock
    # 21: 0x90,  # Hangeul
    # 25: 0x91,  # Hanja
    1: 0x29,  # Escape
    57: 0x2c,  # Spacebar
    # 33: 0x4b,  # Page Up
    # 34: 0x4e,  # Page Down
    # 35: 0x4d,  # End
    # 36: 0x4a,  # Home
    105: 0x50,  # Left Arrow
    103: 0x52,  # Up Arrow
    106: 0x4f,  # Right Arrow
    108: 0x51,  # Down Arrow
    # 41: 0x77,  # Select
    # 43: 0x74,  # Execute
    # 44: 0x46,  # Print Screen
    # 45: 0x49,  # Insert
    # 46: 0x4c,  # Delete
    # 47: 0x75,  # Help
    # 48: 0x27,  # 0
    # 49: 0x1e,  # 1
    # 50: 0x1f,  # 2
    # 51: 0x20,  # 3
    # 52: 0x21,  # 4
    # 53: 0x22,  # 5
    # 54: 0x23,  # 6
    # 55: 0x24,  # 7
    # 56: 0x25,  # 8
    # 57: 0x26,  # 9
    39: 0x33,  # Semicolon
    51: 0xc5,  # <
    13: 0x2e,  # Equal sign
    30: 0x04,  # a
    48: 0x05,  # b
    46: 0x06,  # c
    32: 0x07,  # d
    18: 0x08,  # e
    33: 0x09,  # f
    34: 0x0a,  # g
    35: 0x0b,  # h
    23: 0x0c,  # i
    36: 0x0d,  # j
    37: 0x0e,  # k
    38: 0x0f,  # l
    50: 0x10,  # m
    49: 0x11,  # n
    24: 0x12,  # o
    25: 0x13,  # p
    16: 0x14,  # q
    19: 0x15,  # r
    31: 0x16,  # s
    20: 0x17,  # t
    22: 0x18,  # u
    47: 0x19,  # v
    17: 0x1a,  # w
    45: 0x1b,  # x
    21: 0x1c,  # y
    44: 0x1d,  # z
    125: 0xe3,  # Windows key / Meta Key (Left)
    11: 0x62,  # Numpad 0
    2: 0x59,  # Numpad 1
    3: 0x5a,  # Numpad 2
    4: 0x5b,  # Numpad 3
    5: 0x5c,  # Numpad 4
    6: 0x5d,  # Numpad 5
    7: 0x5e,  # Numpad 6
    8: 0x5f,  # Numpad 7
    9: 0x60,  # Numpad 8
    10: 0x61,  # Numpad 9
    # 112: 0x3a,  # F1
    # 113: 0x3b,  # F2
    # 114: 0x3c,  # F3
    # 115: 0x3d,  # F4
    # 116: 0x3e,  # F5
    # 117: 0x3f,  # F6
    # 118: 0x40,  # F7
    # 119: 0x41,  # F8
    # 120: 0x42,  # F9
    # 121: 0x43,  # F10
    # 122: 0x44,  # F11
    # 123: 0x45,  # F12
    # 124: 0x68,  # F13
    # 125: 0x69,  # F14
    # 126: 0x6a,  # F15
    # 127: 0x6b,  # F16
    # 128: 0x6c,  # F17
    # 129: 0x6d,  # F18
    # 130: 0x6e,  # F19
    # 131: 0x6f,  # F20
    # 132: 0x70,  # F21
    # 133: 0x71,  # F22
    # 134: 0x72,  # F23
    # 144: 0x53,  # Num Lock
    # 145: 0x47,  # Scroll Lock
    # 161: 0x1e,  # !
    # 163: 0x32,  # Hash
    # 173: 0x2d,  # Minus
    # 179: 0xe8,  # Media play/pause
    # 168: 0xfa,  # Refresh
    # 186: 0x33,  # Semicolon
    # 187: 0x2e,  # Equal sign
    51: 0x36,  # Comma
    12: 0x2d,  # Minus sign
    52: 0x37,  # Period
    53: 0x38,  # Forward slash
    # 192: 0x35,  # Accent grave
    26: 0x2f,  # Left bracket ([, {])
    43: 0x31,  # Back slash
    27: 0x30,  # Right bracket (], })
    40: 0x34,  # Single quote
    41: 0x35,  # Accent grave (`)
}

def send(control_keys, keycode):
  if not keycode in KEY_CODE_TO_HID.keys():
    return

  with open(hid_path, 'wb+') as hid_handle:
    buf = [0] * 8
    buf[0] = control_keys
    buf[2] = KEY_CODE_TO_HID[keycode]
    hid_handle.write(bytearray(buf))
    hid_handle.write(bytearray([0] * 8))

# TODO: see if evdev has a lookup table already
class Keystate(Enum):
  UP = 0
  DOWN = 1
  HOLD = 2

  @staticmethod
  def values():
    return list(map(lambda c: c.value, Keystate))


control_keys = {
  ecodes.KEY_LEFTCTRL: False,
  ecodes.KEY_LEFTSHIFT: False,
  ecodes.KEY_LEFTALT: False,
  ecodes.KEY_LEFTMETA: False
}

print(control_keys)

control_chars = 0

for event in device.read_loop():
  # only allow for key input event
  if event.type != ecodes.EV_KEY:
    continue
  
  keycode = event.code
  if keycode in control_keys.keys():
    if not control_keys[keycode] and event.value in [Keystate.DOWN.value]:
      print('pressed key', categorize(event))
      control_keys[keycode] = True
    elif control_keys[keycode] and event.value == Keystate.UP.value:
      print('key up', categorize(event))
      control_keys[keycode] = False

  # TODO: get all modifiers working
  if event.value == Keystate.UP.value:
    for i, (k, v) in enumerate(control_keys.items()):
      if (control_keys[k]):
        control_chars |= 1 << i
      else:
        control_chars = 0

    # send code
    send(control_chars, event.code)