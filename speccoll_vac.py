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
z3 = -1310*mm-tgtpos  

x4 = 149.23*mm 
z4 = -1310*mm-tgtpos

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
#flangeUScollar0
x1 = 149.23*mm 
z1 = -1310*mm-tgtpos
x2 = 184.15*mm  
z2 = -1310*mm-tgtpos
x3 = 184.15*mm 
z3 = -1300.66*mm-tgtpos  
x4 = 152.4*mm 
z4 = -1300.66*mm-tgtpos
x5 = 152.4*mm 
z5 = -1293.67*mm-tgtpos  
x6 = 149.23*mm 
z6 = -1293.67*mm-tgtpos

pipeflange_UScollar0_top = polygon(
    (
        [z1, x1],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)
pipeflange_UScollar0_bottom = polygon(
    (
        [z1, -x1],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
        
    ),
    notSource=False,
    isConcave=True,
)

#beampipeUScollar0
x1 = 146.05*mm 
z1 = -1293.67*mm-tgtpos
x2 = 152.4*mm  
z2 = -1293.67*mm-tgtpos
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
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
        
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
#beampipeDScollar0
x1 = 146.05*mm 
z1 = -1000*mm-tgtpos
x2 = 152.4*mm  
z2 = -1000*mm-tgtpos
x3 = 152.4*mm 
z3 = -885.648*mm-tgtpos  
x4 = 184.15*mm 
z4 = -885.648*mm-tgtpos
x5 = 184.15*mm 
z5 = -856.439*mm-tgtpos  
x6 = 146.05*mm 
z6 = -856.439*mm-tgtpos

pipe_DScollar0_top = polygon(
    (
        [z1, x1],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)
pipe_DScollar0_bottom = polygon(
    (
        [z1, -x1],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
        
    ),
    notSource=False,
    isConcave=True,
)

### Flange upstream of bellows 2 (bellows2USflange)
x1 = 149.23*mm 
z1 = -856.439*mm-tgtpos
x2 = 184.15*mm  
z2 = -856.439*mm-tgtpos
x3 = 184.15*mm 
z3 = -828.63*mm-tgtpos  
x4 = 152.4*mm 
z4 = -828.63*mm-tgtpos
x5 = 152.4*mm 
z5 = -831.17*mm-tgtpos  
x6 = 149.23*mm 
z6 = -831.17*mm-tgtpos

bellows2_USflange_top = polygon(
    (
        [z1, x1],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)
bellows2_USflange_bot = polygon(
    (
        [z1, -x1],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
    isConcave=True,
)

### bellows 2 (bellows2)
x1 = 149.23*mm 
z1 = -831.17*mm-tgtpos
x2 = 152.40*mm  
z2 = -831.17*mm-tgtpos
x3 = 152.40*mm 
z3 = -773.05*mm-tgtpos  
x4 = 190.5*mm 
z4 = -773.05*mm-tgtpos
x5 = 190.5*mm 
z5 = -484.15*mm-tgtpos
x6 = 152.40*mm  
z6 = -484.15*mm-tgtpos
x7 = 152.40*mm 
z7 = -424.51*mm-tgtpos  
x8 = 149.23*mm 
z8 = -424.51*mm-tgtpos

bellows2_top = polygon(
    (
        [z1, x1],
        [z8, x8],
        [z7, x7],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)
bellows2_bot = polygon(
    (
        [z1, -x1],
        [z8, -x8],
        [z7, -x7],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
    isConcave=True,
)

### bellows 2 DSflange (bellows2DSflange)
x1 = 152.4*mm 
z1 = -428.58*mm-tgtpos
x2 = 184.15*mm  
z2 = -428.58*mm-tgtpos
x3 = 184.15*mm 
z3 = -400.05*mm-tgtpos  
x4 = 149.23*mm 
z4 = -400.05*mm-tgtpos
x5 = 149.23*mm 
z5 = -424.51*mm-tgtpos  
x6 = 152.4*mm 
z6 = -424.51*mm-tgtpos

bellows2_DSflange_top = polygon(
    (
        [z1, x1],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)
bellows2_DSflange_bot = polygon(
    (
        [z1, -x1],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
    isConcave=True,
)

###  Upstream Enclosure US pipe
x1 = 149.225*mm 
z1 = -400.05*mm-tgtpos
x2 = 184.15*mm  
z2 = -400.05*mm-tgtpos
x3 = 184.15*mm 
z3 = -371.475*mm-tgtpos  
x4 = 152.4*mm 
z4 = -371.475*mm-tgtpos
x5 = 152.4*mm 
z5 = -367.665*mm-tgtpos
x6 = 155.575*mm  
z6 = -367.665*mm-tgtpos
x7 = 155.575*mm 
z7 = -204.597*mm-tgtpos  
x8 = 149.225*mm 
z8 = -204.597*mm-tgtpos

upstream_enclosure_USpipe_top = polygon(
    (
        [z1, x1],
        [z8, x8],
        [z7, x7],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)
upstream_enclosure_USpipe_bottom = polygon(
    (
        [z1, -x1],
        [z8, -x8],
        [z7, -x7],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
    isConcave=True,
)

###  Upstream Enclosure US Wall (EnclosureFront_US)
x1 = 155.575*mm 
z1 = (-204.597-50.8)*mm-tgtpos

x2 = 552.45*mm    
z2 = (-204.597-50.8)*mm-tgtpos

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
upstream_enclosure_USwall_bottom = polygon(
    (
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
)

###  Upstream Enclosure Side Wall 
x1 = (1104.9/2.0-25.4)*mm
z1 = -204.597*mm-tgtpos

x2 = 552.45*mm    
z2 = -204.597*mm-tgtpos

x3 = 552.45*mm 
z3 = 3592.703*mm-tgtpos  

x4 = (1104.9/2.0-25.4)*mm 
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
z3 = (3592.703+50.8)*mm-tgtpos  

x4 = 344.488*mm 
z4 = (3592.703+50.8)*mm-tgtpos

upstream_enclosure_DSwall_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)

upstream_enclosure_DSwall_bottom = polygon(
    (
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
)

### Collimator 1

#UScoll_1
x1 = 0.020300
z1 = 325*mm-tgtpos
x2 = 0.025400
z2 = 325*mm-tgtpos
x3 = 0.025400
z3 = 365*mm-tgtpos
x4 = 0.022000
z4 = 365*mm-tgtpos
x5 = 0.022000
z5 = 870*mm-tgtpos
x6 = 0.024000
z6 = 870*mm-tgtpos
x7 = 0.024000
z7 = 885*mm-tgtpos
x8 = 0.022000
z8 = 885*mm-tgtpos
x9 = 0.022000
z9 = 900*mm-tgtpos
x10 = 0.014536
z10 = 900*mm-tgtpos
x11 = 0.014427
z11 = 870*mm-tgtpos
x12 = 0.013900
z12 = 725*mm-tgtpos
x13 = 0.014400
z13 = 635*mm-tgtpos
x14 = 0.015400
z14 = 515*mm-tgtpos
x15 = 0.016550
z15 = 425*mm-tgtpos
x16 = 0.018800
z16 = 365*mm-tgtpos
x17 = 0.018875
z17 = 355*mm-tgtpos

col1_top = polygon(
    (
        [z1, x1],
        [z17, x17],
        [z16, x16],
        [z15, x15],
        [z14, x14],
        [z13, x13],
        [z12, x12],
        [z11, x11],
        [z10, x10],
        [z9, x9],
        [z8, x8],
        [z7, x7],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)

col1_bot = polygon(
    (
        [z1, -x1],
        [z17, -x17],
        [z16, -x16],
        [z15, -x15],
        [z14, -x14],
        [z13, -x13],
        [z12, -x12],
        [z11, -x11],
        [z10, -x10],
        [z9, -x9],
        [z8, -x8],
        [z7, -x7],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
    isConcave=True,
)

#col1_h20_phys1
x1_h20_1 = 0.02200
z1_h20_1 = 365*mm-tgtpos
x2_h20_1 = 0.02540
z2_h20_1 = 365*mm-tgtpos
x3_h20_1 = 0.02540
z3_h20_1 = 365*mm-tgtpos + 20*mm
x4_h20_1 = 0.02200
z4_h20_1 = 365*mm-tgtpos + 20*mm

col1_h20_1_top = polygon(
    (
        [z1_h20_1, x1_h20_1],
        [z4_h20_1, x4_h20_1],
        [z3_h20_1, x3_h20_1],
        [z2_h20_1, x2_h20_1],
    ),
    notSource=False,
)

col1_h20_1_bot = polygon(
    (
        [z1_h20_1, -x1_h20_1],
        [z4_h20_1, -x4_h20_1],
        [z3_h20_1, -x3_h20_1],
        [z2_h20_1, -x2_h20_1],
    ),
    notSource=False,
)

#col1_h20_phys2
x1_h20_2 = 0.02200
z1_h20_2 = 850*mm-tgtpos
x2_h20_2 = 0.02540
z2_h20_2 = 850*mm-tgtpos
x3_h20_2 = 0.02540
z3_h20_2 = 880*mm-tgtpos
x4_h20_2 = 0.02400
z4_h20_2 = 880*mm-tgtpos
x5_h20_2 = 0.02400
z5_h20_2 = 870*mm-tgtpos
x6_h20_2 = 0.02200
z6_h20_2 = 870*mm-tgtpos

col1_h20_2_top = polygon(
    (
        [z1_h20_2, x1_h20_2],
        [z6_h20_2, x6_h20_2],
        [z5_h20_2, x5_h20_2],
        [z4_h20_2, x4_h20_2],
        [z3_h20_2, x3_h20_2],
        [z2_h20_2, x2_h20_2],
    ),
    notSource=False,
    isConcave=True,
)

col1_h20_2_bot = polygon(
    (
        [z1_h20_2, -x1_h20_2],
        [z6_h20_2, -x6_h20_2],
        [z5_h20_2, -x5_h20_2],
        [z4_h20_2, -x4_h20_2],
        [z3_h20_2, -x3_h20_2],
        [z2_h20_2, -x2_h20_2],
    ),
    notSource=False,
    isConcave=True,
)

#col1_h20_CW
x1_h20_CW = 0.02200
z1_h20_CW = 375*mm-tgtpos
x2_h20_CW = 0.02540
z2_h20_CW = 375*mm-tgtpos
x3_h20_CW = 0.02540
z3_h20_CW = 375*mm-tgtpos + 465*mm
x4_h20_CW = 0.02200
z4_h20_CW = 375*mm-tgtpos + 465*mm

col1_h20_CW_top = polygon(
    (
        [z1_h20_CW, x1_h20_CW],
        [z4_h20_CW, x4_h20_CW],
        [z3_h20_CW, x3_h20_CW],
        [z2_h20_CW, x2_h20_CW],
    ),
    notSource=False,
)

col1_h20_CW_bot = polygon(
    (
        [z1_h20_CW, -x1_h20_CW],
        [z4_h20_CW, -x4_h20_CW],
        [z3_h20_CW, -x3_h20_CW],
        [z2_h20_CW, -x2_h20_CW],
    ),
    notSource=False,
)

#col1_jacket
x1_jack = 0.02540
z1_jack = 325*mm-tgtpos
x2_jack = 0.02950
z2_jack = 325*mm-tgtpos
x3_jack = 0.03050
z3_jack = 750*mm-tgtpos
x4_jack = 0.02730
z4_jack = 750*mm-tgtpos
x5_jack = 0.02730
z5_jack = 800*mm-tgtpos
x6_jack = 0.02540
z6_jack = 800*mm-tgtpos

col1_jacket_top = polygon(
    (
        [z1_jack, x1_jack],
        [z6_jack, x6_jack],
        [z5_jack, x5_jack],
        [z4_jack, x4_jack],
        [z3_jack, x3_jack],
        [z2_jack, x2_jack],
    ),
    notSource=False,
    isConcave=True,
)

col1_jacket_bot = polygon(
    (
        [z1_jack, -x1_jack],
        [z6_jack, -x6_jack],
        [z5_jack, -x5_jack],
        [z4_jack, -x4_jack],
        [z3_jack, -x3_jack],
        [z2_jack, -x2_jack],
    ),
    notSource=False,
    isConcave=True,
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

#PbWall_1
x1=230*mm
z1=3541.903*mm-tgtpos
x2=406.4*mm
z2=3541.903*mm-tgtpos
x3=406.4*mm
z3=3592.703*mm-tgtpos
x4=330.2*mm
z4=3592.703*mm-tgtpos
x5=330.2*mm
z5=3694.303*mm-tgtpos
x6=230*mm
z6=3694.303*mm-tgtpos

US_Pbwall1_top = polygon(
    (
        [z1, x1],
        [z6, x6],
        [z5, x5],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
    isConcave=True,
)
US_Pbwall1_bot = polygon(
    (
        [z1, -x1],
        [z6, -x6],
        [z5, -x5],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
    isConcave=True,
)

#PbWall_2
x1=344.388*mm
z1=(3592.703+50.8)*mm-tgtpos
x2=533.4*mm
z2=(3592.703+50.8)*mm-tgtpos
x3=533.4*mm
z3=(3592.703+50.8+101.6)*mm-tgtpos
x4=344.488*mm
z4=(3592.703+50.8+101.6)*mm-tgtpos

US_Pbwall2_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
US_Pbwall2_bot = polygon(
    (
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
)

#Bellows 3 
#bellows3physical
x1 = 330.175*mm
z1 = 4226.3*mm-tgtpos
x2 = 361.175*mm
z2 = 4226.3*mm-tgtpos
x3 = 361.175*mm
z3 = 4645.7*mm-tgtpos
x4 = 330.175*mm
z4 = 4645.7*mm-tgtpos

bellows3_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows3_bot = polygon(
    (
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
)

#bellows3flangeUS
x1 = 330.175*mm
z1 = 4181.85*mm-tgtpos
x2 = 418.125*mm
z2 = 4181.85*mm-tgtpos
x3 = 418.125*mm
z3 = 4225.95*mm-tgtpos
x4 = 330.175*mm
z4 = 4225.95*mm-tgtpos

bellows3flangeUS_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows3flangeUS_bot = polygon(
    (
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
)

#bellows3flangeDS
x1 = 330.175*mm
z1 = 4646.05*mm-tgtpos
x2 = 418.125*mm
z2 = 4646.05*mm-tgtpos
x3 = 418.125*mm
z3 = 4690.15*mm-tgtpos
x4 = 330.175*mm
z4 = 4690.15*mm-tgtpos

bellows3flangeDS_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    ),
    notSource=False,
)
bellows3flangeDS_bot = polygon(
    (
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    ),
    notSource=False,
)

### Pipe downstream of upstream enclosure before bellows 3
#This part seems to not exist in remoll
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
#This part seems to not exist in remoll
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

#Photon blocker (formerly photon scaper)
#PhotonBlocker_phys2
x1 = 40*mm
z1 = 9207.5*mm
x2 = 61.968*mm
z2 = 9207.5*mm
x3 = 61.968*mm
z3 = 9309.1*mm
x4 = 40*mm
z4 = 9309.1*mm

Blocker_ring_top = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    )
)
Blocker_ring_bot = polygon(
    (
        [z1, -x1],
        [z4, -x4],
        [z3, -x3],
        [z2, -x2],
    )
)

#PhotonBlocker_phys1_ & PhotonBlocker_phys2_
x1 = 61.968*mm
z1 = 9207.5*mm
x2 = 140.11*mm
z2 = 9207.5*mm
x3 = 140.11*mm
z3 = 9309.1*mm
x4 = 61.968*mm
z4 = 9309.1*mm

Blocker_12 = polygon(
    (
        [z1, x1],
        [z4, x4],
        [z3, x3],
        [z2, x2],
    )
)

##Photon scaper (depricated)
##+ve y-direction 
x1_Scaper_1 = 40*mm
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

##-ve y-direction (Just a portion of phys2)
x1_Scaper_2 = 40*mm
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
z2_coll_5 = 12.057824

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
z2_coll_51 = 12.170549

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
#Lintel_s1 and Lintel_s2 can be generalized as one lintel at y=0

x1_lintel = -0.48485
z1_lintel = 9.64399 + 4.5

x2_lintel = -0.80685
z2_lintel = 9.64399 + 4.5

x3_lintel = -0.80685
z3_lintel = 9.74399 + 4.5

x4_lintel = -0.48485
z4_lintel = 9.74399 + 4.5


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
#Shifting up by 3 mm (verify in future)
x1_DS_coil2 = 0.04353 + 0.003
z1_DS_coil2 = 5.94774 + 4.5

x2_DS_coil2 = 0.21424 + 0.003
z2_DS_coil2 = 5.94774 + 4.5

x3_DS_coil2 = 0.238 + 0.003
z3_DS_coil2 = 6.97179 + 4.5

x4_DS_coil2 = 0.04353 + 0.003
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
#Shifting up by 3 mm (verify in future)
x1_DS_coil3 = 0.04642 + 0.003
z1_DS_coil3 = 6.98652 + 4.5

x2_DS_coil3 = 0.26058 + 0.003
z2_DS_coil3 = 6.98652 + 4.5

x3_DS_coil3 = 0.27708 + 0.003
z3_DS_coil3 = 7.96320 + 4.5

x4_DS_coil3 = 0.04642 + 0.003
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
z1_solid_epoxy_1 = 4.933935 + 4.5

x2_solid_epoxy_1 = 0.041
z2_solid_epoxy_1 = 4.933935 + 4.5

x3_solid_epoxy_1 = 0.041
z3_solid_epoxy_1 = 4.933935 + 1.002241 + 4.5

x4_solid_epoxy_1 = 0.038
z4_solid_epoxy_1 = 4.933935 + 1.002241 + 4.5

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
z1_solid_epoxy_2 = 5.950606 + 4.5

x2_solid_epoxy_2 = 0.0465
z2_solid_epoxy_2 = 5.950606 + 4.5

x3_solid_epoxy_2 = 0.0465
z3_solid_epoxy_2 = 5.950606 + 1.022596 + 4.5

x4_solid_epoxy_2 = 0.0435
z4_solid_epoxy_2 = 5.950606 + 1.022596 + 4.5

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
z1_solid_epoxy_3 = 6.98673 + 4.5

x2_solid_epoxy_3 = 0.049
z2_solid_epoxy_3 = 6.98673 + 4.5

x3_solid_epoxy_3 = 0.049
z3_solid_epoxy_3 = 6.98673 + 0.51327 + 0.460415 + 4.5

x4_solid_epoxy_3 = 0.046
z4_solid_epoxy_3 = 6.98673 + 0.51327 + 0.460415 + 4.5

Solid_epoxy_3 = polygon(
    (
        [z1_solid_epoxy_3, x1_solid_epoxy_3],
        [z4_solid_epoxy_3, x4_solid_epoxy_3],
        [z3_solid_epoxy_3, x3_solid_epoxy_3],
        [z2_solid_epoxy_3, x2_solid_epoxy_3],
    ),
    notSource=False,
)

x1_solid_epoxy_5 = 0.052808
z1_solid_epoxy_5 = 8.096987 + 4.5

x2_solid_epoxy_5 = 0.055808
z2_solid_epoxy_5 = 8.096987 + 4.5

x3_solid_epoxy_5 = 0.055808 + .021844
z3_solid_epoxy_5 = 8.096987 + 1.666033 + 4.5

x4_solid_epoxy_5 = 0.052808 + .021844
z4_solid_epoxy_5 = 8.096987 + 1.666033 + 4.5

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
x1_Col6A_1 = -0.070787 #For y=0 slice  
z1_Col6A_1 = 9.555904 + 4.5

x2_Col6A_1 = -0.05531
z2_Col6A_1 = 9.555904 + 4.5

x3_Col6A_1 = -0.05629 
z3_Col6A_1 = 9.625754 + 4.5

x4_Col6A_1 = -0.070787 #For y=0 slice  
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
x1_Col6A_2 = -0.070787 #For y=0 slice
z1_Col6A_2 = 9.638454 + 4.5

x2_Col6A_2 = -0.05646
z2_Col6A_2 = 9.638454 + 4.5

x3_Col6A_2 = -0.05744
z3_Col6A_2 = 9.708304 + 4.5

x4_Col6A_2 = -0.070787  #For y=0 slice
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
x1_Col6B_1 = -0.12000  #For y=0 slice
z1_Col6B_1 = 10.927504 + 4.5

x2_Col6B_1 = -0.08000  
z2_Col6B_1 = 10.927504 + 4.5

x3_Col6B_1 = -0.08147  
z3_Col6B_1 = 10.997354 + 4.5

x4_Col6B_1 = -0.12000  #For y=0 slice
z4_Col6B_1 = 10.997354 + 4.5

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
x1_Col6B_2 = -0.12000 #For y=0 slice
z1_Col6B_2 = 11.010054 + 4.5

x2_Col6B_2 = -0.08173
z2_Col6B_2 = 11.010054 + 4.5

x3_Col6B_2 = -0.08320
z3_Col6B_2 = 11.079904 + 4.5

x4_Col6B_2 = -0.12000 #For y=0 slice
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

#Driftpipe_end

x1_driftend = 0.73025
z1_driftend = 17.23691
x2_driftend = 0.73026
z2_driftend = 17.23691
x3_driftend = 0.73025 + 0.0254
z3_driftend = 17.23691 + 0.0254
x4_driftend = 1.27000
z4_driftend = 17.23691 + 0.4239 - 0.0762
x5_driftend = 1.27000
z5_driftend = 17.23691 + 0.4239
x6_driftend = 1.27000 - 0.0254
z6_driftend = 17.23691 + 0.4239
x7_driftend = 1.27000 - 0.0254
z7_driftend = 17.23691 + 0.4239 - 0.0762
x8_driftend = 0.73025
z8_driftend = 17.23691 + 0.0254

Driftpipe_end_top= polygon(
    (
        [z1_driftend, x1_driftend],
        [z8_driftend, x8_driftend],
        [z7_driftend, x7_driftend],
        [z6_driftend, x6_driftend],
        [z5_driftend, x5_driftend],
        [z4_driftend, x4_driftend],
        [z3_driftend, x3_driftend],
        [z2_driftend, x2_driftend],
    ),
    notSource=False,
    isConcave=True,
)

Driftpipe_end_bot= polygon(
    (
        [z1_driftend, -x1_driftend],
        [z8_driftend, -x8_driftend],
        [z7_driftend, -x7_driftend],
        [z6_driftend, -x6_driftend],
        [z5_driftend, -x5_driftend],
        [z4_driftend, -x4_driftend],
        [z3_driftend, -x3_driftend],
        [z2_driftend, -x2_driftend],
    ),
    notSource=False,
    isConcave=True,
)

#Driftpipe

x1_drift = 1.24778
z1_drift = 17.660806
x2_drift = 1.27000  
z2_drift = 17.660806
x3_drift = 1.27000
z3_drift = 17.660806 + 5.6602
x4_drift = 1.24778
z4_drift = 17.660806 + 5.6602

Driftpipe_top= polygon(
    (
        [z1_drift, x1_drift],
        [z4_drift, x4_drift],
        [z3_drift, x3_drift],
        [z2_drift, x2_drift],
    ),
    notSource=False,
    isConcave=True,
)

Driftpipe_bot= polygon(
    (
        [z1_drift, -x1_drift],
        [z4_drift, -x4_drift],
        [z3_drift, -x3_drift],
        [z2_drift, -x2_drift],
    ),
    notSource=False,
    isConcave=True,
)

#Driftpipe_vacuum

x1_drift_vac = 1.27329
z1_drift_vac = 23.18932
x2_drift_vac = 1.31039
z2_drift_vac = 23.18932
x3_drift_vac = 1.32232
z3_drift_vac = 23.18932 + 96.012*mm
x4_drift_vac = 1.39700
z4_drift_vac = 23.18932 + 101.6*mm
x5_drift_vac = 1.39700
z5_drift_vac = 23.18932 + 165.1*mm
x6_drift_vac = 1.27229
z6_drift_vac = 23.18932 + 165.1*mm
x7_drift_vac = 1.27329
z7_drift_vac = 23.18932 + 101.6*mm

Drift_vac_top = polygon(
    (
        [z1_drift_vac, x1_drift_vac],
        [z7_drift_vac, x7_drift_vac],
        [z6_drift_vac, x6_drift_vac],
        [z5_drift_vac, x5_drift_vac],
        [z4_drift_vac, x4_drift_vac],
        [z3_drift_vac, x3_drift_vac],
        [z2_drift_vac, x2_drift_vac],
    ),
    notSource=False,
    isConcave=True,
)

Drift_vac_bot = polygon(
    (
        [z1_drift_vac, -x1_drift_vac],
        [z7_drift_vac, -x7_drift_vac],
        [z6_drift_vac, -x6_drift_vac],
        [z5_drift_vac, -x5_drift_vac],
        [z4_drift_vac, -x4_drift_vac],
        [z3_drift_vac, -x3_drift_vac],
        [z2_drift_vac, -x2_drift_vac],
    ),
    notSource=False,
    isConcave=True,
)

#DS window flange

x1_win_flan = 1.01143  
z1_win_flan = 23.35442

x2_win_flan = 1.39700  
z2_win_flan = 23.35442

x3_win_flan = 1.39700
z3_win_flan = 23.35442 + 0.0635

x4_win_flan = 1.06756  
z4_win_flan = 23.35442 + 0.0635

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
x1_DSendtube_US = 0.68580 
z1_DSendtube_US = 16.651814

x2_DSendtube_US = 0.69580  
z2_DSendtube_US = 16.651814

x3_DSendtube_US = 0.69580
z3_DSendtube_US = 16.711814

x4_DSendtube_US = 0.68580 
z4_DSendtube_US = 16.711814

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
x1_DSendtube_DS = 0.72390
z1_DSendtube_DS = 17.143739

x2_DSendtube_DS = 0.73025
z2_DSendtube_DS = 17.143739

x3_DSendtube_DS = 0.73025
z3_DSendtube_DS = 17.143739 + 0.11857

x4_DSendtube_DS = 0.72390
z4_DSendtube_DS = 17.143739 + 0.11857

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

#US flange (DSendtube_USflange)
x1_DSendtube_USflange = 0.68580
z1_DSendtube_USflange = 16.711939
x2_DSendtube_USflange = 0.78740
z2_DSendtube_USflange = 16.711939
x3_DSendtube_USflange = 0.78740
z3_DSendtube_USflange = 16.711939 + 0.03175
x4_DSendtube_USflange = 0.68580 
z4_DSendtube_USflange = 16.711939 + 0.03175

DSendtube_USflange_top = polygon(
    (
        [z1_DSendtube_USflange, x1_DSendtube_USflange],
        [z4_DSendtube_USflange, x4_DSendtube_USflange],
        [z3_DSendtube_USflange, x3_DSendtube_USflange],
        [z2_DSendtube_USflange, x2_DSendtube_USflange],
    ),
    notSource=False,
    isConcave=True,
)

DSendtube_USflange_bot = polygon(
    (
        [z1_DSendtube_USflange, -x1_DSendtube_USflange],
        [z4_DSendtube_USflange, -x4_DSendtube_USflange],
        [z3_DSendtube_USflange, -x3_DSendtube_USflange],
        [z2_DSendtube_USflange, -x2_DSendtube_USflange],
    ),
    notSource=False,
    isConcave=True,
)

#DS flange (DSendtube_DSflange)
x1_DSendtube_DSflange = 0.73025
z1_DSendtube_DSflange = 17.127864
x2_DSendtube_DSflange = 0.81280
z2_DSendtube_DSflange = 17.127864
x3_DSendtube_DSflange = 0.81280
z3_DSendtube_DSflange = 17.127864 + 0.03175
x4_DSendtube_DSflange = 0.73025
z4_DSendtube_DSflange = 17.127864 + 0.03175

DSendtube_DSflange_top = polygon(
    (
        [z1_DSendtube_DSflange, x1_DSendtube_DSflange],
        [z4_DSendtube_DSflange, x4_DSendtube_DSflange],
        [z3_DSendtube_DSflange, x3_DSendtube_DSflange],
        [z2_DSendtube_DSflange, x2_DSendtube_DSflange],
    ),
    notSource=False,
    isConcave=True,
)

DSendtube_DSflange_bot = polygon(
    (
        [z1_DSendtube_DSflange, -x1_DSendtube_DSflange],
        [z4_DSendtube_DSflange, -x4_DSendtube_DSflange],
        [z3_DSendtube_DSflange, -x3_DSendtube_DSflange],
        [z2_DSendtube_DSflange, -x2_DSendtube_DSflange],
    ),
    notSource=False,
    isConcave=True,
)

#bellows4_flangeUS/DS (formerly LowCycleBellows_flanges)

x1_lowcyclebellows_flange = 0.68560
z1_lowcyclebellows_flange = 16.743689

x2_lowcyclebellows_flange = 0.68560 + 0.10160
z2_lowcyclebellows_flange = 16.743689

x3_lowcyclebellows_flange = 0.68560 + 0.10160
z3_lowcyclebellows_flange = 16.743689 + 0.01524

x4_lowcyclebellows_flange = 0.68560 
z4_lowcyclebellows_flange = 16.743689 + 0.01524

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
        [z1_lowcyclebellows_flange+0.38481, x1_lowcyclebellows_flange],
        [z4_lowcyclebellows_flange+0.38481, x4_lowcyclebellows_flange],
        [z3_lowcyclebellows_flange+0.38481, x3_lowcyclebellows_flange+0.0256],
        [z2_lowcyclebellows_flange+0.38481, x2_lowcyclebellows_flange+0.0256],
    ),
    notSource=False,
)

LowCycleBellows_flangeDS_bot = polygon(
    (
        [z1_lowcyclebellows_flange+0.38481, -x1_lowcyclebellows_flange],
        [z4_lowcyclebellows_flange+0.38481, -x4_lowcyclebellows_flange],
        [z3_lowcyclebellows_flange+0.38481, -x3_lowcyclebellows_flange-0.0256],
        [z2_lowcyclebellows_flange+0.38481, -x2_lowcyclebellows_flange-0.0256],
    ),
    notSource=False,
)

#bellows4 (formerly LowCycleBellows)
x1_lowcyclebellows = 0.68560
z1_lowcyclebellows = 16.758929
x2_lowcyclebellows = 0.74275
z2_lowcyclebellows = 16.758929
x3_lowcyclebellows = 0.74275
z3_lowcyclebellows = 16.758929 + 0.36957
x4_lowcyclebellows = 0.68560
z4_lowcyclebellows = 16.758929 + 0.36957

LowCycleBellows_top = polygon(
    (
        [z1_lowcyclebellows, x1_lowcyclebellows],
        [z4_lowcyclebellows, x4_lowcyclebellows],
        [z3_lowcyclebellows, x3_lowcyclebellows],
        [z2_lowcyclebellows, x2_lowcyclebellows],
    ),
    notSource=False,
    isConcave=True,
)

LowCycleBellows_bot = polygon(
    (
        [z1_lowcyclebellows, -x1_lowcyclebellows],
        [z4_lowcyclebellows, -x4_lowcyclebellows],
        [z3_lowcyclebellows, -x3_lowcyclebellows],
        [z2_lowcyclebellows, -x2_lowcyclebellows],
    ),
    notSource=False,
    isConcave=True,
)

#DSpipe (near Barite_Collar2)

#DSpipe_flange (Exact shape)
x1_DSpipeflange = 0.50190
z1_DSpipeflange = 23.01152
x2_DSpipeflange = 0.50191
z2_DSpipeflange = 23.01152
x3_DSpipeflange = 0.50854
z3_DSpipeflange = 23.01152 + 0.00356
x4_DSpipeflange = 0.51054
z4_DSpipeflange = 23.01152 + 0.00508
x5_DSpipeflange = 0.50978
z5_DSpipeflange = 23.01152 + 0.00686
x6_DSpipeflange = 0.51029
z6_DSpipeflange = 23.01152 + 0.00965
x7_DSpipeflange = 0.50470
z7_DSpipeflange = 23.01152 + 0.01092
x8_DSpipeflange = 0.52146
z8_DSpipeflange = 23.01152 + 0.01600
x9_DSpipeflange = 0.52375
z9_DSpipeflange = 23.01152 + 0.02184
x10_DSpipeflange = 0.52553
z10_DSpipeflange = 23.01152 + 0.02286
x11_DSpipeflange = 0.52527
z11_DSpipeflange = 23.01152 + 0.02464
x12_DSpipeflange = 0.52553
z12_DSpipeflange = 23.01152 + 0.04496
x13_DSpipeflange = 0.52527
z13_DSpipeflange = 23.01152 + 0.05004
x14_DSpipeflange = 0.51740
z14_DSpipeflange = 23.01152 + 0.05309
x15_DSpipeflange = 0.50470
z15_DSpipeflange = 23.01152 + 0.05613
x16_DSpipeflange = 0.50470
z16_DSpipeflange = 23.01152 + 0.07849
x17_DSpipeflange = 0.50013
z17_DSpipeflange = 23.01152 + 0.07849
x18_DSpipeflange = 0.50013
z18_DSpipeflange = 23.01152 + 0.05613
x19_DSpipeflange = 0.51283
z19_DSpipeflange = 23.01152 + 0.05309
x20_DSpipeflange = 0.52070
z20_DSpipeflange = 23.01152 + 0.05004
x21_DSpipeflange = 0.52095
z21_DSpipeflange = 23.01152 + 0.04496
x22_DSpipeflange = 0.52070
z22_DSpipeflange = 23.01152 + 0.02464
x23_DSpipeflange = 0.52095
z23_DSpipeflange = 23.01152 + 0.02286
x24_DSpipeflange = 0.51918
z24_DSpipeflange = 23.01152 + 0.02184
x25_DSpipeflange = 0.51689
z25_DSpipeflange = 23.01152 + 0.01600
x26_DSpipeflange = 0.50013
z26_DSpipeflange = 23.01152 + 0.01092
x27_DSpipeflange = 0.50571
z27_DSpipeflange = 23.01152 + 0.00965
x28_DSpipeflange = 0.50521
z28_DSpipeflange = 23.01152 + 0.00686
x29_DSpipeflange = 0.50597
z29_DSpipeflange = 23.01152 + 0.00508
x30_DSpipeflange = 0.50013
z30_DSpipeflange = 23.01152 + 0.00356

DSpipeflange_top = polygon(
    (
        [z1_DSpipeflange, x1_DSpipeflange],
        [z30_DSpipeflange, x30_DSpipeflange],
        [z29_DSpipeflange, x29_DSpipeflange],
        [z28_DSpipeflange, x28_DSpipeflange],
        [z27_DSpipeflange, x27_DSpipeflange],
        [z26_DSpipeflange, x26_DSpipeflange],
        [z25_DSpipeflange, x25_DSpipeflange],
        [z24_DSpipeflange, x24_DSpipeflange],
        [z23_DSpipeflange, x23_DSpipeflange],
        [z22_DSpipeflange, x22_DSpipeflange],
        [z21_DSpipeflange, x21_DSpipeflange],
        [z20_DSpipeflange, x20_DSpipeflange],
        [z19_DSpipeflange, x19_DSpipeflange],
        [z18_DSpipeflange, x18_DSpipeflange],
        [z17_DSpipeflange, x17_DSpipeflange],
        [z16_DSpipeflange, x16_DSpipeflange],
        [z15_DSpipeflange, x15_DSpipeflange],
        [z14_DSpipeflange, x14_DSpipeflange],
        [z13_DSpipeflange, x13_DSpipeflange],
        [z12_DSpipeflange, x12_DSpipeflange],
        [z11_DSpipeflange, x11_DSpipeflange],
        [z10_DSpipeflange, x10_DSpipeflange],
        [z9_DSpipeflange, x9_DSpipeflange],
        [z8_DSpipeflange, x8_DSpipeflange],
        [z7_DSpipeflange, x7_DSpipeflange],
        [z6_DSpipeflange, x6_DSpipeflange],
        [z5_DSpipeflange, x5_DSpipeflange],
        [z4_DSpipeflange, x4_DSpipeflange],
        [z3_DSpipeflange, x3_DSpipeflange],
        [z2_DSpipeflange, x2_DSpipeflange],
    ),
    notSource=False,
    isConcave=True,
)

DSpipeflange_bot = polygon(
    (
        [z1_DSpipeflange, -x1_DSpipeflange],
        [z30_DSpipeflange, -x30_DSpipeflange],
        [z29_DSpipeflange, -x29_DSpipeflange],
        [z28_DSpipeflange, -x28_DSpipeflange],
        [z27_DSpipeflange, -x27_DSpipeflange],
        [z26_DSpipeflange, -x26_DSpipeflange],
        [z25_DSpipeflange, -x25_DSpipeflange],
        [z24_DSpipeflange, -x24_DSpipeflange],
        [z23_DSpipeflange, -x23_DSpipeflange],
        [z22_DSpipeflange, -x22_DSpipeflange],
        [z21_DSpipeflange, -x21_DSpipeflange],
        [z20_DSpipeflange, -x20_DSpipeflange],
        [z19_DSpipeflange, -x19_DSpipeflange],
        [z18_DSpipeflange, -x18_DSpipeflange],
        [z17_DSpipeflange, -x17_DSpipeflange],
        [z16_DSpipeflange, -x16_DSpipeflange],
        [z15_DSpipeflange, -x15_DSpipeflange],
        [z14_DSpipeflange, -x14_DSpipeflange],
        [z13_DSpipeflange, -x13_DSpipeflange],
        [z12_DSpipeflange, -x12_DSpipeflange],
        [z11_DSpipeflange, -x11_DSpipeflange],
        [z10_DSpipeflange, -x10_DSpipeflange],
        [z9_DSpipeflange, -x9_DSpipeflange],
        [z8_DSpipeflange, -x8_DSpipeflange],
        [z7_DSpipeflange, -x7_DSpipeflange],
        [z6_DSpipeflange, -x6_DSpipeflange],
        [z5_DSpipeflange, -x5_DSpipeflange],
        [z4_DSpipeflange, -x4_DSpipeflange],
        [z3_DSpipeflange, -x3_DSpipeflange],
        [z2_DSpipeflange, -x2_DSpipeflange],
    ),
    notSource=False,
    isConcave=True,
)

#DSpipe1
x1_DSpipe1 = 0.50013
z1_DSpipe1 = 23.090256

x2_DSpipe1 = 0.50470
z2_DSpipe1 = 23.090256

x3_DSpipe1 = 0.50470
z3_DSpipe1 = 23.090256 + 0.14910

x4_DSpipe1 = 0.50013
z4_DSpipe1 = 23.090256 + 0.14910

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

#DSpipe1_bellow (exact)
x1_DSpipe1_bellow = 0.50000
z1_DSpipe1_bellow = 23.59669
x2_DSpipe1_bellow = 0.52900
z2_DSpipe1_bellow = 23.59669
x3_DSpipe1_bellow = 0.52900
z3_DSpipe1_bellow = 23.59669 + 0.00635
x4_DSpipe1_bellow = 0.50635
z4_DSpipe1_bellow = 23.59669 + 0.00635
x5_DSpipe1_bellow = 0.50635
z5_DSpipe1_bellow = 23.59669 + 0.03365
x6_DSpipe1_bellow = 0.52900
z6_DSpipe1_bellow = 23.59669 + 0.03365
x7_DSpipe1_bellow = 0.52976
z7_DSpipe1_bellow = 23.59669 + 0.14635
x8_DSpipe1_bellow = 0.50650
z8_DSpipe1_bellow = 23.59669 + 0.14635
x9_DSpipe1_bellow = 0.50650
z9_DSpipe1_bellow = 23.59669 + 0.17365
x10_DSpipe1_bellow = 0.52976
z10_DSpipe1_bellow = 23.59669 + 0.17365
x11_DSpipe1_bellow = 0.52976
z11_DSpipe1_bellow = 23.59669 + 0.18000
x12_DSpipe1_bellow = 0.50076
z12_DSpipe1_bellow = 23.59669 + 0.18000

DSpipe1_bellow_top = polygon(
    (
        [z1_DSpipe1_bellow, x1_DSpipe1_bellow],
        [z12_DSpipe1_bellow, x12_DSpipe1_bellow],
        [z11_DSpipe1_bellow, x11_DSpipe1_bellow],
        [z10_DSpipe1_bellow, x10_DSpipe1_bellow],
        [z9_DSpipe1_bellow, x9_DSpipe1_bellow],
        [z8_DSpipe1_bellow, x8_DSpipe1_bellow],
        [z7_DSpipe1_bellow, x7_DSpipe1_bellow],
        [z6_DSpipe1_bellow, x6_DSpipe1_bellow],
        [z5_DSpipe1_bellow, x5_DSpipe1_bellow],
        [z4_DSpipe1_bellow, x4_DSpipe1_bellow],
        [z3_DSpipe1_bellow, x3_DSpipe1_bellow],
        [z2_DSpipe1_bellow, x2_DSpipe1_bellow],
    ),
    notSource=False,
    isConcave=True,
)

DSpipe1_bellow_bot = polygon(
    (
        [z1_DSpipe1_bellow, -x1_DSpipe1_bellow],
        [z12_DSpipe1_bellow, -x12_DSpipe1_bellow],
        [z11_DSpipe1_bellow, -x11_DSpipe1_bellow],
        [z10_DSpipe1_bellow, -x10_DSpipe1_bellow],
        [z9_DSpipe1_bellow, -x9_DSpipe1_bellow],
        [z8_DSpipe1_bellow, -x8_DSpipe1_bellow],
        [z7_DSpipe1_bellow, -x7_DSpipe1_bellow],
        [z6_DSpipe1_bellow, -x6_DSpipe1_bellow],
        [z5_DSpipe1_bellow, -x5_DSpipe1_bellow],
        [z4_DSpipe1_bellow, -x4_DSpipe1_bellow],
        [z3_DSpipe1_bellow, -x3_DSpipe1_bellow],
        [z2_DSpipe1_bellow, -x2_DSpipe1_bellow],
    ),
    notSource=False,
    isConcave=True,
)

#DSpipe2_DSpipe2_1 (actual name)
x1_DSpipe2_DS = 0.50478
z1_DSpipe2_DS = 23.801765

x2_DSpipe2_DS = 0.50954
z2_DSpipe2_DS = 23.801765

x3_DSpipe2_DS = 0.51088
z3_DSpipe2_DS = 23.801765 + 0.03093

x4_DSpipe2_DS = 0.50612
z4_DSpipe2_DS = 23.801765 + 0.03093

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
z1_DSpipe3 = 23.915451

x2_DSpipe3 = 0.52805
z2_DSpipe3 = 23.915451

x3_DSpipe3 = 0.69550
z3_DSpipe3 = 29.972105

x4_DSpipe3 = 0.67645
z4_DSpipe3 = 29.972105

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

#DSpipe1_flange (exact shape)
x1_DSpipe1_flange = 0.49700
z1_DSpipe1_flange = 23.57169
x2_DSpipe1_flange = 0.49950
z2_DSpipe1_flange = 23.57169
x3_DSpipe1_flange = 0.49950
z3_DSpipe1_flange = 23.57169 + 0.005
x4_DSpipe1_flange = 0.50500
z4_DSpipe1_flange = 23.57169 + 0.005
x5_DSpipe1_flange = 0.50500
z5_DSpipe1_flange = 23.57169 + 0.013
x6_DSpipe1_flange = 0.52900 
z6_DSpipe1_flange = 23.57169 + 0.013
x7_DSpipe1_flange = 0.52900
z7_DSpipe1_flange = 23.57169 + 0.025
x8_DSpipe1_flange = 0.49700
z8_DSpipe1_flange = 23.57169 + 0.025

DSpipe1_flange_top = polygon(
    (
        [z1_DSpipe1_flange, x1_DSpipe1_flange],
        [z8_DSpipe1_flange, x8_DSpipe1_flange],
        [z7_DSpipe1_flange, x7_DSpipe1_flange],
        [z6_DSpipe1_flange, x6_DSpipe1_flange],
        [z5_DSpipe1_flange, x5_DSpipe1_flange],
        [z4_DSpipe1_flange, x4_DSpipe1_flange],
        [z3_DSpipe1_flange, x3_DSpipe1_flange],
        [z2_DSpipe1_flange, x2_DSpipe1_flange],
    ),
    notSource=False,
    isConcave=True,
)

DSpipe1_flange_bot = polygon(
    (
        [z1_DSpipe1_flange, -x1_DSpipe1_flange],
        [z8_DSpipe1_flange, -x8_DSpipe1_flange],
        [z7_DSpipe1_flange, -x7_DSpipe1_flange],
        [z6_DSpipe1_flange, -x6_DSpipe1_flange],
        [z5_DSpipe1_flange, -x5_DSpipe1_flange],
        [z4_DSpipe1_flange, -x4_DSpipe1_flange],
        [z3_DSpipe1_flange, -x3_DSpipe1_flange],
        [z2_DSpipe1_flange, -x2_DSpipe1_flange],
    ),
    notSource=False,
    isConcave=True,
)

#DSpipe2_USplate (slightly approximated x positions. Should not matter unless resolution of 0.001 or less)
x1_DSpipe2_US = 0.50076
z1_DSpipe2_US = 23.77669
x2_DSpipe2_US = 0.52975
z2_DSpipe2_US = 23.77669
x3_DSpipe2_US = 0.52975
z3_DSpipe2_US = 23.77669 + 0.012
x4_DSpipe2_US = 0.50557
z4_DSpipe2_US = 23.77669 + 0.012
x5_DSpipe2_US = 0.50557
z5_DSpipe2_US = 23.77669 + 0.020
x6_DSpipe2_US = 0.50493
z6_DSpipe2_US = 23.77669 + 0.020
x7_DSpipe2_US = 0.50493
z7_DSpipe2_US = 23.77669 + 0.025
x8_DSpipe2_US = 0.50160
z8_DSpipe2_US = 23.77669 + 0.025

DSpipe2_US_top = polygon(
    (
        [z1_DSpipe2_US, x1_DSpipe2_US],
        [z8_DSpipe2_US, x8_DSpipe2_US],
        [z7_DSpipe2_US, x7_DSpipe2_US],
        [z6_DSpipe2_US, x6_DSpipe2_US],
        [z5_DSpipe2_US, x5_DSpipe2_US],
        [z4_DSpipe2_US, x4_DSpipe2_US],
        [z3_DSpipe2_US, x3_DSpipe2_US],
        [z2_DSpipe2_US, x2_DSpipe2_US],
    ),
    notSource=False,
    isConcave=True,
)

DSpipe2_US_bot = polygon(
    (
        [z1_DSpipe2_US, -x1_DSpipe2_US],
        [z8_DSpipe2_US, -x8_DSpipe2_US],
        [z7_DSpipe2_US, -x7_DSpipe2_US],
        [z6_DSpipe2_US, -x6_DSpipe2_US],
        [z5_DSpipe2_US, -x5_DSpipe2_US],
        [z4_DSpipe2_US, -x4_DSpipe2_US],
        [z3_DSpipe2_US, -x3_DSpipe2_US],
        [z2_DSpipe2_US, -x2_DSpipe2_US],
    ),
    notSource=False,
    isConcave=True,
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
allpolys.append(pipeflange_UScollar0_top)
allpolys.append(pipeflange_UScollar0_bottom)
allpolys.append(collar0_top)
allpolys.append(collar0_bottom)
allpolys.append(pipe_DScollar0_top)
allpolys.append(pipe_DScollar0_bottom)

allpolys.append(bellows2_USflange_top)
allpolys.append(bellows2_USflange_bot)
allpolys.append(bellows2_top)
allpolys.append(bellows2_bot)
allpolys.append(bellows2_DSflange_top)
allpolys.append(bellows2_DSflange_bot)

allpolys.append(upstream_enclosure_USpipe_top)
allpolys.append(upstream_enclosure_USpipe_bottom)
allpolys.append(upstream_enclosure_USwall_top)
allpolys.append(upstream_enclosure_USwall_bottom)
allpolys.append(upstream_enclosure_sidewall_top)
allpolys.append(upstream_enclosure_sidewall_bottom)
allpolys.append(upstream_enclosure_DSwall_top)
allpolys.append(upstream_enclosure_DSwall_bottom)

allpolys.append(col1_top)
allpolys.append(col1_bot)
allpolys.append(col1_h20_1_top)
allpolys.append(col1_h20_1_bot)
allpolys.append(col1_h20_2_top)
allpolys.append(col1_h20_2_bot)
allpolys.append(col1_h20_CW_top)
allpolys.append(col1_h20_CW_bot)
allpolys.append(col1_jacket_top)
allpolys.append(col1_jacket_bot)

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

allpolys.append(US_Pbwall1_top)
allpolys.append(US_Pbwall1_bot)
allpolys.append(US_Pbwall2_top)
allpolys.append(US_Pbwall2_bot)

#allpolys.append(upstream_enclosure_DSpipe_top)
#allpolys.append(upstream_enclosure_DSpipe_bottom)
#allpolys.append(upstream_enclosure_DSpipe_flange_top)
#allpolys.append(upstream_enclosure_DSpipe_flange_bottom)
allpolys.append(bellows3_top)
allpolys.append(bellows3_bot)
allpolys.append(bellows3flangeUS_top)
allpolys.append(bellows3flangeUS_bot)
allpolys.append(bellows3flangeDS_top)
allpolys.append(bellows3flangeDS_bot)

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

#allpolys.append(Scaper_11)
#allpolys.append(Scaper_12)
allpolys.append(Blocker_12)
allpolys.append(Blocker_ring_top)
allpolys.append(Blocker_ring_bot)

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
allpolys.append(LowCycleBellows_top)
allpolys.append(LowCycleBellows_bot)

allpolys.append(Driftpipe_end_top)
allpolys.append(Driftpipe_end_bot)
allpolys.append(Driftpipe_top)
allpolys.append(Driftpipe_bot)
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
