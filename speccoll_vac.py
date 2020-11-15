#!/usr/bin/python 
from poly import polygon
from poly import face 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from drawlight import drawlight

sources = []
allpolys = []

OffSet1 = 0.0017

tgtoffset = 0.5
tgtlen = 1.25
#tgtrad = 0.04
#tgtrad = 0.002
tgtrad = 1.4142*0.0025

target = polygon( ([-tgtlen/2,-tgtrad], [tgtlen/2, -tgtrad], [tgtlen/2,tgtrad], [-tgtlen/2,tgtrad]) )

################################################################

###### Lead shield in the target region (for collimating photons)

#seg 1
x1_shield_top=0.145
x1_shield_bottom=-1.150
z1_shield=1.200

x2_shield_top=1.400 
x2_shield_bottom=-0.140
z2_shield=1.200

x3_shield_top=1.400
x3_shield_bottom=-0.140
z3_shield=1.600

x4_shield_top=0.145
x4_shield_bottom=-1.150
z4_shield=1.600


shield_top  = polygon( ([z1_shield,  x1_shield_top], [z4_shield,  x4_shield_top], [z3_shield,  x3_shield_top], [z2_shield,  x2_shield_top] ), notSource=False)
shield_bottom = polygon( ([z1_shield, x1_shield_bottom], [z4_shield, x4_shield_bottom], [z3_shield, x3_shield_bottom], [z2_shield, x2_shield_bottom] ), notSource=False)

###### Lead collar (for collimating photons)

#seg 1
x1_collar=0.074#+0.05
z1_collar=2.851#+1.5

x2_collar=0.330 #*1.414 The collar is a rectangle (in CAD), but the narrow dimension is the one relevant for here
z2_collar=2.851#+1.5

x3_collar=0.330 #*1.414
z3_collar=3.051#+1.5

x4_collar=0.074#+0.05
z4_collar=3.051#+1.5


collar_top    = polygon( ([z1_collar,  x1_collar], [z4_collar,  x4_collar], [z3_collar,  x3_collar], [z2_collar,  x2_collar] ), notSource=False)
collar_bottom = polygon( ([z2_collar, -x2_collar], [z3_collar, -x3_collar], [z4_collar, -x4_collar], [z1_collar, -x1_collar] ), notSource=False)


###### Beam pipe after lead collar and collimator 2
x1_pipe17=0.096825
z1_pipe17=1.600

x2_pipe17=0.1016
z2_pipe17=1.600

x3_pipe17=0.1016
z3_pipe17=2.49123

x4_pipe17=0.096825
z4_pipe17=2.49123

coll_pipe171   = polygon( ([z1_pipe17, x1_pipe17], [z4_pipe17, x4_pipe17], [z3_pipe17, x3_pipe17], [z2_pipe17, x2_pipe17] ), notSource=False)
coll_pipe172   = polygon( ([z2_pipe17, -x2_pipe17], [z3_pipe17, -x3_pipe17], [z4_pipe17, -x4_pipe17], [z1_pipe17, -x1_pipe17] ), notSource=False)

#flange
x1_pipe18=0.1016
z1_pipe18=2.49123

x2_pipe18=0.20955
z2_pipe18=2.49123

x3_pipe18=0.20955
z3_pipe18=2.49123+0.05715

x4_pipe18=0.1016
z4_pipe18=2.49123+0.05715

coll_pipe181   = polygon( ([z1_pipe18, x1_pipe18], [z4_pipe18, x4_pipe18], [z3_pipe18, x3_pipe18], [z2_pipe18, x2_pipe18] ), notSource=False)
coll_pipe182   = polygon( ([z2_pipe18, -x2_pipe18], [z3_pipe18, -x3_pipe18], [z4_pipe18, -x4_pipe18], [z1_pipe18, -x1_pipe18] ), notSource=False)

x1_pipe19=0.17145
z1_pipe19=2.49123+0.05715

x2_pipe19=0.1778
z2_pipe19=2.49123+0.05715

