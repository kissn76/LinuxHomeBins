#!/bin/sh

pkill keepassx

SERVER="almos.lan"
SERVERUSERNAME="nn"
SERVERPATH="/home/nn/syncthing/config/Sync/keepassx"
MOUNTPATH="/tmp/nn/mnt/keepassx"
FILENAME="nn_keepass2.kdbx"
KEYFILENAME="nn_keepassx2.key"

FAILOVERPATH="/home/nn/Letöltések/Syncthing/nn_keepassx/"

if [ ${SERVER} != 0 ]; then
  sleep 5
  mkdir -p ${MOUNTPATH}
  sshfs ${SERVERUSERNAME}@${SERVER}:${SERVERPATH} ${MOUNTPATH}
  sleep 2
  keepassxc "--keyfile" ${MOUNTPATH}"/"${KEYFILENAME} ${MOUNTPATH}"/"${FILENAME}
else
  keepassxc "--keyfile" ${FAILOVERPATH}"/"${KEYFILENAME} ${FAILOVERPATH}"/"${FILENAME}
fi
