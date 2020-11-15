#!/bin/bash

sh /home/user/.fehbg &

setxkbmap -layout us,ru -option grp:alt_shift_toggle &
xinput set-prop "Synaptics TM3096-006" "libinput Tapping Enabled" 1 &

dunst &
picom --config /home/user/.config/picom/picom.conf --focus-exclude "! name~=''" &
xss-lock slock &

exec qtile