x3_pipe19=0.1778
z3_pipe19=5.975

x4_pipe19=0.17145
z4_pipe19=5.975

coll_pipe191   = polygon( ([z1_pipe19, x1_pipe19], [z4_pipe19, x4_pipe19], [z3_pipe19, x3_pipe19], [z2_pipe19, x2_pipe19] ), notSource=False)
coll_pipe192   = polygon( ([z2_pipe19, -x2_pipe19], [z3_pipe19, -x3_pipe19], [z4_pipe19, -x4_pipe19], [z1_pipe19, -x1_pipe19] ), notSource=False)

#flange
x1_pipe20=0.1778
z1_pipe20=5.975

x2_pipe20=0.34449
z2_pipe20=5.975

x3_pipe20=0.34449
z3_pipe20=5.975+0.08255

x4_pipe20=0.1778
z4_pipe20=5.975+0.08255

coll_pipe201   = polygon( ([z1_pipe20, x1_pipe20], [z4_pipe20, x4_pipe20], [z3_pipe20, x3_pipe20], [z2_pipe20, x2_pipe20] ), notSource=False)
coll_pipe202   = polygon( ([z2_pipe20, -x2_pipe20], [z3_pipe20, -x3_pipe20], [z4_pipe20, -x4_pipe20], [z1_pipe20, -x1_pipe20] ), notSource=False)

x1_pipe21=0.295275
z1_pipe21=5.975+0.08255

x2_pipe21=0.3048
z2_pipe21=5.975+0.08255

x3_pipe21=0.3048
z3_pipe21=8.250682

x4_pipe21=0.295275
z4_pipe21=8.250682

coll_pipe211   = polygon( ([z1_pipe21, x1_pipe21], [z4_pipe21, x4_pipe21], [z3_pipe21, x3_pipe21], [z2_pipe21, x2_pipe21] ), notSource=False)
coll_pipe212   = polygon( ([z2_pipe21, -x2_pipe21], [z3_pipe21, -x3_pipe21], [z4_pipe21, -x4_pipe21], [z1_pipe21, -x1_pipe21] ), notSource=False)

#front plate for vacuum vessels
x1_pipe22=0.250063
z1_pipe22=8.250682

x2_pipe22=1.36525
z2_pipe22=8.250682

x3_pipe22=1.36525
z3_pipe22=8.250682+0.068326

x4_pipe22=0.250063
z4_pipe22=8.250682+0.068326

coll_pipe221   = polygon( ([z1_pipe22, x1_pipe22], [z4_pipe22, x4_pipe22], [z3_pipe22, x3_pipe22], [z2_pipe22, x2_pipe22] ), notSource=False)
coll_pipe222   = polygon( ([z2_pipe22, -x2_pipe22], [z3_pipe22, -x3_pipe22], [z4_pipe22, -x4_pipe22], [z1_pipe22, -x1_pipe22] ), notSource=False)

x1_pipe23=1.250188
z1_pipe23=8.250682+0.068326

x2_pipe23=1275.588
z2_pipe23=8.250682+0.068326

x3_pipe23=1275.588
z3_pipe23=12.300+4.5-0.068326

x4_pipe23=1.250188
z4_pipe23=12.300+4.5-0.068326

coll_pipe231   = polygon( ([z1_pipe23, x1_pipe23], [z4_pipe23, x4_pipe23], [z3_pipe23, x3_pipe23], [z2_pipe23, x2_pipe23] ), notSource=False)
coll_pipe232   = polygon( ([z2_pipe23, -x2_pipe23], [z3_pipe23, -x3_pipe23], [z4_pipe23, -x4_pipe23], [z1_pipe23, -x1_pipe23] ), notSource=False)

x1_pipe24=0.595
z1_pipe24=12.300+4.5-0.068326

x2_pipe24=1.36525
z2_pipe24=12.300+4.5-0.068326

x3_pipe24=1.36525
z3_pipe24=12.300+4.5

x4_pipe24=0.595
z4_pipe24=12.300+4.5

