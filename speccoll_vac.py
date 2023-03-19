#!/usr/bin/python
from poly import polygon
from poly import face
import gi
import numpy as np

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from drawlight import drawlight

sources = []
allpolys = []

tgtpos = -4.5
mm = 1e-3
cm = 1e-2
m = 1
tgtlen = 1.25*m
tgtrad = 1.4142*0.0025*m

target = polygon(
    (
        [-tgtlen / 2, -tgtrad],
        [tgtlen / 2, -tgtrad],
        [tgtlen / 2, tgtrad],
        [-tgtlen / 2, tgtrad],
    )
)

### bellows 1 USflange
x1 = 149.23*mm 
z1 = -3427.73*mm-tgtpos

x2 = 184.15*mm  
z2 = -3427.73*mm-tgtpos

x3 = 184.15*mm 
z3 = -3399.15*mm-tgtpos  

x4 = 149.23*mm 
z4 = -3399.15*mm-tgtpos

bellows1_USflange_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows1_USflange_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 1 seg 1
x1 = 149.23*mm
z1 = -3399.15*mm-tgtpos

x2 = 152.40*mm
z2 = -3399.15*mm-tgtpos

x3 = 152.40*mm 
z3 = -3343.58*mm-tgtpos  

x4 = 149.23*mm 
z4 = -3343.58*mm-tgtpos

bellows1_seg1_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows1_seg1_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 1 seg 2
x1 = 149.23*mm 
z1 = -3343.58*mm-tgtpos

x2 = 190.50*mm  
z2 = -3343.58*mm-tgtpos

x3 = 190.50*mm 
z3 = -3054.68*mm-tgtpos  

x4 = 149.23*mm 
z4 = -3054.68*mm-tgtpos

bellows1_seg2_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows1_seg2_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 1 seg 3
x1 = 149.23*mm 
z1 = -3054.68*mm-tgtpos

x2 = 152.4*mm  
z2 = -3054.68*mm-tgtpos

x3 = 152.4*mm 
z3 = -2999.10*mm-tgtpos  

x4 = 149.23*mm 
z4 = -2999.10*mm-tgtpos

bellows1_seg3_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows1_seg3_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 1 DSflange
x1 = 149.23*mm 
z1 = -2999.10*mm-tgtpos

x2 = 184.15*mm  
z2 = -2999.10*mm-tgtpos

x3 = 184.15*mm 
z3 = -2941.954*mm-tgtpos  

x4 = 149.23*mm 
z4 = -2941.954*mm-tgtpos

bellows1_DSflange_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows1_DSflange_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Pipe between bellows 1 and 2
x1 = 146.05*mm 
z1 = -2941.954*mm-tgtpos

x2 = 152.40*mm  
z2 = -2941.954*mm-tgtpos

x3 = 152.40*mm 
z3 = -1357.81*mm-tgtpos  

x4 = 146.05*mm 
z4 = -1357.81*mm-tgtpos

bellows12_pipe_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows12_pipe_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Flange after bellows12 pipe
x1 = 149.23*mm 
z1 = -1357.81*mm-tgtpos

x2 = 184.15*mm  
z2 = -1357.81*mm-tgtpos

x3 = 184.15*mm 
z3 = -1300.66*mm-tgtpos  

x4 = 149.23*mm 
z4 = -1300.66*mm-tgtpos

bellows12_pipe_DSflange_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows12_pipe_DSflange_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Pipe segment upstream of collar 0
x1 = 146.05*mm 
z1 = -1300.66*mm-tgtpos

x2 = 152.4*mm  
z2 = -1300.66*mm-tgtpos

x3 = 152.4*mm 
z3 = -1200*mm-tgtpos  

x4 = 146.05*mm 
z4 = -1200*mm-tgtpos

pipe_UScollar0_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
pipe_UScollar0_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

# Collar 0
x1 = 0.0762  
z1 = -1.2-tgtpos

x2 = 0.330   
z2 = -1.2-tgtpos

x3 = 0.330  
z3 = -1.0-tgtpos  

x4 = 0.0762  
z4 = -1.0-tgtpos  

collar0_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
collar0_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Pipe segment downstream of collar 0
x1 = 146.05*mm 
z1 = -1000*mm-tgtpos

x2 = 152.4*mm  
z2 = -1000*mm-tgtpos

x3 = 152.4*mm 
z3 = -885.648*mm-tgtpos  

x4 = 146.05*mm 
z4 = -885.648*mm-tgtpos

pipe_DScollar0_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
pipe_DScollar0_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Flange upstream of bellows 2
x1 = 149.23*mm 
z1 = -885.648*mm-tgtpos

x2 = 184.15*mm  
z2 = -885.648*mm-tgtpos

x3 = 184.15*mm 
z3 = -828.63*mm-tgtpos  

x4 = 149.23*mm 
z4 = -828.63*mm-tgtpos

bellows2_USflange_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows2_USflange_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 2 seg 1
x1 = 149.23*mm 
z1 = -828.63*mm-tgtpos

x2 = 152.40*mm  
z2 = -828.63*mm-tgtpos

x3 = 152.40*mm 
z3 = -773.05*mm-tgtpos  

x4 = 149.23*mm 
z4 = -773.05*mm-tgtpos

bellows2_seg1_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows2_seg1_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 2 seg 2
x1 = 149.23*mm 
z1 = -773.05*mm-tgtpos

x2 = 190.50*mm  
z2 = -773.05*mm-tgtpos

x3 = 190.50*mm 
z3 = -484.15*mm-tgtpos  

x4 = 149.23*mm 
z4 = -484.15*mm-tgtpos

bellows2_seg2_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows2_seg2_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 2 seg 3
x1 = 149.23*mm 
z1 = -484.15*mm-tgtpos

x2 = 152.4*mm  
z2 = -484.15*mm-tgtpos

x3 = 152.4*mm 
z3 = -428.58*mm-tgtpos  

x4 = 149.23*mm 
z4 = -428.58*mm-tgtpos

bellows2_seg3_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows2_seg3_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### bellows 2 DSflange
x1 = 149.23*mm 
z1 = -428.58*mm-tgtpos

x2 = 184.15*mm  
z2 = -428.58*mm-tgtpos

x3 = 184.15*mm 
z3 = -371.475*mm-tgtpos  

x4 = 149.23*mm 
z4 = -371.475*mm-tgtpos

bellows2_DSflange_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows2_DSflange_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

###  Upstream Enclosure US pipe
x1 = 149.23*mm 
z1 = -371.475*mm-tgtpos

x2 = 155.575*mm  
z2 = -371.475*mm-tgtpos

x3 = 155.575*mm 
z3 = -204.597*mm-tgtpos  

x4 = 149.23*mm 
z4 = -204.597*mm-tgtpos

upstream_enclosure_USpipe_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
upstream_enclosure_USpipe_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

