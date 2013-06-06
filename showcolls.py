#!/usr/bin/python

from poly import polygon
from poly import face 
from gi.repository import Gtk


from drawlight import drawlight

sources = []
allpolys = []

target = polygon( ([0,0.0], [1.0 ,0.0] , [1.0 ,0.01], [0 ,0.01]) )

mypoly2 = polygon( ([2,0], [3, 0], [3,1], [2,1]), isDetector=True )

mypoly3 = polygon( ([1.7, 0.1], [1.8,  0.1], [1.8,0.2], [1.7,0.2]) )
mypoly4 = polygon( ([1.7, 0.4], [1.8,  0.4], [1.8,0.5], [1.7,0.5]) )

mirror = polygon( ([1.7, -0.5], [1.8,  -0.5], [1.8,-0.4], [1.7,-0.4]) )

sources.append(target)
allpolys.append(mypoly2)
#allpolys.append(mypoly3)

#allpolys.append(mypoly4)
allpolys.append(mirror)

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
