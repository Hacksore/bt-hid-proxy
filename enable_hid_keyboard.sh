#!/usr/bin/env bash

# Echo commands to stdout.
set -x

# Exit on first error.
set -e

# Treat undefined environment variables as errors.
set -u

if ! grep 'dtoverlay=dwc2' /boot/config; then
  echo "dtoverlay=dwc2" >> /boot/config.txt
fi

if ! grep dwc2 /etc/modules; then
  echo "dwc2" >> /etc/modules
fi

ENABLE_RPI_HID_PATH=/opt/enable-rpi-hid
ENABLE_RPI_HID_DIR=$(dirname $ENABLE_RPI_HID_PATH)

mkdir -p "$ENABLE_RPI_HID_DIR"
wget https://raw.githubusercontent.com/mtlynch/ansible-role-key-mime-pi/master/files/enable-rpi-hid \
  -O "$ENABLE_RPI_HID_PATH"
chmod +x "$ENABLE_RPI_HID_PATH"

cd $(mktemp -d)
wget https://raw.githubusercontent.com/mtlynch/ansible-role-key-mime-pi/master/templates/usb-gadget.systemd.j2
sed -e "s@{{ key_mime_pi_initialize_hid_script_path }}@${ENABLE_RPI_HID_PATH}@g" \
  usb-gadget.systemd.j2 > /lib/systemd/system/usb-gadget.service

systemctl daemon-reload
systemctl enable usb-gadget.service