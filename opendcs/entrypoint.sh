#!/usr/bin/env bash

# set umask
umask 0002

# rm $LRGSHOME/lrgsstatus.html || true
# touch $LRGSHOME/lrgsstatus.html
# chmod 777 $LRGSHOME/lrgsstatus.html

# # Attempt to remove file if exists
# rm /status/index.html || true
# ln -s $LRGSHOME/lrgsstatus.html $LRGSHOME/lrgsstatus/index.html

python $LRGSHOME/replaceVars.py && startLRGS