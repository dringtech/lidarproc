'''Module to house the Lidar class'''
import os
import re
import numpy
import png


def coords(filename):
    '''Calculate the coordinates of a filename'''
    return (int(filename[2:4]), int(filename[4:6]))


class Lidar(object):
    '''Class to handle reading and processing LIDAR data'''

    def __init__(self, model, resolution, base):
        self.dirname = None
        self.start_cell = None
        self.grid_size = None
        self.matrix = None
        self.model = model
        dimension = re.findall(r'(\d+)(\D+)', resolution)[0]
        self.cell_size = int(1e6 / (
            int(dimension[0]) * (1000 if dimension[1] == 'm' else 1)))
        self.base = base

    def _process_cell(self, filename):
        location = [c-self.start_cell[i]
                    for i, c
                    in enumerate(coords(filename))]
        # print x, y, dimension, path
        x_start = location[0] * self.cell_size
        y_start = (self.grid_size[1]-1-location[1]) * self.cell_size
        print y_start
        try:
            data = numpy.loadtxt(os.path.join(self.dirname, filename),
                                 skiprows=6)
            data[data == -9999] = numpy.nan
            self.matrix[y_start:y_start+self.cell_size,
                        x_start:x_start+self.cell_size] = data
        except IOError:
            pass

    def load(self, dirname):
        if not os.path.isdir(dirname):
            raise Exception('Argument must be a directory {}'.format(dirname))

        self.dirname = dirname
        files = [f for f
                 in os.listdir(dirname)
                 if os.path.isfile(os.path.join(dirname, f))]
        grid = map(set, zip(*[coords(f) for f in files]))
        self.start_cell = list(map(min, grid))
        self.grid_size = list(map(len, grid))
        self.matrix = numpy.empty([x * self.cell_size for x in self.grid_size])
        self.matrix.fill(numpy.nan)

        map(self._process_cell, files)

    def write_csv(self, path):
        '''Save the current matrix as a csv file'''
        numpy.savetxt(path, self.matrix, delimiter=",")

    def normalise(self):
        self.matrix[numpy.isnan(self.matrix)] = self.matrix[numpy.isfinite(self.matrix)].min() - 1
        self.matrix -= self.matrix.min()
        self.matrix *= 255.0/self.matrix.max()

    def write_png(self, path):
        with open(path, 'wb') as pngfile:
            w = png.Writer(self.cell_size*self.grid_size[0],
                           self.cell_size*self.grid_size[1],
                           greyscale=True)
            w.write(pngfile, self.matrix)

    def summary(self):
        return self.matrix.min(), self.matrix.max()
