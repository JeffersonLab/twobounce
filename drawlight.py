#!/usr/bin/python 
from gi.repository import Gtk
import cairo
import math

import poly


class drawlight(Gtk.Window):

    def __init__(self, polys):
        super(drawlight, self).__init__()

#	self.winw = 1024.0
#	self.winh = 768.0
        self.winw = 1000.0
        self.winh = 800.0

        self.zmin = -4.0
#        self.zmax =  6.0
        self.zmax = 30.0
#        self.zmax = 10.0

        self.yscale = 8.0
        #self.yscale = 1.0
        
        self.init_ui()
        self.polys = polys

 
    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Moller Collimators")
        self.resize(self.winw, self.winh)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    
    def on_draw(self, wid, cr):
        cr.set_antialias(cairo.ANTIALIAS_NONE)


        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.paint()
        w, h = self.get_size()      

        scaleval = self.winw/(self.zmax-self.zmin)

        cr.scale(scaleval,  -scaleval)
        cr.translate( -self.zmin, -self.winh/scaleval/2)

        for apoly in self.polys:
            for aface in apoly.faces:
                #        	print "drawing ", aface.v1[0], aface.v1[1], " -> ", aface.v2[0], aface.v2[1]
                if not aface.isEthereal:
                    cr.move_to( aface.v1[0], aface.v1[1]*self.yscale )
                    cr.line_to( aface.v2[0], aface.v2[1]*self.yscale )
                    cr.set_line_width(1.0/scaleval)
                    cr.set_source_rgb(0.5, 0.5, 0.5)
                    cr.stroke()
                    
                    # Lit by secondaries
                    for lface in aface.getlitfaces(2):
                        cr.move_to( lface.v1[0], lface.v1[1]*self.yscale )
                        cr.line_to( lface.v2[0], lface.v2[1]*self.yscale )
                        if lface.isDetector:
                            cr.set_line_width(4.0/scaleval)
                        else:
                            cr.set_line_width(2.0/scaleval)
                            #        	    cr.set_source_rgb(0.7, 0.5, 0.1)
                            cr.set_source_rgb(0.1, 0.5, 0.1)
                            cr.stroke()
                            
                    # Lit by primaries
                for lface in aface.getlitfaces():
                    cr.move_to( lface.v1[0], lface.v1[1]*self.yscale )
                    cr.line_to( lface.v2[0], lface.v2[1]*self.yscale )
                    if lface.isDetector:
                        cr.set_line_width(4.0/scaleval)
                    else:
                        cr.set_line_width(2.0/scaleval)
                    cr.set_source_rgb(1.0, 0.0, 0.0)
                    cr.stroke()

                for lface in aface.getlitfaces(3):
                    cr.move_to( lface.v1[0], lface.v1[1]*self.yscale )
                    cr.line_to( lface.v2[0], lface.v2[1]*self.yscale )
                    cr.set_line_width(3.0/scaleval)
                    cr.set_source_rgb(1.0, 0.0, 1.0)
                    cr.stroke()
        #self.get_picture()

    def get_picture(self):
        drawable = self.movie_window.window
        colormap = drawable.get_colormap()
        pixbuf = Gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, 0, 8, *drawable.get_size())
        pixbuf = pixbuf.get_from_drawable(drawable, colormap, 0,0,0,0, *drawable.get_size())
        pixbuf.save(r'somefile.png', 'png')

"""


        # Pixel by pixel stuff
        cr.set_line_width(1.0/scaleval)
        height = self.winh*(self.zmax-self.zmin)/self.winw
        cr.set_source_rgba(0.0, 0.0, 1.0, 1.0)

        for apoly in self.polys:
            for xidx in range(int(self.winw)):
        	for yidx in range(int(self.winh)):
        	    xval = self.zmin + xidx*(self.zmax-self.zmin)/self.winw;
        	    yval = -height/2 + yidx*height/self.winh;

        	    cr.move_to( xval, yval )
        	    cr.line_to( xval, yval + 1.0/scaleval)
        	    cr.stroke()
"""

    

def main():
    app = drawlight()
    Gtk.main()
        
if __name__ == "__main__":    
    main()
