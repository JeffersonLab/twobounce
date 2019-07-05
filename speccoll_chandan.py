#!/usr/bin/python 
from poly import polygon
from poly import face 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from drawlight import drawlight

sources = []
allpolys = []


tgtoffset = 0.5
tgtlen = 1.25
#tgtrad = 0.04
#tgtrad = 0.002
tgtrad = 1.4142*0.0025

target = polygon( ([-tgtlen/2,-tgtrad], [tgtlen/2, -tgtrad], [tgtlen/2,tgtrad], [-tgtlen/2,tgtrad]) )

################################################################

###### Lead collar (for collimating photons)

#seg 1
x1_collar=0.074#+0.05
z1_collar=2.851#+1.5

x2_collar=0.185 #*1.414 The collar is a rectangle (in CAD), but the narrow dimension is the one relevant for here
z2_collar=2.851#+1.5

x3_collar=0.185 #*1.414
z3_collar=3.051#+1.5

x4_collar=0.074#+0.05
z4_collar=3.051#+1.5


collar_top    = polygon( ([z1_collar,  x1_collar], [z4_collar,  x4_collar], [z3_collar,  x3_collar], [z2_collar,  x2_collar] ), notSource=False)
collar_bottom = polygon( ([z2_collar, -x2_collar], [z3_collar, -x3_collar], [z4_collar, -x4_collar], [z1_collar, -x1_collar] ), notSource=False)

#################################################################

######inner photon collimator (Col 1)
# Previous implementation assumed it was a solid shape from front face to back face, 
# but this neglects the fact that it tapers inwards a lot in the first 30cm and then 
# untapers in the last 10cm - updating by splitting into 5 segments

col1_inner_offset = 0.0019

x1_inner_photon_1=0.024-col1_inner_offset
z1_inner_photon_1=5.175-tgtoffset

x2_inner_photon_1=0.031703 # 0.05670 is the outer radius of the Col1 cooling fans, 0.031703 is the outer radius of Col1 otherwise
z2_inner_photon_1=5.175-tgtoffset

x3_inner_photon_1=0.031703
z3_inner_photon_1=5.275-tgtoffset

x4_inner_photon_1=0.024-col1_inner_offset
z4_inner_photon_1=5.275-tgtoffset

x1_inner_photon_2=0.020386-col1_inner_offset
z1_inner_photon_2=5.275-tgtoffset

x2_inner_photon_2=0.028703
z2_inner_photon_2=5.275-tgtoffset

x3_inner_photon_2=0.028703
z3_inner_photon_2=5.375-tgtoffset

x4_inner_photon_2=0.020386-col1_inner_offset
z4_inner_photon_2=5.375-tgtoffset

x1_inner_photon_3=0.018696-col1_inner_offset
z1_inner_photon_3=5.375-tgtoffset

x2_inner_photon_3=0.026703
z2_inner_photon_3=5.375-tgtoffset

x3_inner_photon_3=0.026703
z3_inner_photon_3=5.475-tgtoffset

x4_inner_photon_3=0.018696-col1_inner_offset
z4_inner_photon_3=5.475-tgtoffset

x1_inner_photon_4=0.015529-col1_inner_offset
z1_inner_photon_4=5.475-tgtoffset

x2_inner_photon_4=0.026703
z2_inner_photon_4=5.475-tgtoffset

x3_inner_photon_4=0.026703
z3_inner_photon_4=5.575-tgtoffset

x4_inner_photon_4=0.015529-col1_inner_offset
z4_inner_photon_4=5.575-tgtoffset

x1_inner_photon_5=0.015529-col1_inner_offset
z1_inner_photon_5=5.575-tgtoffset

x2_inner_photon_5=0.026703
z2_inner_photon_5=5.575-tgtoffset

x3_inner_photon_5=0.026703
z3_inner_photon_5=5.675-tgtoffset

x4_inner_photon_5=0.015808-col1_inner_offset
z4_inner_photon_5=5.675-tgtoffset

# one has to assign the coordinates in anti-clock sequence
coll_inner_photon_top_1    = polygon( ([z1_inner_photon_1,  x1_inner_photon_1], [z4_inner_photon_1,  x4_inner_photon_1], [z3_inner_photon_1,  x3_inner_photon_1], [z2_inner_photon_1,  x2_inner_photon_1] ), notSource=False)
coll_inner_photon_bottom_1 = polygon( ([z2_inner_photon_1, -x2_inner_photon_1], [z3_inner_photon_1, -x3_inner_photon_1], [z4_inner_photon_1, -x4_inner_photon_1], [z1_inner_photon_1, -x1_inner_photon_1] ), notSource=False)

coll_inner_photon_top_2    = polygon( ([z1_inner_photon_2,  x1_inner_photon_2], [z4_inner_photon_2,  x4_inner_photon_2], [z3_inner_photon_2,  x3_inner_photon_2], [z2_inner_photon_2,  x2_inner_photon_2] ), notSource=False)
coll_inner_photon_bottom_2 = polygon( ([z2_inner_photon_2, -x2_inner_photon_2], [z3_inner_photon_2, -x3_inner_photon_2], [z4_inner_photon_2, -x4_inner_photon_2], [z1_inner_photon_2, -x1_inner_photon_2] ), notSource=False)

coll_inner_photon_top_3    = polygon( ([z1_inner_photon_3,  x1_inner_photon_3], [z4_inner_photon_3,  x4_inner_photon_3], [z3_inner_photon_3,  x3_inner_photon_3], [z2_inner_photon_3,  x2_inner_photon_3] ), notSource=False)
coll_inner_photon_bottom_3 = polygon( ([z2_inner_photon_3, -x2_inner_photon_3], [z3_inner_photon_3, -x3_inner_photon_3], [z4_inner_photon_3, -x4_inner_photon_3], [z1_inner_photon_3, -x1_inner_photon_3] ), notSource=False)

coll_inner_photon_top_4    = polygon( ([z1_inner_photon_4,  x1_inner_photon_4], [z4_inner_photon_4,  x4_inner_photon_4], [z3_inner_photon_4,  x3_inner_photon_4], [z2_inner_photon_4,  x2_inner_photon_4] ), notSource=False)
coll_inner_photon_bottom_4 = polygon( ([z2_inner_photon_4, -x2_inner_photon_4], [z3_inner_photon_4, -x3_inner_photon_4], [z4_inner_photon_4, -x4_inner_photon_4], [z1_inner_photon_4, -x1_inner_photon_4] ), notSource=False)

coll_inner_photon_top_5    = polygon( ([z1_inner_photon_5,  x1_inner_photon_5], [z4_inner_photon_5,  x4_inner_photon_5], [z3_inner_photon_5,  x3_inner_photon_5], [z2_inner_photon_5,  x2_inner_photon_5] ), notSource=False)
coll_inner_photon_bottom_5 = polygon( ([z2_inner_photon_5, -x2_inner_photon_5], [z3_inner_photon_5, -x3_inner_photon_5], [z4_inner_photon_5, -x4_inner_photon_5], [z1_inner_photon_5, -x1_inner_photon_5] ), notSource=False)


#########collimator 2,  three segments
increasecolth = 0.05
coll2offset = 0.000
#seg 1
x1_coll_2_1=-0.035
z1_coll_2_1=5.825-tgtoffset

x2_coll_2_1=-0.026
#x2_coll_2_1=-0.02955
z2_coll_2_1=5.825-tgtoffset

