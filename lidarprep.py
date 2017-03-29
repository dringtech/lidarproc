#!/usr/bin/env python
import sys, os, re, numpy, png

# Last part of the path is the name
dirname = os.path.split(sys.argv[1])

filename = dirname[-1]

# Assumes of the form LIDAR-DTM-2M-SD92
(lidar, type, resolution, base) = filename.lower().split('-')

dimension = 1000/int(re.findall(r'\d+', resolution)[0])

cells = (10,10)

result = numpy.empty((dimension*cells[0], dimension*cells[1], ))
result.fill(numpy.nan)

def fname(x, y):
    return ''.join([base[0:3], str(x), base[3], str(y), '_', type, '_', resolution, '.asc'])

for x in range(0, cells[0]):
    for y in range(0, cells[1]):
        path = dirname + (fname(x, y),)
        print x, y, dimension, path
        x_start = x * dimension
        y_start = (cells[1]-1-y) * dimension
        try:
            data = numpy.loadtxt(os.path.join( *path ), skiprows=6)
            data[data==-9999] = numpy.nan
            result[y_start:y_start+dimension,x_start:x_start+dimension] = data
        except IOError:
            next

numpy.savetxt('output/'+filename+".csv", result, delimiter=",")

pngfile = open('output/'+filename+'.png', 'wb')
w = png.Writer(dimension*cells[0], dimension*cells[1], greyscale=True)
result[numpy.isnan(result)] = result[numpy.isfinite(result)].min() - 1
print result.min(), result.max()
result -= result.min()
result *= 255.0/result.max()
w.write(pngfile,result)
pngfile.close()
