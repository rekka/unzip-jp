#!/usr/bin/env python

# Extracts a zip archive while converting file names from Shift-JIS encoding to UTF-8
import zipfile
import sys
import os

if len(sys.argv) != 2:
    print('No archive name.')
    exit(1)

name = sys.argv[1]

directory = os.path.splitext(os.path.basename(name))[0]

if not os.path.exists(directory):
    os.makedirs(directory)

with zipfile.ZipFile(name, 'r') as z:
    for f in z.infolist():
        uf = f.filename.decode('sjis').encode('utf8')
        with open(os.path.join(directory, uf), 'w') as dest:
            dest.write(z.read(f))