x3_coll_2_1=-0.026
#x3_coll_2_1=-0.02955
z3_coll_2_1=5.975-tgtoffset

x4_coll_2_1=-0.035
z4_coll_2_1=5.975-tgtoffset


coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), notSource=False)
#coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), isDetector=True)


#seg 2

x1_coll_2_2=-0.150
#x1_coll_2_2=-0.300
z1_coll_2_2=5.825-tgtoffset

x2_coll_2_2=-0.108
#x2_coll_2_2=-0.108
z2_coll_2_2=5.825-tgtoffset

x3_coll_2_2=-0.108
#x3_coll_2_2=-0.108
z3_coll_2_2=5.975-tgtoffset

x4_coll_2_2=-0.150
#x4_coll_2_2=-0.300
z4_coll_2_2=5.975-tgtoffset


coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), notSource=False)
#coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), isDetector=True)

#seg 3

x1_coll_2_3=0.026
#x1_coll_2_3=0.02955
z1_coll_2_3=5.825-tgtoffset

x2_coll_2_3= 0.150
#x2_coll_2_3= 0.300
z2_coll_2_3=5.825-tgtoffset

x3_coll_2_3= 0.150
#x3_coll_2_3= 0.300
z3_coll_2_3=5.975-tgtoffset

x4_coll_2_3=0.026
#x4_coll_2_3=0.02955
z4_coll_2_3=5.975-tgtoffset


coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), notSource=False)
#coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), isDetector=True)


############# Col2 photon collimating inner_pipe
##pipe
x1_pipe0=0.023
z1_pipe0=5.675-tgtoffset

x2_pipe0=0.026
z2_pipe0=5.675-tgtoffset

x3_pipe0=0.030
z3_pipe0=5.825-tgtoffset

x4_pipe0=0.027
z4_pipe0=5.825-tgtoffset


coll_pipe01   = polygon( ([z1_pipe0, x1_pipe0], [z4_pipe0, x4_pipe0], [z3_pipe0, x3_pipe0], [z2_pipe0, x2_pipe0] ), notSource=False)
coll_pipe02   = polygon( ([z2_pipe0, -x2_pipe0], [z3_pipe0, -x3_pipe0], [z4_pipe0, -x4_pipe0], [z1_pipe0, -x1_pipe0] ), notSource=False)

##pipe to aviod open space between Col2 and beam pipe desigened by Dave
x1_pipe1_1=0.022225
z1_pipe1_1=5.475-coll2offset

x2_pipe1_1=0.027
z2_pipe1_1=5.475-coll2offset

x3_pipe1_1=0.027
z3_pipe1_1=5.50

x4_pipe1_1=0.022225
z4_pipe1_1=5.50


coll_pipe11_1   = polygon( ([z1_pipe1_1, x1_pipe1_1], [z4_pipe1_1, x4_pipe1_1], [z3_pipe1_1, x3_pipe1_1], [z2_pipe1_1, x2_pipe1_1] ), notSource=False)
coll_pipe12_1   = polygon( ([z2_pipe1_1, -x2_pipe1_1], [z3_pipe1_1, -x3_pipe1_1], [z4_pipe1_1, -x4_pipe1_1], [z1_pipe1_1, -x1_pipe1_1] ), notSource=False)
##pipe
x1_pipe1=0.021336
z1_pipe1=5.475-coll2offset

x2_pipe1=0.022225
z2_pipe1=5.475-coll2offset

x3_pipe1=0.022225
z3_pipe1=5.750

x4_pipe1=0.021336
z4_pipe1=5.750


coll_pipe11   = polygon( ([z1_pipe1, x1_pipe1], [z4_pipe1, x4_pipe1], [z3_pipe1, x3_pipe1], [z2_pipe1, x2_pipe1] ), notSource=False)
coll_pipe12   = polygon( ([z2_pipe1, -x2_pipe1], [z3_pipe1, -x3_pipe1], [z4_pipe1, -x4_pipe1], [z1_pipe1, -x1_pipe1] ), notSource=False)

##step
x1_pipe2=0.021336
z1_pipe2=5.750

x2_pipe2=0.0238125
z2_pipe2=5.750

x3_pipe2=0.0238125
z3_pipe2=5.800

x4_pipe2=0.021336
z4_pipe2=5.800

coll_pipe21   = polygon( ([z1_pipe2, x1_pipe2], [z4_pipe2, x4_pipe2], [z3_pipe2, x3_pipe2], [z2_pipe2, x2_pipe2] ), notSource=False)
coll_pipe22   = polygon( ([z2_pipe2, -x2_pipe2], [z3_pipe2, -x3_pipe2], [z4_pipe2, -x4_pipe2], [z1_pipe2, -x1_pipe2] ), notSource=False)


##pipe
x1_pipe3=0.0229235
z1_pipe3=5.800

x2_pipe3=0.0238125
z2_pipe3=5.800

x3_pipe3=0.0238125
z3_pipe3=6.050

x4_pipe3=0.0229235
z4_pipe3=6.050


coll_pipe31   = polygon( ([z1_pipe3, x1_pipe3], [z4_pipe3, x4_pipe3], [z3_pipe3, x3_pipe3], [z2_pipe3, x2_pipe3] ), notSource=False)
coll_pipe32   = polygon( ([z2_pipe3, -x2_pipe3], [z3_pipe3, -x3_pipe3], [z4_pipe3, -x4_pipe3], [z1_pipe3, -x1_pipe3] ), notSource=False)

##step
x1_pipe4=0.0229235
z1_pipe4=6.050

x2_pipe4=0.0254
z2_pipe4=6.050

x3_pipe4=0.0254
z3_pipe4=6.100

x4_pipe4=0.0229235
z4_pipe4=6.100


coll_pipe41   = polygon( ([z1_pipe4, x1_pipe4], [z4_pipe4, x4_pipe4], [z3_pipe4, x3_pipe4], [z2_pipe4, x2_pipe4] ), notSource=False)
coll_pipe42   = polygon( ([z2_pipe4, -x2_pipe4], [z3_pipe4, -x3_pipe4], [z4_pipe4, -x4_pipe4], [z1_pipe4, -x1_pipe4] ), notSource=False)

##pipe
x1_pipe5=0.024511
z1_pipe5=6.100

x2_pipe5=0.0254
z2_pipe5=6.100

x3_pipe5=0.0254
z3_pipe5=6.450

x4_pipe5=0.024511
z4_pipe5=6.450


coll_pipe51   = polygon( ([z1_pipe5, x1_pipe5], [z4_pipe5, x4_pipe5], [z3_pipe5, x3_pipe5], [z2_pipe5, x2_pipe5] ), notSource=False)
coll_pipe52   = polygon( ([z2_pipe5, -x2_pipe5], [z3_pipe5, -x3_pipe5], [z4_pipe5, -x4_pipe5], [z1_pipe5, -x1_pipe5] ), notSource=False)

##step
x1_pipe6=0.024511
z1_pipe6=6.450

x2_pipe6=0.0254
z2_pipe6=6.450

x3_pipe6=0.0254
z3_pipe6=6.500

x4_pipe6=0.024511
z4_pipe6=6.500


coll_pipe61   = polygon( ([z1_pipe6, x1_pipe6], [z4_pipe6, x4_pipe6], [z3_pipe6, x3_pipe6], [z2_pipe6, x2_pipe6] ), notSource=False)
coll_pipe62   = polygon( ([z2_pipe6, -x2_pipe6], [z3_pipe6, -x3_pipe6], [z4_pipe6, -x4_pipe6], [z1_pipe6, -x1_pipe6] ), notSource=False)