coll_pipe241   = polygon( ([z1_pipe24, x1_pipe24], [z4_pipe24, x4_pipe24], [z3_pipe24, x3_pipe24], [z2_pipe24, x2_pipe24] ), notSource=False)
coll_pipe242   = polygon( ([z2_pipe24, -x2_pipe24], [z3_pipe24, -x3_pipe24], [z4_pipe24, -x4_pipe24], [z1_pipe24, -x1_pipe24] ), notSource=False)
###### Hybrid upstream Lead collar (for ep scattering)

x1_collar3=0.265
z1_collar3=4.4305+4.5

x2_collar3=1.2
z2_collar3=4.4305+4.5

x3_collar3=1.2
z3_collar3=4.6805+4.5

x4_collar3=0.265
z4_collar3=4.6805+4.5


collar3_top    = polygon( ([z1_collar3,  x1_collar3], [z4_collar3,  x4_collar3], [z3_collar3,  x3_collar3], [z2_collar3,  x2_collar3] ), notSource=False)
collar3_bottom = polygon( ([z2_collar3, -x2_collar3], [z3_collar3, -x3_collar3], [z4_collar3, -x4_collar3], [z1_collar3, -x1_collar3] ), notSource=False)

#################################################################

###### First downstream Lead collar (for ep scattering)

x1_collar1=0.600
z1_collar1=12.250+4.5

x2_collar1=0.750 
z2_collar1=12.250+4.5

x3_collar1=0.750
z3_collar1=12.400+4.5

x4_collar1=0.600
z4_collar1=12.400+4.5


collar_top1    = polygon( ([z1_collar1,  x1_collar1], [z4_collar1,  x4_collar1], [z3_collar1,  x3_collar1], [z2_collar1,  x2_collar1] ), notSource=False)
collar_bottom1 = polygon( ([z2_collar1, -x2_collar1], [z3_collar1, -x3_collar1], [z4_collar1, -x4_collar1], [z1_collar1, -x1_collar1] ), notSource=False)

###### Second downstream Lead collar (for ep scattering)

x1_collar2=0.952
z1_collar2=18.850+4.5

x2_collar2=1.200
z2_collar2=18.850+4.5

x3_collar2=1.200
z3_collar2=19.000+4.5

x4_collar2=0.952
z4_collar2=19.000+4.5


collar_top2    = polygon( ([z1_collar2,  x1_collar2], [z4_collar2,  x4_collar2], [z3_collar2,  x3_collar2], [z2_collar2,  x2_collar2] ), notSource=False)
collar_bottom2 = polygon( ([z2_collar2, -x2_collar2], [z3_collar2, -x3_collar2], [z4_collar2, -x4_collar2], [z1_collar2, -x1_collar2] ), notSource=False)

#################################################################

######inner photon collimator (Col 1)
# Updated on Nov 8 2020 with merged extended collimator

x1_inner_photon_1=0.020 
z1_inner_photon_1=4.675

x2_inner_photon_1=0.027 
z2_inner_photon_1=4.675

x3_inner_photon_1=0.027
z3_inner_photon_1=4.775

x4_inner_photon_1=0.01625 
z4_inner_photon_1=4.775

x1_inner_photon_2=0.01625 
z1_inner_photon_2=4.775

x2_inner_photon_2=0.0275
z2_inner_photon_2=4.775

x3_inner_photon_2=0.0275
z3_inner_photon_2=4.865

x4_inner_photon_2=0.0151
z4_inner_photon_2=4.865

x1_inner_photon_3=0.0151
z1_inner_photon_3=4.865

x2_inner_photon_3=0.0275
z2_inner_photon_3=4.865

x3_inner_photon_3=0.0275
z3_inner_photon_3=4.985

x4_inner_photon_3=0.0141 
z4_inner_photon_3=4.985

x1_inner_photon_4=0.0141
z1_inner_photon_4=4.985

x2_inner_photon_4=0.0275
z2_inner_photon_4=4.985

x3_inner_photon_4=0.0275
z3_inner_photon_4=5.075