###  Upstream Enclosure US Wall 
x1 = 155.575*mm 
z1 = (-204.597-50.8)*1*mm-tgtpos

x2 = 552.45*mm    
z2 = (-204.597-50.8)*1*mm-tgtpos

x3 = 552.45*mm 
z3 = -204.597*mm-tgtpos  

x4 = 155.575*mm 
z4 = -204.597*mm-tgtpos

upstream_enclosure_USwall_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

x1 = 155.575*mm 
z1 = (-204.597-50.8)*1*mm-tgtpos

x2 = 552.45*mm    
z2 = (-204.597-50.8)*1*mm-tgtpos

x3 = 552.45*mm 
z3 = -204.597*mm-tgtpos 

x4 = 155.575*mm 
z4 = -204.597*mm-tgtpos

upstream_enclosure_USwall_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

###  Upstream Enclosure Side Wall 
x1 = (1104.9/2.0-25.4)*1*mm
z1 = -204.597*mm-tgtpos

x2 = 552.45*mm    
z2 = -204.597*mm-tgtpos

x3 = 552.45*mm 
z3 = 3592.703*mm-tgtpos  

x4 = (1104.9/2.0-25.4)*1*mm 
z4 = 3592.703*mm-tgtpos

upstream_enclosure_sidewall_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

x1 = (1104.9/2.0-25.4)*1*mm
z1 = -204.597*mm-tgtpos

x2 = 552.45*mm    
z2 = -204.597*mm-tgtpos

x3 = 552.45*mm 
z3 = 3592.703*mm-tgtpos  

x4 = (1104.9/2.0-25.4)*1*mm 
z4 = 3592.703*mm-tgtpos

upstream_enclosure_sidewall_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

###  Upstream Enclosure DS Wall 
x1 = 344.488*mm 
z1 = 3592.703*mm-tgtpos

x2 = 552.45*mm    
z2 = 3592.703*mm-tgtpos

x3 = 552.45*mm 
z3 = (3592.703+50.8)*1*mm-tgtpos  

x4 = 344.488*mm 
z4 = (3592.703+50.8)*1*mm-tgtpos

upstream_enclosure_DSwall_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

x1 = 344.488*mm 
z1 = 3592.703*mm-tgtpos

x2 = 552.45*mm    
z2 = 3592.703*mm-tgtpos

x3 = 552.45*mm 
z3 = (3592.703+50.8)*1*mm-tgtpos  

x4 = 344.488*mm 
z4 = (3592.703+50.8)*1*mm-tgtpos

upstream_enclosure_DSwall_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Collimator 1

# Seg 1
x1 = 20.3*mm
z1 = 325*mm-tgtpos

x2 = 16.55*mm
z2 = 425*mm-tgtpos

x3 = 29.735*mm
z3 = 425*mm-tgtpos

x4 = 29.5*mm 
z4 = 325*mm-tgtpos


collimator1_seg1_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

collimator1_seg1_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

# Seg 2
x1 = 16.55*mm
z1 = 425*mm-tgtpos

x2 = 15.4*mm
z2 = 515*mm-tgtpos

x3 = 29.947*mm
z3 = 515*mm-tgtpos

x4 = 29.735*mm
z4 = 425*mm-tgtpos

collimator1_seg2_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

collimator1_seg2_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

# Seg 3
x1 = 15.4*mm
z1 = 515*mm-tgtpos

x2 = 14.4*mm
z2 = 635*mm-tgtpos

x3 = 30.229*mm
z3 = 635*mm-tgtpos

x4 = 29.947*mm
z4 = 515*mm-tgtpos

collimator1_seg3_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

collimator1_seg3_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

# Seg 4
x1 = 14.4*mm
z1 = 635*mm-tgtpos

x2 = 13.9*mm
z2 = 725*mm-tgtpos

x3 = 30.441*mm
z3 = 725*mm-tgtpos

x4 = 30.229*mm
z4 = 635*mm-tgtpos

collimator1_seg4_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

collimator1_seg4_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

# Seg 5
x1 = 13.9*mm
z1 = 725*mm-tgtpos

x2 = 13.9*mm+(14.54-13.9)*25/175*1*mm
z2 = 750*mm-tgtpos

x3 = 30.5*mm
z3 = 750*mm-tgtpos

x4 = 30.441*mm
z4 = 725*mm-tgtpos

collimator1_seg5_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

collimator1_seg5_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

# Seg 6
x1 = 13.9*mm+(14.54-13.9)*25/175*1*mm
z1 = 750*mm-tgtpos

x2 = 14.54*1*mm
z2 = 900*mm-tgtpos

x3 = 30.5*mm
z3 = 900*mm-tgtpos

x4 = 30.5*mm
z4 = 750*mm-tgtpos

collimator1_seg6_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

collimator1_seg6_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Collimator 2

# Seg 1

x1 = -35*mm
z1 = 750*mm-tgtpos

x2 = -30.5*mm
z2 = 750*mm-tgtpos

x3 = -30.5*mm
z3 = 900*mm-tgtpos

x4 = -35*mm
z4 = 900*mm-tgtpos

collimator2_seg1 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# Seg 2
x1 = -150*mm
z1 = 750*mm-tgtpos

x2 = -101*mm
z2 = 750*mm-tgtpos

x3 = -101*mm
z3 = 800*mm-tgtpos

x4 = -150*mm
z4 = 800*mm-tgtpos

collimator2_seg2 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# Seg 3

x1 = -150*mm
z1 = 800*mm-tgtpos

x2 = -101*mm
z2 = 800*mm-tgtpos

x3 = -101*mm*(1+np.tan(1.5*np.pi/180))
z3 = 900*mm-tgtpos

x4 = -150*mm
z4 = 900*mm-tgtpos

collimator2_seg3 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# Seg 4

x1 = 30.5*mm
z1 = 750*mm-tgtpos

x2 = 150*mm
z2 = 750*mm-tgtpos

x3 = 150*mm
z3 = 900*mm-tgtpos

x4 = 30.5*mm
z4 = 900*mm-tgtpos

collimator2_seg4 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)


### Upstream Spectrometer Coil (approximated by rectangle extending from beginning of upstream arc to end of downstream arc)

# seg 1
x1 = 33*mm - 1*mm
z1 = 1108.84*mm-(250.68-33)/2.0*mm-1*mm-tgtpos

x2 = 33*mm - 1*mm
z2 = 1108.84*mm+465*mm-tgtpos

x3 = 250.68*mm + 1*mm
z3 = 1108.84*mm+465*mm-tgtpos

x4 = 250.68*mm + 1*mm
z4 = 1108.84*mm-(250.68-33)/2.0*mm-1*mm-tgtpos

uscoil_seg1 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# seg 2
x1 = 33*mm - 1*mm
z1 = 1108.84*mm+465*mm-tgtpos