##pipe
x1_pipe6=0.0260985
z1_pipe6=6.500

x2_pipe6=0.0269875
z2_pipe6=6.500

x3_pipe6=0.0269875
z3_pipe6=6.850

x4_pipe6=0.0260985
z4_pipe6=6.850


coll_pipe61   = polygon( ([z1_pipe6, x1_pipe6], [z4_pipe6, x4_pipe6], [z3_pipe6, x3_pipe6], [z2_pipe6, x2_pipe6] ), notSource=False)
coll_pipe62   = polygon( ([z2_pipe6, -x2_pipe6], [z3_pipe6, -x3_pipe6], [z4_pipe6, -x4_pipe6], [z1_pipe6, -x1_pipe6] ), notSource=False)

#step
x1_pipe7=0.0260985
z1_pipe7=6.850

x2_pipe7=0.028575
z2_pipe7=6.850

x3_pipe7=0.028575
z3_pipe7=6.900

x4_pipe7=0.0260985
z4_pipe7=6.900


coll_pipe71   = polygon( ([z1_pipe7, x1_pipe7], [z4_pipe7, x4_pipe7], [z3_pipe7, x3_pipe7], [z2_pipe7, x2_pipe7] ), notSource=False)
coll_pipe72   = polygon( ([z2_pipe7, -x2_pipe7], [z3_pipe7, -x3_pipe7], [z4_pipe7, -x4_pipe7], [z1_pipe7, -x1_pipe7] ), notSource=False)

##pipe
x1_pipe8=0.027686
z1_pipe8=6.900

x2_pipe8=0.028575
z2_pipe8=6.900

x3_pipe8=0.028575
z3_pipe8=7.250

x4_pipe8=0.027686
z4_pipe8=7.250


coll_pipe81   = polygon( ([z1_pipe8, x1_pipe8], [z4_pipe8, x4_pipe8], [z3_pipe8, x3_pipe8], [z2_pipe8, x2_pipe8] ), notSource=False)
coll_pipe82   = polygon( ([z2_pipe8, -x2_pipe8], [z3_pipe8, -x3_pipe8], [z4_pipe8, -x4_pipe8], [z1_pipe8, -x1_pipe8] ), notSource=False)

##step
x1_pipe9=0.027686
z1_pipe9=7.250

x2_pipe9=0.0301625
z2_pipe9=7.250

x3_pipe9=0.0301625
z3_pipe9=7.300

x4_pipe9=0.027686
z4_pipe9=7.300


coll_pipe91   = polygon( ([z1_pipe9, x1_pipe9], [z4_pipe9, x4_pipe9], [z3_pipe9, x3_pipe9], [z2_pipe9, x2_pipe9] ), notSource=False)
coll_pipe92   = polygon( ([z2_pipe9, -x2_pipe9], [z3_pipe9, -x3_pipe9], [z4_pipe9, -x4_pipe9], [z1_pipe9, -x1_pipe9] ), notSource=False)

##pipe
x1_pipe10=0.0292735
z1_pipe10=7.300

x2_pipe10=0.0301625
z2_pipe10=7.300

x3_pipe10=0.0301625
z3_pipe10=7.550

x4_pipe10=0.0292735
z4_pipe10=7.550


coll_pipe101   = polygon( ([z1_pipe10, x1_pipe10], [z4_pipe10, x4_pipe10], [z3_pipe10, x3_pipe10], [z2_pipe10, x2_pipe10] ), notSource=False)
coll_pipe102   = polygon( ([z2_pipe10, -x2_pipe10], [z3_pipe10, -x3_pipe10], [z4_pipe10, -x4_pipe10], [z1_pipe10, -x1_pipe10] ), notSource=False)

##step
x1_pipe11=0.0292735
z1_pipe11=7.550

x2_pipe11=0.03175
z2_pipe11=7.550

x3_pipe11=0.03175
z3_pipe11=7.600

x4_pipe11=0.0292735
z4_pipe11=7.600


coll_pipe111   = polygon( ([z1_pipe11, x1_pipe11], [z4_pipe11, x4_pipe11], [z3_pipe11, x3_pipe11], [z2_pipe11, x2_pipe11] ), notSource=False)
coll_pipe112   = polygon( ([z2_pipe11, -x2_pipe11], [z3_pipe11, -x3_pipe11], [z4_pipe11, -x4_pipe11], [z1_pipe11, -x1_pipe11] ), notSource=False)

##pipe
x1_pipe12=0.030861
z1_pipe12=7.600

x2_pipe12=0.03175
z2_pipe12=7.600

x3_pipe12=0.03175
z3_pipe12=7.825

x4_pipe12=0.030861
z4_pipe12=7.825


coll_pipe121   = polygon( ([z1_pipe12, x1_pipe12], [z4_pipe12, x4_pipe12], [z3_pipe12, x3_pipe12], [z2_pipe12, x2_pipe12] ), notSource=False)
coll_pipe122   = polygon( ([z2_pipe12, -x2_pipe12], [z3_pipe12, -x3_pipe12], [z4_pipe12, -x4_pipe12], [z1_pipe12, -x1_pipe12] ), notSource=False)

##step
x1_pipe13=0.030861
z1_pipe13=7.825

x2_pipe13=0.034925
z2_pipe13=7.825

x3_pipe13=0.034925
z3_pipe13=7.900 ##wrong in spread sheet

x4_pipe13=0.030861
z4_pipe13=7.900


coll_pipe131   = polygon( ([z1_pipe13, x1_pipe13], [z4_pipe13, x4_pipe13], [z3_pipe13, x3_pipe13], [z2_pipe13, x2_pipe13] ), notSource=False)
coll_pipe132   = polygon( ([z2_pipe13, -x2_pipe13], [z3_pipe13, -x3_pipe13], [z4_pipe13, -x4_pipe13], [z1_pipe13, -x1_pipe13] ), notSource=False)

##pipe
x1_pipe14=0.033274
z1_pipe14=7.900

x2_pipe14=0.034925
z2_pipe14=7.900

x3_pipe14=0.034925
z3_pipe14=9.425

x4_pipe14=0.033274
z4_pipe14=9.425

coll_pipe141   = polygon( ([z1_pipe14, x1_pipe14], [z4_pipe14, x4_pipe14], [z3_pipe14, x3_pipe14], [z2_pipe14, x2_pipe14] ), notSource=False)
coll_pipe142   = polygon( ([z2_pipe14, -x2_pipe14], [z3_pipe14, -x3_pipe14], [z4_pipe14, -x4_pipe14], [z1_pipe14, -x1_pipe14] ), notSource=False)

##step
x1_pipe15=0.033274
z1_pipe15=9.425

x2_pipe15=0.0365125
z2_pipe15=9.425

x3_pipe15=0.0365125
z3_pipe15=9.500

x4_pipe15=0.033274
z4_pipe15=9.500

coll_pipe151   = polygon( ([z1_pipe15, x1_pipe15], [z4_pipe15, x4_pipe15], [z3_pipe15, x3_pipe15], [z2_pipe15, x2_pipe15] ), notSource=False)
coll_pipe152   = polygon( ([z2_pipe15, -x2_pipe15], [z3_pipe15, -x3_pipe15], [z4_pipe15, -x4_pipe15], [z1_pipe15, -x1_pipe15] ), notSource=False)

