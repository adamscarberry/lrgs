#!/usr/bin/env python3
import os

# CDADATA
CDADATA_USERNAME = os.getenv("CDADATA_USERNAME")
CDADATA_PASSWORD = os.getenv("CDADATA_PASSWORD")
# CDABACKUP
CDABACKUP_USERNAME = os.getenv("CDABACKUP_USERNAME")
CDABACKUP_PASSWORD = os.getenv("CDABACKUP_PASSWORD")

# Config file
DDS_RECV_PATH = os.path.join(os.getenv("LRGSHOME"), "ddsrecv.conf")
DDS_RECV_TMP_PATH = os.path.join(os.getenv("LRGSHOME"), "ddsrecv.conf.tmp")

myDict = {
    "CDADATA_USERNAME": CDADATA_USERNAME,
    "CDADATA_PASSWORD": CDADATA_PASSWORD,
    "CDABACKUP_USERNAME": CDABACKUP_USERNAME,
    "CDABACKUP_PASSWORD": CDABACKUP_PASSWORD,
}

with open(DDS_RECV_PATH, "rt") as fin:
    with open(DDS_RECV_TMP_PATH, "wt") as fout:
        for line in fin:
            for k, v in myDict.items():
                if k in line:
                    line = line.replace(k, v)

            fout.write(line)

os.rename(DDS_RECV_TMP_PATH, DDS_RECV_PATH)
print("Env Vars replaced")
exit(0)
