# lidarproc

Python routine to turn downloaded LIDAR data into PNG files.

## Initial Preparation

Run the following commands:

    pip install --requirement requirements.txt

You may wish to run in a [virtual environment][VE], in which case, run the
following commands first:

    virtualenv venv
    . venv/bin/activate


## Running the code

If you're running in a virtual environment, make sure it's activated by
running `. venv/bin/activate`.

You will need to download LIDAR data files from the
[Environment Agency Website][EA]. The LIDAR data comes in two variants
(DSM and DTM) and four resolutions (25cm, 50cm, 1m and 2m). The
difference between the DSM and DTM is that the DSM (Digital Surface Model)
includes man-made objects, whereas the DTM (Digital Terrain Model) does not.
The finer the resolution (i.e. smaller the dimension), the larger the
corresponding files.

The tool supports the DTM and DSM Composites. It's been tested on the 2m and 1m
resolutions. It should work on the 50cm resolution, but tiling the entire
dataset into a single PNG file tends to blow up memory. Some optimisation is
required.

Unzip the files into the `data` directory, and from the project directory round

    ./lidarprep.py data/<dataset>

You will see the individual files being read and jigsawed into a large
matrix. There will then be a short pause while the PNG is prepared and written.
It'll appear in the output directory.

# References

The data was [first released][Blog] in September 2015.


[Blog]: https://environmentagency.blog.gov.uk/2015/09/18/laser-surveys-light-up-open-data/

[VE]: https://virtualenv.pypa.io/en/stable/ 'Link to VirtualEnv homepage'
[EA]: http://environment.data.gov.uk/ds/survey/ 'Link to Survey Data provided by the Environment Agency'
[DG]:  https://data.gov.uk/data/search?q=LIDAR+Composite&publisher=environment-agency 'Search for LIDAR Composite datasets on data.gov.uk'