x4_inner_photon_4=0.013629 
z4_inner_photon_4=5.075

x1_inner_photon_5=0.013629
z1_inner_photon_5=5.075

x2_inner_photon_5=0.0275
z2_inner_photon_5=5.075

x3_inner_photon_5=0.0275
z3_inner_photon_5=5.40

x4_inner_photon_5=0.014536 
z4_inner_photon_5=5.40

x1_inner_photon_6=0.013629
z1_inner_photon_6=5.290

x2_inner_photon_6=0.0275
z2_inner_photon_6=5.290

x3_inner_photon_6=0.0275
z3_inner_photon_6=5.390

x4_inner_photon_6=0.013908 
z4_inner_photon_6=5.390

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

# coll_inner_photon_top_6    = polygon( ([z1_inner_photon_6,  x1_inner_photon_6], [z4_inner_photon_6,  x4_inner_photon_6], [z3_inner_photon_6,  x3_inner_photon_6], [z2_inner_photon_6,  x2_inner_photon_6] ), notSource=False)
# coll_inner_photon_bottom_6 = polygon( ([z2_inner_photon_6, -x2_inner_photon_6], [z3_inner_photon_6, -x3_inner_photon_6], [z4_inner_photon_6, -x4_inner_photon_6], [z1_inner_photon_6, -x1_inner_photon_6] ), notSource=False)


#########collimator 2,  three segments
#seg 1
x1_coll_2_1=-0.035
z1_coll_2_1=5.25

x2_coll_2_1=-0.0275
z2_coll_2_1=5.25

x3_coll_2_1=-0.0275
z3_coll_2_1=5.4

x4_coll_2_1=-0.035
z4_coll_2_1=5.4


coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), notSource=False)
#coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), isDetector=True)


#seg 2

x1_coll_2_2=-0.150
z1_coll_2_2=5.25

x2_coll_2_2=-0.101
z2_coll_2_2=5.25

x3_coll_2_2=-0.101
z3_coll_2_2=5.4

x4_coll_2_2=-0.15
z4_coll_2_2=5.4

coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), notSource=False)
#coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), isDetector=True)

#seg 3

x1_coll_2_3=0.0275
z1_coll_2_3=5.25

x2_coll_2_3= 0.150
z2_coll_2_3=5.25

x3_coll_2_3= 0.1500
z3_coll_2_3=5.4

x4_coll_2_3=0.0275
z4_coll_2_3=5.4


coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), notSource=False)
#coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), isDetector=True)


############# Col2 photon collimating inner_pipe
##pipe
x1_pipe0=0.0205
z1_pipe0=5.4

x2_pipe0=0.0235
z2_pipe0=5.4

x3_pipe0=0.0275
z3_pipe0=7.5

x4_pipe0=0.0305
z4_pipe0=7.5


coll_pipe01   = polygon( ([z1_pipe0, x1_pipe0], [z4_pipe0, x4_pipe0], [z3_pipe0, x3_pipe0], [z2_pipe0, x2_pipe0] ), notSource=False)
coll_pipe02   = polygon( ([z2_pipe0, -x2_pipe0], [z3_pipe0, -x3_pipe0], [z4_pipe0, -x4_pipe0], [z1_pipe0, -x1_pipe0] ), notSource=False)

##pipe  the downstream twobounce shield
x1_pipe1_1=0.0355
z1_pipe1_1=7.875

x2_pipe1_1=0.0385
z2_pipe1_1=7.875

x3_pipe1_1=0.0385
z3_pipe1_1=9.875

x4_pipe1_1=0.0355
z4_pipe1_1=9.875


coll_pipe11_1   = polygon( ([z1_pipe1_1, x1_pipe1_1], [z4_pipe1_1, x4_pipe1_1], [z3_pipe1_1, x3_pipe1_1], [z2_pipe1_1, x2_pipe1_1] ), notSource=False)
coll_pipe12_1   = polygon( ([z2_pipe1_1, -x2_pipe1_1], [z3_pipe1_1, -x3_pipe1_1], [z4_pipe1_1, -x4_pipe1_1], [z1_pipe1_1, -x1_pipe1_1] ), notSource=False)
##pipe
x1_pipe1=0.033*1.03
#x1_pipe1=0.035
z1_pipe1=9.50

