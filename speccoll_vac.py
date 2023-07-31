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

### Collimator 4

# Seg 1

x1 = -26*mm
z1 = 3225*mm-tgtpos

x2 = -51.5*mm
z2 = 3225*mm-tgtpos

x3 = -51.5*mm
z3 = 3375*mm-tgtpos

x4 = -26*mm
z4 = 3375*mm-tgtpos

collimator4_seg1 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# Seg 2
x1 = -185*mm
z1 = 3225*mm-tgtpos

x2 = -250*mm
z2 = 3225*mm-tgtpos

x3 = -250*mm
z3 = 3275*mm-tgtpos

x4 = -185*mm
z4 = 3275*mm-tgtpos

collimator4_seg2 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# Seg 3

x1 = -185*mm
z1 = 3275*mm-tgtpos

x2 = -250*mm
z2 = 3275*mm-tgtpos

x3 = -250*mm
z3 = 3375*mm-tgtpos

x4 = -185*mm*(1+np.tan(7.6*np.pi/180))
z4 = 3375*mm-tgtpos

collimator4_seg3 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

# Seg 4

x1 = 26*mm
z1 = 3375*mm-tgtpos

x2 = 250*mm
z2 = 3375*mm-tgtpos

x3 = 250*mm
z3 = 3225*mm-tgtpos

x4 = 26*mm
z4 = 3225*mm-tgtpos

collimator4_seg4 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

### Upstream Enclosure Lead Wall

# Seg 1

x1=230*mm
z1=3541.903*mm-tgtpos

x2=230*mm
z2=3592.703*mm-tgtpos

x3=406.4*mm
z3=3592.703*mm-tgtpos

x4=406.4*mm
z4=3541.903*mm-tgtpos

US_Pbwall_seg1_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
US_Pbwall_seg1_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

#seg 2
x1=230*mm
z1=3592.703*mm-tgtpos

x2=230*mm
z2=3694.303*mm-tgtpos

x3=330.2*mm
z3=3694.303*mm-tgtpos

x4=330.2*mm
z4=3592.703*mm-tgtpos

US_Pbwall_seg2_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
US_Pbwall_seg2_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

#seg 3
x1=(533.4*2)/2*mm
z1=(3592.703+50.8+101.6/2-101.6/2)*mm-tgtpos

x2=(533.4*2)/2*mm
z2=(3592.703+50.8+101.6/2+101.6/2)*mm-tgtpos

x3=344.488*mm
z3=(3592.703+50.8+101.6/2+101.6/2)*mm-tgtpos

x4=344.488*mm
z4=(3592.703+50.8+101.6/2-101.6/2)*mm-tgtpos

US_Pbwall_seg3_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
US_Pbwall_seg3_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Pipe downstream of upstream enclosure before bellows 3
x1 = 331.788*mm 
z1 = 3592.703*mm-tgtpos

x2 = 331.788*mm  
z2 = 4140.210*mm-tgtpos

x3 = 344.488*mm 
z3 = 4140.210*mm-tgtpos  

x4 = 344.488*mm 
z4 = 3592.703*mm-tgtpos

upstream_enclosure_DSpipe_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
upstream_enclosure_DSpipe_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)

### Upstream enclosure downstream pipe flange

x1 = 331.788*mm 
z1 = 4140.210*mm-tgtpos

x2 = 331.788*mm  
z2 = 4191.010*mm-tgtpos

x3 = 406.4*mm 
z3 = 4191.010*mm-tgtpos  

x4 = 406.4*mm 
z4 = 4140.210*mm-tgtpos

upstream_enclosure_DSpipe_flange_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
upstream_enclosure_DSpipe_flange_bottom = polygon(
    (
        [z2, -x2],
        [z3, -x3],
        [z4, -x4],
        [z1, -x1],
    ),
    notSource=False,
)


###### First downstream Lead collar (for ep scattering)

x1_collar1 = 0.550
z1_collar1 = 11.767124 + 4.5

x2_collar1 = 0.7558659
z2_collar1 = 11.767124 + 4.5

x3_collar1 = 0.7558659
z3_collar1 = 11.767124 + 4.5 + 0.150

x4_collar1 = 0.5631233
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

#Inner Ring
x1_collar2_in = 1.01000
z1_collar2_in = 23.63262

x2_collar2_in = 1.14635
z2_collar2_in = 23.63262

x3_collar2_in = 1.14635
z3_collar2_in = 23.63262 + 0.150

x4_collar2_in = 1.019
z4_collar2_in = 23.63262 + 0.150


collar2_inner_top = polygon(
    (
        [z1_collar2_in, x1_collar2_in],
        [z4_collar2_in, x4_collar2_in],
        [z3_collar2_in, x3_collar2_in],
        [z2_collar2_in, x2_collar2_in],
    ),
    notSource=False,
)
collar2_inner_bottom = polygon(
    (
        [z2_collar2_in, -x2_collar2_in],
        [z3_collar2_in, -x3_collar2_in],
        [z4_collar2_in, -x4_collar2_in],
        [z1_collar2_in, -x1_collar2_in],
    ),
    notSource=False,
)

#Outer Ring
x1_collar2_out = 1.12095
z1_collar2_out = 23.43262

x2_collar2_out = 1.31500
z2_collar2_out = 23.43262

x3_collar2_out = 1.31500
z3_collar2_out = 23.43262 + 0.150

x4_collar2_out = 1.12095
z4_collar2_out = 23.43262 + 0.150


collar2_outer_top = polygon(
    (
        [z1_collar2_out, x1_collar2_out],
        [z4_collar2_out, x4_collar2_out],
        [z3_collar2_out, x3_collar2_out],
        [z2_collar2_out, x2_collar2_out],
    ),
    notSource=False,
)
collar2_outer_bottom = polygon(
    (
        [z2_collar2_out, -x2_collar2_out],
        [z3_collar2_out, -x3_collar2_out],
        [z4_collar2_out, -x4_collar2_out],
        [z1_collar2_out, -x1_collar2_out],
    ),
    notSource=False,
)