##pipe
x1_pipe16=0.0348615
z1_pipe16=9.500

x2_pipe16=0.0365125
z2_pipe16=9.500

x3_pipe16=0.0365125
z3_pipe16=9.925

x4_pipe16=0.0348615
z4_pipe16=9.925

coll_pipe161   = polygon( ([z1_pipe16, x1_pipe16], [z4_pipe16, x4_pipe16], [z3_pipe16, x3_pipe16], [z2_pipe16, x2_pipe16] ), notSource=False)
coll_pipe162   = polygon( ([z2_pipe16, -x2_pipe16], [z3_pipe16, -x3_pipe16], [z4_pipe16, -x4_pipe16], [z1_pipe16, -x1_pipe16] ), notSource=False)

##step
x1_pipe17=0.0348615
z1_pipe17=9.925

x2_pipe17=0.0381
z2_pipe17=9.925

x3_pipe17=0.0381
z3_pipe17=10.000

x4_pipe17=0.0348615
z4_pipe17=10.000

coll_pipe171   = polygon( ([z1_pipe17, x1_pipe17], [z4_pipe17, x4_pipe17], [z3_pipe17, x3_pipe17], [z2_pipe17, x2_pipe17] ), notSource=False)
coll_pipe172   = polygon( ([z2_pipe17, -x2_pipe17], [z3_pipe17, -x3_pipe17], [z4_pipe17, -x4_pipe17], [z1_pipe17, -x1_pipe17] ), notSource=False)

##pipe
x1_pipe18=0.036449
z1_pipe18=10.000

x2_pipe18=0.0381
z2_pipe18=10.000

x3_pipe18=0.0381
z3_pipe18=10.325

x4_pipe18=0.036449
z4_pipe18=10.325

coll_pipe181   = polygon( ([z1_pipe18, x1_pipe18], [z4_pipe18, x4_pipe18], [z3_pipe18, x3_pipe18], [z2_pipe18, x2_pipe18] ), notSource=False)
coll_pipe182   = polygon( ([z2_pipe18, -x2_pipe18], [z3_pipe18, -x3_pipe18], [z4_pipe18, -x4_pipe18], [z1_pipe18, -x1_pipe18] ), notSource=False)

##step
x1_pipe19=0.036449
z1_pipe19=10.325

x2_pipe19=0.0396875
z2_pipe19=10.325

x3_pipe19=0.0396875
z3_pipe19=10.400

x4_pipe19=0.036449
z4_pipe19=10.400

coll_pipe191   = polygon( ([z1_pipe19, x1_pipe19], [z4_pipe19, x4_pipe19], [z3_pipe19, x3_pipe19], [z2_pipe19, x2_pipe19] ), notSource=False)
coll_pipe192   = polygon( ([z2_pipe19, -x2_pipe19], [z3_pipe19, -x3_pipe19], [z4_pipe19, -x4_pipe19], [z1_pipe19, -x1_pipe19] ), notSource=False)

##pipe
x1_pipe20=0.0380365
z1_pipe20=10.400

x2_pipe20=0.0396875
z2_pipe20=10.400

x3_pipe20=0.0396875
z3_pipe20=10.825

x4_pipe20=0.0380365
z4_pipe20=10.825

coll_pipe201   = polygon( ([z1_pipe20, x1_pipe20], [z4_pipe20, x4_pipe20], [z3_pipe20, x3_pipe20], [z2_pipe20, x2_pipe20] ), notSource=False)
coll_pipe202   = polygon( ([z2_pipe20, -x2_pipe20], [z3_pipe20, -x3_pipe20], [z4_pipe20, -x4_pipe20], [z1_pipe20, -x1_pipe20] ), notSource=False)

##step
x1_pipe21=0.0380365
z1_pipe21=10.825

x2_pipe21=0.041275
z2_pipe21=10.825

x3_pipe21=0.041275
z3_pipe21=10.900

x4_pipe21=0.0380365
z4_pipe21=10.900

coll_pipe211   = polygon( ([z1_pipe21, x1_pipe21], [z4_pipe21, x4_pipe21], [z3_pipe21, x3_pipe21], [z2_pipe21, x2_pipe21] ), notSource=False)
coll_pipe212   = polygon( ([z2_pipe21, -x2_pipe21], [z3_pipe21, -x3_pipe21], [z4_pipe21, -x4_pipe21], [z1_pipe21, -x1_pipe21] ), notSource=False)


##pipe
x1_pipe22=0.039624
z1_pipe22=10.900

x2_pipe22=0.041275
z2_pipe22=10.900

x3_pipe22=0.041275
z3_pipe22=11.325

x4_pipe22=0.039624
z4_pipe22=11.325

coll_pipe221   = polygon( ([z1_pipe22, x1_pipe22], [z4_pipe22, x4_pipe22], [z3_pipe22, x3_pipe22], [z2_pipe22, x2_pipe22] ), notSource=False)
coll_pipe222   = polygon( ([z2_pipe22, -x2_pipe22], [z3_pipe22, -x3_pipe22], [z4_pipe22, -x4_pipe22], [z1_pipe22, -x1_pipe22] ), notSource=False)

##step
x1_pipe23=0.039624
z1_pipe23=11.325

x2_pipe23=0.0428625
z2_pipe23=11.325

x3_pipe23=0.0428625
z3_pipe23=11.400

x4_pipe23=0.039624
z4_pipe23=11.400

coll_pipe231   = polygon( ([z1_pipe23, x1_pipe23], [z4_pipe23, x4_pipe23], [z3_pipe23, x3_pipe23], [z2_pipe23, x2_pipe23] ), notSource=False)
coll_pipe232   = polygon( ([z2_pipe23, -x2_pipe23], [z3_pipe23, -x3_pipe23], [z4_pipe23, -x4_pipe23], [z1_pipe23, -x1_pipe23] ), notSource=False)

##pipe
x1_pipe24=0.0412115
z1_pipe24=11.400

x2_pipe24=0.0428625
z2_pipe24=11.400

x3_pipe24=0.0428625
z3_pipe24=11.725

x4_pipe24=0.0412115
z4_pipe24=11.725

coll_pipe241   = polygon( ([z1_pipe24, x1_pipe24], [z4_pipe24, x4_pipe24], [z3_pipe24, x3_pipe24], [z2_pipe24, x2_pipe24] ), notSource=False)
coll_pipe242   = polygon( ([z2_pipe24, -x2_pipe24], [z3_pipe24, -x3_pipe24], [z4_pipe24, -x4_pipe24], [z1_pipe24, -x1_pipe24] ), notSource=False)

##step
x1_pipe25=0.0412115
z1_pipe25=11.725

x2_pipe25=0.04445
z2_pipe25=11.725

x3_pipe25=0.04445
z3_pipe25=11.800

x4_pipe25=0.0412115
z4_pipe25=11.800

coll_pipe251   = polygon( ([z1_pipe25, x1_pipe25], [z4_pipe25, x4_pipe25], [z3_pipe25, x3_pipe25], [z2_pipe25, x2_pipe25] ), notSource=False)
coll_pipe252   = polygon( ([z2_pipe25, -x2_pipe25], [z3_pipe25, -x3_pipe25], [z4_pipe25, -x4_pipe25], [z1_pipe25, -x1_pipe25] ), notSource=False)

