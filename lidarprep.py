#!/usr/bin/env python
# pylint: disable=C0103
import sys
import os
# import re
from lidar import Lidar

# Last part of the path is the name
dirname = sys.argv[1].rstrip('/')

if not os.path.isdir(dirname):
    raise Exception('Argument must be a directory {}'.format(dirname))

# Assumes of the form LIDAR-DTM-2M-SD92
(_, model, resolution, base) = os.path.basename(dirname).lower().split('-')
area = Lidar(model, resolution, base)
area.load(dirname)
exit()




numpy.savetxt('output/'+filename+".csv", result, delimiter=",")

pngfile = open('output/'+filename+'.png', 'wb')
w = png.Writer(dimension*cells[0], dimension*cells[1], greyscale=True)
result[numpy.isnan(result)] = result[numpy.isfinite(result)].min() - 1
print result.min(), result.max()
result -= result.min()
result *= 255.0/result.max()
w.write(pngfile,result)
pngfile.close()