x2_pipe1=0.036*1.03
#x2_pipe1=0.038
z2_pipe1=9.5

x3_pipe1=0.0396*1.03
#x3_pipe1=0.0419
#z3_pipe1=11.3
z3_pipe1=9.875

x4_pipe1=0.0366*1.03
#x4_pipe1=0.0389
#z4_pipe1=11.3
z4_pipe1=9.875


coll_pipe11   = polygon( ([z1_pipe1, x1_pipe1], [z4_pipe1, x4_pipe1], [z3_pipe1, x3_pipe1], [z2_pipe1, x2_pipe1] ), notSource=False)
coll_pipe12   = polygon( ([z2_pipe1, -x2_pipe1], [z3_pipe1, -x3_pipe1], [z4_pipe1, -x4_pipe1], [z1_pipe1, -x1_pipe1] ), notSource=False)

##step
x1_pipe2=0.0366*1.03
#x1_pipe2=0.0389
z1_pipe2=11.3

x2_pipe2=0.0396*1.03
#x2_pipe2=0.0419
z2_pipe2=11.3

x3_pipe2=0.0396*1.03
#x3_pipe2=0.0419
z3_pipe2=11.35
#z3_pipe2=12.37

x4_pipe2=0.0366*1.03
#x4_pipe2=0.0389
z4_pipe2=11.35
#z4_pipe2=12.37

coll_pipe21   = polygon( ([z1_pipe2, x1_pipe2], [z4_pipe2, x4_pipe2], [z3_pipe2, x3_pipe2], [z2_pipe2, x2_pipe2] ), notSource=False)
coll_pipe22   = polygon( ([z2_pipe2, -x2_pipe2], [z3_pipe2, -x3_pipe2], [z4_pipe2, -x4_pipe2], [z1_pipe2, -x1_pipe2] ), notSource=False)

#Downstream beampipe outside the vacuum enclosure
##Downstream window
x1_pipe3=0.50476
z1_pipe3=23.01512

x2_pipe3=0.50714125
z2_pipe3=23.01512

x3_pipe3=0.988+0.00238125
z3_pipe3=23.01512+0.2804

x4_pipe3=0.988
z4_pipe3=23.01512+0.2804


coll_pipe31   = polygon( ([z1_pipe3, x1_pipe3], [z4_pipe3, x4_pipe3], [z3_pipe3, x3_pipe3], [z2_pipe3, x2_pipe3] ), notSource=False)
coll_pipe32   = polygon( ([z2_pipe3, -x2_pipe3], [z3_pipe3, -x3_pipe3], [z4_pipe3, -x4_pipe3], [z1_pipe3, -x1_pipe3] ), notSource=False)

##cylindrical sections
x1_pipe4=0.50476
z1_pipe4=23.010

x2_pipe4=0.50476+0.0047625
z2_pipe4=23.010

x3_pipe4=0.50476+0.0047625
z3_pipe4=23.010+0.454

x4_pipe4=0.50476
z4_pipe4=23.010+0.454

coll_pipe41   = polygon( ([z1_pipe4, x1_pipe4], [z4_pipe4, x4_pipe4], [z3_pipe4, x3_pipe4], [z2_pipe4, x2_pipe4] ), notSource=False)
coll_pipe42   = polygon( ([z2_pipe4, -x2_pipe4], [z3_pipe4, -x3_pipe4], [z4_pipe4, -x4_pipe4], [z1_pipe4, -x1_pipe4] ), notSource=False)

##conical pipe
x1_pipe5=0.504775
z1_pipe5=23.464

x2_pipe5=0.504775+0.0047625
z2_pipe5=23.464

x3_pipe5=0.52833+0.0047625
z3_pipe5=23.464+0.6304