##pipe
x1_pipe26=0.042799
z1_pipe26=11.800

x2_pipe26=0.04445
z2_pipe26=11.800

x3_pipe26=0.04445
z3_pipe26=12.125

x4_pipe26=0.042799
z4_pipe26=12.125

coll_pipe261   = polygon( ([z1_pipe26, x1_pipe26], [z4_pipe26, x4_pipe26], [z3_pipe26, x3_pipe26], [z2_pipe26, x2_pipe26] ), notSource=False)
coll_pipe262   = polygon( ([z2_pipe26, -x2_pipe26], [z3_pipe26, -x3_pipe26], [z4_pipe26, -x4_pipe26], [z1_pipe26, -x1_pipe26] ), notSource=False)

##step
x1_pipe27=0.042799
z1_pipe27=12.125

x2_pipe27=0.0460375
z2_pipe27=12.125

x3_pipe27=0.0460375
z3_pipe27=12.200

x4_pipe27=0.042799
z4_pipe27=12.200

coll_pipe271   = polygon( ([z1_pipe27, x1_pipe27], [z4_pipe27, x4_pipe27], [z3_pipe27, x3_pipe27], [z2_pipe27, x2_pipe27] ), notSource=False)
coll_pipe272   = polygon( ([z2_pipe27, -x2_pipe27], [z3_pipe27, -x3_pipe27], [z4_pipe27, -x4_pipe27], [z1_pipe27, -x1_pipe27] ), notSource=False)

##pipe
x1_pipe28=0.0443865
z1_pipe28=12.200

x2_pipe28=0.0460375
z2_pipe28=12.200

x3_pipe28=0.0460375
z3_pipe28=12.600

x4_pipe28=0.0443865
z4_pipe28=12.600

coll_pipe281   = polygon( ([z1_pipe28, x1_pipe28], [z4_pipe28, x4_pipe28], [z3_pipe28, x3_pipe28], [z2_pipe28, x2_pipe28] ), notSource=False)
coll_pipe282   = polygon( ([z2_pipe28, -x2_pipe28], [z3_pipe28, -x3_pipe28], [z4_pipe28, -x4_pipe28], [z1_pipe28, -x1_pipe28] ), notSource=False)

##step
x1_pipe29=0.0443865
z1_pipe29=12.600

x2_pipe29=0.047625
z2_pipe29=12.600

x3_pipe29=0.047625
z3_pipe29=12.700

x4_pipe29=0.0443865
z4_pipe29=12.700

coll_pipe291   = polygon( ([z1_pipe29, x1_pipe29], [z4_pipe29, x4_pipe29], [z3_pipe29, x3_pipe29], [z2_pipe29, x2_pipe29] ), notSource=False)
coll_pipe292   = polygon( ([z2_pipe29, -x2_pipe29], [z3_pipe29, -x3_pipe29], [z4_pipe29, -x4_pipe29], [z1_pipe29, -x1_pipe29] ), notSource=False)

##pipe
x1_pipe29=0.045974
z1_pipe29=12.700

x2_pipe29=0.047625
z2_pipe29=12.700

x3_pipe29=0.047625
z3_pipe29=13.000

x4_pipe29=0.045974
z4_pipe29=13.000

coll_pipe291   = polygon( ([z1_pipe29, x1_pipe29], [z4_pipe29, x4_pipe29], [z3_pipe29, x3_pipe29], [z2_pipe29, x2_pipe29] ), notSource=False)
coll_pipe292   = polygon( ([z2_pipe29, -x2_pipe29], [z3_pipe29, -x3_pipe29], [z4_pipe29, -x4_pipe29], [z1_pipe29, -x1_pipe29] ), notSource=False)

##step
x1_pipe30=0.045974
z1_pipe30=13.000

x2_pipe30=0.0508
z2_pipe30=13.000

x3_pipe30=0.0508
z3_pipe30=13.100

x4_pipe30=0.045974
z4_pipe30=13.100

coll_pipe301   = polygon( ([z1_pipe30, x1_pipe30], [z4_pipe30, x4_pipe30], [z3_pipe30, x3_pipe30], [z2_pipe30, x2_pipe30] ), notSource=False)
coll_pipe302   = polygon( ([z2_pipe30, -x2_pipe30], [z3_pipe30, -x3_pipe30], [z4_pipe30, -x4_pipe30], [z1_pipe30, -x1_pipe30] ), notSource=False)

##pipe
x1_pipe31=0.049149
z1_pipe31=13.100

x2_pipe31=0.0508
z2_pipe31=13.100

x3_pipe31=0.0508
z3_pipe31=13.200

x4_pipe31=0.049149
z4_pipe31=13.200

coll_pipe311   = polygon( ([z1_pipe31, x1_pipe31], [z4_pipe31, x4_pipe31], [z3_pipe31, x3_pipe31], [z2_pipe31, x2_pipe31] ), notSource=False)
coll_pipe312   = polygon( ([z2_pipe31, -x2_pipe31], [z3_pipe31, -x3_pipe31], [z4_pipe31, -x4_pipe31], [z1_pipe31, -x1_pipe31] ), notSource=False)

##step
x1_pipe32=0.049149
z1_pipe32=13.200

x2_pipe32=0.05715
z2_pipe32=13.200

x3_pipe32=0.05715
z3_pipe32=13.300

x4_pipe32=0.049149
z4_pipe32=13.300

coll_pipe321   = polygon( ([z1_pipe32, x1_pipe32], [z4_pipe32, x4_pipe32], [z3_pipe32, x3_pipe32], [z2_pipe32, x2_pipe32] ), notSource=False)
coll_pipe322   = polygon( ([z2_pipe32, -x2_pipe32], [z3_pipe32, -x3_pipe32], [z4_pipe32, -x4_pipe32], [z1_pipe32, -x1_pipe32] ), notSource=False)

##pipe
x1_pipe33=0.0550418
z1_pipe33=13.300

x2_pipe33=0.05715
z2_pipe33=13.300

x3_pipe33=0.05715
z3_pipe33=13.650

x4_pipe33=0.0550418
z4_pipe33=13.650

coll_pipe331   = polygon( ([z1_pipe33, x1_pipe33], [z4_pipe33, x4_pipe33], [z3_pipe33, x3_pipe33], [z2_pipe33, x2_pipe33] ), notSource=False)
coll_pipe332   = polygon( ([z2_pipe33, -x2_pipe33], [z3_pipe33, -x3_pipe33], [z4_pipe33, -x4_pipe33], [z1_pipe33, -x1_pipe33] ), notSource=False)

##step
x1_pipe34=0.0550418
z1_pipe34=13.650

x2_pipe34=0.0635
z2_pipe34=13.650

x3_pipe34=0.0635
z3_pipe34=13.750

x4_pipe34=0.0550418
z4_pipe34=13.750

coll_pipe341   = polygon( ([z1_pipe34, x1_pipe34], [z4_pipe34, x4_pipe34], [z3_pipe34, x3_pipe34], [z2_pipe34, x2_pipe34] ), notSource=False)
coll_pipe342   = polygon( ([z2_pipe34, -x2_pipe34], [z3_pipe34, -x3_pipe34], [z4_pipe34, -x4_pipe34], [z1_pipe34, -x1_pipe34] ), notSource=False)

##pipe
x1_pipe35=0.0613918
z1_pipe35=13.750

x2_pipe35=0.0635
z2_pipe35=13.750

