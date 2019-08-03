#!/usr/bin/env bash

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

run volumeicon
run light-locker
run xrdb -load ~/.Xresourses
run nm-applet
#exec sleep 1 ; feh --bg-fill Pictures/236642.jpg
#exec sleep 1 ; xrandr --output DVI-1 --pos 0x124
#exec redshift-gtk
#exec xrandr --output HDMI-0 --mode 1280x1024 --right-of DVI-1 --noprimary
