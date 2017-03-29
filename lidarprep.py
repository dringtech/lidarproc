#!/usr/bin/env python
# pylint: disable=C0103
import sys
import os
from lidar import Lidar

# Last part of the path is the name
dirname = sys.argv[1].rstrip('/')
filename = os.path.basename(dirname).lower()

if not os.path.isdir(dirname):
    raise Exception('Argument must be a directory {}'.format(dirname))

# Assumes of the form LIDAR-DTM-2M-SD92
(_, model, resolution, base) = filename.split('-')
area = Lidar(model, resolution, base)
area.load(dirname)

area.write_csv('output/' + filename + '.csv')
area.normalise()
area.write_png('output/' + filename + '.png')
