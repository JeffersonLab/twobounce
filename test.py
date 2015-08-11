#!/usr/bin/python

from poly import polygon
from poly import face 
from gi.repository import Gtk


from drawlight import drawlight

mypoly1 = polygon( ([0,0.5], [1.0 ,0.5] , [1.0 ,0.51], [0 ,0.51]) )

mypoly2 = polygon( ([2,0], [3, 0], [3,1], [2,1]) )

print mypoly1.pts
print mypoly2.pts

mypoly2.light( [mypoly1], () )

for aface in mypoly2.faces:
    print [aface.v1, aface.v2], aface.lit1
    if aface.getlitfaces():
	for lface in aface.getlitfaces():
	    print lface.v1, lface.v2
    print ""

mydraw = drawlight( [mypoly1, mypoly2] )

Gtk.main()
