#!/usr/bin/python 
from poly import polygon
from poly import face 
from gi.repository import Gtk


from drawlight import drawlight

sources = []
allpolys = []

tgtlen = 1.5
#tgtrad = 0.04
#tgtrad = 0.002
tgtrad = 0.0025

target = polygon( ([-tgtlen/2,-tgtrad], [tgtlen/2, -tgtrad], [tgtlen/2,tgtrad], [-tgtlen/2,tgtrad]) )


uscoll1_r1_up    = 0.024
uscoll1_r1_dn    = 0.015529
uscoll1_r2    = 0.031703
uscoll1_thick = 0.5
uscoll1_z     = 5.425-0.25

uscoll1_up   = polygon( ([uscoll1_z-uscoll1_thick/2, uscoll1_r1_up], [uscoll1_z+uscoll1_thick/2, uscoll1_r1_dn], [uscoll1_z+uscoll1_thick/2, uscoll1_r2], [uscoll1_z-uscoll1_thick/2, uscoll1_r2] ), notSource=False)

uscoll1_down = polygon( ([uscoll1_z-uscoll1_thick/2, -uscoll1_r2], [uscoll1_z+uscoll1_thick/2, -uscoll1_r2], [uscoll1_z+uscoll1_thick/2, -uscoll1_r1_dn], [uscoll1_z-uscoll1_thick/2, -uscoll1_r1_up] ), notSource=False)


uscoll2_r1    = 0.026
uscoll2_r2    = 0.034
uscoll2_r3    = 0.110
uscoll2_r4    = 0.330
uscoll2_thick = 0.1
uscoll2_z     = 5.925

uscoll2_up   = polygon( ([uscoll2_z-uscoll2_thick/2, uscoll2_r1], [uscoll2_z+uscoll2_thick/2, uscoll2_r1], [uscoll2_z+uscoll2_thick/2, uscoll2_r4], [uscoll2_z-uscoll2_thick/2, uscoll2_r4] ))
uscoll2_down = polygon( ([uscoll2_z-uscoll2_thick/2, -uscoll2_r2], [uscoll2_z+uscoll2_thick/2, -uscoll2_r2], [uscoll2_z+uscoll2_thick/2, -uscoll2_r1], [uscoll2_z-uscoll2_thick/2, -uscoll2_r1] ))

uscoll2_out_down = polygon( ([uscoll2_z-uscoll2_thick/2, -uscoll2_r4], [uscoll2_z+uscoll2_thick/2, -uscoll2_r4], [uscoll2_z+uscoll2_thick/2, -uscoll2_r3], [uscoll2_z-uscoll2_thick/2, -uscoll2_r3] ))


###################################################################



#dscoll1_r1    = 0.034
dscoll1_r1    = 0.026
dscoll1_r2    = 0.058
dscoll1_thick = 0.2
dscoll1_z     = 9.575

dscoll1_up   = polygon( ([dscoll1_z-dscoll1_thick/2, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r2], [dscoll1_z-dscoll1_thick/2, dscoll1_r2] ), notSource=False)
dscoll1_down = polygon( ([dscoll1_z-dscoll1_thick/2, -dscoll1_r2], [dscoll1_z+dscoll1_thick/2, -dscoll1_r2], [dscoll1_z+dscoll1_thick/2, -dscoll1_r1], [dscoll1_z-dscoll1_thick/2, -dscoll1_r1] ), notSource=False)


dscoll2_r1    = 0.038
dscoll2_r2    = 0.065
dscoll2_r3    = 0.223
dscoll2_r4    = 0.330
dscoll2_thick = 0.1
dscoll2_z     = 9.825

dscoll2_up   = polygon( ([dscoll2_z-dscoll2_thick/2, dscoll2_r1], [dscoll2_z+dscoll2_thick/2, dscoll2_r1], [dscoll2_z+dscoll2_thick/2, dscoll2_r4], [dscoll2_z-dscoll2_thick/2, dscoll2_r4] ))

dscoll2_down = polygon( ([dscoll2_z-dscoll2_thick/2, -dscoll2_r2], [dscoll2_z+dscoll2_thick/2, -dscoll2_r2], [dscoll2_z+dscoll2_thick/2, -dscoll2_r1], [dscoll2_z-dscoll2_thick/2, -dscoll2_r1] ))

dscoll2_out_down = polygon( ([dscoll2_z-dscoll2_thick/2, -dscoll2_r4], [dscoll2_z+dscoll2_thick/2, -dscoll2_r4], [dscoll2_z+dscoll2_thick/2, -dscoll2_r3], [dscoll2_z-dscoll2_thick/2, -dscoll2_r3] ))



dscoll3_r1    = 0.072
#dscoll3_r2    = 0.140
dscoll3_r2    = 0.10297
dscoll3_thick = 0.1
dscoll3_z     = 12.65

dscoll3_up   = polygon( ([dscoll3_z-dscoll3_thick/2, dscoll3_r1], [dscoll3_z+dscoll3_thick/2, dscoll3_r1], [dscoll3_z+dscoll3_thick/2, dscoll3_r2], [dscoll3_z-dscoll3_thick/2, dscoll3_r2] ))
dscoll3_down = polygon( ([dscoll3_z-dscoll3_thick/2, -dscoll3_r2], [dscoll3_z+dscoll3_thick/2, -dscoll3_r2], [dscoll3_z+dscoll3_thick/2, -dscoll3_r1], [dscoll3_z-dscoll3_thick/2, -dscoll3_r1] ))