x4_pipe5=0.52833
z4_pipe5=23.464+0.6304


coll_pipe51   = polygon( ([z1_pipe5, x1_pipe5], [z4_pipe5, x4_pipe5], [z3_pipe5, x3_pipe5], [z2_pipe5, x2_pipe5] ), notSource=False)
coll_pipe52   = polygon( ([z2_pipe5, -x2_pipe5], [z3_pipe5, -x3_pipe5], [z4_pipe5, -x4_pipe5], [z1_pipe5, -x1_pipe5] ), notSource=False)

##flange+bellow
x1_pipe6=0.5235
z1_pipe6=24.0944

x2_pipe6=0.55335
z2_pipe6=24.0944

x3_pipe6=0.5536
z3_pipe6=24.3067

x4_pipe6=0.525
z4_pipe6=24.3067

coll_pipe61   = polygon( ([z1_pipe6, x1_pipe6], [z4_pipe6, x4_pipe6], [z3_pipe6, x3_pipe6], [z2_pipe6, x2_pipe6] ), notSource=False)
coll_pipe62   = polygon( ([z2_pipe6, -x2_pipe6], [z3_pipe6, -x3_pipe6], [z4_pipe6, -x4_pipe6], [z1_pipe6, -x1_pipe6] ), notSource=False)

##conical pipe
x1_pipe7=0.5266
z1_pipe7=24.3067

x2_pipe7=0.5266+0.00635
z2_pipe7=24.3067

x3_pipe7=0.550+0.00635
z3_pipe7=24.3067+0.1873

x4_pipe7=0.550
z4_pipe7=24.3067+0.1873


coll_pipe71   = polygon( ([z1_pipe7, x1_pipe7], [z4_pipe7, x4_pipe7], [z3_pipe7, x3_pipe7], [z2_pipe7, x2_pipe7] ), notSource=False)
coll_pipe72   = polygon( ([z2_pipe7, -x2_pipe7], [z3_pipe7, -x3_pipe7], [z4_pipe7, -x4_pipe7], [z1_pipe7, -x1_pipe7] ), notSource=False)


##conical pipe
x1_pipe8=0.550
z1_pipe8=24.494

x2_pipe8=0.550+0.01905
z2_pipe8=24.494

x3_pipe8=0.74645+0.01905
z3_pipe8=24.494+6.506

x4_pipe8=0.74645
z4_pipe8=24.494+6.506

coll_pipe81   = polygon( ([z1_pipe8, x1_pipe8], [z4_pipe8, x4_pipe8], [z3_pipe8, x3_pipe8], [z2_pipe8, x2_pipe8] ), notSource=False)
coll_pipe82   = polygon( ([z2_pipe8, -x2_pipe8], [z3_pipe8, -x3_pipe8], [z4_pipe8, -x4_pipe8], [z1_pipe8, -x1_pipe8] ), notSource=False)


##pipe after Vaccum chamber after hybrid
##Step
x1_pipe14=0.600
z1_pipe14=12.405+4.5

x2_pipe14=1.2627
z2_pipe14=12.405+4.5

x3_pipe14=1.2627
z3_pipe14=12.4431+4.5

x4_pipe14=0.600
z4_pipe14=12.4431+4.5

coll_pipe141   = polygon( ([z1_pipe14, x1_pipe14], [z4_pipe14, x4_pipe14], [z3_pipe14, x3_pipe14], [z2_pipe14, x2_pipe14] ), notSource=False)
coll_pipe142   = polygon( ([z2_pipe14, -x2_pipe14], [z3_pipe14, -x3_pipe14], [z4_pipe14, -x4_pipe14], [z1_pipe14, -x1_pipe14] ), notSource=False)

##pipe
x1_pipe15=1.250
z1_pipe15=12.4431+4.5

x2_pipe15=1.2627
z2_pipe15=12.4431+4.5

x3_pipe15=1.2627
z3_pipe15=18.8569+4.5

x4_pipe15=1.250
z4_pipe15=18.8569+4.5