x3_pipe35=0.0635
z3_pipe35=14.475

x4_pipe35=0.0613918
z4_pipe35=14.475

coll_pipe351   = polygon( ([z1_pipe35, x1_pipe35], [z4_pipe35, x4_pipe35], [z3_pipe35, x3_pipe35], [z2_pipe35, x2_pipe35] ), notSource=False)
coll_pipe352   = polygon( ([z2_pipe35, -x2_pipe35], [z3_pipe35, -x3_pipe35], [z4_pipe35, -x4_pipe35], [z1_pipe35, -x1_pipe35] ), notSource=False)

##step
x1_pipe36=0.0613918
z1_pipe36=14.475

x2_pipe36=0.0762
z2_pipe36=14.475

x3_pipe36=0.0762
z3_pipe36=14.500

x4_pipe36=0.0613918
z4_pipe36=14.500

coll_pipe361   = polygon( ([z1_pipe36, x1_pipe36], [z4_pipe36, x4_pipe36], [z3_pipe36, x3_pipe36], [z2_pipe36, x2_pipe36] ), notSource=False)
coll_pipe362   = polygon( ([z2_pipe36, -x2_pipe36], [z3_pipe36, -x3_pipe36], [z4_pipe36, -x4_pipe36], [z1_pipe36, -x1_pipe36] ), notSource=False)

##pipe
x1_pipe37=0.073152
z1_pipe37=14.500

x2_pipe37=0.0762
z2_pipe37=14.500

x3_pipe37=0.0762
z3_pipe37=16.475

x4_pipe37=0.073152
z4_pipe37=16.475

coll_pipe371   = polygon( ([z1_pipe37, x1_pipe37], [z4_pipe37, x4_pipe37], [z3_pipe37, x3_pipe37], [z2_pipe37, x2_pipe37] ), notSource=False)
coll_pipe372   = polygon( ([z2_pipe37, -x2_pipe37], [z3_pipe37, -x3_pipe37], [z4_pipe37, -x4_pipe37], [z1_pipe37, -x1_pipe37] ), notSource=False)

##step
x1_pipe38=0.073152
z1_pipe38=16.475

x2_pipe38=0.1016
z2_pipe38=16.475

x3_pipe38=0.1016
z3_pipe38=16.500

x4_pipe38=0.073152
z4_pipe38=16.500

coll_pipe381   = polygon( ([z1_pipe38, x1_pipe38], [z4_pipe38, x4_pipe38], [z3_pipe38, x3_pipe38], [z2_pipe38, x2_pipe38] ), notSource=False)
coll_pipe382   = polygon( ([z2_pipe38, -x2_pipe38], [z3_pipe38, -x3_pipe38], [z4_pipe38, -x4_pipe38], [z1_pipe38, -x1_pipe38] ), notSource=False)


##pipe
x1_pipe39=0.0968502
z1_pipe39=16.500

x2_pipe39=0.1016
z2_pipe39=16.500

x3_pipe39=0.1016
z3_pipe39=19.475

x4_pipe39=0.0968502
z4_pipe39=19.475

coll_pipe391   = polygon( ([z1_pipe39, x1_pipe39], [z4_pipe39, x4_pipe39], [z3_pipe39, x3_pipe39], [z2_pipe39, x2_pipe39] ), notSource=False)
coll_pipe392   = polygon( ([z2_pipe39, -x2_pipe39], [z3_pipe39, -x3_pipe39], [z4_pipe39, -x4_pipe39], [z1_pipe39, -x1_pipe39] ), notSource=False)


##step
x1_pipe40=0.0968502
z1_pipe40=19.475

x2_pipe40=0.14605
z2_pipe40=19.475

x3_pipe40=0.14605
z3_pipe40=19.500

x4_pipe40=0.0968502
z4_pipe40=19.500

coll_pipe401   = polygon( ([z1_pipe40, x1_pipe40], [z4_pipe40, x4_pipe40], [z3_pipe40, x3_pipe40], [z2_pipe40, x2_pipe40] ), notSource=False)
coll_pipe402   = polygon( ([z2_pipe40, -x2_pipe40], [z3_pipe40, -x3_pipe40], [z4_pipe40, -x4_pipe40], [z1_pipe40, -x1_pipe40] ), notSource=False)

##pipe
x1_pipe41=0.14605
z1_pipe41=19.500

x2_pipe41=0.1524
z2_pipe41=19.500

x3_pipe41=0.1524
z3_pipe41=25.475

x4_pipe41=0.14605
z4_pipe41=25.475

coll_pipe411   = polygon( ([z1_pipe41, x1_pipe41], [z4_pipe41, x4_pipe41], [z3_pipe41, x3_pipe41], [z2_pipe41, x2_pipe41] ), notSource=False)
coll_pipe412   = polygon( ([z2_pipe41, -x2_pipe41], [z3_pipe41, -x3_pipe41], [z4_pipe41, -x4_pipe41], [z1_pipe41, -x1_pipe41] ), notSource=False)

##step
x1_pipe42=0.14605
z1_pipe42=25.475

x2_pipe42=0.193675
z2_pipe42=25.475

x3_pipe42=0.193675
z3_pipe42=25.500

x4_pipe42=0.14605
z4_pipe42=25.500

coll_pipe421   = polygon( ([z1_pipe42, x1_pipe42], [z4_pipe42, x4_pipe42], [z3_pipe42, x3_pipe42], [z2_pipe42, x2_pipe42] ), notSource=False)
coll_pipe422   = polygon( ([z2_pipe42, -x2_pipe42], [z3_pipe42, -x3_pipe42], [z4_pipe42, -x4_pipe42], [z1_pipe42, -x1_pipe42] ), notSource=False)

##pipe
x1_pipe43=0.193675
z1_pipe43=25.500

x2_pipe43=0.2032
z2_pipe43=25.500

x3_pipe43=0.2032
z3_pipe43=34.000

x4_pipe43=0.193675
z4_pipe43=34.000

coll_pipe431   = polygon( ([z1_pipe43, x1_pipe43], [z4_pipe43, x4_pipe43], [z3_pipe43, x3_pipe43], [z2_pipe43, x2_pipe43] ), notSource=False)
coll_pipe432   = polygon( ([z2_pipe43, -x2_pipe43], [z3_pipe43, -x3_pipe43], [z4_pipe43, -x4_pipe43], [z1_pipe43, -x1_pipe43] ), notSource=False)

################# collimator 4, 3 segmentations

downstream_col4_shift=-1.5
dss=downstream_col4_shift ### This shift is largely arbitrary

#seg 1

x1_coll_4_1=-0.254 #Was simulation -0.300 # Was CAD -0.254
#x1_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
z1_coll_4_1=9.775+dss-tgtoffset

x2_coll_4_1=-0.16787 #-0.1714 #Was -0.23495, then was -0.1655, current sculpt values reflect updated moller envelopes at this upstream z position
#x2_coll_4_1=-0.1714 #-0.1714 #Was -0.23495, then was -0.1655, current sculpt values reflect updated moller envelopes at this upstream z position
z2_coll_4_1=9.775+dss-tgtoffset

x3_coll_4_1=-0.16787 # -0.1714 #Was -0.23495, then was -0.1655
#x3_coll_4_1=-0.1714 # -0.1714 #Was -0.23495, then was -0.1655
z3_coll_4_1=9.875+dss-tgtoffset

