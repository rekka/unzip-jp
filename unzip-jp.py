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
import codecs

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
        z.setpassword(password.encode('cp850','replace'))
    for f in z.infolist():
        bad_filename = f.filename
        if bytes != str:
            # Python 3 - decode filename into bytes
            # assume CP437 - these zip files were from Windows anyway
            bad_filename = bytes(bad_filename, 'cp437')
        try:
            uf = codecs.decode(bad_filename, 'sjis')
        except:
            uf = codecs.decode(bad_filename, 'shift_jisx0213')
        # need to print repr in Python 2 as we may encounter UnicodeEncodeError
        # when printing to a Windows console
        print(repr(uf))
        filename=os.path.join(directory, uf)
        # create directories if necessary
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        # don't try to write to directories
        if not filename.endswith('/'):
            with open(filename, 'wb') as dest:
                dest.write(z.read(f))