coll_pipe151   = polygon( ([z1_pipe15, x1_pipe15], [z4_pipe15, x4_pipe15], [z3_pipe15, x3_pipe15], [z2_pipe15, x2_pipe15] ), notSource=False)
coll_pipe152   = polygon( ([z2_pipe15, -x2_pipe15], [z3_pipe15, -x3_pipe15], [z4_pipe15, -x4_pipe15], [z1_pipe15, -x1_pipe15] ), notSource=False)

##Step
x1_pipe16=0.952
z1_pipe16=18.8569+4.5

x2_pipe16=1.2627
z2_pipe16=18.8569+4.5

x3_pipe16=1.2627
z3_pipe16=18.895+4.5

x4_pipe16=0.952
z4_pipe16=18.895+4.5


coll_pipe161   = polygon( ([z1_pipe16, x1_pipe16], [z4_pipe16, x4_pipe16], [z3_pipe16, x3_pipe16], [z2_pipe16, x2_pipe16] ), notSource=False)
coll_pipe162   = polygon( ([z2_pipe16, -x2_pipe16], [z3_pipe16, -x3_pipe16], [z4_pipe16, -x4_pipe16], [z1_pipe16, -x1_pipe16] ), notSource=False)


################# collimator 4, 3 segmentations

downstream_col4_shift=-1.5
dss=downstream_col4_shift ### This shift is largely arbitrary

#seg 1

x1_coll_4_1=-0.250 #Was simulation -0.300 # Was CAD -0.254
#x1_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
z1_coll_4_1=9.725+dss-tgtoffset

x2_coll_4_1=-0.1965 #-0.1714 #Was -0.23495, then was -0.1655, current sculpt values reflect updated moller envelopes at this upstream z position
#x2_coll_4_1=-0.1714 #-0.1714 #Was -0.23495, then was -0.1655, current sculpt values reflect updated moller envelopes at this upstream z position
z2_coll_4_1=9.725+dss-tgtoffset

x3_coll_4_1=-0.1965 # -0.1714 #Was -0.23495, then was -0.1655
#x3_coll_4_1=-0.1714 # -0.1714 #Was -0.23495, then was -0.1655
z3_coll_4_1=9.875+dss-tgtoffset

x4_coll_4_1=-0.250 #Was simulation -0.300 # Was CAD -0.254
#x4_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
z4_coll_4_1=9.875+dss-tgtoffset


coll_4_1   = polygon( ([z1_coll_4_1, x1_coll_4_1], [z4_coll_4_1, x4_coll_4_1], [z3_coll_4_1, x3_coll_4_1], [z2_coll_4_1, x2_coll_4_1]), notSource=False)


#seg 2

x1_coll_4_2=-0.0535 #0.05 #Was -0.06377, then was -0.0525
#x1_coll_4_2=-0.05 #0.05 #Was -0.06377, then was -0.0525
z1_coll_4_2=9.775+dss-tgtoffset

x2_coll_4_2=-0.030861
z2_coll_4_2=9.775+dss-tgtoffset

x3_coll_4_2=-0.030861
z3_coll_4_2=9.875+dss-tgtoffset

x4_coll_4_2=-0.0535 #0.05 #Was -0.06377, then was -0.0525
#x4_coll_4_2=-0.05 #0.05 #Was -0.06377, then was -0.0525
z4_coll_4_2=9.875+dss-tgtoffset


coll_4_2   = polygon( ([z1_coll_4_2, x1_coll_4_2], [z4_coll_4_2, x4_coll_4_2], [z3_coll_4_2, x3_coll_4_2], [z2_coll_4_2, x2_coll_4_2]), notSource=False)

#seg 3

x1_coll_4_3=0.030861
z1_coll_4_3=9.775+dss-tgtoffset

x2_coll_4_3=0.250 #Was simulation -0.300 # Was CAD -0.254
#x2_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
z2_coll_4_3=9.775+dss-tgtoffset

x3_coll_4_3=0.250 #Was simulation -0.300 # Was CAD -0.254
#x3_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
z3_coll_4_3=9.875+dss-tgtoffset

