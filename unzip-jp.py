#!/usr/bin/env python

# Extracts a zip archive while converting file names from Shift-JIS encoding to UTF-8.
#
# Example:
#   python unzip-jp.py archive.zip
#
#       Creates a directory `archive` and extracts the archive there.
#
import zipfile
import sys
import os

if len(sys.argv) < 2:
    print('No archive name.')
    print('')
    print('Usage: unzip-jp archive [password]')
    exit(1)

name = sys.argv[1]

if len(sys.argv) > 2:
    password = sys.argv[2]
else:
    password = None

directory = os.path.splitext(os.path.basename(name))[0]

if not os.path.exists(directory):
    os.makedirs(directory)

with zipfile.ZipFile(name, 'r') as z:
    if password:
        z.setpassword(password)
    for f in z.infolist():
        try:
            uf = f.filename.decode('sjis').encode('utf8')
        except:
            uf = f.filename.decode('shift_jisx0213').encode('utf8')
        print(uf)
        filename=os.path.join(directory, uf)
        # create directories if necessary
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, 'w') as dest:
            dest.write(z.read(f))