x2 = 33*mm - 1*mm
z2 = 1108.84*mm+515*mm-tgtpos

x3 = 260.54*mm + 1*mm
z3 = 1108.84*mm+515*mm-tgtpos

x4 = 250.68*mm + 1*mm
z4 =  1108.84*mm+465*mm-tgtpos

uscoil_seg2 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# seg 3
x1 = 33*mm - 1*mm
z1 = 1108.84*mm+515*mm-tgtpos

x2 = 33*mm - 1*mm
z2 = 2886.93*mm+(260.54-33)/2.0*mm+1*mm-tgtpos

x3 = 260.54*mm + 1*mm
z3 = 2886.93*mm+(260.54-33)/2.0*mm+1*mm-tgtpos

x4 = 260.54*mm + 1*mm
z4 = 1108.84*mm+515*mm-tgtpos

uscoil_seg3 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

### Upstream 2bounce shield

# Front insert
x1 = -30.875*mm
z1 = 936.5*mm-tgtpos

x2 = -30.875*mm
z2 = (936.5+12.7)*mm-tgtpos

x3 = -25*mm
z3 = (936.5+12.7)*mm-tgtpos

x4 = -25*mm
z4 = 936.5*mm-tgtpos

twobounce_front_insert_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
twobounce_front_insert_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

# Main tube (azimuthally aligned with acceptance region)
x1 = -36*mm
z1 = (936.5+12.7)*mm-tgtpos

x2 = -36*mm
z2 = (936.5+2152.65-12.7)*mm-tgtpos

x3 = -25*mm
z3 = (936.5+2152.65-12.7)*mm-tgtpos

x4 = -25*mm
z4 = (936.5+12.7)*mm-tgtpos

twobounce_acceptance = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# Main tube (azimuthally aligned with coil)
x1 = 25*mm
z1 = (936.5+12.7)*mm-tgtpos

x2 = 25*mm
z2 = (936.5+2152.65-12.7)*mm-tgtpos

x3 = 32*mm
z3 = (936.5+2152.65-12.7)*mm-tgtpos

x4 = 32*mm
z4 = (936.5+12.7)*mm-tgtpos

twobounce_coil = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# End insert
x1 = -30.875*mm
z1 = (936.5+2152.65-12.7)*mm-tgtpos

x2 = -30.875*mm
z2 = (936.5+2152.65)*mm-tgtpos

x3 = -25*mm
z3 = (936.5+2152.65)*mm-tgtpos

x4 = -25*mm
z4 = (936.5+2152.65-12.7)*mm-tgtpos

twobounce_end_insert_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
twobounce_end_insert_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)




################################################################

###### Lead collar (for collimating photons)



###### Hybrid upstream Lead collar (for ep scattering)

x1_collar3 = 0.240  # This is including the beampipe
# x1_collar3=0.23835
# z1_collar3=4.4305+4.5
z1_collar3 = 8.066

x2_collar3 = 0.540
# z2_collar3=4.4305+4.5
z2_collar3 = 8.066

x3_collar3 = 0.540
# z3_collar3=4.6805+4.5
z3_collar3 = 8.216

x4_collar3 = 0.240
# x4_collar3=0.23835
# z4_collar3=4.6805+4.5
z4_collar3 = 8.216


collar3_top = polygon(
    (
        [z1_collar3, x1_collar3],
        [z4_collar3, x4_collar3],
        [z3_collar3, x3_collar3],
        [z2_collar3, x2_collar3],
    ),
    notSource=False,
)
collar3_bottom = polygon(
    (
        [z2_collar3, -x2_collar3],
        [z3_collar3, -x3_collar3],
        [z4_collar3, -x4_collar3],
        [z1_collar3, -x1_collar3],
    ),
    notSource=False,
)

#################################################################

###### First downstream Lead collar (for ep scattering)

x1_collar1 = 0.620
z1_collar1 = 11.767124 + 4.5

x2_collar1 = 0.750
z2_collar1 = 11.767124 + 4.5

x3_collar1 = 0.750
z3_collar1 = 11.767124 + 4.5 + 0.150

x4_collar1 = 0.630
z4_collar1 = 11.767124 + 4.5 + 0.150


collar_top1 = polygon(
    (
        [z1_collar1, x1_collar1],
        [z4_collar1, x4_collar1],
        [z3_collar1, x3_collar1],
        [z2_collar1, x2_collar1],
    ),
    notSource=False,
)
collar_bottom1 = polygon(
    (
        [z2_collar1, -x2_collar1],
        [z3_collar1, -x3_collar1],
        [z4_collar1, -x4_collar1],
        [z1_collar1, -x1_collar1],
    ),
    notSource=False,
)

###### Second downstream Lead collar (for ep scattering)

x1_collar2 = 1.010
z1_collar2 = 19.13269 + 4.5

x2_collar2 = 1.315
z2_collar2 = 19.13269 + 4.5

x3_collar2 = 1.315
z3_collar2 = 19.13269 + 4.5 + 0.150

x4_collar2 = 1.019
z4_collar2 = 19.13269 + 4.5 + 0.150


collar_top2 = polygon(
    (
        [z1_collar2, x1_collar2],
        [z4_collar2, x4_collar2],
        [z3_collar2, x3_collar2],
        [z2_collar2, x2_collar2],
    ),
    notSource=False,
)
collar_bottom2 = polygon(
    (
        [z2_collar2, -x2_collar2],
        [z3_collar2, -x3_collar2],
        [z4_collar2, -x4_collar2],
        [z1_collar2, -x1_collar2],
    ),
    notSource=False,
)


### Pipe after US vessel
x1_US_pipe1 = 0.230
z1_US_pipe1 = 8.23438

x2_US_pipe1 = 0.23635
z2_US_pipe1 = 8.23438

x3_US_pipe1 = 0.23635
z3_US_pipe1 = 8.23438 + 0.44133

x4_US_pipe1 = 0.230
z4_US_pipe1 = 8.23438 + 0.44133

US_pipe1_up = polygon(
    (
        [z1_US_pipe1, x1_US_pipe1],
        [z4_US_pipe1, x4_US_pipe1],
        [z3_US_pipe1, x3_US_pipe1],
        [z2_US_pipe1, x2_US_pipe1],
    ),
    notSource=False,
)
US_pipe1_lo = polygon(
    (
        [z2_US_pipe1, -x2_US_pipe1],
        [z3_US_pipe1, -x3_US_pipe1],
        [z4_US_pipe1, -x4_US_pipe1],
        [z1_US_pipe1, -x1_US_pipe1],
    ),
    notSource=False,
)

####US CAN exit Flange 1
###Part1
##section1
x1_US_flange1_1_1 = 0.23635
z1_US_flange1_1_1 = 8.65666

x2_US_flange1_1_1 = 0.4191
z2_US_flange1_1_1 = 8.65666