##############Downstream vessel###############
# Front Plate upper part
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

# Front Plate lower part
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

# Back Plate upper part - it has three parts
x1_DSCAN_Back_up_1 = 0.74930
z1_DSCAN_Back_up_1 = 16.52509

x2_DSCAN_Back_up_1 = 1.20015
z2_DSCAN_Back_up_1 = 16.52509

x3_DSCAN_Back_up_1 = 1.20015
z3_DSCAN_Back_up_1 = 16.52509 + 0.08255

x4_DSCAN_Back_up_1 = 0.74930
z4_DSCAN_Back_up_1 = 16.52509 + 0.08255


DSCAN_Back_up_1 = polygon(
    (
        [z1_DSCAN_Back_up_1, x1_DSCAN_Back_up_1],
        [z4_DSCAN_Back_up_1, x4_DSCAN_Back_up_1],
        [z3_DSCAN_Back_up_1, x3_DSCAN_Back_up_1],
        [z2_DSCAN_Back_up_1, x2_DSCAN_Back_up_1],
    ),
    notSource=False,
)

x1_DSCAN_Back_up_2 = 0.67564
z1_DSCAN_Back_up_2 = 16.52509 + 0.08255

x2_DSCAN_Back_up_2 = 1.20015
z2_DSCAN_Back_up_2 = 16.52509 + 0.08255

x3_DSCAN_Back_up_2 = 1.20015
z3_DSCAN_Back_up_2 = 16.52509 + 0.1016

x4_DSCAN_Back_up_2 = 0.67564 
z4_DSCAN_Back_up_2 = 16.52509 + 0.1016


DSCAN_Back_up_2 = polygon(
    (
        [z1_DSCAN_Back_up_2, x1_DSCAN_Back_up_2],
        [z4_DSCAN_Back_up_2, x4_DSCAN_Back_up_2],
        [z3_DSCAN_Back_up_2, x3_DSCAN_Back_up_2],
        [z2_DSCAN_Back_up_2, x2_DSCAN_Back_up_2],
    ),
    notSource=False,
)

x1_DSCAN_Back_up_3 = 0.68834
z1_DSCAN_Back_up_3 = 16.52509 + 0.1016

x2_DSCAN_Back_up_3 = 1.20015
z2_DSCAN_Back_up_3 = 16.52509 + 0.1016

x3_DSCAN_Back_up_3 = 1.20015
z3_DSCAN_Back_up_3 = 16.52509 + 0.127

x4_DSCAN_Back_up_3 = 0.68834 
z4_DSCAN_Back_up_3 = 16.52509 + 0.127


DSCAN_Back_up_3 = polygon(
    (
        [z1_DSCAN_Back_up_3, x1_DSCAN_Back_up_3],
        [z4_DSCAN_Back_up_3, x4_DSCAN_Back_up_3],
        [z3_DSCAN_Back_up_3, x3_DSCAN_Back_up_3],
        [z2_DSCAN_Back_up_3, x2_DSCAN_Back_up_3],
    ),
    notSource=False,
)

# Back Plate lower part - it has three parts
x1_DSCAN_Back_low_1 = -1.4224
z1_DSCAN_Back_low_1 = 16.52509

x2_DSCAN_Back_low_1 = -0.74930
z2_DSCAN_Back_low_1 = 16.52509

x3_DSCAN_Back_low_1 = -0.74930
z3_DSCAN_Back_low_1 = 16.52509 + 0.08255

x4_DSCAN_Back_low_1 = -1.4224
z4_DSCAN_Back_low_1 = 16.52509 + 0.08255


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
z1_DSCAN_Back_low_2 = 16.52509 + 0.08255

x2_DSCAN_Back_low_2 = -0.67564
z2_DSCAN_Back_low_2 = 16.52509 + 0.08255

x3_DSCAN_Back_low_2 = -0.67564
z3_DSCAN_Back_low_2 = 16.52509 + 0.1016

x4_DSCAN_Back_low_2 = -1.4224
z4_DSCAN_Back_low_2 = 16.52509 + 0.1016


DSCAN_Back_low_2 = polygon(
    (
        [z1_DSCAN_Back_low_2, x1_DSCAN_Back_low_2],
        [z4_DSCAN_Back_low_2, x4_DSCAN_Back_low_2],
        [z3_DSCAN_Back_low_2, x3_DSCAN_Back_low_2],
        [z2_DSCAN_Back_low_2, x2_DSCAN_Back_low_2],
    ),
    notSource=False,
)

x1_DSCAN_Back_low_3 = -1.4224
z1_DSCAN_Back_low_3 = 16.52509 + 0.1016

x2_DSCAN_Back_low_3 = -0.68834
z2_DSCAN_Back_low_3 = 16.52509 + 0.1016

x3_DSCAN_Back_low_3 = -0.68834
z3_DSCAN_Back_low_3 = 16.52509 + 0.127

x4_DSCAN_Back_low_3 = -1.4224
z4_DSCAN_Back_low_3 = 16.52509 + 0.127


