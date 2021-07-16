#!/usr/bin/env python2

# Copy metadata from source tree

import sys
import os
import shutil

if __name__ == '__main__':

    source = sys.argv[1]
    dest = sys.argv[2]

    if os.path.exists(dest ):
        shutil.rmtree(dest )

    shutil.copytree(source, dest, ignore=shutil.ignore_patterns('*.wem','*.bnk'))

