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


#################################################################

######inner photon collimator

x1_inner_photon=0.024
z1_inner_photon=5.175

x2_inner_photon=0.0317
z2_inner_photon=5.175

x3_inner_photon=0.03175
z3_inner_photon=5.7

x4_inner_photon=0.0165
z4_inner_photon=5.7

# one has to assign the coordinates in anti-clock sequence
coll_inner_photon_1   = polygon( ([z1_inner_photon, x1_inner_photon], [z4_inner_photon, x4_inner_photon], [z3_inner_photon, x3_inner_photon], [z2_inner_photon, x2_inner_photon] ), notSource=False)

coll_inner_photon_2 = polygon( ([z2_inner_photon, -x2_inner_photon], [z3_inner_photon, -x3_inner_photon], [z4_inner_photon, -x4_inner_photon], [z1_inner_photon, -x1_inner_photon] ), notSource=False)


#########collimator 2,  three segments

#seg 1
x1_coll_2_1=-0.15+ (-0.5)
z1_coll_2_1=5.875

x2_coll_2_1=-0.098
z2_coll_2_1=5.875

x3_coll_2_1=-0.098
z3_coll_2_1=5.975

x4_coll_2_1=-0.15+(-0.5)
z4_coll_2_1=5.975


coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), notSource=False)


#seg 2

x1_coll_2_2=-0.0353
z1_coll_2_2=5.875

x2_coll_2_2=-0.026
z2_coll_2_2=5.875

x3_coll_2_2=-0.026
z3_coll_2_2=5.975

x4_coll_2_2=-0.0353
z4_coll_2_2=5.975


coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), notSource=False)

#seg 3

x1_coll_2_3=0.026
z1_coll_2_3=5.875

x2_coll_2_3=0.15+0.5
z2_coll_2_3=5.875

x3_coll_2_3=0.15+0.5
z3_coll_2_3=5.975

x4_coll_2_3=0.026
z4_coll_2_3=5.975


coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), notSource=False)


#############inner_pipe

x1_inner_pipe=0.0265
z1_inner_pipe=5.975

x2_inner_pipe=0.0295
z2_inner_pipe=5.975

x3_inner_pipe=0.034
z3_inner_pipe=7.92

x4_inner_pipe=0.031
z4_inner_pipe=7.92


coll_inner_pipe_1   = polygon( ([z1_inner_pipe, x1_inner_pipe], [z4_inner_pipe, x4_inner_pipe], [z3_inner_pipe, x3_inner_pipe], [z2_inner_pipe, x2_inner_pipe] ))
coll_inner_pipe_2   = polygon( ([z2_inner_pipe, -x2_inner_pipe], [z3_inner_pipe, -x3_inner_pipe], [z4_inner_pipe, -x4_inner_pipe], [z1_inner_pipe, -x1_inner_pipe] ))

################# collimator 4, 3 segmentations

#seg 1

x1_coll_4_1=-0.254
z1_coll_4_1=9.775

x2_coll_4_1=-0.23495
z2_coll_4_1=9.775

x3_coll_4_1=-0.23495
z3_coll_4_1=9.875

x4_coll_4_1=-0.254
z4_coll_4_1=9.875


coll_4_1   = polygon( ([z1_coll_4_1, x1_coll_4_1], [z4_coll_4_1, x4_coll_4_1], [z3_coll_4_1, x3_coll_4_1], [z2_coll_4_1, x2_coll_4_1] ))


#seg 2

x1_coll_4_2=-0.06377
z1_coll_4_2=9.775

x2_coll_4_2=-0.030
z2_coll_4_2=9.775

x3_coll_4_2=-0.030
z3_coll_4_2=9.875

x4_coll_4_2=-0.06377
z4_coll_4_2=9.875


coll_4_2   = polygon( ([z1_coll_4_2, x1_coll_4_2], [z4_coll_4_2, x4_coll_4_2], [z3_coll_4_2, x3_coll_4_2], [z2_coll_4_2, x2_coll_4_2] ))

