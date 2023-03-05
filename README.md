# Twobounce - MOLLER 

## Required packages
python gtk3

## Details
A polygon is given by four array pairs of coordinates, polygons are pushed
into an array of polygons and then poly::light is called on all combinations
twice to determine the two bounce lighting

speccoll_vac.py is the most up-to-date geometry available. Previous older versions are located in ./old.

Can be run on ifarm if x-forwarding is enabled. Currently can not be run in an interactive job.



## Description of variables in speccoll_vac.py

| Syntax      | Description   | Value (m)     | Comments |
| ----------- | -----------   | ---------     | ---------|
| tgtlen      | Target Length | 1.25          |          |
| tgtrad      | Target Radius | 1.4142*0.0025 | 5x5 mm raster implies diagonally farthest point from center is at sqrt((0.0025)^2+(0.0025)^2) m |
  
