[Unit]
Description=Create virtual keyboard USB gadget
After=syslog.target

[Service]
Type=oneshot
User=root
ExecStart={{ key_mime_pi_initialize_hid_script_path }}

[Install]
WantedBy=local-fs.target