x3_US_flange1_1_1 = 0.4191
z3_US_flange1_1_1 = 8.65666 + 0.01905

x4_US_flange1_1_1 = 0.23635
z4_US_flange1_1_1 = 8.65666 + 0.01905

US_flange1_1_1_up = polygon(
    (
        [z1_US_flange1_1_1, x1_US_flange1_1_1],
        [z4_US_flange1_1_1, x4_US_flange1_1_1],
        [z3_US_flange1_1_1, x3_US_flange1_1_1],
        [z2_US_flange1_1_1, x2_US_flange1_1_1],
    ),
    notSource=False,
)
US_flange1_1_1_lo = polygon(
    (
        [z2_US_flange1_1_1, -x2_US_flange1_1_1],
        [z3_US_flange1_1_1, -x3_US_flange1_1_1],
        [z4_US_flange1_1_1, -x4_US_flange1_1_1],
        [z1_US_flange1_1_1, -x1_US_flange1_1_1],
    ),
    notSource=False,
)

##section2
x2_US_flange1_1_2 = 0.24765
z2_US_flange1_1_2 = 8.65666 + 0.01905

x1_US_flange1_1_2 = 0.4191
z1_US_flange1_1_2 = 8.65666 + 0.01905

x4_US_flange1_1_2 = 0.4191
z4_US_flange1_1_2 = 8.65666 + 0.01905 + 0.01588

x3_US_flange1_1_2 = 0.24765
z3_US_flange1_1_2 = 8.65666 + 0.01905 + 0.01588

US_flange1_1_2_up = polygon(
    (
        [z1_US_flange1_1_2, x1_US_flange1_1_2],
        [z4_US_flange1_1_2, x4_US_flange1_1_2],
        [z3_US_flange1_1_2, x3_US_flange1_1_2],
        [z2_US_flange1_1_2, x2_US_flange1_1_2],
    ),
    notSource=False,
)
US_flange1_1_2_lo = polygon(
    (
        [z2_US_flange1_1_2, -x2_US_flange1_1_2],
        [z3_US_flange1_1_2, -x3_US_flange1_1_2],
        [z4_US_flange1_1_2, -x4_US_flange1_1_2],
        [z1_US_flange1_1_2, -x1_US_flange1_1_2],
    ),
    notSource=False,
)

###Part2
##section1
x2_US_flange1_2_1 = 0.3302
z2_US_flange1_2_1 = 8.69158

x1_US_flange1_2_1 = 0.4191
z1_US_flange1_2_1 = 8.69158

x4_US_flange1_2_1 = 0.4191
z4_US_flange1_2_1 = 8.69158 + 0.0254

x3_US_flange1_2_1 = 0.3302
z3_US_flange1_2_1 = 8.69158 + 0.0254

US_flange1_2_1_up = polygon(
    (
        [z1_US_flange1_2_1, x1_US_flange1_2_1],
        [z4_US_flange1_2_1, x4_US_flange1_2_1],
        [z3_US_flange1_2_1, x3_US_flange1_2_1],
        [z2_US_flange1_2_1, x2_US_flange1_2_1],
    ),
    notSource=False,
)
US_flange1_2_1_lo = polygon(
    (
        [z2_US_flange1_2_1, -x2_US_flange1_2_1],
        [z3_US_flange1_2_1, -x3_US_flange1_2_1],
        [z4_US_flange1_2_1, -x4_US_flange1_2_1],
        [z1_US_flange1_2_1, -x1_US_flange1_2_1],
    ),
    notSource=False,
)

##section2
x2_US_flange1_2_2 = 0.33095
z2_US_flange1_2_2 = 8.69158 + 0.0254

x1_US_flange1_2_2 = 0.4191
z1_US_flange1_2_2 = 8.69158 + 0.0254

x4_US_flange1_2_2 = 0.4191
z4_US_flange1_2_2 = 8.69158 + 0.0254 + 0.01905

x3_US_flange1_2_2 = 0.33095
z3_US_flange1_2_2 = 8.69158 + 0.0254 + 0.01905

US_flange1_2_2_up = polygon(
    (
        [z1_US_flange1_2_2, x1_US_flange1_2_2],
        [z4_US_flange1_2_2, x4_US_flange1_2_2],
        [z3_US_flange1_2_2, x3_US_flange1_2_2],
        [z2_US_flange1_2_2, x2_US_flange1_2_2],
    ),
    notSource=False,
)
US_flange1_2_2_lo = polygon(
    (
        [z2_US_flange1_2_2, -x2_US_flange1_2_2],
        [z3_US_flange1_2_2, -x3_US_flange1_2_2],
        [z4_US_flange1_2_2, -x4_US_flange1_2_2],
        [z1_US_flange1_2_2, -x1_US_flange1_2_2],
    ),
    notSource=False,
)


###Next pipe - it has three parts
##part1
x2_US_pipe2_1 = 0.3302
z2_US_pipe2_1 = 8.71698

x1_US_pipe2_1 = 0.33095
z1_US_pipe2_1 = 8.71698

x4_US_pipe2_1 = 0.33095
z4_US_pipe2_1 = 8.71698 + 0.06106

x3_US_pipe2_1 = 0.3302
z3_US_pipe2_1 = 8.71698 + 0.06106

US_pipe2_1_up = polygon(
    (
        [z1_US_pipe2_1, x1_US_pipe2_1],
        [z4_US_pipe2_1, x4_US_pipe2_1],
        [z3_US_pipe2_1, x3_US_pipe2_1],
        [z2_US_pipe2_1, x2_US_pipe2_1],
    ),
    notSource=False,
)
US_pipe2_1_lo = polygon(
    (
        [z2_US_pipe2_1, -x2_US_pipe2_1],
        [z3_US_pipe2_1, -x3_US_pipe2_1],
        [z4_US_pipe2_1, -x4_US_pipe2_1],
        [z1_US_pipe2_1, -x1_US_pipe2_1],
    ),
    notSource=False,
)

##part2
x2_US_pipe2_2 = 0.3302
z2_US_pipe2_2 = 8.71698 + 0.06106

x1_US_pipe2_2 = 0.361175
z1_US_pipe2_2 = 8.71698 + 0.06106

x4_US_pipe2_2 = 0.361175
z4_US_pipe2_2 = 8.71698 + 0.06106 + 0.33222

x3_US_pipe2_2 = 0.3302
z3_US_pipe2_2 = 8.71698 + 0.06106 + 0.33222

US_pipe2_2_up = polygon(
    (
        [z1_US_pipe2_2, x1_US_pipe2_2],
        [z4_US_pipe2_2, x4_US_pipe2_2],
        [z3_US_pipe2_2, x3_US_pipe2_2],
        [z2_US_pipe2_2, x2_US_pipe2_2],
    ),
    notSource=False,
)
US_pipe2_2_lo = polygon(
    (
        [z2_US_pipe2_2, -x2_US_pipe2_2],
        [z3_US_pipe2_2, -x3_US_pipe2_2],
        [z4_US_pipe2_2, -x4_US_pipe2_2],
        [z1_US_pipe2_2, -x1_US_pipe2_2],
    ),
    notSource=False,
)