x4_coll_4_1=-0.254 #Was simulation -0.300 # Was CAD -0.254
#x4_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
z4_coll_4_1=9.875+dss-tgtoffset


coll_4_1   = polygon( ([z1_coll_4_1, x1_coll_4_1], [z4_coll_4_1, x4_coll_4_1], [z3_coll_4_1, x3_coll_4_1], [z2_coll_4_1, x2_coll_4_1]), notSource=False)


#seg 2

x1_coll_4_2=-0.0525 #0.05 #Was -0.06377, then was -0.0525
#x1_coll_4_2=-0.05 #0.05 #Was -0.06377, then was -0.0525
z1_coll_4_2=9.775+dss-tgtoffset

x2_coll_4_2=-0.030
z2_coll_4_2=9.775+dss-tgtoffset

x3_coll_4_2=-0.030
z3_coll_4_2=9.875+dss-tgtoffset

x4_coll_4_2=-0.0525 #0.05 #Was -0.06377, then was -0.0525
#x4_coll_4_2=-0.05 #0.05 #Was -0.06377, then was -0.0525
z4_coll_4_2=9.875+dss-tgtoffset


coll_4_2   = polygon( ([z1_coll_4_2, x1_coll_4_2], [z4_coll_4_2, x4_coll_4_2], [z3_coll_4_2, x3_coll_4_2], [z2_coll_4_2, x2_coll_4_2]), notSource=False)

#seg 3

x1_coll_4_3=0.030
z1_coll_4_3=9.775+dss-tgtoffset

x2_coll_4_3=0.254 #Was simulation -0.300 # Was CAD -0.254
#x2_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
z2_coll_4_3=9.775+dss-tgtoffset

x3_coll_4_3=0.254 #Was simulation -0.300 # Was CAD -0.254
#x3_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
z3_coll_4_3=9.875+dss-tgtoffset

x4_coll_4_3=0.030
z4_coll_4_3=9.875+dss-tgtoffset


coll_4_3   = polygon( ([z1_coll_4_3, x1_coll_4_3], [z4_coll_4_3, x4_coll_4_3], [z3_coll_4_3, x3_coll_4_3], [z2_coll_4_3, x2_coll_4_3]), notSource=False)


######### collimator 5 (shaped like a tuning fork), 1 seg


x1_coll_5=-0.1055 # use this if you just want the exact y=0 slice
z1_coll_5=12.8-tgtoffset

x2_coll_5=-0.07316 #from GDML
z2_coll_5=12.8-tgtoffset  #thickness of collimator 5 = 35 mm

x3_coll_5=-0.07316 #from GDML
z3_coll_5=12.87-tgtoffset

x4_coll_5=-0.1055 # use this if you just want the exact y=0 slice
z4_coll_5=12.87-tgtoffset

coll_5   = polygon( ([z1_coll_5, x1_coll_5], [z4_coll_5, x4_coll_5], [z3_coll_5, x3_coll_5], [z2_coll_5, x2_coll_5]), notSource=False)


#### quartz

#quartz1 = polygon( ([28.0, 0.6], [28.01, 0.6], [28.01, 1.4], [28, 1.4]), isDetector=True )
#quartz2 = polygon( ([28.0, -1.4], [28.01, -1.4], [28.01, -0.6], [28, -0.6]), isDetector=True )

det_inner_radius=0.69 # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
det_outer_radius=1.30 # ring 6 quartz ends at 1.2, PMTs begin at 1.3
det_z_pos=26.5
det_z_extent=1.0 # was = .02 for ideal detector

quartz1 = polygon( ([det_z_pos, det_inner_radius], [det_z_pos+det_z_extent, det_inner_radius], [det_z_pos+det_z_extent, det_outer_radius], [det_z_pos, det_outer_radius]), isDetector=True )
quartz2 = polygon( ([det_z_pos, -det_outer_radius], [det_z_pos+det_z_extent, -det_outer_radius], [det_z_pos+det_z_extent, -det_inner_radius], [det_z_pos, -det_inner_radius]), isDetector=True )

#### sub-quartz array detector to give an idea about the available space before photons become an issue again

sub_det_inner_radius=0.6 # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
sub_det_outer_radius=0.689 # ring 6 quartz ends at 1.2, PMTs begin at 1.3
sub_det_z_pos=26.5
sub_det_z_extent=1.0 # was = .02 for ideal detector
#sub_det_inner_radius=0.06 # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
#sub_det_outer_radius=0.689 # ring 6 quartz ends at 1.2, PMTs begin at 1.3
#sub_det_z_pos=6.0
#sub_det_z_extent=1.0 # was = .02 for ideal detector

sub_quartz1 = polygon( ([sub_det_z_pos, sub_det_inner_radius], [sub_det_z_pos+sub_det_z_extent, sub_det_inner_radius], [sub_det_z_pos+sub_det_z_extent, sub_det_outer_radius], [sub_det_z_pos, sub_det_outer_radius]), isDetector=True )
sub_quartz2 = polygon( ([sub_det_z_pos, -sub_det_outer_radius], [sub_det_z_pos+sub_det_z_extent, -sub_det_outer_radius], [sub_det_z_pos+sub_det_z_extent, -sub_det_inner_radius], [sub_det_z_pos, -sub_det_inner_radius]), isDetector=True )


#quartz1 = polygon( ([28.0, 0.55], [28.02, 0.55], [28.02, 1.3], [28, 1.3]), isDetector=True )
#quartz2 = polygon( ([28.0, -1.3], [28.02, -1.3], [28.02, -0.55], [28, -0.55]), isDetector=True )

##################################################################################################################################

sources.append(target)

allpolys.append(collar_top)
allpolys.append(collar_bottom)

allpolys.append(coll_inner_photon_top_1)
allpolys.append(coll_inner_photon_bottom_1)
allpolys.append(coll_inner_photon_top_2)
allpolys.append(coll_inner_photon_bottom_2)
allpolys.append(coll_inner_photon_top_3)
allpolys.append(coll_inner_photon_bottom_3)
allpolys.append(coll_inner_photon_top_4)
allpolys.append(coll_inner_photon_bottom_4)
allpolys.append(coll_inner_photon_top_5)
allpolys.append(coll_inner_photon_bottom_5)

allpolys.append(coll_2_1)
allpolys.append(coll_2_2)
allpolys.append(coll_2_3)

allpolys.append(coll_pipe01)
allpolys.append(coll_pipe02)

allpolys.append(coll_pipe11_1)
allpolys.append(coll_pipe12_1)

allpolys.append(coll_pipe11)
allpolys.append(coll_pipe12)

allpolys.append(coll_pipe21)
allpolys.append(coll_pipe22)

allpolys.append(coll_pipe31)
allpolys.append(coll_pipe32)

allpolys.append(coll_pipe41)
allpolys.append(coll_pipe42)

allpolys.append(coll_pipe51)
allpolys.append(coll_pipe52)

allpolys.append(coll_pipe61)
allpolys.append(coll_pipe62)

allpolys.append(coll_pipe71)
allpolys.append(coll_pipe72)


allpolys.append(coll_pipe81)
allpolys.append(coll_pipe82)

allpolys.append(coll_pipe91)
allpolys.append(coll_pipe92)

allpolys.append(coll_pipe101)
allpolys.append(coll_pipe102)

allpolys.append(coll_pipe111)
allpolys.append(coll_pipe112)

