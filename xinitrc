#!/bin/bash

sh /home/leon/.fehbg &

setxkbmap -layout us,ru -option grp:alt_shift_toggle &

dunst &
picom --config /home/leon/.config/picom/picom.conf --focus-exclude "! name~=''" &
xss-lock slock &

exec qtile