x4_coll_4_3=0.030861
z4_coll_4_3=9.875+dss-tgtoffset


coll_4_3   = polygon( ([z1_coll_4_3, x1_coll_4_3], [z4_coll_4_3, x4_coll_4_3], [z3_coll_4_3, x3_coll_4_3], [z2_coll_4_3, x2_coll_4_3]), notSource=False)


######### collimator 5 (shaped like a tuning fork), 1 seg


x1_coll_5=-0.11638 # use this if you just want the exact y=0 slice
z1_coll_5=12.8-tgtoffset

x2_coll_5=-0.07422 #from GDML
z2_coll_5=12.8-tgtoffset  #thickness of collimator 5 = 35 mm

x3_coll_5=-0.07422 #from GDML
z3_coll_5=12.87-tgtoffset

x4_coll_5=-0.11638 # use this if you just want the exact y=0 slice
z4_coll_5=12.87-tgtoffset

coll_5   = polygon( ([z1_coll_5, x1_coll_5], [z4_coll_5, x4_coll_5], [z3_coll_5, x3_coll_5], [z2_coll_5, x2_coll_5]), notSource=False)

###### Lintel (for ep scattering)

x1_lintel=0.435
z1_lintel=7.785+4.5

x2_lintel=0.650
z2_lintel=7.785+4.5

x3_lintel=0.650
z3_lintel=7.885+4.5

x4_lintel=0.435
z4_lintel=7.885+4.5


#collar_top2    = polygon( ([z1_lintel,  x1_lintel], [z4_lintel,  x4_lintel], [z3_lintel,  x3_lintel], [z2_lintel,  x2_lintel] ), notSource=False)
lintel = polygon( ([z2_lintel, -x2_lintel], [z3_lintel, -x3_lintel], [z4_lintel, -x4_lintel], [z1_lintel, -x1_lintel] ), notSource=False)

#################################################################

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

allpolys.append(shield_top)
allpolys.append(shield_bottom)

allpolys.append(collar_top)
allpolys.append(collar_bottom)

allpolys.append(collar_top1)
allpolys.append(collar_bottom1)

allpolys.append(collar_top2)
allpolys.append(collar_bottom2)

allpolys.append(collar3_top)
allpolys.append(collar3_bottom)

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

#allpolys.append(coll_pipe11)
#allpolys.append(coll_pipe12)

#allpolys.append(coll_pipe21)
#allpolys.append(coll_pipe22)

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

allpolys.append(coll_pipe141)
allpolys.append(coll_pipe142)

allpolys.append(coll_pipe151)
allpolys.append(coll_pipe152)

allpolys.append(coll_pipe161)
allpolys.append(coll_pipe162)

#allpolys.append(coll_pipe171)
#allpolys.append(coll_pipe172)
#
#allpolys.append(coll_pipe181)
#allpolys.append(coll_pipe182)
#
#allpolys.append(coll_pipe191)
#allpolys.append(coll_pipe192)
#
#allpolys.append(coll_pipe201)
#allpolys.append(coll_pipe202)
#
#allpolys.append(coll_pipe211)
#allpolys.append(coll_pipe212)
#
#allpolys.append(coll_pipe221)
#allpolys.append(coll_pipe222)
#
#allpolys.append(coll_pipe231)
#allpolys.append(coll_pipe232)
#
#allpolys.append(coll_pipe241)
#allpolys.append(coll_pipe242)

allpolys.append(coll_4_1)
allpolys.append(coll_4_2)
allpolys.append(coll_4_3)


allpolys.append(coll_5)
allpolys.append(lintel)

allpolys.append(quartz1)
allpolys.append(quartz2)
#allpolys.append(sub_quartz1)
#allpolys.append(sub_quartz2)

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

print("Starting")

for apoly in allpolys:
    otherpolys = list(allpolys)
    otherpolys.remove(apoly)
    apoly.light( sources, otherpolys )

print("Doing once bounce lighting")

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