quartz1 = polygon( ([28.0, 0.6], [28.01, 0.6], [28.01, 1.4], [28, 1.4]), isDetector=True )
quartz2 = polygon( ([28.0, -1.4], [28.01, -1.4], [28.01, -0.6], [28, -0.6]), isDetector=True )

sources.append(target)

allpolys.append(uscoll1_up)
allpolys.append(uscoll1_down)
allpolys.append(uscoll2_up)
allpolys.append(uscoll2_down)
allpolys.append(uscoll2_out_down)

#allpolys.append(dscoll1_up)
#allpolys.append(dscoll1_down)
allpolys.append(dscoll2_up)
allpolys.append(dscoll2_down)
allpolys.append(dscoll2_out_down)

#allpolys.append(dscoll3_up)
allpolys.append(dscoll3_down)

allpolys.append(quartz1)
allpolys.append(quartz2)

###########################################
#  Rough out blocking areas

for i in range(6):
    z = 10 + i*3.0
#    ghost  = polygon(([z,-1.4],[z+0.001,-1.4],[z+0.001,1.4], [z,1.4]), isEthereal=True )
    ghost  = polygon(([z,-1.4],[z+1.5,-1.4],[z+1.5,1.4], [z,1.4]), isEthereal=True )
#    allpolys.append(ghost)

#  One bounce ghost regions
ghost1a = polygon(([28,-1.4], [28, -1.39], [uscoll1_z-uscoll1_thick/2+0.01, uscoll1_r1_up], [uscoll1_z-uscoll1_thick/2, uscoll1_r1_up]), isEthereal=True)

ghost1b = polygon(([28,-0.6], [28, -0.59], [uscoll1_z+uscoll1_thick/2+0.01, uscoll1_r1_dn], [uscoll1_z+uscoll1_thick/2, uscoll1_r1_dn]), isEthereal=True)

#ghost2a = polygon(([28,-1.4], [28, -1.39], [dscoll1_z-dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z-dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

#ghost2b = polygon(([28,-0.6], [28, -0.59], [dscoll1_z+dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

#allpolys.append(ghost1a)
#allpolys.append(ghost1b)
#allpolys.append(ghost2a)
#allpolys.append(ghost2b)

#  Raw

z1 = 6.1
z2 = 7.1

t = uscoll2_r2 - uscoll2_r1

slope = (dscoll2_r1- uscoll2_r1)/(dscoll2_thick/2+dscoll2_z - uscoll2_z-uscoll2_thick/2)

gr1 = uscoll2_r1 + slope*(z1 - uscoll2_z - uscoll2_thick/2)
gr2 = uscoll2_r1 + slope*(z2 - uscoll2_z - uscoll2_thick/2)

smallghost1 = polygon(( [z1, -gr1-t], [z2, -gr2-t], [z2, -gr2], [z1, -gr1]), isEthereal = False)

print "Ghost blocking points:"
print smallghost1.pts[0][0], smallghost1.pts[0][1]
print "\t", smallghost1.pts[3][1]
print smallghost1.pts[1][0], smallghost1.pts[1][1]
print "\t", smallghost1.pts[2][1]


#smallghost2 = polygon( ([10.1729, -0.0277], [10.7712, -0.0738], [13.7226, -0.1123], [11.374, -0.0320] ), isEthereal=False)

#smallghost1 = polygon(( [6.3932, -0.0350], [8.0240, -0.0425], [7.6242, -0.0334], [6.2734, -0.0281]), isEthereal = False)
#smallghost2 = polygon( ([10.1729, -0.0277], [10.6515, -0.0566], [13.2529, -0.0882], [11.374, -0.0320] ), isEthereal=False)


# straight z
#smallghost1 = polygon(( [6.2734, -0.0334], [7.6852, -0.0385], [7.6852, -0.0334], [6.2734, -0.0281]), isEthereal = False)
#smallghost2 = polygon( ([10.1729, -0.0277], [10.1729, -0.0566], [11.3749, -0.0566], [11.374, -0.0320] ), isEthereal=False)

# Reduce z
#smallghost1 = polygon(( [6.273, -0.039 ], [7.874, -0.0474], [7.874, -0.0383691664116], [6.273, -0.0274]), isEthereal = False)
#smallghost2 = polygon( ([10.472, -0.0431780215291], [10.472, -0.0697], [12.074, -0.079], [12.074, -0.0490] ), isEthereal=False)

allpolys.append(smallghost1)
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

print "Ghost intersections:"

#  Print out ghost region values
for aghost in [ghost1a, ghost1b, smallghost1]:
    for aface in aghost.faces:
	print "Of ", aface.v1[0], aface.v1[1], " -> ", aface.v2[0], aface.v2[1]
	for lface in aface.getlitfaces():
	    print "\t", lface.v1[0], lface.v1[1], " -> ", lface.v2[0], lface.v2[1]

mydraw = drawlight(allpolys+sources)

Gtk.main()