##part3
x2_US_pipe2_3 = 0.3302
z2_US_pipe2_3 = 8.71698 + 0.06106 + 0.33222

x3_US_pipe2_3 = 0.33095
z3_US_pipe2_3 = 8.71698 + 0.06106 + 0.33222

x4_US_pipe2_3 = 0.33095
z4_US_pipe2_3 = 8.71698 + 0.06106 + 0.33222 + 0.06146

x1_US_pipe2_3 = 0.3302
z1_US_pipe2_3 = 8.71698 + 0.06106 + 0.33222 + 0.06146

US_pipe2_3_up = polygon(
    (
        [z1_US_pipe2_3, x1_US_pipe2_3],
        [z4_US_pipe2_3, x4_US_pipe2_3],
        [z3_US_pipe2_3, x3_US_pipe2_3],
        [z2_US_pipe2_3, x2_US_pipe2_3],
    ),
    notSource=False,
)
US_pipe2_3_lo = polygon(
    (
        [z2_US_pipe2_3, -x2_US_pipe2_3],
        [z3_US_pipe2_3, -x3_US_pipe2_3],
        [z4_US_pipe2_3, -x4_US_pipe2_3],
        [z1_US_pipe2_3, -x1_US_pipe2_3],
    ),
    notSource=False,
)


##############Downstream vessel###############
# Fornt Plate upper part
x1_DSCAN_Front_up = 0.3302
z1_DSCAN_Front_up = 9.19671

x2_DSCAN_Front_up = 1.20015
z2_DSCAN_Front_up = 9.19671

x3_DSCAN_Front_up = 1.20015
z3_DSCAN_Front_up = 9.19671 + 0.127

x4_DSCAN_Front_up = 0.3302
z4_DSCAN_Front_up = 9.19671 + 0.127


DSCAN_Front_up = polygon(
    (
        [z1_DSCAN_Front_up, x1_DSCAN_Front_up],
        [z4_DSCAN_Front_up, x4_DSCAN_Front_up],
        [z3_DSCAN_Front_up, x3_DSCAN_Front_up],
        [z2_DSCAN_Front_up, x2_DSCAN_Front_up],
    ),
    notSource=False,
)

# Fornt Plate lower part
x1_DSCAN_Front_low = -1.4224
z1_DSCAN_Front_low = 9.19671

x2_DSCAN_Front_low = -0.3302
z2_DSCAN_Front_low = 9.19671

x3_DSCAN_Front_low = -0.3302
z3_DSCAN_Front_low = 9.19671 + 0.127

x4_DSCAN_Front_low = -1.4224
z4_DSCAN_Front_low = 9.19671 + 0.127


DSCAN_Front_low = polygon(
    (
        [z1_DSCAN_Front_low, x1_DSCAN_Front_low],
        [z4_DSCAN_Front_low, x4_DSCAN_Front_low],
        [z3_DSCAN_Front_low, x3_DSCAN_Front_low],
        [z2_DSCAN_Front_low, x2_DSCAN_Front_low],
    ),
    notSource=False,
)

# Base plate
x1_DSCAN_Bot = -1.3843 - 0.07925
z1_DSCAN_Bot = 9.19671

x2_DSCAN_Bot = -1.3843
z2_DSCAN_Bot = 9.19671

x3_DSCAN_Bot = -1.3843
z3_DSCAN_Bot = 9.19671 + 7.45537

x4_DSCAN_Bot = -1.3843 - 0.07925
z4_DSCAN_Bot = 9.19671 + 7.45537


DSCAN_Bot = polygon(
    (
        [z1_DSCAN_Bot, x1_DSCAN_Bot],
        [z4_DSCAN_Bot, x4_DSCAN_Bot],
        [z3_DSCAN_Bot, x3_DSCAN_Bot],
        [z2_DSCAN_Bot, x2_DSCAN_Bot],
    ),
    notSource=False,
)

# Top plate
x1_DSCAN_Top = 1.20015
z1_DSCAN_Top = 9.24751

x2_DSCAN_Top = 1.22555
z2_DSCAN_Top = 9.24751

x3_DSCAN_Top = 1.22555
z3_DSCAN_Top = 9.24751 + 7.35377

x4_DSCAN_Top = 1.20015
z4_DSCAN_Top = 9.24751 + 7.35377


DSCAN_Top = polygon(
    (
        [z1_DSCAN_Top, x1_DSCAN_Top],
        [z4_DSCAN_Top, x4_DSCAN_Top],
        [z3_DSCAN_Top, x3_DSCAN_Top],
        [z2_DSCAN_Top, x2_DSCAN_Top],
    ),
    notSource=False,
)

# Back Plate upper part - it has two parts
x1_DSCAN_Back_up_1 = 0.6475
z1_DSCAN_Back_up_1 = 16.52509

x2_DSCAN_Back_up_1 = 1.20015
z2_DSCAN_Back_up_1 = 16.52509

x3_DSCAN_Back_up_1 = 1.20015
z3_DSCAN_Back_up_1 = 16.52509 + 0.1016

x4_DSCAN_Back_up_1 = 0.6475
z4_DSCAN_Back_up_1 = 16.52509 + 0.1016


DSCAN_Back_up_1 = polygon(
    (
        [z1_DSCAN_Back_up_1, x1_DSCAN_Back_up_1],
        [z4_DSCAN_Back_up_1, x4_DSCAN_Back_up_1],
        [z3_DSCAN_Back_up_1, x3_DSCAN_Back_up_1],
        [z2_DSCAN_Back_up_1, x2_DSCAN_Back_up_1],
    ),
    notSource=False,
)

x1_DSCAN_Back_up_2 = 0.6604
z1_DSCAN_Back_up_2 = 16.52509 + 0.1016

x2_DSCAN_Back_up_2 = 1.20015
z2_DSCAN_Back_up_2 = 16.52509 + 0.1016

x3_DSCAN_Back_up_2 = 1.20015
z3_DSCAN_Back_up_2 = 16.52509 + 0.1016 + 0.0254

x4_DSCAN_Back_up_2 = 0.6604
z4_DSCAN_Back_up_2 = 16.52509 + 0.1016 + 0.0254


DSCAN_Back_up_2 = polygon(
    (
        [z1_DSCAN_Back_up_2, x1_DSCAN_Back_up_2],
        [z4_DSCAN_Back_up_2, x4_DSCAN_Back_up_2],
        [z3_DSCAN_Back_up_2, x3_DSCAN_Back_up_2],
        [z2_DSCAN_Back_up_2, x2_DSCAN_Back_up_2],
    ),
    notSource=False,
)

