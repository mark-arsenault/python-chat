#!/usr/bin/env bash
# Purpose - Disable broken touchscreen inputs, run startup routines
# Author - Mark Arsenault {https://markarsenault.tk} under GPL+ 2.0
KEYBOARD_ID=""
MOUSE_ID=""


# determine the pointer id's of surface pro touchscreen that is cracked

MOUSE_ID="$(xinput list --id-only 'pointer:NTRG0001:01 1B96:1B05')"
KEYBOARD_ID="$(xinput list --id-only 'keyboard:NTRG0001:01 1B96:1B05')"
# disable them
if [ -n "$MOUSE_ID" ]; then
  xinput disable "$MOUSE_ID"
  xinput disable "$KEYBOARD_ID"
fi

# Open Guake & Thunderbird
sleep 1
thunderbird
sleep 1
guake

exit 0