#seg 3

x1_coll_4_3=0.030
z1_coll_4_3=9.775

x2_coll_4_3=0.254
z2_coll_4_3=9.775

x3_coll_4_3=0.254
z3_coll_4_3=9.875

x4_coll_4_3=0.030
z4_coll_4_3=9.875


coll_4_3   = polygon( ([z1_coll_4_3, x1_coll_4_3], [z4_coll_4_3, x4_coll_4_3], [z3_coll_4_3, x3_coll_4_3], [z2_coll_4_3, x2_coll_4_3] ))

#############inner_pipe_2

x1_inner_pipe_2=0.033
z1_inner_pipe_2=9.875

x2_inner_pipe_2=0.036
z2_inner_pipe_2=9.875 

x3_inner_pipe_2_tmp=0.0396
z3_inner_pipe_2_tmp=11.450

x4_inner_pipe_2_tmp=0.0366
z4_inner_pipe_2_tmp=11.450

z3=11.45+0.4
x3_inner_pipe_2=(x3_inner_pipe_2_tmp-x2_inner_pipe_2)/(z3_inner_pipe_2_tmp-z2_inner_pipe_2)*(z3-z2_inner_pipe_2)+x2_inner_pipe_2
z3_inner_pipe_2=z3

z4=11.45+0.4
x4_inner_pipe_2=(x4_inner_pipe_2_tmp-x1_inner_pipe_2)/(z4_inner_pipe_2_tmp-z1_inner_pipe_2)*(z4-z1_inner_pipe_2)+x1_inner_pipe_2
z4_inner_pipe_2=z4



coll_inner_pipe_2_1   = polygon( ([z1_inner_pipe_2, x1_inner_pipe_2], [z4_inner_pipe_2, x4_inner_pipe_2], [z3_inner_pipe_2, x3_inner_pipe_2], [z2_inner_pipe_2, x2_inner_pipe_2] ))
coll_inner_pipe_2_2   = polygon( ([z2_inner_pipe_2, -x2_inner_pipe_2], [z3_inner_pipe_2, -x3_inner_pipe_2], [z4_inner_pipe_2, -x4_inner_pipe_2], [z1_inner_pipe_2, -x1_inner_pipe_2] ))


#########collimator 5, 1 seg
x1_coll_5=-0.1055
z1_coll_5=12.8

x2_coll_5=-0.042
z2_coll_5=12.8

x3_coll_5=-0.042
z3_coll_5=12.87

x4_coll_5=-0.1055
z4_coll_5=12.87


coll_5   = polygon( ([z1_coll_5, x1_coll_5], [z4_coll_5, x4_coll_5], [z3_coll_5, x3_coll_5], [z2_coll_5, x2_coll_5] ))


#### quartz

#quartz1 = polygon( ([28.0, 0.6], [28.01, 0.6], [28.01, 1.4], [28, 1.4]), isDetector=True )
#quartz2 = polygon( ([28.0, -1.4], [28.01, -1.4], [28.01, -0.6], [28, -0.6]), isDetector=True )

quartz1 = polygon( ([28.0, 0.55], [28.02, 0.55], [28.02, 1.3], [28, 1.3]), isDetector=True )
quartz2 = polygon( ([28.0, -1.3], [28.02, -1.3], [28.02, -0.55], [28, -0.55]), isDetector=True )

##################################################################################################################################

sources.append(target)



allpolys.append(coll_inner_photon_1)
allpolys.append(coll_inner_photon_2)

allpolys.append(coll_2_1)
allpolys.append(coll_2_2)
allpolys.append(coll_2_3)

allpolys.append(coll_inner_pipe_1)
allpolys.append(coll_inner_pipe_2)

allpolys.append(coll_4_1)
allpolys.append(coll_4_2)
allpolys.append(coll_4_3)

allpolys.append(coll_inner_pipe_2_1)
allpolys.append(coll_inner_pipe_2_2)

allpolys.append(coll_5)

allpolys.append(quartz1)
allpolys.append(quartz2)

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
