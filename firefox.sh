#!/bin/sh

xhost +si:localuser:browser
sudo -u browser -H /usr/bin/firefox $1