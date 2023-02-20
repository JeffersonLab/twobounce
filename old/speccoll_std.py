#!/usr/bin/python

from poly import polygon
from poly import face 
from gi.repository import Gtk


from drawlight import drawlight

sources = []
allpolys = []

tgtlen = 1.5
tgtrad = 0.04

target = polygon( ([-tgtlen/2,-tgtrad], [tgtlen/2, -tgtrad], [tgtlen/2,tgtrad], [-tgtlen/2,tgtrad]) )


uscoll1_r1    = 0.023
uscoll1_r2    = 0.030
uscoll1_thick = 0.2
uscoll1_z     = 5.575

uscoll1_up   = polygon( ([uscoll1_z-uscoll1_thick/2, uscoll1_r1], [uscoll1_z+uscoll1_thick/2, uscoll1_r1], [uscoll1_z+uscoll1_thick/2, uscoll1_r2], [uscoll1_z-uscoll1_thick/2, uscoll1_r2] ))

uscoll1_down = polygon( ([uscoll1_z-uscoll1_thick/2, -uscoll1_r2], [uscoll1_z+uscoll1_thick/2, -uscoll1_r2], [uscoll1_z+uscoll1_thick/2, -uscoll1_r1], [uscoll1_z-uscoll1_thick/2, -uscoll1_r1] ))


uscoll2_r1    = 0.026
uscoll2_r2    = 0.034
uscoll2_r3    = 0.110
uscoll2_r4    = 0.300
uscoll2_thick = 0.1
uscoll2_z     = 5.925

uscoll2_up   = polygon( ([uscoll2_z-uscoll2_thick/2, uscoll2_r1], [uscoll2_z+uscoll2_thick/2, uscoll2_r1], [uscoll2_z+uscoll2_thick/2, uscoll2_r4], [uscoll2_z-uscoll2_thick/2, uscoll2_r4] ))
uscoll2_down = polygon( ([uscoll2_z-uscoll2_thick/2, -uscoll2_r2], [uscoll2_z+uscoll2_thick/2, -uscoll2_r2], [uscoll2_z+uscoll2_thick/2, -uscoll2_r1], [uscoll2_z-uscoll2_thick/2, -uscoll2_r1] ))

uscoll2_out_down = polygon( ([uscoll2_z-uscoll2_thick/2, -uscoll2_r4], [uscoll2_z+uscoll2_thick/2, -uscoll2_r4], [uscoll2_z+uscoll2_thick/2, -uscoll2_r3], [uscoll2_z-uscoll2_thick/2, -uscoll2_r3] ))


###################################################################



dscoll1_r1    = 0.034
dscoll1_r2    = 0.058
dscoll1_thick = 0.2
dscoll1_z     = 9.575

dscoll1_up   = polygon( ([dscoll1_z-dscoll1_thick/2, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r2], [dscoll1_z-dscoll1_thick/2, dscoll1_r2] ))
dscoll1_down = polygon( ([dscoll1_z-dscoll1_thick/2, -dscoll1_r2], [dscoll1_z+dscoll1_thick/2, -dscoll1_r2], [dscoll1_z+dscoll1_thick/2, -dscoll1_r1], [dscoll1_z-dscoll1_thick/2, -dscoll1_r1] ))


dscoll2_r1    = 0.038
dscoll2_r2    = 0.065
dscoll2_r3    = 0.223
dscoll2_r4    = 0.300
dscoll2_thick = 0.1
dscoll2_z     = 9.825

dscoll2_up   = polygon( ([dscoll2_z-dscoll2_thick/2, dscoll2_r1], [dscoll2_z+dscoll2_thick/2, dscoll2_r1], [dscoll2_z+dscoll2_thick/2, dscoll2_r4], [dscoll2_z-dscoll2_thick/2, dscoll2_r4] ))

dscoll2_down = polygon( ([dscoll2_z-dscoll2_thick/2, -dscoll2_r2], [dscoll2_z+dscoll2_thick/2, -dscoll2_r2], [dscoll2_z+dscoll2_thick/2, -dscoll2_r1], [dscoll2_z-dscoll2_thick/2, -dscoll2_r1] ))

dscoll2_out_down = polygon( ([dscoll2_z-dscoll2_thick/2, -dscoll2_r4], [dscoll2_z+dscoll2_thick/2, -dscoll2_r4], [dscoll2_z+dscoll2_thick/2, -dscoll2_r3], [dscoll2_z-dscoll2_thick/2, -dscoll2_r3] ))



quartz1 = polygon( ([28.0, 0.6], [28.01, 0.6], [28.01, 1.4], [28, 1.4]), isDetector=True )
quartz2 = polygon( ([28.0, -1.4], [28.01, -1.4], [28.01, -0.6], [28, -0.6]), isDetector=True )

sources.append(target)

allpolys.append(uscoll1_up)
allpolys.append(uscoll1_down)
allpolys.append(uscoll2_up)
allpolys.append(uscoll2_down)
allpolys.append(uscoll2_out_down)

allpolys.append(dscoll1_up)
allpolys.append(dscoll1_down)
allpolys.append(dscoll2_up)
allpolys.append(dscoll2_down)
allpolys.append(dscoll2_out_down)

allpolys.append(quartz1)
allpolys.append(quartz2)

print sources
print allpolys

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

mydraw = drawlight(allpolys+sources)

Gtk.main()
