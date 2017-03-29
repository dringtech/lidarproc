# lidarprep

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

E

[VE]: https://virtualenv.pypa.io/en/stable/ 'Link to VirtualEnv homepage'
[EA]: http://environment.data.gov.uk/ds/survey/ 'Link to Survey Data provided by the Environment Agency'
[DG]:  https://data.gov.uk/data/search?q=LIDAR+Composite&publisher=environment-agency 'Search for LIDAR Composite datasets on data.gov.uk'