allpolys.append(coll_pipe121)
allpolys.append(coll_pipe122)

allpolys.append(coll_pipe131)
allpolys.append(coll_pipe132)

allpolys.append(coll_pipe141)
allpolys.append(coll_pipe142)

allpolys.append(coll_pipe151)
allpolys.append(coll_pipe152)

allpolys.append(coll_pipe161)
allpolys.append(coll_pipe162)

allpolys.append(coll_pipe171)
allpolys.append(coll_pipe172)

allpolys.append(coll_pipe181)
allpolys.append(coll_pipe182)

allpolys.append(coll_pipe191)
allpolys.append(coll_pipe192)

allpolys.append(coll_pipe201)
allpolys.append(coll_pipe202)

allpolys.append(coll_pipe211)
allpolys.append(coll_pipe212)

allpolys.append(coll_pipe221)
allpolys.append(coll_pipe222)

allpolys.append(coll_pipe231)
allpolys.append(coll_pipe232)

allpolys.append(coll_pipe241)
allpolys.append(coll_pipe242)

allpolys.append(coll_pipe251)
allpolys.append(coll_pipe252)

allpolys.append(coll_pipe261)
allpolys.append(coll_pipe262)

allpolys.append(coll_pipe271)
allpolys.append(coll_pipe272)

allpolys.append(coll_pipe281)
allpolys.append(coll_pipe282)

allpolys.append(coll_pipe291)
allpolys.append(coll_pipe292)

allpolys.append(coll_pipe301)
allpolys.append(coll_pipe302)

allpolys.append(coll_pipe311)
allpolys.append(coll_pipe312)

allpolys.append(coll_pipe321)
allpolys.append(coll_pipe322)

allpolys.append(coll_pipe331)
allpolys.append(coll_pipe332)

allpolys.append(coll_pipe341)
allpolys.append(coll_pipe342)

allpolys.append(coll_pipe351)
allpolys.append(coll_pipe352)

allpolys.append(coll_pipe361)
allpolys.append(coll_pipe362)

allpolys.append(coll_pipe371)
allpolys.append(coll_pipe372)

allpolys.append(coll_pipe381)
allpolys.append(coll_pipe382)

allpolys.append(coll_pipe391)
allpolys.append(coll_pipe392)

allpolys.append(coll_pipe401)
allpolys.append(coll_pipe402)

allpolys.append(coll_pipe411)
allpolys.append(coll_pipe412)

allpolys.append(coll_pipe421)
allpolys.append(coll_pipe422)

allpolys.append(coll_pipe431)
allpolys.append(coll_pipe432)


allpolys.append(coll_4_1)
allpolys.append(coll_4_2)
allpolys.append(coll_4_3)


allpolys.append(coll_5)

allpolys.append(quartz1)
allpolys.append(quartz2)
allpolys.append(sub_quartz1)
allpolys.append(sub_quartz2)

########################################################################
#  Rough out blocking areas

#for i in range(6):
#    z = 10 + i*3.0
#    ghost  = polygon(([z,-1.4],[z+0.001,-1.4],[z+0.001,1.4], [z,1.4]), isEthereal=True )
#   ghost  = polygon(([z,-1.4],[z+1.5,-1.4],[z+1.5,1.4], [z,1.4]), isEthereal=True )
#    allpolys.append(ghost)

#  One bounce ghost regions
##################################1
#ghost1a = polygon(([28,-1.4], [28, -1.39], [uscoll1_z-uscoll1_thick/2+0.01, uscoll1_r1_up], [uscoll1_z-uscoll1_thick/2, uscoll1_r1_up]), isEthereal=True)
###############################################2
#ghost1b = polygon(([28,-0.6], [28, -0.59], [uscoll1_z+uscoll1_thick/2+0.01, uscoll1_r1_dn], [uscoll1_z+uscoll1_thick/2, uscoll1_r1_dn]), isEthereal=True)

#ghost2a = polygon(([28,-1.4], [28, -1.39], [dscoll1_z-dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z-dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

#ghost2b = polygon(([28,-0.6], [28, -0.59], [dscoll1_z+dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

#allpolys.append(ghost1a)
#allpolys.append(ghost1b)
#allpolys.append(ghost2a)
#allpolys.append(ghost2b)

#  Raw

#z1 = 6.1
#z2 = 7.1

#t = uscoll2_r2 - uscoll2_r1

#slope = (dscoll2_r1- uscoll2_r1)/(dscoll2_thick/2+dscoll2_z - uscoll2_z-uscoll2_thick/2)

#gr1 = uscoll2_r1 + slope*(z1 - uscoll2_z - uscoll2_thick/2)
#gr2 = uscoll2_r1 + slope*(z2 - uscoll2_z - uscoll2_thick/2)

#smallghost1 = polygon(( [z1, -gr1-t], [z2, -gr2-t], [z2, -gr2], [z1, -gr1]), isEthereal = False)

#print "Ghost blocking points:"
#print smallghost1.pts[0][0], smallghost1.pts[0][1]
#print "\t", smallghost1.pts[3][1]
#print smallghost1.pts[1][0], smallghost1.pts[1][1]
#print "\t", smallghost1.pts[2][1]


#smallghost2 = polygon( ([10.1729, -0.0277], [10.7712, -0.0738], [13.7226, -0.1123], [11.374, -0.0320] ), isEthereal=False)

#smallghost1 = polygon(( [6.3932, -0.0350], [8.0240, -0.0425], [7.6242, -0.0334], [6.2734, -0.0281]), isEthereal = False)
#smallghost2 = polygon( ([10.1729, -0.0277], [10.6515, -0.0566], [13.2529, -0.0882], [11.374, -0.0320] ), isEthereal=False)


# straight z
#smallghost1 = polygon(( [6.2734, -0.0334], [7.6852, -0.0385], [7.6852, -0.0334], [6.2734, -0.0281]), isEthereal = False)
#smallghost2 = polygon( ([10.1729, -0.0277], [10.1729, -0.0566], [11.3749, -0.0566], [11.374, -0.0320] ), isEthereal=False)

# Reduce z
#smallghost1 = polygon(( [6.273, -0.039 ], [7.874, -0.0474], [7.874, -0.0383691664116], [6.273, -0.0274]), isEthereal = False)
#smallghost2 = polygon( ([10.472, -0.0431780215291], [10.472, -0.0697], [12.074, -0.079], [12.074, -0.0490] ), isEthereal=False)

#################################################################
#allpolys.append(smallghost1)
###by YX3
#################################################################

#allpolys.append(smallghost2)

#print sources
#print allpolys

print "Starting"

for apoly in allpolys:
    otherpolys = list(allpolys)
    otherpolys.remove(apoly)
    apoly.light( sources, otherpolys )

print "Doing once bounce lighting"

# One bounce
for apoly in allpolys:
    otherpolys = list(allpolys)
    otherpolys.remove(apoly)
    apoly.light(otherpolys, [], 2 )

#print "Ghost intersections:"

#  Print out ghost region values
#for aghost in [ghost1a, ghost1b, smallghost1]:
#    for aface in aghost.faces:
#	print "Of ", aface.v1[0], aface.v1[1], " -> ", aface.v2[0], aface.v2[1]
#	for lface in aface.getlitfaces():
#	    print "\t", lface.v1[0], lface.v1[1], " -> ", lface.v2[0], lface.v2[1]

mydraw = drawlight(allpolys+sources)

Gtk.main()