# Back Plate lower part - lt has two parts
x1_DSCAN_Back_low_1 = -1.4224
z1_DSCAN_Back_low_1 = 16.52509

x2_DSCAN_Back_low_1 = -0.6475
z2_DSCAN_Back_low_1 = 16.52509

x3_DSCAN_Back_low_1 = -0.6475
z3_DSCAN_Back_low_1 = 16.52509 + 0.1016

x4_DSCAN_Back_low_1 = -1.4224
z4_DSCAN_Back_low_1 = 16.52509 + 0.1016


DSCAN_Back_low_1 = polygon(
    (
        [z1_DSCAN_Back_low_1, x1_DSCAN_Back_low_1],
        [z4_DSCAN_Back_low_1, x4_DSCAN_Back_low_1],
        [z3_DSCAN_Back_low_1, x3_DSCAN_Back_low_1],
        [z2_DSCAN_Back_low_1, x2_DSCAN_Back_low_1],
    ),
    notSource=False,
)

x1_DSCAN_Back_low_2 = -1.4224
z1_DSCAN_Back_low_2 = 16.52509 + 0.1016

x2_DSCAN_Back_low_2 = -0.6604
z2_DSCAN_Back_low_2 = 16.52509 + 0.1016

x3_DSCAN_Back_low_2 = -0.6604
z3_DSCAN_Back_low_2 = 16.52509 + 0.1016 + 0.0254

x4_DSCAN_Back_low_2 = -1.4224
z4_DSCAN_Back_low_2 = 16.52509 + 0.1016 + 0.0254


DSCAN_Back_low_2 = polygon(
    (
        [z1_DSCAN_Back_low_2, x1_DSCAN_Back_low_2],
        [z4_DSCAN_Back_low_2, x4_DSCAN_Back_low_2],
        [z3_DSCAN_Back_low_2, x3_DSCAN_Back_low_2],
        [z2_DSCAN_Back_low_2, x2_DSCAN_Back_low_2],
    ),
    notSource=False,
)


##Photon Scaper
##+ve y-direction
x1_Scaper_1 = 0.040
z1_Scaper_1 = 9.2075

x2_Scaper_1 = 0.140
z2_Scaper_1 = 9.2075

x3_Scaper_1 = 0.140
z3_Scaper_1 = 9.3091

x4_Scaper_1 = 0.040
z4_Scaper_1 = 9.3091


Scaper_11 = polygon(
    (
        [z1_Scaper_1, x1_Scaper_1],
        [z4_Scaper_1, x4_Scaper_1],
        [z3_Scaper_1, x3_Scaper_1],
        [z2_Scaper_1, x2_Scaper_1],
    ),
    notSource=False,
)

##-ve y-direction
x1_Scaper_2 = 0.040
z1_Scaper_2 = 9.2075

x2_Scaper_2 = 0.0608
z2_Scaper_2 = 9.2075

x3_Scaper_2 = 0.0608
z3_Scaper_2 = 9.3091

x4_Scaper_2 = 0.040
z4_Scaper_2 = 9.3091


Scaper_12 = polygon(
    (
        [z2_Scaper_2, -x2_Scaper_2],
        [z3_Scaper_2, -x3_Scaper_2],
        [z4_Scaper_2, -x4_Scaper_2],
        [z1_Scaper_2, -x1_Scaper_2],
    ),
    notSource=False,
)

################# collimator 4, 3 segmentations

# seg 1

x1_coll_4_1 = -0.250  
z1_coll_4_1 = 7.725 

x2_coll_4_1 = -0.185
z2_coll_4_1 = 7.725 

x3_coll_4_1 = -0.1983  # 185+100*tan(7.6 deg)
z3_coll_4_1 = 7.875 

x4_coll_4_1 = -0.250 
z4_coll_4_1 = 7.875 


coll_4_1 = polygon(
    (
        [z1_coll_4_1, x1_coll_4_1],
        [z4_coll_4_1, x4_coll_4_1],
        [z3_coll_4_1, x3_coll_4_1],
        [z2_coll_4_1, x2_coll_4_1],
    ),
    notSource=False,
)


# seg 2

x1_coll_4_2 = -0.0515  
z1_coll_4_2 = 7.775 

x2_coll_4_2 = -0.040
z2_coll_4_2 = 7.775 

x3_coll_4_2 = -0.040
z3_coll_4_2 = 7.875 

x4_coll_4_2 = -0.0515  
z4_coll_4_2 = 7.875 


coll_4_2 = polygon(
    (
        [z1_coll_4_2, x1_coll_4_2],
        [z4_coll_4_2, x4_coll_4_2],
        [z3_coll_4_2, x3_coll_4_2],
        [z2_coll_4_2, x2_coll_4_2],
    ),
    notSource=False,
)

# seg 3

x1_coll_4_3 = 0.040
z1_coll_4_3 = 7.775 

x2_coll_4_3 = 0.250  # Was simulation -0.300 # Was CAD -0.254
z2_coll_4_3 = 7.775 

x3_coll_4_3 = 0.250  # Was simulation -0.300 # Was CAD -0.254
z3_coll_4_3 = 7.875 

x4_coll_4_3 = 0.040
z4_coll_4_3 = 7.875 


coll_4_3 = polygon(
    (
        [z1_coll_4_3, x1_coll_4_3],
        [z4_coll_4_3, x4_coll_4_3],
        [z3_coll_4_3, x3_coll_4_3],
        [z2_coll_4_3, x2_coll_4_3],
    ),
    notSource=False,
)


######### collimator 5 (shaped like a tuning fork), 1 seg


x1_coll_5 = -0.100  # use this if you just want the exact y=0 slice
z1_coll_5 = 12.057824

x2_coll_5 = -0.045  # from GDML
z2_coll_5 = 12.057824  # thickness of collimator 5 = 35 mm

x3_coll_5 = -0.045  # from GDML
z3_coll_5 = 12.157824

x4_coll_5 = -0.100  # use this if you just want the exact y=0 slice
z4_coll_5 = 12.157824

coll_5 = polygon(
    (
        [z1_coll_5, x1_coll_5],
        [z4_coll_5, x4_coll_5],
        [z3_coll_5, x3_coll_5],
        [z2_coll_5, x2_coll_5],
    ),
    notSource=False,
)


x1_coll_51 = -0.1026  # use this if you just want the exact y=0 slice
z1_coll_51 = 12.170549

x2_coll_51 = -0.046  # from GDML
z2_coll_51 = 12.170549  # thickness of collimator 5 = 35 mm

x3_coll_51 = -0.046  # from GDML
z3_coll_51 = 12.270549

x4_coll_51 = -0.1026  # use this if you just want the exact y=0 slice
z4_coll_51 = 12.270549

