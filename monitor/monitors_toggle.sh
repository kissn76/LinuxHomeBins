#!/bin/sh

# A megadott monitor ki be kapcsolása

MONITOR=${1}

MONITORSTATE=$(xrandr | grep "^${MONITOR}" | grep -Eo '[1-9][0-9]*x[1-9][0-9]*')

if [ -z ${MONITORSTATE} ]
then
  xrandr --output ${MONITOR} --auto
else
  xrandr --output ${MONITOR} --off
  sleep 5
  xrandr --output ${MONITOR} --auto
fi
