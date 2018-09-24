#!/bin/sh

# A megadott monitorok bekapcsolása
# Argumentumok szerint balról jobbra lesz az elhelyezkedés
# Első argumentum lesz a bal szélső monitor, egyben a primary

PRIMARYMONITOR=""
PREVMONITOR=""

MYMONITORS=${@}

MONITORS=$(xrandr | grep -Eo '^[^ S][a-zA-Z0-9-]*')

for i in ${MONITORS}
do
  xrandr --output ${i} --off
done

m=1
for i in ${MYMONITORS}
do
  c=1
  for e in ${MONITORS}
  do
    if [ ${c} -eq ${i} ]
    then
      xrandr --output ${e} --auto
      if [ ${m} -gt 1 ]
      then
        xrandr --output ${e} --right-of ${PREVMONITOR}
      else
        PRIMARYMONITOR=${e}
      fi
      PREVMONITOR=${e}
    fi
    c=$((c+1))
  done
  m=$((m+1))
done

xrandr --output ${PRIMARYMONITOR} --primary

#xrandr --output ${MONITOR} --off
#xrandr --output ${MONITOR} --auto
#xrandr --output ${MONITOR} --right-of ${MONITOR2}
#xrandr --output ${MONITOR} --primary