coll_51 = polygon(
    (
        [z1_coll_51, x1_coll_51],
        [z4_coll_51, x4_coll_51],
        [z3_coll_51, x3_coll_51],
        [z2_coll_51, x2_coll_51],
    ),
    notSource=False,
)

###### Lintel (for ep scattering)

x1_lintel = -0.478
z1_lintel = 9.5573 + 4.5

x2_lintel = -0.800
z2_lintel = 9.5573 + 4.5

x3_lintel = -0.800
z3_lintel = 9.6573 + 4.5

x4_lintel = -0.478
z4_lintel = 9.6573 + 4.5


lintel = polygon(
    (
        [z1_lintel, x1_lintel],
        [z4_lintel, x4_lintel],
        [z3_lintel, x3_lintel],
        [z2_lintel, x2_lintel],
    ),
    notSource=False,
)


#################DS coil  ###########################
x1_DS_coil1 = 0.04103
z1_DS_coil1 = 4.93010 + 4.5

x2_DS_coil1 = 0.17520
z2_DS_coil1 = 4.93010 + 4.5

x3_DS_coil1 = 0.19825
z3_DS_coil1 = 5.93616 + 4.5

x4_DS_coil1 = 0.04103
z4_DS_coil1 = 5.93616 + 4.5

DS_Coil1 = polygon(
    (
        [z1_DS_coil1, x1_DS_coil1],
        [z4_DS_coil1, x4_DS_coil1],
        [z3_DS_coil1, x3_DS_coil1],
        [z2_DS_coil1, x2_DS_coil1],
    ),
    notSource=False,
)

x1_DS_coil2 = 0.04353
z1_DS_coil2 = 5.94774 + 4.5

x2_DS_coil2 = 0.21424
z2_DS_coil2 = 5.94774 + 4.5

x3_DS_coil2 = 0.238
z3_DS_coil2 = 6.97179 + 4.5

x4_DS_coil2 = 0.04353
z4_DS_coil2 = 6.97179 + 4.5

DS_Coil2 = polygon(
    (
        [z1_DS_coil2, x1_DS_coil2],
        [z4_DS_coil2, x4_DS_coil2],
        [z3_DS_coil2, x3_DS_coil2],
        [z2_DS_coil2, x2_DS_coil2],
    ),
    notSource=False,
)

x1_DS_coil3 = 0.04642
z1_DS_coil3 = 6.98652 + 4.5

x2_DS_coil3 = 0.26058
z2_DS_coil3 = 6.98652 + 4.5

x3_DS_coil3 = 0.27708
z3_DS_coil3 = 7.96320 + 4.5

x4_DS_coil3 = 0.04642
z4_DS_coil3 = 7.96320 + 4.5

DS_Coil3 = polygon(
    (
        [z1_DS_coil3, x1_DS_coil3],
        [z4_DS_coil3, x4_DS_coil3],
        [z3_DS_coil3, x3_DS_coil3],
        [z2_DS_coil3, x2_DS_coil3],
    ),
    notSource=False,
)

x1_DS_coil4_1 = 0.05681
z1_DS_coil4_1 = 7.97874 + 4.5

x2_DS_coil4_1 = 0.34382
z2_DS_coil4_1 = 7.97874 + 4.5

x3_DS_coil4_1 = 0.42368
z3_DS_coil4_1 = 9.76061 + 4.5

x4_DS_coil4_1 = 0.07865
z4_DS_coil4_1 = 9.76061 + 4.5

DS_Coil4_1 = polygon(
    (
        [z1_DS_coil4_1, x1_DS_coil4_1],
        [z4_DS_coil4_1, x4_DS_coil4_1],
        [z3_DS_coil4_1, x3_DS_coil4_1],
        [z2_DS_coil4_1, x2_DS_coil4_1],
    ),
    notSource=False,
)

x1_DS_coil4_2 = 0.07865
z1_DS_coil4_2 = 9.76061 + 4.5

x2_DS_coil4_2 = 0.29841
z2_DS_coil4_2 = 9.76061 + 4.5

x3_DS_coil4_2 = 0.38464
z3_DS_coil4_2 = 11.11293 + 4.5

x4_DS_coil4_2 = 0.16008
z4_DS_coil4_2 = 11.11293 + 4.5

DS_Coil4_2 = polygon(
    (
        [z1_DS_coil4_2, x1_DS_coil4_2],
        [z4_DS_coil4_2, x4_DS_coil4_2],
        [z3_DS_coil4_2, x3_DS_coil4_2],
        [z2_DS_coil4_2, x2_DS_coil4_2],
    ),
    notSource=False,
)

x1_DS_coil4_3 = 0.16008
z1_DS_coil4_3 = 11.11293 + 4.5

x2_DS_coil4_3 = 0.38464
z2_DS_coil4_3 = 11.11293 + 4.5

x3_DS_coil4_3 = 0.39290
z3_DS_coil4_3 = 11.79868 + 4.5

x4_DS_coil4_3 = 0.12692
z4_DS_coil4_3 = 11.79868 + 4.5

DS_Coil4_3 = polygon(
    (
        [z1_DS_coil4_3, x1_DS_coil4_3],
        [z4_DS_coil4_3, x4_DS_coil4_3],
        [z3_DS_coil4_3, x3_DS_coil4_3],
        [z2_DS_coil4_3, x2_DS_coil4_3],
    ),
    notSource=False,
)

# Col6A
x1_Col6A = -0.1058  # use this if you just want the exact y=0 slice
z1_Col6A = 9.555904 + 4.5

x2_Col6A = -0.055314  # from GDML
z2_Col6A = 9.555904 + 4.5

x3_Col6A = -0.061143  # from GDML
z3_Col6A = 9.708304 + 4.5

x4_Col6A = -0.1058  # use this if you just want the exact y=0 slice
z4_Col6A = 9.708304 + 4.5

Col6A = polygon(
    (
        [z1_Col6A, x1_Col6A],
        [z4_Col6A, x4_Col6A],
        [z3_Col6A, x3_Col6A],
        [z2_Col6A, x2_Col6A],
    ),
    notSource=False,
)

# Col6B
x1_Col6B = -0.1224  # use this if you just want the exact y=0 slice
z1_Col6B = 10.9275 + 4.5

x2_Col6B = -0.070  # from GDML
z2_Col6B = 10.9275 + 4.5

x3_Col6B = -0.07536  # from GDML
z3_Col6B = 11.079904 + 4.5

x4_Col6B = -0.1224  # use this if you just want the exact y=0 slice
z4_Col6B = 11.079904 + 4.5

Col6B = polygon(
    (
        [z1_Col6B, x1_Col6B],
        [z4_Col6B, x4_Col6B],
        [z3_Col6B, x3_Col6B],
        [z2_Col6B, x2_Col6B],
    ),
    notSource=False,
)


#################################################################

#### quartz