DSCAN_Back_low_3 = polygon(
    (
        [z1_DSCAN_Back_low_3, x1_DSCAN_Back_low_3],
        [z4_DSCAN_Back_low_3, x4_DSCAN_Back_low_3],
        [z3_DSCAN_Back_low_3, x3_DSCAN_Back_low_3],
        [z2_DSCAN_Back_low_3, x2_DSCAN_Back_low_3],
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

######### Collimator 5 (shaped like a tuning fork), 1 seg


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

#Tungsten Belly Plates

x1_solid_epoxy_1 = 0.038
z1_solid_epoxy_1 = 4.93201 + 4.5

x2_solid_epoxy_1 = 0.041
z2_solid_epoxy_1 = 4.93201 + 4.5

x3_solid_epoxy_1 = 0.041
z3_solid_epoxy_1 = 5.93425 + 4.5

x4_solid_epoxy_1 = 0.038
z4_solid_epoxy_1 = 5.93425 + 4.5

Solid_epoxy_1 = polygon(
    (
        [z1_solid_epoxy_1, x1_solid_epoxy_1],
        [z4_solid_epoxy_1, x4_solid_epoxy_1],
        [z3_solid_epoxy_1, x3_solid_epoxy_1],
        [z2_solid_epoxy_1, x2_solid_epoxy_1],
    ),
    notSource=False,
)

x1_solid_epoxy_2 = 0.0435
z1_solid_epoxy_2 = 5.94847 + 4.5

x2_solid_epoxy_2 = 0.0465
z2_solid_epoxy_2 = 5.94847 + 4.5

x3_solid_epoxy_2 = 0.0465
z3_solid_epoxy_2 = 6.97106 + 4.5

x4_solid_epoxy_2 = 0.0435
z4_solid_epoxy_2 = 6.97106 + 4.5

Solid_epoxy_2 = polygon(
    (
        [z1_solid_epoxy_2, x1_solid_epoxy_2],
        [z4_solid_epoxy_2, x4_solid_epoxy_2],
        [z3_solid_epoxy_2, x3_solid_epoxy_2],
        [z2_solid_epoxy_2, x2_solid_epoxy_2],
    ),
    notSource=False,
)

#Solid epoxy 3 & 4 have been merged
x1_solid_epoxy_3 = 0.046
z1_solid_epoxy_3 = 6.98802 + 4.5

x2_solid_epoxy_3 = 0.049
z2_solid_epoxy_3 = 6.98802 + 4.5

x3_solid_epoxy_3 = 0.049
z3_solid_epoxy_3 = 7.96170 + 4.5

x4_solid_epoxy_3 = 0.046
z4_solid_epoxy_3 = 7.96170 + 4.5

Solid_epoxy_3 = polygon(
    (
        [z1_solid_epoxy_3, x1_solid_epoxy_3],
        [z4_solid_epoxy_3, x4_solid_epoxy_3],
        [z3_solid_epoxy_3, x3_solid_epoxy_3],
        [z2_solid_epoxy_3, x2_solid_epoxy_3],
    ),
    notSource=False,
)

x1_solid_epoxy_5 = 0.05281
z1_solid_epoxy_5 = 8.03666 + 4.5

x2_solid_epoxy_5 = 0.05581
z2_solid_epoxy_5 = 8.03666 + 4.5

x3_solid_epoxy_5 = 0.05581 + .02184
z3_solid_epoxy_5 = 9.70269 + 4.5

x4_solid_epoxy_5 = 0.05281 + .02184
z4_solid_epoxy_5 = 9.70269 + 4.5

Solid_epoxy_5 = polygon(
    (
        [z1_solid_epoxy_5, x1_solid_epoxy_5],
        [z4_solid_epoxy_5, x4_solid_epoxy_5],
        [z3_solid_epoxy_5, x3_solid_epoxy_5],
        [z2_solid_epoxy_5, x2_solid_epoxy_5],
    ),
    notSource=False,
)

# Collimator 6A

#seg 1
x1_Col6A_1 = -0.08990  # use this if you just want the exact y=0 slice
z1_Col6A_1 = 9.555904 + 4.5

x2_Col6A_1 = -0.05531  # from GDML
z2_Col6A_1 = 9.555904 + 4.5

x3_Col6A_1 = -0.05629  # from GDML
z3_Col6A_1 = 9.625754 + 4.5

x4_Col6A_1 = -0.08990  # use this if you just want the exact y=0 slice
z4_Col6A_1 = 9.625754 + 4.5

Col6A_1 = polygon(
    (
        [z1_Col6A_1, x1_Col6A_1],
        [z4_Col6A_1, x4_Col6A_1],
        [z3_Col6A_1, x3_Col6A_1],
        [z2_Col6A_1, x2_Col6A_1],
    ),
    notSource=False,
)

#seg 2
x1_Col6A_2 = -0.08990  # use this if you just want the exact y=0 slice
z1_Col6A_2 = 9.638454 + 4.5

x2_Col6A_2 = -0.05646  # from GDML
z2_Col6A_2 = 9.638454 + 4.5

x3_Col6A_2 = -0.05744  # from GDML
z3_Col6A_2 = 9.708304 + 4.5

x4_Col6A_2 = -0.08890  # use this if you just want the exact y=0 slice
z4_Col6A_2 = 9.708304 + 4.5

Col6A_2 = polygon(
    (
        [z1_Col6A_2, x1_Col6A_2],
        [z4_Col6A_2, x4_Col6A_2],
        [z3_Col6A_2, x3_Col6A_2],
        [z2_Col6A_2, x2_Col6A_2],
    ),
    notSource=False,
)

# Collimator 6B

#seg 1
x1_Col6B_1 = -0.12000  # use this if you just want the exact y=0 slice
z1_Col6B_1 = 10.92750 + 4.5

x2_Col6B_1 = -0.08000  # from GDML
z2_Col6B_1 = 10.92750 + 4.5

x3_Col6B_1 = -0.08147  # from GDML
z3_Col6B_1 = 10.99735 + 4.5

x4_Col6B_1 = -0.12000  # use this if you just want the exact y=0 slice
z4_Col6B_1 = 10.99735 + 4.5

Col6B_1 = polygon(
    (
        [z1_Col6B_1, x1_Col6B_1],
        [z4_Col6B_1, x4_Col6B_1],
        [z3_Col6B_1, x3_Col6B_1],
        [z2_Col6B_1, x2_Col6B_1],
    ),
    notSource=False,
)

#seg 2
x1_Col6B_2 = -0.12000  # use this if you just want the exact y=0 slice
z1_Col6B_2 = 11.010054 + 4.5

x2_Col6B_2 = -0.08173  # from GDML
z2_Col6B_2 = 11.010054 + 4.5

x3_Col6B_2 = -0.08320  # from GDML
z3_Col6B_2 = 11.079904 + 4.5

x4_Col6B_2 = -0.12000  # use this if you just want the exact y=0 slice
z4_Col6B_2 = 11.079904 + 4.5

Col6B_2 = polygon(
    (
        [z1_Col6B_2, x1_Col6B_2],
        [z4_Col6B_2, x4_Col6B_2],
        [z3_Col6B_2, x3_Col6B_2],
        [z2_Col6B_2, x2_Col6B_2],
    ),
    notSource=False,
)

#Drift chamber

#Driftpipe ~ left wall
x1_drift_1u = 0.68834  # use this if you just want the exact y=0 slice
z1_drift_1u = 17.35487

x2_drift_1u = 1.27229  # from GDML
z2_drift_1u = 17.35487

x3_drift_1u = 1.27229  # from GDML
z3_drift_1u = 17.35487 + 0.02210

x4_drift_1u = 0.68834  # use this if you just want the exact y=0 slice
z4_drift_1u = 17.35487 + 0.02210

Drift_wall_top = polygon(
    (
        [z1_drift_1u, x1_drift_1u],
        [z4_drift_1u, x4_drift_1u],
        [z3_drift_1u, x3_drift_1u],
        [z2_drift_1u, x2_drift_1u],
    ),
    notSource=False,
)

Drift_wall_bottom = polygon(
    (
        [z1_drift_1u, -x1_drift_1u],
        [z4_drift_1u, -x4_drift_1u],
        [z3_drift_1u, -x3_drift_1u],
        [z2_drift_1u, -x2_drift_1u],
    ),
    notSource=False,
)

#Driftpipe ~ main body
x1_drift_2u = 1.24993  
z1_drift_2u = 17.35487 + 0.02210

x2_drift_2u = 1.27229  # from GDML
z2_drift_2u = 17.35487 + 0.02210

x3_drift_2u = 1.27229  # from GDML
z3_drift_2u = 17.35487 + 5.97408

x4_drift_2u = 1.24993  
z4_drift_2u = 17.35487 + 5.97408

Drift_body_top = polygon(
    (
        [z1_drift_2u, x1_drift_2u],
        [z4_drift_2u, x4_drift_2u],
        [z3_drift_2u, x3_drift_2u],
        [z2_drift_2u, x2_drift_2u],
    ),
    notSource=False,
)

Drift_body_bottom = polygon(
    (
        [z1_drift_2u, -x1_drift_2u],
        [z4_drift_2u, -x4_drift_2u],
        [z3_drift_2u, -x3_drift_2u],
        [z2_drift_2u, -x2_drift_2u],
    ),
    notSource=False,
)

#Driftpipe vacuum (Driftpipe_vacuum). Approximating as 1 segment (instead of 3)

x1_drift_vac = 1.27229
z1_drift_vac = 23.18925

x2_drift_vac = 1.39700
z2_drift_vac = 23.18925

x3_drift_vac = 1.39700
z3_drift_vac = 23.18925 + 0.16510

x4_drift_vac = 1.27229 
z4_drift_vac = 23.18925 + 0.16510

Drift_vac_top = polygon(
    (
        [z1_drift_vac, x1_drift_vac],
        [z4_drift_vac, x4_drift_vac],
        [z3_drift_vac, x3_drift_vac],
        [z2_drift_vac, x2_drift_vac],
    ),
    notSource=False,
)

Drift_vac_bot = polygon(
    (
        [z1_drift_vac, -x1_drift_vac],
        [z4_drift_vac, -x4_drift_vac],
        [z3_drift_vac, -x3_drift_vac],
        [z2_drift_vac, -x2_drift_vac],
    ),
    notSource=False,
)

#DS window flange

x1_win_flan = 1.01143  
z1_win_flan = 23.35435

x2_win_flan = 1.39700  
z2_win_flan = 23.35435

x3_win_flan = 1.39700
z3_win_flan = 23.35435 + 0.0635

x4_win_flan = 1.06756  
z4_win_flan = 23.35435 + 0.0635

DS_window_flange_top = polygon(
    (
        [z1_win_flan, x1_win_flan],
        [z4_win_flan, x4_win_flan],
        [z3_win_flan, x3_win_flan],
        [z2_win_flan, x2_win_flan],
    ),
    notSource=False,
)

DS_window_flange_bot = polygon(
    (
        [z1_win_flan, -x1_win_flan],
        [z4_win_flan, -x4_win_flan],
        [z3_win_flan, -x3_win_flan],
        [z2_win_flan, -x2_win_flan],
    ),
    notSource=False,
)

#DSendtube

#US (DSendtube_phys)
x1_DSendtube_US = 0.67247 
z1_DSendtube_US = 16.60125

x2_DSendtube_US = 0.68517  
z2_DSendtube_US = 16.60125

x3_DSendtube_US = 0.68517
z3_DSendtube_US = 16.75827

x4_DSendtube_US = 0.67247  
z4_DSendtube_US = 16.75827

DSendtube_US_top = polygon(
    (
        [z1_DSendtube_US, x1_DSendtube_US],
        [z4_DSendtube_US, x4_DSendtube_US],
        [z3_DSendtube_US, x3_DSendtube_US],
        [z2_DSendtube_US, x2_DSendtube_US],
    ),
    notSource=False,
)

DSendtube_US_bot = polygon(
    (
        [z1_DSendtube_US, -x1_DSendtube_US],
        [z4_DSendtube_US, -x4_DSendtube_US],
        [z3_DSendtube_US, -x3_DSendtube_US],
        [z2_DSendtube_US, -x2_DSendtube_US],
    ),
    notSource=False,
)

#DS (DSpipeNeck_phys)
x1_DSendtube_DS = 0.67247 
z1_DSendtube_DS = 17.18916

x2_DSendtube_DS = 0.68517 
z2_DSendtube_DS = 17.18916

x3_DSendtube_DS = 0.68517
z3_DSendtube_DS = 17.18916 + 0.16886

x4_DSendtube_DS = 0.67247  
z4_DSendtube_DS = 17.18916 + 0.16886

DSendtube_DS_top = polygon(
    (
        [z1_DSendtube_DS, x1_DSendtube_DS],
        [z4_DSendtube_DS, x4_DSendtube_DS],
        [z3_DSendtube_DS, x3_DSendtube_DS],
        [z2_DSendtube_DS, x2_DSendtube_DS],
    ),
    notSource=False,
)

DSendtube_DS_bot = polygon(
    (
        [z1_DSendtube_DS, -x1_DSendtube_DS],
        [z4_DSendtube_DS, -x4_DSendtube_DS],
        [z3_DSendtube_DS, -x3_DSendtube_DS],
        [z2_DSendtube_DS, -x2_DSendtube_DS],
    ),
    notSource=False,
)

#US flange (DSendtube_USflange). Should be 3 segments of varying height, but this is fine
x1_DSendtube_USflange = 0.67247 
z1_DSendtube_USflange = 16.75827

x2_DSendtube_USflange = 0.79947
z2_DSendtube_USflange = 16.75827

x3_DSendtube_USflange = 0.79947
z3_DSendtube_USflange = 16.75827 + 0.04445

x4_DSendtube_USflange = 0.67247  
z4_DSendtube_USflange = 16.75827 + 0.04445

DSendtube_USflange_top = polygon(
    (
        [z1_DSendtube_USflange, x1_DSendtube_USflange],
        [z4_DSendtube_USflange, x4_DSendtube_USflange],
        [z3_DSendtube_USflange, x3_DSendtube_USflange],
        [z2_DSendtube_USflange, x2_DSendtube_USflange],
    ),
    notSource=False,
)

DSendtube_USflange_bot = polygon(
    (
        [z1_DSendtube_USflange, -x1_DSendtube_USflange],
        [z4_DSendtube_USflange, -x4_DSendtube_USflange],
        [z3_DSendtube_USflange, -x3_DSendtube_USflange],
        [z2_DSendtube_USflange, -x2_DSendtube_USflange],
    ),
    notSource=False,
)

#DS flange (DSendtube_DSflange). Should be 3 segments of varying height, but this is fine
x1_DSendtube_DSflange = 0.67247 
z1_DSendtube_DSflange = 17.18916 - 0.04445

x2_DSendtube_DSflange = 0.79947
z2_DSendtube_DSflange = 17.18916 - 0.04445

x3_DSendtube_DSflange = 0.79947
z3_DSendtube_DSflange = 17.18916

x4_DSendtube_DSflange = 0.67247  
z4_DSendtube_DSflange = 17.18916

DSendtube_DSflange_top = polygon(
    (
        [z1_DSendtube_DSflange, x1_DSendtube_DSflange],
        [z4_DSendtube_DSflange, x4_DSendtube_DSflange],
        [z3_DSendtube_DSflange, x3_DSendtube_DSflange],
        [z2_DSendtube_DSflange, x2_DSendtube_DSflange],
    ),
    notSource=False,
)

DSendtube_DSflange_bot = polygon(
    (
        [z1_DSendtube_DSflange, -x1_DSendtube_DSflange],
        [z4_DSendtube_DSflange, -x4_DSendtube_DSflange],
        [z3_DSendtube_DSflange, -x3_DSendtube_DSflange],
        [z2_DSendtube_DSflange, -x2_DSendtube_DSflange],
    ),
    notSource=False,
)

#LowCycleBellows_flanges 

x1_lowcyclebellows_flange = 0.67587 
z1_lowcyclebellows_flange = 16.80272

x2_lowcyclebellows_flange = 0.79947
z2_lowcyclebellows_flange = 16.80272

x3_lowcyclebellows_flange = 0.79947
z3_lowcyclebellows_flange = 16.80272 + 0.03175

x4_lowcyclebellows_flange = 0.67587 
z4_lowcyclebellows_flange = 16.80272 + 0.03175

LowCycleBellows_flangeUS_top = polygon(
    (
        [z1_lowcyclebellows_flange, x1_lowcyclebellows_flange],
        [z4_lowcyclebellows_flange, x4_lowcyclebellows_flange],
        [z3_lowcyclebellows_flange, x3_lowcyclebellows_flange],
        [z2_lowcyclebellows_flange, x2_lowcyclebellows_flange],
    ),
    notSource=False,
)

LowCycleBellows_flangeUS_bot = polygon(
    (
        [z1_lowcyclebellows_flange, -x1_lowcyclebellows_flange],
        [z4_lowcyclebellows_flange, -x4_lowcyclebellows_flange],
        [z3_lowcyclebellows_flange, -x3_lowcyclebellows_flange],
        [z2_lowcyclebellows_flange, -x2_lowcyclebellows_flange],
    ),
    notSource=False,
)

LowCycleBellows_flangeDS_top = polygon(
    (
        [z1_lowcyclebellows_flange+0.31115, x1_lowcyclebellows_flange],
        [z4_lowcyclebellows_flange+0.31115, x4_lowcyclebellows_flange],
        [z3_lowcyclebellows_flange+0.31115, x3_lowcyclebellows_flange],
        [z2_lowcyclebellows_flange+0.31115, x2_lowcyclebellows_flange],
    ),
    notSource=False,
)

LowCycleBellows_flangeDS_bot = polygon(
    (
        [z1_lowcyclebellows_flange+0.31115, -x1_lowcyclebellows_flange],
        [z4_lowcyclebellows_flange+0.31115, -x4_lowcyclebellows_flange],
        [z3_lowcyclebellows_flange+0.31115, -x3_lowcyclebellows_flange],
        [z2_lowcyclebellows_flange+0.31115, -x2_lowcyclebellows_flange],
    ),
    notSource=False,
)

#LowCycleBellows (Approximated as 3 segments without loss. Is 9 in remoll)

#seg 1
x1_lowcyclebellows1 = 0.67247
z1_lowcyclebellows1 = 16.80272 + .00330

x2_lowcyclebellows1 = 0.75197
z2_lowcyclebellows1 = 16.80272 + .00330

x3_lowcyclebellows1 = 0.75197
z3_lowcyclebellows1 = 16.80272 + .00330 + 0.08890

x4_lowcyclebellows1 = 0.67247
z4_lowcyclebellows1 = 16.80272 + .00330 + 0.08890

LowCycleBellows_seg1_top = polygon(
    (
        [z1_lowcyclebellows1, x1_lowcyclebellows1],
        [z4_lowcyclebellows1, x4_lowcyclebellows1],
        [z3_lowcyclebellows1, x3_lowcyclebellows1],
        [z2_lowcyclebellows1, x2_lowcyclebellows1],
    ),
    notSource=False,
)

LowCycleBellows_seg1_bot = polygon(
    (
        [z1_lowcyclebellows1, -x1_lowcyclebellows1],
        [z4_lowcyclebellows1, -x4_lowcyclebellows1],
        [z3_lowcyclebellows1, -x3_lowcyclebellows1],
        [z2_lowcyclebellows1, -x2_lowcyclebellows1],
    ),
    notSource=False,
)

#seg 2
x1_lowcyclebellows2 = 0.74867
z1_lowcyclebellows2 = 16.80272 + .00330 + 0.08890

x2_lowcyclebellows2 = 0.75197
z2_lowcyclebellows2 = 16.80272 + .00330 + 0.08890

x3_lowcyclebellows2 = 0.75197
z3_lowcyclebellows2 = 16.80272 + 0.08890 + 0.15545

x4_lowcyclebellows2 = 0.74867
z4_lowcyclebellows2 = 16.80272 + 0.08890 + 0.15545

LowCycleBellows_seg2_top = polygon(
    (
        [z1_lowcyclebellows2, x1_lowcyclebellows2],
        [z4_lowcyclebellows2, x4_lowcyclebellows2],
        [z3_lowcyclebellows2, x3_lowcyclebellows2],
        [z2_lowcyclebellows2, x2_lowcyclebellows2],
    ),
    notSource=False,
)

LowCycleBellows_seg2_bot = polygon(
    (
        [z1_lowcyclebellows2, -x1_lowcyclebellows2],
        [z4_lowcyclebellows2, -x4_lowcyclebellows2],
        [z3_lowcyclebellows2, -x3_lowcyclebellows2],
        [z2_lowcyclebellows2, -x2_lowcyclebellows2],
    ),
    notSource=False,
)

#seg 3
x1_lowcyclebellows3 = 0.67247
z1_lowcyclebellows3 = 16.80272 + 0.08890 + 0.15545

x2_lowcyclebellows3 = 0.75197
z2_lowcyclebellows3 = 16.80272 + 0.08890 + 0.15545

x3_lowcyclebellows3 = 0.75197
z3_lowcyclebellows3 = 16.80272 + 0.08890 + 0.15545 + 0.00330 + 0.09220

x4_lowcyclebellows3 = 0.67247
z4_lowcyclebellows3 = 16.80272 + 0.08890 + 0.15545 + 0.00330 + 0.09220

LowCycleBellows_seg3_top = polygon(
    (
        [z1_lowcyclebellows3, x1_lowcyclebellows3],
        [z4_lowcyclebellows3, x4_lowcyclebellows3],
        [z3_lowcyclebellows3, x3_lowcyclebellows3],
        [z2_lowcyclebellows3, x2_lowcyclebellows3],
    ),
    notSource=False,
)

LowCycleBellows_seg3_bot = polygon(
    (
        [z1_lowcyclebellows3, -x1_lowcyclebellows3],
        [z4_lowcyclebellows3, -x4_lowcyclebellows3],
        [z3_lowcyclebellows3, -x3_lowcyclebellows3],
        [z2_lowcyclebellows3, -x2_lowcyclebellows3],
    ),
    notSource=False,
)

#DSpipe (near Barite_Collar2)

#DSpipe_flange (shape highly approximated)
x1_DSpipeflange = 0.50190
z1_DSpipeflange = 23.08967 - 0.00025 - 0.07849

x2_DSpipeflange = 0.50191
z2_DSpipeflange = 23.08967 - 0.00025 - 0.07849

x3_DSpipeflange = 0.50470
z3_DSpipeflange = 23.08967 - 0.00025

x4_DSpipeflange = 0.50013
z4_DSpipeflange = 23.08967 - 0.00025

DSpipeflange_top = polygon(
    (
        [z1_DSpipeflange, x1_DSpipeflange],
        [z4_DSpipeflange, x4_DSpipeflange],
        [z3_DSpipeflange, x3_DSpipeflange],
        [z2_DSpipeflange, x2_DSpipeflange],
    ),
    notSource=False,
)

DSpipeflange_bot = polygon(
    (
        [z1_DSpipeflange, -x1_DSpipeflange],
        [z4_DSpipeflange, -x4_DSpipeflange],
        [z3_DSpipeflange, -x3_DSpipeflange],
        [z2_DSpipeflange, -x2_DSpipeflange],
    ),
    notSource=False,
)

#DSpipe1
x1_DSpipe1 = 0.50013
z1_DSpipe1 = 23.08967

x2_DSpipe1 = 0.50470
z2_DSpipe1 = 23.08967

x3_DSpipe1 = 0.50470
z3_DSpipe1 = 23.08967 + 0.14910

x4_DSpipe1 = 0.50013
z4_DSpipe1 = 23.08967 + 0.14910

DSpipe1_top = polygon(
    (
        [z1_DSpipe1, x1_DSpipe1],
        [z4_DSpipe1, x4_DSpipe1],
        [z3_DSpipe1, x3_DSpipe1],
        [z2_DSpipe1, x2_DSpipe1],
    ),
    notSource=False,
)

DSpipe1_bot = polygon(
    (
        [z1_DSpipe1, -x1_DSpipe1],
        [z4_DSpipe1, -x4_DSpipe1],
        [z3_DSpipe1, -x3_DSpipe1],
        [z2_DSpipe1, -x2_DSpipe1],
    ),
    notSource=False,
)

#DSpipe_vacuumtube_phys

#DSpipe1_bellow
x1_DSpipe1_bellow = 0.50000
z1_DSpipe1_bellow = 23.57162

x2_DSpipe1_bellow = 0.52900
z2_DSpipe1_bellow = 23.57162

x3_DSpipe1_bellow = 0.52976
z3_DSpipe1_bellow = 23.57162 + 0.18000

x4_DSpipe1_bellow = 0.50076
z4_DSpipe1_bellow = 23.57162 + 0.18000

DSpipe1_bellow_top = polygon(
    (
        [z1_DSpipe1_bellow, x1_DSpipe1_bellow],
        [z4_DSpipe1_bellow, x4_DSpipe1_bellow],
        [z3_DSpipe1_bellow, x3_DSpipe1_bellow],
        [z2_DSpipe1_bellow, x2_DSpipe1_bellow],
    ),
    notSource=False,
)

DSpipe1_bellow_bot = polygon(
    (
        [z1_DSpipe1_bellow, -x1_DSpipe1_bellow],
        [z4_DSpipe1_bellow, -x4_DSpipe1_bellow],
        [z3_DSpipe1_bellow, -x3_DSpipe1_bellow],
        [z2_DSpipe1_bellow, -x2_DSpipe1_bellow],
    ),
    notSource=False,
)

#DSpipe1_flange (approximate shape)
x1_DSpipe1_flange = 0.49700
z1_DSpipe1_flange = 23.57162 - 0.025

x2_DSpipe1_flange = 0.49950
z2_DSpipe1_flange = 23.57162 - 0.025

x3_DSpipe1_flange = 0.52900
z3_DSpipe1_flange = 23.57162

x4_DSpipe1_flange = 0.49700
z4_DSpipe1_flange = 23.57162

DSpipe1_flange_top = polygon(
    (
        [z1_DSpipe1_flange, x1_DSpipe1_flange],
        [z4_DSpipe1_flange, x4_DSpipe1_flange],
        [z3_DSpipe1_flange, x3_DSpipe1_flange],
        [z2_DSpipe1_flange, x2_DSpipe1_flange],
    ),
    notSource=False,
)

DSpipe1_flange_bot = polygon(
    (
        [z1_DSpipe1_flange, -x1_DSpipe1_flange],
        [z4_DSpipe1_flange, -x4_DSpipe1_flange],
        [z3_DSpipe1_flange, -x3_DSpipe1_flange],
        [z2_DSpipe1_flange, -x2_DSpipe1_flange],
    ),
    notSource=False,
)

#DSpipe2_USplate (approximate shape)
x1_DSpipe2_US = 0.50076
z1_DSpipe2_US = 23.75162

x2_DSpipe2_US = 0.52975
z2_DSpipe2_US = 23.75162

x3_DSpipe2_US = 0.50493
z3_DSpipe2_US = 23.75162 + 0.025

x4_DSpipe2_US = 0.50160
z4_DSpipe2_US = 23.75162 + 0.025

DSpipe2_US_top = polygon(
    (
        [z1_DSpipe2_US, x1_DSpipe2_US],
        [z4_DSpipe2_US, x4_DSpipe2_US],
        [z3_DSpipe2_US, x3_DSpipe2_US],
        [z2_DSpipe2_US, x2_DSpipe2_US],
    ),
    notSource=False,
)

DSpipe2_US_bot = polygon(
    (
        [z1_DSpipe2_US, -x1_DSpipe2_US],
        [z4_DSpipe2_US, -x4_DSpipe2_US],
        [z3_DSpipe2_US, -x3_DSpipe2_US],
        [z2_DSpipe2_US, -x2_DSpipe2_US],
    ),
    notSource=False,
)

#DSpipe2_DSpipe2_1 (actual name)
x1_DSpipe2_DS = 0.50478
z1_DSpipe2_DS = 23.77662

x2_DSpipe2_DS = 0.50954
z2_DSpipe2_DS = 23.77662

x3_DSpipe2_DS = 0.51088
z3_DSpipe2_DS = 23.77662 + 0.03093

x4_DSpipe2_DS = 0.50612
z4_DSpipe2_DS = 23.77662 + 0.03093

DSpipe2_DS_top = polygon(
    (
        [z1_DSpipe2_DS, x1_DSpipe2_DS],
        [z4_DSpipe2_DS, x4_DSpipe2_DS],
        [z3_DSpipe2_DS, x3_DSpipe2_DS],
        [z2_DSpipe2_DS, x2_DSpipe2_DS],
    ),
    notSource=False,
)

DSpipe2_DS_bot = polygon(
    (
        [z1_DSpipe2_DS, -x1_DSpipe2_DS],
        [z4_DSpipe2_DS, -x4_DSpipe2_DS],
        [z3_DSpipe2_DS, -x3_DSpipe2_DS],
        [z2_DSpipe2_DS, -x2_DSpipe2_DS],
    ),
    notSource=False,
)

#DSpipe3 (just DSpipe3_DSpipe)

x1_DSpipe3 = 0.52170
z1_DSpipe3 = 23.91538

x2_DSpipe3 = 0.52805
z2_DSpipe3 = 23.91538

x3_DSpipe3 = 0.69550
z3_DSpipe3 = 29.97204

x4_DSpipe3 = 0.67645
z4_DSpipe3 = 29.97204

DSpipe3_top = polygon(
    (
        [z1_DSpipe3, x1_DSpipe3],
        [z4_DSpipe3, x4_DSpipe3],
        [z3_DSpipe3, x3_DSpipe3],
        [z2_DSpipe3, x2_DSpipe3],
    ),
    notSource=False,
)

DSpipe3_bot = polygon(
    (
        [z1_DSpipe3, -x1_DSpipe3],
        [z4_DSpipe3, -x4_DSpipe3],
        [z3_DSpipe3, -x3_DSpipe3],
        [z2_DSpipe3, -x2_DSpipe3],
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

allpolys.append(collimator4_seg1)
allpolys.append(collimator4_seg2)
allpolys.append(collimator4_seg3)
allpolys.append(collimator4_seg4)

allpolys.append(US_Pbwall_seg1_top)
allpolys.append(US_Pbwall_seg1_bottom)
allpolys.append(US_Pbwall_seg2_top)
allpolys.append(US_Pbwall_seg2_bottom)
allpolys.append(US_Pbwall_seg3_top)
allpolys.append(US_Pbwall_seg3_bottom)

allpolys.append(upstream_enclosure_DSpipe_top)
allpolys.append(upstream_enclosure_DSpipe_bottom)
allpolys.append(upstream_enclosure_DSpipe_flange_top)
allpolys.append(upstream_enclosure_DSpipe_flange_bottom)

allpolys.append(collar_top1)
allpolys.append(collar_bottom1)

allpolys.append(collar2_inner_top)
allpolys.append(collar2_inner_bottom)
allpolys.append(collar2_outer_top)
allpolys.append(collar2_outer_bottom)

allpolys.append(DSCAN_Front_up)
allpolys.append(DSCAN_Front_low)

allpolys.append(DSCAN_Top)
allpolys.append(DSCAN_Bot)

allpolys.append(DSCAN_Back_up_1)
allpolys.append(DSCAN_Back_up_2)
allpolys.append(DSCAN_Back_up_3)
allpolys.append(DSCAN_Back_low_1)
allpolys.append(DSCAN_Back_low_2)
allpolys.append(DSCAN_Back_low_3)

allpolys.append(Scaper_11)
allpolys.append(Scaper_12)

allpolys.append(coll_5)
allpolys.append(coll_51)
allpolys.append(lintel)

allpolys.append(Col6A_1)
allpolys.append(Col6A_2)
allpolys.append(Col6B_1)
allpolys.append(Col6B_2)

allpolys.append(DS_Coil1)
allpolys.append(DS_Coil2)
allpolys.append(DS_Coil3)
allpolys.append(DS_Coil4_1)
allpolys.append(DS_Coil4_2)
allpolys.append(DS_Coil4_3)

allpolys.append(Solid_epoxy_1)
allpolys.append(Solid_epoxy_2)
allpolys.append(Solid_epoxy_3)
allpolys.append(Solid_epoxy_5)

allpolys.append(DSendtube_US_top)
allpolys.append(DSendtube_US_bot)
allpolys.append(DSendtube_DS_top)
allpolys.append(DSendtube_DS_bot)

allpolys.append(DSendtube_USflange_top)
allpolys.append(DSendtube_USflange_bot)
allpolys.append(DSendtube_DSflange_top)
allpolys.append(DSendtube_DSflange_bot)

allpolys.append(LowCycleBellows_flangeUS_top)
allpolys.append(LowCycleBellows_flangeUS_bot)
allpolys.append(LowCycleBellows_flangeDS_top)
allpolys.append(LowCycleBellows_flangeDS_bot)
allpolys.append(LowCycleBellows_seg1_top)
allpolys.append(LowCycleBellows_seg1_bot)
allpolys.append(LowCycleBellows_seg2_top)
allpolys.append(LowCycleBellows_seg2_bot)
allpolys.append(LowCycleBellows_seg3_top)
allpolys.append(LowCycleBellows_seg3_bot)

allpolys.append(Drift_wall_top)
allpolys.append(Drift_wall_bottom)
allpolys.append(Drift_body_top)
allpolys.append(Drift_body_bottom)

allpolys.append(Drift_vac_top)
allpolys.append(Drift_vac_bot)
allpolys.append(DS_window_flange_top)
allpolys.append(DS_window_flange_bot)
allpolys.append(DSpipe1_top)
allpolys.append(DSpipe1_bot)
allpolys.append(DSpipeflange_top)
allpolys.append(DSpipeflange_bot)
allpolys.append(DSpipe1_flange_top)
allpolys.append(DSpipe1_flange_bot)
allpolys.append(DSpipe1_bellow_top)
allpolys.append(DSpipe1_bellow_bot)
allpolys.append(DSpipe2_US_top)
allpolys.append(DSpipe2_DS_bot)
allpolys.append(DSpipe2_US_top)
allpolys.append(DSpipe2_DS_bot)

allpolys.append(DSpipe3_top)
allpolys.append(DSpipe3_bot)

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
