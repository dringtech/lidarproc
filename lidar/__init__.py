import os
import re
import numpy


class Lidar:
    '''Class to handle reading and processing LIDAR data'''
    def _make_range(self, base):
        return [str(x + int(base)) for x in range(10)]

    def __init__(self, model, resolution, base):
        self.model = model
        self.resolution = resolution
        self.base = base
        eastings = self._make_range(base[2:4])
        northings = self._make_range(base[4:6])
        self.cells = [(x+y) for y in northings for x in eastings]

        # TODO make this work with resolution of CM, not just M
        self.dimension = 1000/int(re.findall(r'\d+', self.resolution)[0])
        self.result = numpy.empty((self.dimension*10, self.dimension*10))
        self.result.fill(numpy.nan)

    def _process_cell(self, cell, index):
        def fname(cell):
            return ''.join([self.base[0:2], cell, '_', self.model, '_', self.resolution, '.asc'])
        filename = fname(cell)
        return filename, os.path.exists(filename)

    def load(self, dirname):
        if not os.path.isdir(dirname):
            raise Exception('Argument must be a directory {}'.format(dirname))

        print [self._process_cell(e, i) for i, e in enumerate(self.cells)]

        # for i in self.cells):
            # _process_cell(self.cells(i), i)
        # for x in range(0, cells[0]):
        #     for y in range(0, cells[1]):
        #         path = dirname + (fname(x, y),)
        #         print x, y, dimension, path
        #         x_start = x * dimension
        #         y_start = (cells[1]-1-y) * dimension
        #         try:
        #             data = numpy.loadtxt(os.path.join( *path ), skiprows=6)
        #             data[data==-9999] = numpy.nan
        #             result[y_start:y_start+dimension,x_start:x_start+dimension] = data
        #         except IOError:
        #             next


    def savetxt(self, path):
        pass

    def writepng(self, path, options={}):
        pass

    def summary(self):
        pass