# quartz1 = polygon( ([28.0, 0.6], [28.01, 0.6], [28.01, 1.4], [28, 1.4]), isDetector=True )
# quartz2 = polygon( ([28.0, -1.4], [28.01, -1.4], [28.01, -0.6], [28, -0.6]), isDetector=True )

det_inner_radius = (
    0.69  # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
)
det_outer_radius = 1.30  # ring 6 quartz ends at 1.2, PMTs begin at 1.3
det_z_pos = 26.5
det_z_extent = 1.0  # was = .02 for ideal detector

quartz1 = polygon(
    (
        [det_z_pos, det_inner_radius],
        [det_z_pos + det_z_extent, det_inner_radius],
        [det_z_pos + det_z_extent, det_outer_radius],
        [det_z_pos, det_outer_radius],
    ),
    isDetector=True,
)
quartz2 = polygon(
    (
        [det_z_pos, -det_outer_radius],
        [det_z_pos + det_z_extent, -det_outer_radius],
        [det_z_pos + det_z_extent, -det_inner_radius],
        [det_z_pos, -det_inner_radius],
    ),
    isDetector=True,
)

##################################################################################################################################

sources.append(target)

allpolys.append(bellows1_USflange_top)
allpolys.append(bellows1_USflange_bottom)
allpolys.append(bellows1_seg1_top)
allpolys.append(bellows1_seg1_bottom)
allpolys.append(bellows1_seg2_top)
allpolys.append(bellows1_seg2_bottom)
allpolys.append(bellows1_seg3_top)
allpolys.append(bellows1_seg3_bottom)
allpolys.append(bellows1_DSflange_top)
allpolys.append(bellows1_DSflange_bottom)

allpolys.append(bellows12_pipe_top)
allpolys.append(bellows12_pipe_bottom)

allpolys.append(bellows12_pipe_DSflange_top)
allpolys.append(bellows12_pipe_DSflange_bottom)

allpolys.append(pipe_UScollar0_top)
allpolys.append(pipe_UScollar0_bottom)
allpolys.append(collar0_top)
allpolys.append(collar0_bottom)
allpolys.append(pipe_DScollar0_top)
allpolys.append(pipe_DScollar0_bottom)

allpolys.append(bellows2_USflange_top)
allpolys.append(bellows2_USflange_bottom)
allpolys.append(bellows2_seg1_top)
allpolys.append(bellows2_seg1_bottom)
allpolys.append(bellows2_seg2_top)
allpolys.append(bellows2_seg2_bottom)
allpolys.append(bellows2_seg3_top)
allpolys.append(bellows2_seg3_bottom)
allpolys.append(bellows2_DSflange_top)
allpolys.append(bellows2_DSflange_bottom)

allpolys.append(upstream_enclosure_USpipe_top)
allpolys.append(upstream_enclosure_USpipe_bottom)

allpolys.append(upstream_enclosure_USwall_top)
allpolys.append(upstream_enclosure_USwall_bottom)
allpolys.append(upstream_enclosure_sidewall_top)
allpolys.append(upstream_enclosure_sidewall_bottom)
allpolys.append(upstream_enclosure_DSwall_top)
allpolys.append(upstream_enclosure_DSwall_bottom)

allpolys.append(collimator1_seg1_top)
allpolys.append(collimator1_seg1_bottom)
allpolys.append(collimator1_seg2_top)
allpolys.append(collimator1_seg2_bottom)
allpolys.append(collimator1_seg3_top)
allpolys.append(collimator1_seg3_bottom)
allpolys.append(collimator1_seg4_top)
allpolys.append(collimator1_seg4_bottom)
allpolys.append(collimator1_seg5_top)
allpolys.append(collimator1_seg5_bottom)
allpolys.append(collimator1_seg6_top)
allpolys.append(collimator1_seg6_bottom)

allpolys.append(collimator2_seg1)
allpolys.append(collimator2_seg2)
allpolys.append(collimator2_seg3)
allpolys.append(collimator2_seg4)

allpolys.append(uscoil_seg1)
allpolys.append(uscoil_seg2)
allpolys.append(uscoil_seg3)

allpolys.append(twobounce_front_insert_top)
allpolys.append(twobounce_front_insert_bottom)
allpolys.append(twobounce_acceptance)
allpolys.append(twobounce_coil)
allpolys.append(twobounce_end_insert_top)
allpolys.append(twobounce_end_insert_bottom)

allpolys.append(collar_top1)
allpolys.append(collar_bottom1)

allpolys.append(collar_top2)
allpolys.append(collar_bottom2)

allpolys.append(collar3_top)
allpolys.append(collar3_bottom)

allpolys.append(US_pipe1_lo)
allpolys.append(US_pipe1_up)

allpolys.append(US_flange1_1_1_up)
allpolys.append(US_flange1_1_1_lo)
allpolys.append(US_flange1_1_2_up)
allpolys.append(US_flange1_1_2_lo)
allpolys.append(US_flange1_2_1_up)
allpolys.append(US_flange1_2_1_lo)
allpolys.append(US_flange1_2_2_up)
allpolys.append(US_flange1_2_2_lo)

allpolys.append(US_pipe2_1_up)
allpolys.append(US_pipe2_1_lo)
allpolys.append(US_pipe2_2_up)
allpolys.append(US_pipe2_2_lo)
allpolys.append(US_pipe2_3_up)
allpolys.append(US_pipe2_3_lo)

allpolys.append(DSCAN_Front_up)
allpolys.append(DSCAN_Front_low)

allpolys.append(DSCAN_Top)
allpolys.append(DSCAN_Bot)

allpolys.append(DSCAN_Back_up_1)
allpolys.append(DSCAN_Back_up_2)
allpolys.append(DSCAN_Back_low_1)
allpolys.append(DSCAN_Back_low_2)

allpolys.append(Scaper_11)
allpolys.append(Scaper_12)

allpolys.append(coll_4_1)
allpolys.append(coll_4_2)
allpolys.append(coll_4_3)


allpolys.append(coll_5)
allpolys.append(coll_51)
allpolys.append(lintel)


allpolys.append(Col6A)
allpolys.append(Col6B)

allpolys.append(DS_Coil1)
allpolys.append(DS_Coil2)
allpolys.append(DS_Coil3)
allpolys.append(DS_Coil4_1)
allpolys.append(DS_Coil4_2)
allpolys.append(DS_Coil4_3)

allpolys.append(quartz1)
allpolys.append(quartz2)

# print sources
# print allpolys

print("Starting")

for apoly in allpolys:
    otherpolys = list(allpolys)
    otherpolys.remove(apoly)
    apoly.light(sources, otherpolys)

print("Doing once bounce lighting")

# One bounce
for apoly in allpolys:
    otherpolys = list(allpolys)
    otherpolys.remove(apoly)
    apoly.light(otherpolys, [], 2)

mydraw = drawlight(allpolys + sources)

Gtk.main()
