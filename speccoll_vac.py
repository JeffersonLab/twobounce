#!/usr/bin/python
from poly import polygon
from poly import face
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from drawlight import drawlight

sources = []
allpolys = []

tgtlen = 1.25
tgtrad = 1.4142 * 0.0025

target = polygon(
    (
        [-tgtlen / 2, -tgtrad],
        [tgtlen / 2, -tgtrad],
        [tgtlen / 2, tgtrad],
        [-tgtlen / 2, tgtrad],
    )
)

### Target tube
x1_tgt_tube = 0.0360045
z1_tgt_tube = -0.625

x2_tgt_tube = 0.045
z2_tgt_tube = -0.625

x3_tgt_tube = 0.045
z3_tgt_tube = 0.625

x4_tgt_tube = 0.0360045
z4_tgt_tube = 0.625


####Target chamber upstream end
x1_tgt_us = 0.0508
z1_tgt_us = -0.9906

x2_tgt_us = 0.9144
z2_tgt_us = -0.9906

x3_tgt_us = 0.9144
z3_tgt_us = -0.889

x4_tgt_us = 0.0508
z4_tgt_us = -0.889

tgt_US_1 = polygon(
    (
        [z1_tgt_us, x1_tgt_us],
        [z4_tgt_us, x4_tgt_us],
        [z3_tgt_us, x3_tgt_us],
        [z2_tgt_us, x2_tgt_us],
    ),
    notSource=False,
)
tgt_US_2 = polygon(
    (
        [z2_tgt_us, -x2_tgt_us],
        [z3_tgt_us, -x3_tgt_us],
        [z4_tgt_us, -x4_tgt_us],
        [z1_tgt_us, -x1_tgt_us],
    ),
    notSource=False,
)

x1_tgt_ds = 0.1016
z1_tgt_ds = 0.889

x2_tgt_ds = 0.9144
z2_tgt_ds = 0.889

x3_tgt_ds = 0.9144
z3_tgt_ds = 0.9906

x4_tgt_ds = 0.1016
z4_tgt_ds = 0.9906

tgt_DS_1 = polygon(
    (
        [z1_tgt_ds, x1_tgt_ds],
        [z4_tgt_ds, x4_tgt_ds],
        [z3_tgt_ds, x3_tgt_ds],
        [z2_tgt_ds, x2_tgt_ds],
    ),
    notSource=False,
)
tgt_DS_2 = polygon(
    (
        [z2_tgt_ds, -x2_tgt_ds],
        [z3_tgt_ds, -x3_tgt_ds],
        [z4_tgt_ds, -x4_tgt_ds],
        [z1_tgt_ds, -x1_tgt_ds],
    ),
    notSource=False,
)

### Target chamber top shielding
x1_tgt_TopShield = 1.085
z1_tgt_TopShield = -3.175

x2_tgt_TopShield = 1.485
z2_tgt_TopShield = -3.175

x3_tgt_TopShield = 1.485
z3_tgt_TopShield = 3.175

x4_tgt_TopShield = 1.085
z4_tgt_TopShield = 3.175

tgt_TopShield_top = polygon(
    (
        [z1_tgt_TopShield, x1_tgt_TopShield],
        [z4_tgt_TopShield, x4_tgt_TopShield],
        [z3_tgt_TopShield, x3_tgt_TopShield],
        [z2_tgt_TopShield, x2_tgt_TopShield],
    ),
    notSource=False,
)

### Target chamber DS shielding top piece
x1_tgt_DSShield1 = 0.453
z1_tgt_DSShield1 = 3.175 - 1.4

x2_tgt_DSShield1 = 1.085
z2_tgt_DSShield1 = 3.175 - 1.4

x3_tgt_DSShield1 = 1.085
z3_tgt_DSShield1 = 3.175

x4_tgt_DSShield1 = 0.453
z4_tgt_DSShield1 = 3.175

tgt_DSShield_top = polygon(
    (
        [z1_tgt_DSShield1, x1_tgt_DSShield1],
        [z4_tgt_DSShield1, x4_tgt_DSShield1],
        [z3_tgt_DSShield1, x3_tgt_DSShield1],
        [z2_tgt_DSShield1, x2_tgt_DSShield1],
    ),
    notSource=False,
)

### Target chamber DS shielding bottom piece
x1_tgt_DSShield2 = 0.453
z1_tgt_DSShield2 = 3.175 - 1.4

x2_tgt_DSShield2 = 2.969
z2_tgt_DSShield2 = 3.175 - 1.4

x3_tgt_DSShield2 = 2.969
z3_tgt_DSShield2 = 3.175

x4_tgt_DSShield2 = 0.453
z4_tgt_DSShield2 = 3.175

tgt_DSShield_bottom = polygon(
    (
        [z2_tgt_DSShield2, -x2_tgt_DSShield2],
        [z3_tgt_DSShield2, -x3_tgt_DSShield2],
        [z4_tgt_DSShield2, -x4_tgt_DSShield2],
        [z1_tgt_DSShield2, -x1_tgt_DSShield2],
    ),
    notSource=False,
)

### Target Region Barite outer
x1_tgt_barite1 = 0.331
z1_tgt_barite1 = 1.975

x2_tgt_barite1 = 0.450
z2_tgt_barite1 = 1.975

x3_tgt_barite1 = 0.450
z3_tgt_barite1 = 3.175

x4_tgt_barite1 = 0.331
z4_tgt_barite1 = 3.175

tgt_barite1_top = polygon(
    (
        [z1_tgt_barite1, x1_tgt_barite1],
        [z4_tgt_barite1, x4_tgt_barite1],
        [z3_tgt_barite1, x3_tgt_barite1],
        [z2_tgt_barite1, x2_tgt_barite1],
    ),
    notSource=False,
)
tgt_barite1_bottom = polygon(
    (
        [z2_tgt_barite1, -x2_tgt_barite1],
        [z3_tgt_barite1, -x3_tgt_barite1],
        [z4_tgt_barite1, -x4_tgt_barite1],
        [z1_tgt_barite1, -x1_tgt_barite1],
    ),
    notSource=False,
)

### Target Region Barite inner
x1_tgt_barite2 = 0.150
z1_tgt_barite2 = 2.225

x2_tgt_barite2 = 0.330
z2_tgt_barite2 = 2.225

x3_tgt_barite2 = 0.330
z3_tgt_barite2 = 2.725

x4_tgt_barite2 = 0.150
z4_tgt_barite2 = 2.725

tgt_barite2_top = polygon(
    (
        [z1_tgt_barite2, x1_tgt_barite2],
        [z4_tgt_barite2, x4_tgt_barite2],
        [z3_tgt_barite2, x3_tgt_barite2],
        [z2_tgt_barite2, x2_tgt_barite2],
    ),
    notSource=False,
)
tgt_barite2_bottom = polygon(
    (
        [z2_tgt_barite2, -x2_tgt_barite2],
        [z3_tgt_barite2, -x3_tgt_barite2],
        [z4_tgt_barite2, -x4_tgt_barite2],
        [z1_tgt_barite2, -x1_tgt_barite2],
    ),
    notSource=False,
)

### Pipe after target chamber
#
x1_tgt_pipe0 = 0.1016
z1_tgt_pipe0 = 0.83185

x2_tgt_pipe0 = 0.110
z2_tgt_pipe0 = 0.83185

x3_tgt_pipe0 = 0.110
z3_tgt_pipe0 = 0.8763 + 0.1016

x4_tgt_pipe0 = 0.1016
z4_tgt_pipe0 = 0.8763 + 0.1016

# tgt_pipe0_up   = polygon( ([z1_tgt_pipe0, x1_tgt_pipe0], [z4_tgt_pipe0, x4_tgt_pipe0], [z3_tgt_pipe0, x3_tgt_pipe0], [z2_tgt_pipe0, x2_tgt_pipe0] ),  isEthereal=True)
# tgt_pipe0_lo   = polygon( ([z2_tgt_pipe0, -x2_tgt_pipe0], [z3_tgt_pipe0, -x3_tgt_pipe0], [z4_tgt_pipe0, -x4_tgt_pipe0], [z1_tgt_pipe0, -x1_tgt_pipe0] ), isEthereal=True)

tgt_pipe0_up = polygon(
    (
        [z1_tgt_pipe0, x1_tgt_pipe0],
        [z4_tgt_pipe0, x4_tgt_pipe0],
        [z3_tgt_pipe0, x3_tgt_pipe0],
        [z2_tgt_pipe0, x2_tgt_pipe0],
    ),
    notSource=False,
)
tgt_pipe0_lo = polygon(
    (
        [z2_tgt_pipe0, -x2_tgt_pipe0],
        [z3_tgt_pipe0, -x3_tgt_pipe0],
        [z4_tgt_pipe0, -x4_tgt_pipe0],
        [z1_tgt_pipe0, -x1_tgt_pipe0],
    ),
    notSource=False,
)

# x1_tgt_pipe1=0.09525
# z1_tgt_pipe1=0.90094
#
# x2_tgt_pipe1=0.1016
# z2_tgt_pipe1=0.90094
#
# x3_tgt_pipe1=0.1016
# z3_tgt_pipe1=0.90094+0.2032
#
# x4_tgt_pipe1=0.09525
# z4_tgt_pipe1=0.90094+0.2032

x1_tgt_pipe1 = 0.1600
# z1_tgt_pipe1=1.150
z1_tgt_pipe1 = 0.8763 + 0.1016

x2_tgt_pipe1 = 0.167
# z2_tgt_pipe1=1.150
z2_tgt_pipe1 = 0.8763 + 0.1016

x3_tgt_pipe1 = 0.167
z3_tgt_pipe1 = 3.300

x4_tgt_pipe1 = 0.1600
z4_tgt_pipe1 = 3.300

tgt_pipe1_up = polygon(
    (
        [z1_tgt_pipe1, x1_tgt_pipe1],
        [z4_tgt_pipe1, x4_tgt_pipe1],
        [z3_tgt_pipe1, x3_tgt_pipe1],
        [z2_tgt_pipe1, x2_tgt_pipe1],
    ),
    notSource=False,
)
tgt_pipe1_lo = polygon(
    (
        [z2_tgt_pipe1, -x2_tgt_pipe1],
        [z3_tgt_pipe1, -x3_tgt_pipe1],
        [z4_tgt_pipe1, -x4_tgt_pipe1],
        [z1_tgt_pipe1, -x1_tgt_pipe1],
    ),
    notSource=False,
)

# tgt_pipe1_up   = polygon( ([z1_tgt_pipe1, x1_tgt_pipe1], [z4_tgt_pipe1, x4_tgt_pipe1], [z3_tgt_pipe1, x3_tgt_pipe1], [z2_tgt_pipe1, x2_tgt_pipe1] ), isEthereal=True)
# tgt_pipe1_lo   = polygon( ([z2_tgt_pipe1, -x2_tgt_pipe1], [z3_tgt_pipe1, -x3_tgt_pipe1], [z4_tgt_pipe1, -x4_tgt_pipe1], [z1_tgt_pipe1, -x1_tgt_pipe1] ), isEthereal=True)


x2_tgt_pipe4_5 = 0.127
z2_tgt_pipe4_5 = 3.500

x1_tgt_pipe4_5 = 0.122225
z1_tgt_pipe4_5 = 3.500

x4_tgt_pipe4_5 = 0.122225
z4_tgt_pipe4_5 = 3.41046 + 0.47374

x3_tgt_pipe4_5 = 0.127
z3_tgt_pipe4_5 = 3.41046 + 0.47374

tgt_pipe4_5_up = polygon(
    (
        [z1_tgt_pipe4_5, x1_tgt_pipe4_5],
        [z4_tgt_pipe4_5, x4_tgt_pipe4_5],
        [z3_tgt_pipe4_5, x3_tgt_pipe4_5],
        [z2_tgt_pipe4_5, x2_tgt_pipe4_5],
    ),
    notSource=False,
)
tgt_pipe4_5_lo = polygon(
    (
        [z2_tgt_pipe4_5, -x2_tgt_pipe4_5],
        [z3_tgt_pipe4_5, -x3_tgt_pipe4_5],
        [z4_tgt_pipe4_5, -x4_tgt_pipe4_5],
        [z1_tgt_pipe4_5, -x1_tgt_pipe4_5],
    ),
    notSource=False,
)


####Flange 4
###Part1
##section1
x2_tgt_flange4_1_1 = 0.152995
z2_tgt_flange4_1_1 = 3.86845

x1_tgt_flange4_1_1 = 0.127255
z1_tgt_flange4_1_1 = 3.86845

x4_tgt_flange4_1_1 = 0.127255
z4_tgt_flange4_1_1 = 3.86845 + 0.01575

x3_tgt_flange4_1_1 = 0.152995
z3_tgt_flange4_1_1 = 3.86845 + 0.01575

tgt_flange4_1_1_up = polygon(
    (
        [z1_tgt_flange4_1_1, x1_tgt_flange4_1_1],
        [z4_tgt_flange4_1_1, x4_tgt_flange4_1_1],
        [z3_tgt_flange4_1_1, x3_tgt_flange4_1_1],
        [z2_tgt_flange4_1_1, x2_tgt_flange4_1_1],
    ),
    notSource=False,
)
tgt_flange4_1_1_lo = polygon(
    (
        [z2_tgt_flange4_1_1, -x2_tgt_flange4_1_1],
        [z3_tgt_flange4_1_1, -x3_tgt_flange4_1_1],
        [z4_tgt_flange4_1_1, -x4_tgt_flange4_1_1],
        [z1_tgt_flange4_1_1, -x1_tgt_flange4_1_1],
    ),
    notSource=False,
)

##section2
x2_tgt_flange4_1_2 = 0.152995
z2_tgt_flange4_1_2 = 3.86845 + 0.01575

x1_tgt_flange4_1_2 = 0.123825
z1_tgt_flange4_1_2 = 3.86845 + 0.01575

x4_tgt_flange4_1_2 = 0.123825
z4_tgt_flange4_1_2 = 3.86845 + 0.01575 + 0.0127

x3_tgt_flange4_1_2 = 0.152995
z3_tgt_flange4_1_2 = 3.86845 + 0.01575 + 0.0127

tgt_flange4_1_2_up = polygon(
    (
        [z1_tgt_flange4_1_2, x1_tgt_flange4_1_2],
        [z4_tgt_flange4_1_2, x4_tgt_flange4_1_2],
        [z3_tgt_flange4_1_2, x3_tgt_flange4_1_2],
        [z2_tgt_flange4_1_2, x2_tgt_flange4_1_2],
    ),
    notSource=False,
)
tgt_flange4_1_2_lo = polygon(
    (
        [z2_tgt_flange4_1_2, -x2_tgt_flange4_1_2],
        [z3_tgt_flange4_1_2, -x3_tgt_flange4_1_2],
        [z4_tgt_flange4_1_2, -x4_tgt_flange4_1_2],
        [z1_tgt_flange4_1_2, -x1_tgt_flange4_1_2],
    ),
    notSource=False,
)

###Part2
##section1
x2_tgt_flange4_2_1 = 0.152995
z2_tgt_flange4_2_1 = 3.8969

x1_tgt_flange4_2_1 = 0.123825
z1_tgt_flange4_2_1 = 3.8969

x4_tgt_flange4_2_1 = 0.123825
z4_tgt_flange4_2_1 = 3.8969 + 0.0127

x3_tgt_flange4_2_1 = 0.152995
z3_tgt_flange4_2_1 = 3.8969 + 0.0127

tgt_flange4_2_1_up = polygon(
    (
        [z1_tgt_flange4_2_1, x1_tgt_flange4_2_1],
        [z4_tgt_flange4_2_1, x4_tgt_flange4_2_1],
        [z3_tgt_flange4_2_1, x3_tgt_flange4_2_1],
        [z2_tgt_flange4_2_1, x2_tgt_flange4_2_1],
    ),
    notSource=False,
)
tgt_flange4_2_1_lo = polygon(
    (
        [z2_tgt_flange4_2_1, -x2_tgt_flange4_2_1],
        [z3_tgt_flange4_2_1, -x3_tgt_flange4_2_1],
        [z4_tgt_flange4_2_1, -x4_tgt_flange4_2_1],
        [z1_tgt_flange4_2_1, -x1_tgt_flange4_2_1],
    ),
    notSource=False,
)

##section2
x2_tgt_flange4_2_2 = 0.152995
z2_tgt_flange4_2_2 = 3.8969 + 0.0127

x1_tgt_flange4_2_2 = 0.127255
z1_tgt_flange4_2_2 = 3.8969 + 0.0127

x4_tgt_flange4_2_2 = 0.127255
z4_tgt_flange4_2_2 = 3.8969 + 0.01575 + 0.0127

x3_tgt_flange4_2_2 = 0.152995
z3_tgt_flange4_2_2 = 3.8969 + 0.01575 + 0.0127

tgt_flange4_2_2_up = polygon(
    (
        [z1_tgt_flange4_2_2, x1_tgt_flange4_2_2],
        [z4_tgt_flange4_2_2, x4_tgt_flange4_2_2],
        [z3_tgt_flange4_2_2, x3_tgt_flange4_2_2],
        [z2_tgt_flange4_2_2, x2_tgt_flange4_2_2],
    ),
    notSource=False,
)
tgt_flange4_2_2_lo = polygon(
    (
        [z2_tgt_flange4_2_2, -x2_tgt_flange4_2_2],
        [z3_tgt_flange4_2_2, -x3_tgt_flange4_2_2],
        [z4_tgt_flange4_2_2, -x4_tgt_flange4_2_2],
        [z1_tgt_flange4_2_2, -x1_tgt_flange4_2_2],
    ),
    notSource=False,
)

###Next pipe - it has three parts
##part1
x2_tgt_pipe5_1 = 0.127
z2_tgt_pipe5_1 = 3.9096

x1_tgt_pipe5_1 = 0.12624
z1_tgt_pipe5_1 = 3.9096

x4_tgt_pipe5_1 = 0.12624
z4_tgt_pipe5_1 = 3.9096 + 0.0508

x3_tgt_pipe5_1 = 0.127
z3_tgt_pipe5_1 = 3.9096 + 0.0508

tgt_pipe5_1_up = polygon(
    (
        [z1_tgt_pipe5_1, x1_tgt_pipe5_1],
        [z4_tgt_pipe5_1, x4_tgt_pipe5_1],
        [z3_tgt_pipe5_1, x3_tgt_pipe5_1],
        [z2_tgt_pipe5_1, x2_tgt_pipe5_1],
    ),
    notSource=False,
)
tgt_pipe5_1_lo = polygon(
    (
        [z2_tgt_pipe5_1, -x2_tgt_pipe5_1],
        [z3_tgt_pipe5_1, -x3_tgt_pipe5_1],
        [z4_tgt_pipe5_1, -x4_tgt_pipe5_1],
        [z1_tgt_pipe5_1, -x1_tgt_pipe5_1],
    ),
    notSource=False,
)

##part2
x2_tgt_pipe5_2 = 0.13894
z2_tgt_pipe5_2 = 3.9096 + 0.0508

x1_tgt_pipe5_2 = 0.12624
z1_tgt_pipe5_2 = 3.9096 + 0.0508

x4_tgt_pipe5_2 = 0.12624
z4_tgt_pipe5_2 = 3.9096 + 0.0508 + 0.22739

x3_tgt_pipe5_2 = 0.13894
z3_tgt_pipe5_2 = 3.9096 + 0.0508 + 0.22739

tgt_pipe5_2_up = polygon(
    (
        [z1_tgt_pipe5_2, x1_tgt_pipe5_2],
        [z4_tgt_pipe5_2, x4_tgt_pipe5_2],
        [z3_tgt_pipe5_2, x3_tgt_pipe5_2],
        [z2_tgt_pipe5_2, x2_tgt_pipe5_2],
    ),
    notSource=False,
)
tgt_pipe5_2_lo = polygon(
    (
        [z2_tgt_pipe5_2, -x2_tgt_pipe5_2],
        [z3_tgt_pipe5_2, -x3_tgt_pipe5_2],
        [z4_tgt_pipe5_2, -x4_tgt_pipe5_2],
        [z1_tgt_pipe5_2, -x1_tgt_pipe5_2],
    ),
    notSource=False,
)

##part3
x2_tgt_pipe5_3 = 0.127
z2_tgt_pipe5_3 = 3.9096 + 0.0508 + 0.22739

x1_tgt_pipe5_3 = 0.12624
z1_tgt_pipe5_3 = 3.9096 + 0.0508 + 0.22739

x4_tgt_pipe5_3 = 0.12624
z4_tgt_pipe5_3 = 3.9096 + 0.0508 + 0.22739 + 0.0508

x3_tgt_pipe5_3 = 0.127
z3_tgt_pipe5_3 = 3.9096 + 0.0508 + 0.22739 + 0.0508

tgt_pipe5_3_up = polygon(
    (
        [z1_tgt_pipe5_3, x1_tgt_pipe5_3],
        [z4_tgt_pipe5_3, x4_tgt_pipe5_3],
        [z3_tgt_pipe5_3, x3_tgt_pipe5_3],
        [z2_tgt_pipe5_3, x2_tgt_pipe5_3],
    ),
    notSource=False,
)
tgt_pipe5_3_lo = polygon(
    (
        [z2_tgt_pipe5_3, -x2_tgt_pipe5_3],
        [z3_tgt_pipe5_3, -x3_tgt_pipe5_3],
        [z4_tgt_pipe5_3, -x4_tgt_pipe5_3],
        [z1_tgt_pipe5_3, -x1_tgt_pipe5_3],
    ),
    notSource=False,
)

####Flange 5
###Part1
##section1
x2_tgt_flange5_1_1 = 0.152995
z2_tgt_flange5_1_1 = 4.24945

x1_tgt_flange5_1_1 = 0.127255
z1_tgt_flange5_1_1 = 4.24945

x4_tgt_flange5_1_1 = 0.127255
z4_tgt_flange5_1_1 = 4.24945 + 0.01575

x3_tgt_flange5_1_1 = 0.152995
z3_tgt_flange5_1_1 = 4.24945 + 0.01575

tgt_flange5_1_1_up = polygon(
    (
        [z1_tgt_flange5_1_1, x1_tgt_flange5_1_1],
        [z4_tgt_flange5_1_1, x4_tgt_flange5_1_1],
        [z3_tgt_flange5_1_1, x3_tgt_flange5_1_1],
        [z2_tgt_flange5_1_1, x2_tgt_flange5_1_1],
    ),
    notSource=False,
)
tgt_flange5_1_1_lo = polygon(
    (
        [z2_tgt_flange5_1_1, -x2_tgt_flange5_1_1],
        [z3_tgt_flange5_1_1, -x3_tgt_flange5_1_1],
        [z4_tgt_flange5_1_1, -x4_tgt_flange5_1_1],
        [z1_tgt_flange5_1_1, -x1_tgt_flange5_1_1],
    ),
    notSource=False,
)

##section2
x2_tgt_flange5_1_2 = 0.152995
z2_tgt_flange5_1_2 = 4.24945 + 0.01575

x1_tgt_flange5_1_2 = 0.123825
z1_tgt_flange5_1_2 = 4.24945 + 0.01575

x4_tgt_flange5_1_2 = 0.123825
z4_tgt_flange5_1_2 = 4.24945 + 0.01575 + 0.0127

x3_tgt_flange5_1_2 = 0.152995
z3_tgt_flange5_1_2 = 4.24945 + 0.01575 + 0.0127

tgt_flange5_1_2_up = polygon(
    (
        [z1_tgt_flange5_1_2, x1_tgt_flange5_1_2],
        [z4_tgt_flange5_1_2, x4_tgt_flange5_1_2],
        [z3_tgt_flange5_1_2, x3_tgt_flange5_1_2],
        [z2_tgt_flange5_1_2, x2_tgt_flange5_1_2],
    ),
    notSource=False,
)
tgt_flange5_1_2_lo = polygon(
    (
        [z2_tgt_flange5_1_2, -x2_tgt_flange5_1_2],
        [z3_tgt_flange5_1_2, -x3_tgt_flange5_1_2],
        [z4_tgt_flange5_1_2, -x4_tgt_flange5_1_2],
        [z1_tgt_flange5_1_2, -x1_tgt_flange5_1_2],
    ),
    notSource=False,
)

###Part2
##section1
x2_tgt_flange5_2_1 = 0.152995
z2_tgt_flange5_2_1 = 4.2779

x1_tgt_flange5_2_1 = 0.123825
z1_tgt_flange5_2_1 = 4.2779

x4_tgt_flange5_2_1 = 0.123825
z4_tgt_flange5_2_1 = 4.2779 + 0.0127

x3_tgt_flange5_2_1 = 0.152995
z3_tgt_flange5_2_1 = 4.2779 + 0.0127

tgt_flange5_2_1_up = polygon(
    (
        [z1_tgt_flange5_2_1, x1_tgt_flange5_2_1],
        [z4_tgt_flange5_2_1, x4_tgt_flange5_2_1],
        [z3_tgt_flange5_2_1, x3_tgt_flange5_2_1],
        [z2_tgt_flange5_2_1, x2_tgt_flange5_2_1],
    ),
    notSource=False,
)
tgt_flange5_2_1_lo = polygon(
    (
        [z2_tgt_flange5_2_1, -x2_tgt_flange5_2_1],
        [z3_tgt_flange5_2_1, -x3_tgt_flange5_2_1],
        [z4_tgt_flange5_2_1, -x4_tgt_flange5_2_1],
        [z1_tgt_flange5_2_1, -x1_tgt_flange5_2_1],
    ),
    notSource=False,
)

##section2
x2_tgt_flange5_2_2 = 0.152995
z2_tgt_flange5_2_2 = 4.2779 + 0.0127

x1_tgt_flange5_2_2 = 0.127255
z1_tgt_flange5_2_2 = 4.2779 + 0.0127

x4_tgt_flange5_2_2 = 0.127255
z4_tgt_flange5_2_2 = 4.2779 + 0.01575 + 0.0127

x3_tgt_flange5_2_2 = 0.152995
z3_tgt_flange5_2_2 = 4.2779 + 0.01575 + 0.0127

tgt_flange5_2_2_up = polygon(
    (
        [z1_tgt_flange5_2_2, x1_tgt_flange5_2_2],
        [z4_tgt_flange5_2_2, x4_tgt_flange5_2_2],
        [z3_tgt_flange5_2_2, x3_tgt_flange5_2_2],
        [z2_tgt_flange5_2_2, x2_tgt_flange5_2_2],
    ),
    notSource=False,
)
tgt_flange5_2_2_lo = polygon(
    (
        [z2_tgt_flange5_2_2, -x2_tgt_flange5_2_2],
        [z3_tgt_flange5_2_2, -x3_tgt_flange5_2_2],
        [z4_tgt_flange5_2_2, -x4_tgt_flange5_2_2],
        [z1_tgt_flange5_2_2, -x1_tgt_flange5_2_2],
    ),
    notSource=False,
)

###Next pipe
##part1
x2_tgt_pipe6_1 = 0.127
z2_tgt_pipe6_1 = 4.2906

x1_tgt_pipe6_1 = 0.12065
z1_tgt_pipe6_1 = 4.2906

x4_tgt_pipe6_1 = 0.12065
z4_tgt_pipe6_1 = 4.2906 + 0.127

x3_tgt_pipe6_1 = 0.127
z3_tgt_pipe6_1 = 4.2906 + 0.127

tgt_pipe6_1_up = polygon(
    (
        [z1_tgt_pipe6_1, x1_tgt_pipe6_1],
        [z4_tgt_pipe6_1, x4_tgt_pipe6_1],
        [z3_tgt_pipe6_1, x3_tgt_pipe6_1],
        [z2_tgt_pipe6_1, x2_tgt_pipe6_1],
    ),
    notSource=False,
)
tgt_pipe6_1_lo = polygon(
    (
        [z2_tgt_pipe6_1, -x2_tgt_pipe6_1],
        [z3_tgt_pipe6_1, -x3_tgt_pipe6_1],
        [z4_tgt_pipe6_1, -x4_tgt_pipe6_1],
        [z1_tgt_pipe6_1, -x1_tgt_pipe6_1],
    ),
    notSource=False,
)


################################################################

###### Lead collar (for collimating photons)

# seg 1
x1_collar = 0.0762  # +0.05
z1_collar = 3.300  # +1.5
# z1_collar=3.12202#+1.5

x2_collar = 0.330  # *1.414 The collar is a rectangle (in CAD), but the narrow dimension is the one relevant for here
z2_collar = 3.300  # +1.5
# z2_collar=3.12202#+1.5

x3_collar = 0.330  # *1.414
z3_collar = 3.500  # +1.5
# z3_collar=3.32202#+1.5

x4_collar = 0.0762  # +0.05
z4_collar = 3.500  # +1.5
# z4_collar=3.32202#+1.5


collar_top = polygon(
    (
        [z1_collar, x1_collar],
        [z4_collar, x4_collar],
        [z3_collar, x3_collar],
        [z2_collar, x2_collar],
    ),
    notSource=False,
)
collar_bottom = polygon(
    (
        [z2_collar, -x2_collar],
        [z3_collar, -x3_collar],
        [z4_collar, -x4_collar],
        [z1_collar, -x1_collar],
    ),
    notSource=False,
)


###### Beam pipe after lead collar and collimator 2
x1_pipe17 = 0.096825
z1_pipe17 = 1.600

x2_pipe17 = 0.1016
z2_pipe17 = 1.600

x3_pipe17 = 0.1016
z3_pipe17 = 2.49123

x4_pipe17 = 0.096825
z4_pipe17 = 2.49123

coll_pipe171 = polygon(
    (
        [z1_pipe17, x1_pipe17],
        [z4_pipe17, x4_pipe17],
        [z3_pipe17, x3_pipe17],
        [z2_pipe17, x2_pipe17],
    ),
    notSource=False,
)
coll_pipe172 = polygon(
    (
        [z2_pipe17, -x2_pipe17],
        [z3_pipe17, -x3_pipe17],
        [z4_pipe17, -x4_pipe17],
        [z1_pipe17, -x1_pipe17],
    ),
    notSource=False,
)

# flange
x1_pipe18 = 0.1016
z1_pipe18 = 2.49123

x2_pipe18 = 0.20955
z2_pipe18 = 2.49123

x3_pipe18 = 0.20955
z3_pipe18 = 2.49123 + 0.05715

x4_pipe18 = 0.1016
z4_pipe18 = 2.49123 + 0.05715

coll_pipe181 = polygon(
    (
        [z1_pipe18, x1_pipe18],
        [z4_pipe18, x4_pipe18],
        [z3_pipe18, x3_pipe18],
        [z2_pipe18, x2_pipe18],
    ),
    notSource=False,
)
coll_pipe182 = polygon(
    (
        [z2_pipe18, -x2_pipe18],
        [z3_pipe18, -x3_pipe18],
        [z4_pipe18, -x4_pipe18],
        [z1_pipe18, -x1_pipe18],
    ),
    notSource=False,
)

x1_pipe19 = 0.17145
z1_pipe19 = 2.49123 + 0.05715

x2_pipe19 = 0.1778
z2_pipe19 = 2.49123 + 0.05715

x3_pipe19 = 0.1778
z3_pipe19 = 5.975

x4_pipe19 = 0.17145
z4_pipe19 = 5.975

coll_pipe191 = polygon(
    (
        [z1_pipe19, x1_pipe19],
        [z4_pipe19, x4_pipe19],
        [z3_pipe19, x3_pipe19],
        [z2_pipe19, x2_pipe19],
    ),
    notSource=False,
)
coll_pipe192 = polygon(
    (
        [z2_pipe19, -x2_pipe19],
        [z3_pipe19, -x3_pipe19],
        [z4_pipe19, -x4_pipe19],
        [z1_pipe19, -x1_pipe19],
    ),
    notSource=False,
)

# flange
x1_pipe20 = 0.1778
z1_pipe20 = 5.975

x2_pipe20 = 0.34449
z2_pipe20 = 5.975

x3_pipe20 = 0.34449
z3_pipe20 = 5.975 + 0.08255

x4_pipe20 = 0.1778
z4_pipe20 = 5.975 + 0.08255

coll_pipe201 = polygon(
    (
        [z1_pipe20, x1_pipe20],
        [z4_pipe20, x4_pipe20],
        [z3_pipe20, x3_pipe20],
        [z2_pipe20, x2_pipe20],
    ),
    notSource=False,
)
coll_pipe202 = polygon(
    (
        [z2_pipe20, -x2_pipe20],
        [z3_pipe20, -x3_pipe20],
        [z4_pipe20, -x4_pipe20],
        [z1_pipe20, -x1_pipe20],
    ),
    notSource=False,
)

x1_pipe21 = 0.295275
z1_pipe21 = 5.975 + 0.08255

x2_pipe21 = 0.3048
z2_pipe21 = 5.975 + 0.08255

x3_pipe21 = 0.3048
z3_pipe21 = 8.250682

x4_pipe21 = 0.295275
z4_pipe21 = 8.250682

coll_pipe211 = polygon(
    (
        [z1_pipe21, x1_pipe21],
        [z4_pipe21, x4_pipe21],
        [z3_pipe21, x3_pipe21],
        [z2_pipe21, x2_pipe21],
    ),
    notSource=False,
)
coll_pipe212 = polygon(
    (
        [z2_pipe21, -x2_pipe21],
        [z3_pipe21, -x3_pipe21],
        [z4_pipe21, -x4_pipe21],
        [z1_pipe21, -x1_pipe21],
    ),
    notSource=False,
)

# front plate for vacuum vessels
x1_pipe22 = 0.250063
z1_pipe22 = 8.250682

x2_pipe22 = 1.36525
z2_pipe22 = 8.250682

x3_pipe22 = 1.36525
z3_pipe22 = 8.250682 + 0.068326

x4_pipe22 = 0.250063
z4_pipe22 = 8.250682 + 0.068326

coll_pipe221 = polygon(
    (
        [z1_pipe22, x1_pipe22],
        [z4_pipe22, x4_pipe22],
        [z3_pipe22, x3_pipe22],
        [z2_pipe22, x2_pipe22],
    ),
    notSource=False,
)
coll_pipe222 = polygon(
    (
        [z2_pipe22, -x2_pipe22],
        [z3_pipe22, -x3_pipe22],
        [z4_pipe22, -x4_pipe22],
        [z1_pipe22, -x1_pipe22],
    ),
    notSource=False,
)

x1_pipe23 = 1.250188
z1_pipe23 = 8.250682 + 0.068326

x2_pipe23 = 1275.588
z2_pipe23 = 8.250682 + 0.068326

x3_pipe23 = 1275.588
z3_pipe23 = 12.300 + 4.5 - 0.068326

x4_pipe23 = 1.250188
z4_pipe23 = 12.300 + 4.5 - 0.068326

coll_pipe231 = polygon(
    (
        [z1_pipe23, x1_pipe23],
        [z4_pipe23, x4_pipe23],
        [z3_pipe23, x3_pipe23],
        [z2_pipe23, x2_pipe23],
    ),
    notSource=False,
)
coll_pipe232 = polygon(
    (
        [z2_pipe23, -x2_pipe23],
        [z3_pipe23, -x3_pipe23],
        [z4_pipe23, -x4_pipe23],
        [z1_pipe23, -x1_pipe23],
    ),
    notSource=False,
)

x1_pipe24 = 0.595
z1_pipe24 = 12.300 + 4.5 - 0.068326

x2_pipe24 = 1.36525
z2_pipe24 = 12.300 + 4.5 - 0.068326

x3_pipe24 = 1.36525
z3_pipe24 = 12.300 + 4.5

x4_pipe24 = 0.595
z4_pipe24 = 12.300 + 4.5

coll_pipe241 = polygon(
    (
        [z1_pipe24, x1_pipe24],
        [z4_pipe24, x4_pipe24],
        [z3_pipe24, x3_pipe24],
        [z2_pipe24, x2_pipe24],
    ),
    notSource=False,
)
coll_pipe242 = polygon(
    (
        [z2_pipe24, -x2_pipe24],
        [z3_pipe24, -x3_pipe24],
        [z4_pipe24, -x4_pipe24],
        [z1_pipe24, -x1_pipe24],
    ),
    notSource=False,
)
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

#################################################################

######inner photon collimator (Col 1)
# Updated on Nov 8 2020 with merged extended collimator

x1_inner_photon_1 = 0.020 + 0.0003
z1_inner_photon_1 = 4.675 + 0.15

x2_inner_photon_1 = 0.0295
z2_inner_photon_1 = 4.675 + 0.15

x3_inner_photon_1 = 0.02974
z3_inner_photon_1 = 4.775 + 0.15

x4_inner_photon_1 = 0.01625 + 0.0003
z4_inner_photon_1 = 4.775 + 0.15

x1_inner_photon_2 = 0.01625 + 0.0003
z1_inner_photon_2 = 4.775 + 0.15

x2_inner_photon_2 = 0.02974
z2_inner_photon_2 = 4.775 + 0.15

x3_inner_photon_2 = 0.02995
z3_inner_photon_2 = 4.865 + 0.15

x4_inner_photon_2 = 0.0151 + 0.0003
z4_inner_photon_2 = 4.865 + 0.15

x1_inner_photon_3 = 0.0151 + 0.0003
z1_inner_photon_3 = 4.865 + 0.15

x2_inner_photon_3 = 0.02995
z2_inner_photon_3 = 4.865 + 0.15

x3_inner_photon_3 = 0.03023
z3_inner_photon_3 = 4.985 + 0.15

x4_inner_photon_3 = 0.0141 + 0.0003
z4_inner_photon_3 = 4.985 + 0.15

x1_inner_photon_4 = 0.0141 + 0.0003
z1_inner_photon_4 = 4.985 + 0.15

x2_inner_photon_4 = 0.03023
z2_inner_photon_4 = 4.985 + 0.15

x3_inner_photon_4 = 0.0305
z3_inner_photon_4 = 5.075 + 0.15

x4_inner_photon_4 = 0.0139
z4_inner_photon_4 = 5.075 + 0.15

x1_inner_photon_5 = 0.0139
z1_inner_photon_5 = 5.075 + 0.15

x2_inner_photon_5 = 0.0305
z2_inner_photon_5 = 5.075 + 0.15

x3_inner_photon_5 = 0.0275
z3_inner_photon_5 = 5.40

x4_inner_photon_5 = 0.014536
z4_inner_photon_5 = 5.40

x1_inner_photon_6 = 0.0139  # not used now 12/01/2021
z1_inner_photon_6 = 5.290

x2_inner_photon_6 = 0.0275
z2_inner_photon_6 = 5.290

x3_inner_photon_6 = 0.0275
z3_inner_photon_6 = 5.390

x4_inner_photon_6 = 0.013908
z4_inner_photon_6 = 5.390

# one has to assign the coordinates in anti-clock sequence
coll_inner_photon_top_1 = polygon(
    (
        [z1_inner_photon_1, x1_inner_photon_1],
        [z4_inner_photon_1, x4_inner_photon_1],
        [z3_inner_photon_1, x3_inner_photon_1],
        [z2_inner_photon_1, x2_inner_photon_1],
    ),
    notSource=False,
)
coll_inner_photon_bottom_1 = polygon(
    (
        [z2_inner_photon_1, -x2_inner_photon_1],
        [z3_inner_photon_1, -x3_inner_photon_1],
        [z4_inner_photon_1, -x4_inner_photon_1],
        [z1_inner_photon_1, -x1_inner_photon_1],
    ),
    notSource=False,
)

coll_inner_photon_top_2 = polygon(
    (
        [z1_inner_photon_2, x1_inner_photon_2],
        [z4_inner_photon_2, x4_inner_photon_2],
        [z3_inner_photon_2, x3_inner_photon_2],
        [z2_inner_photon_2, x2_inner_photon_2],
    ),
    notSource=False,
)
coll_inner_photon_bottom_2 = polygon(
    (
        [z2_inner_photon_2, -x2_inner_photon_2],
        [z3_inner_photon_2, -x3_inner_photon_2],
        [z4_inner_photon_2, -x4_inner_photon_2],
        [z1_inner_photon_2, -x1_inner_photon_2],
    ),
    notSource=False,
)

coll_inner_photon_top_3 = polygon(
    (
        [z1_inner_photon_3, x1_inner_photon_3],
        [z4_inner_photon_3, x4_inner_photon_3],
        [z3_inner_photon_3, x3_inner_photon_3],
        [z2_inner_photon_3, x2_inner_photon_3],
    ),
    notSource=False,
)
coll_inner_photon_bottom_3 = polygon(
    (
        [z2_inner_photon_3, -x2_inner_photon_3],
        [z3_inner_photon_3, -x3_inner_photon_3],
        [z4_inner_photon_3, -x4_inner_photon_3],
        [z1_inner_photon_3, -x1_inner_photon_3],
    ),
    notSource=False,
)

coll_inner_photon_top_4 = polygon(
    (
        [z1_inner_photon_4, x1_inner_photon_4],
        [z4_inner_photon_4, x4_inner_photon_4],
        [z3_inner_photon_4, x3_inner_photon_4],
        [z2_inner_photon_4, x2_inner_photon_4],
    ),
    notSource=False,
)
coll_inner_photon_bottom_4 = polygon(
    (
        [z2_inner_photon_4, -x2_inner_photon_4],
        [z3_inner_photon_4, -x3_inner_photon_4],
        [z4_inner_photon_4, -x4_inner_photon_4],
        [z1_inner_photon_4, -x1_inner_photon_4],
    ),
    notSource=False,
)

coll_inner_photon_top_5 = polygon(
    (
        [z1_inner_photon_5, x1_inner_photon_5],
        [z4_inner_photon_5, x4_inner_photon_5],
        [z3_inner_photon_5, x3_inner_photon_5],
        [z2_inner_photon_5, x2_inner_photon_5],
    ),
    notSource=False,
)
coll_inner_photon_bottom_5 = polygon(
    (
        [z2_inner_photon_5, -x2_inner_photon_5],
        [z3_inner_photon_5, -x3_inner_photon_5],
        [z4_inner_photon_5, -x4_inner_photon_5],
        [z1_inner_photon_5, -x1_inner_photon_5],
    ),
    notSource=False,
)

# coll_inner_photon_top_6    = polygon( ([z1_inner_photon_6,  x1_inner_photon_6], [z4_inner_photon_6,  x4_inner_photon_6], [z3_inner_photon_6,  x3_inner_photon_6], [z2_inner_photon_6,  x2_inner_photon_6] ), notSource=False)
# coll_inner_photon_bottom_6 = polygon( ([z2_inner_photon_6, -x2_inner_photon_6], [z3_inner_photon_6, -x3_inner_photon_6], [z4_inner_photon_6, -x4_inner_photon_6], [z1_inner_photon_6, -x1_inner_photon_6] ), notSource=False)


#########collimator 2,  three segments
# seg 1
x1_coll_2_1 = -0.035
z1_coll_2_1 = 5.25

x2_coll_2_1 = -0.0275
z2_coll_2_1 = 5.25

x3_coll_2_1 = -0.0275
z3_coll_2_1 = 5.4

x4_coll_2_1 = -0.035
z4_coll_2_1 = 5.4


coll_2_1 = polygon(
    (
        [z1_coll_2_1, x1_coll_2_1],
        [z4_coll_2_1, x4_coll_2_1],
        [z3_coll_2_1, x3_coll_2_1],
        [z2_coll_2_1, x2_coll_2_1],
    ),
    notSource=False,
)
# coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), isDetector=True)


# seg 2

x1_coll_2_2 = -0.150
z1_coll_2_2 = 5.25

x2_coll_2_2 = -0.101
z2_coll_2_2 = 5.25

x3_coll_2_2 = -0.101
z3_coll_2_2 = 5.4

x4_coll_2_2 = -0.15
z4_coll_2_2 = 5.4

coll_2_2 = polygon(
    (
        [z1_coll_2_2, x1_coll_2_2],
        [z4_coll_2_2, x4_coll_2_2],
        [z3_coll_2_2, x3_coll_2_2],
        [z2_coll_2_2, x2_coll_2_2],
    ),
    notSource=False,
)
# coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), isDetector=True)

# seg 3

x1_coll_2_3 = 0.0275
z1_coll_2_3 = 5.25

x2_coll_2_3 = 0.150
z2_coll_2_3 = 5.25

x3_coll_2_3 = 0.1500
z3_coll_2_3 = 5.4

x4_coll_2_3 = 0.0275
z4_coll_2_3 = 5.4


coll_2_3 = polygon(
    (
        [z1_coll_2_3, x1_coll_2_3],
        [z4_coll_2_3, x4_coll_2_3],
        [z3_coll_2_3, x3_coll_2_3],
        [z2_coll_2_3, x2_coll_2_3],
    ),
    notSource=False,
)
# coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), isDetector=True)

##############Upstream coil#######################

x1_US_coil = 0.03016
z1_US_coil = 5.60882

x2_US_coil = 0.03016 + 0.21793
z2_US_coil = 5.60882

x3_US_coil = 0.034767 + 0.22758
z3_US_coil = 7.38632

x4_US_coil = 0.034767
z4_US_coil = 7.38632

US_Coil = polygon(
    (
        [z1_US_coil, x1_US_coil],
        [z4_US_coil, x4_US_coil],
        [z3_US_coil, x3_US_coil],
        [z2_US_coil, x2_US_coil],
    ),
    notSource=False,
)

############# Col2 photon collimating inner_pipe
##pipe
x1_pipe0 = 0.027  # 0.0205
z1_pipe0 = 5.4

x2_pipe0 = 0.030  # 0.0235
z2_pipe0 = 5.4

x3_pipe0 = 0.030  # 0.0305
z3_pipe0 = 7.2

x4_pipe0 = 0.027  # 0.0275
z4_pipe0 = 7.2


coll_pipe01 = polygon(
    (
        [z1_pipe0, x1_pipe0],
        [z4_pipe0, x4_pipe0],
        [z3_pipe0, x3_pipe0],
        [z2_pipe0, x2_pipe0],
    ),
    notSource=False,
)
coll_pipe02 = polygon(
    (
        [z2_pipe0, -x2_pipe0],
        [z3_pipe0, -x3_pipe0],
        [z4_pipe0, -x4_pipe0],
        [z1_pipe0, -x1_pipe0],
    ),
    notSource=False,
)

##############Upstream vessel###############
# Fornt Plate upper part
x1_USCAN_Front_up = 0.127
z1_USCAN_Front_up = 4.36553

x2_USCAN_Front_up = 0.3302
z2_USCAN_Front_up = 4.36553

x3_USCAN_Front_up = 0.3302
z3_USCAN_Front_up = 4.36553 + 0.0508

x4_USCAN_Front_up = 0.127
z4_USCAN_Front_up = 4.36553 + 0.0508


USCAN_Front_up = polygon(
    (
        [z1_USCAN_Front_up, x1_USCAN_Front_up],
        [z4_USCAN_Front_up, x4_USCAN_Front_up],
        [z3_USCAN_Front_up, x3_USCAN_Front_up],
        [z2_USCAN_Front_up, x2_USCAN_Front_up],
    ),
    notSource=False,
)

# Fornt Plate lower part
x1_USCAN_Front_low = -0.4826
z1_USCAN_Front_low = 4.36553

x2_USCAN_Front_low = -0.127
z2_USCAN_Front_low = 4.36553

x3_USCAN_Front_low = -0.127
z3_USCAN_Front_low = 4.36553 + 0.0508

x4_USCAN_Front_low = -0.4826
z4_USCAN_Front_low = 4.36553 + 0.0508


USCAN_Front_low = polygon(
    (
        [z1_USCAN_Front_low, x1_USCAN_Front_low],
        [z4_USCAN_Front_low, x4_USCAN_Front_low],
        [z3_USCAN_Front_low, x3_USCAN_Front_low],
        [z2_USCAN_Front_low, x2_USCAN_Front_low],
    ),
    notSource=False,
)

# Base plate
x1_USCAN_Bot = -0.4826 - 0.09525
z1_USCAN_Bot = 4.28933

x2_USCAN_Bot = -0.4826
z2_USCAN_Bot = 4.28933

x3_USCAN_Bot = -0.4826
z3_USCAN_Bot = 4.28933 + 4.0521

x4_USCAN_Bot = -0.4826 - 0.09525
z4_USCAN_Bot = 4.28933 + 4.0521


USCAN_Bot = polygon(
    (
        [z1_USCAN_Bot, x1_USCAN_Bot],
        [z4_USCAN_Bot, x4_USCAN_Bot],
        [z3_USCAN_Bot, x3_USCAN_Bot],
        [z2_USCAN_Bot, x2_USCAN_Bot],
    ),
    notSource=False,
)

# Top plate
x1_USCAN_Top = 0.33020
z1_USCAN_Top = 4.39093

x2_USCAN_Top = 0.33020 + 0.0254
z2_USCAN_Top = 4.39093

x3_USCAN_Top = 0.33020 + 0.0254
z3_USCAN_Top = 4.39093 + 3.8489

x4_USCAN_Top = 0.33020
z4_USCAN_Top = 4.39093 + 3.8489


USCAN_Top = polygon(
    (
        [z1_USCAN_Top, x1_USCAN_Top],
        [z4_USCAN_Top, x4_USCAN_Top],
        [z3_USCAN_Top, x3_USCAN_Top],
        [z2_USCAN_Top, x2_USCAN_Top],
    ),
    notSource=False,
)

# Back Plate upper part
x1_USCAN_Back_up = 0.23635
z1_USCAN_Back_up = 8.21443

x2_USCAN_Back_up = 0.3302
z2_USCAN_Back_up = 8.21443

x3_USCAN_Back_up = 0.3302
z3_USCAN_Back_up = 8.21443 + 0.0508

x4_USCAN_Back_up = 0.23635
z4_USCAN_Back_up = 8.21443 + 0.0508


USCAN_Back_up = polygon(
    (
        [z1_USCAN_Back_up, x1_USCAN_Back_up],
        [z4_USCAN_Back_up, x4_USCAN_Back_up],
        [z3_USCAN_Back_up, x3_USCAN_Back_up],
        [z2_USCAN_Back_up, x2_USCAN_Back_up],
    ),
    notSource=False,
)

# Back Plate lower part
x1_USCAN_Back_low = -0.4826
z1_USCAN_Back_low = 8.21443

x2_USCAN_Back_low = -0.23635
z2_USCAN_Back_low = 8.21443

x3_USCAN_Back_low = -0.23635
z3_USCAN_Back_low = 8.21443 + 0.0508

x4_USCAN_Back_low = -0.4826
z4_USCAN_Back_low = 8.21443 + 0.0508


USCAN_Back_low = polygon(
    (
        [z1_USCAN_Back_low, x1_USCAN_Back_low],
        [z4_USCAN_Back_low, x4_USCAN_Back_low],
        [z3_USCAN_Back_low, x3_USCAN_Back_low],
        [z2_USCAN_Back_low, x2_USCAN_Back_low],
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

##pipe1  the downstream twobounce shield

# epoxy shield pipe1
x1_DSShield_1 = 0.033
z1_DSShield_1 = 9.4

x2_DSShield_1 = 0.039
z2_DSShield_1 = 9.4

x3_DSShield_1 = 0.0395
z3_DSShield_1 = 9.6

x4_DSShield_1 = 0.0345
z4_DSShield_1 = 9.6


DSShield_11 = polygon(
    (
        [z1_DSShield_1, x1_DSShield_1],
        [z4_DSShield_1, x4_DSShield_1],
        [z3_DSShield_1, x3_DSShield_1],
        [z2_DSShield_1, x2_DSShield_1],
    ),
    notSource=False,
)
DSShield_12 = polygon(
    (
        [z2_DSShield_1, -x2_DSShield_1],
        [z3_DSShield_1, -x3_DSShield_1],
        [z4_DSShield_1, -x4_DSShield_1],
        [z1_DSShield_1, -x1_DSShield_1],
    ),
    notSource=False,
)


# epoxy shield pipe2
x1_DSShield_2 = 0.042
z1_DSShield_2 = 11.5

x2_DSShield_2 = 0.045
z2_DSShield_2 = 11.5

x3_DSShield_2 = 0.045
z3_DSShield_2 = 11.67

x4_DSShield_2 = 0.042
z4_DSShield_2 = 11.67


DSShield_21 = polygon(
    (
        [z1_DSShield_2, x1_DSShield_2],
        [z4_DSShield_2, x4_DSShield_2],
        [z3_DSShield_2, x3_DSShield_2],
        [z2_DSShield_2, x2_DSShield_2],
    ),
    notSource=False,
)
DSShield_22 = polygon(
    (
        [z2_DSShield_2, -x2_DSShield_2],
        [z3_DSShield_2, -x3_DSShield_2],
        [z4_DSShield_2, -x4_DSShield_2],
        [z1_DSShield_2, -x1_DSShield_2],
    ),
    notSource=False,
)

x1_pipe1_1 = 0.0305
z1_pipe1_1 = 7.88

x2_pipe1_1 = 0.031
z2_pipe1_1 = 7.88

x3_pipe1_1 = 0.035
z3_pipe1_1 = 9.4

x4_pipe1_1 = 0.0345
z4_pipe1_1 = 9.4


coll_pipe11_1 = polygon(
    (
        [z1_pipe1_1, x1_pipe1_1],
        [z4_pipe1_1, x4_pipe1_1],
        [z3_pipe1_1, x3_pipe1_1],
        [z2_pipe1_1, x2_pipe1_1],
    ),
    notSource=False,
)
coll_pipe12_1 = polygon(
    (
        [z2_pipe1_1, -x2_pipe1_1],
        [z3_pipe1_1, -x3_pipe1_1],
        [z4_pipe1_1, -x4_pipe1_1],
        [z1_pipe1_1, -x1_pipe1_1],
    ),
    notSource=False,
)
##pipe2  the downstream twobounce shield
x1_pipe1_2 = 0.0345
z1_pipe1_2 = 9.405

x2_pipe1_2 = 0.035
z2_pipe1_2 = 9.405

x3_pipe1_2 = 0.0385
z3_pipe1_2 = 10.530

x4_pipe1_2 = 0.038
z4_pipe1_2 = 10.530


coll_pipe11_2 = polygon(
    (
        [z1_pipe1_2, x1_pipe1_2],
        [z4_pipe1_2, x4_pipe1_2],
        [z3_pipe1_2, x3_pipe1_2],
        [z2_pipe1_2, x2_pipe1_2],
    ),
    notSource=False,
)
coll_pipe12_2 = polygon(
    (
        [z2_pipe1_2, -x2_pipe1_2],
        [z3_pipe1_2, -x3_pipe1_2],
        [z4_pipe1_2, -x4_pipe1_2],
        [z1_pipe1_2, -x1_pipe1_2],
    ),
    notSource=False,
)

##pipe3  the downstream twobounce shield
x1_pipe1_3 = 0.038
z1_pipe1_3 = 10.535

x2_pipe1_3 = 0.0385
z2_pipe1_3 = 10.535

x3_pipe1_3 = 0.043
z3_pipe1_3 = 11.590

x4_pipe1_3 = 0.0425
z4_pipe1_3 = 11.590

coll_pipe11_3 = polygon(
    (
        [z1_pipe1_3, x1_pipe1_3],
        [z4_pipe1_3, x4_pipe1_3],
        [z3_pipe1_3, x3_pipe1_3],
        [z2_pipe1_3, x2_pipe1_3],
    ),
    notSource=False,
)
coll_pipe12_3 = polygon(
    (
        [z2_pipe1_3, -x2_pipe1_3],
        [z3_pipe1_3, -x3_pipe1_3],
        [z4_pipe1_3, -x4_pipe1_3],
        [z1_pipe1_3, -x1_pipe1_3],
    ),
    notSource=False,
)

##pipe4  the downstream twobounce shield
x1_pipe1_4 = 0.0425
z1_pipe1_4 = 11.595

x2_pipe1_4 = 0.043
z2_pipe1_4 = 11.595

x3_pipe1_4 = 0.0475
z3_pipe1_4 = 12.615

x4_pipe1_4 = 0.047
z4_pipe1_4 = 12.615

coll_pipe11_4 = polygon(
    (
        [z1_pipe1_4, x1_pipe1_4],
        [z4_pipe1_4, x4_pipe1_4],
        [z3_pipe1_4, x3_pipe1_4],
        [z2_pipe1_4, x2_pipe1_4],
    ),
    notSource=False,
)
coll_pipe12_4 = polygon(
    (
        [z2_pipe1_4, -x2_pipe1_4],
        [z3_pipe1_4, -x3_pipe1_4],
        [z4_pipe1_4, -x4_pipe1_4],
        [z1_pipe1_4, -x1_pipe1_4],
    ),
    notSource=False,
)

##pipe5  the downstream twobounce shield
x1_pipe1_5 = 0.047
z1_pipe1_5 = 12.620

x2_pipe1_5 = 0.0475
z2_pipe1_5 = 12.620

x3_pipe1_5 = 0.062
z3_pipe1_5 = 16.748

x4_pipe1_5 = 0.0615
z4_pipe1_5 = 16.748

coll_pipe11_5 = polygon(
    (
        [z1_pipe1_5, x1_pipe1_5],
        [z4_pipe1_5, x4_pipe1_5],
        [z3_pipe1_5, x3_pipe1_5],
        [z2_pipe1_5, x2_pipe1_5],
    ),
    notSource=False,
)
coll_pipe12_5 = polygon(
    (
        [z2_pipe1_5, -x2_pipe1_5],
        [z3_pipe1_5, -x3_pipe1_5],
        [z4_pipe1_5, -x4_pipe1_5],
        [z1_pipe1_5, -x1_pipe1_5],
    ),
    notSource=False,
)

##pipe6  the downstream twobounce shield
x1_pipe1_6 = 0.0615
z1_pipe1_6 = 16.752

x2_pipe1_6 = 0.062
z2_pipe1_6 = 16.752

x3_pipe1_6 = 0.0765
z3_pipe1_6 = 19.995

x4_pipe1_6 = 0.076
z4_pipe1_6 = 19.995

coll_pipe11_6 = polygon(
    (
        [z1_pipe1_6, x1_pipe1_6],
        [z4_pipe1_6, x4_pipe1_6],
        [z3_pipe1_6, x3_pipe1_6],
        [z2_pipe1_6, x2_pipe1_6],
    ),
    notSource=False,
)
coll_pipe12_6 = polygon(
    (
        [z2_pipe1_6, -x2_pipe1_6],
        [z3_pipe1_6, -x3_pipe1_6],
        [z4_pipe1_6, -x4_pipe1_6],
        [z1_pipe1_6, -x1_pipe1_6],
    ),
    notSource=False,
)


# Downstream beampipe outside the vacuum enclosure
##Downstream window
x1_pipe3 = 0.50476
z1_pipe3 = 23.01512

x2_pipe3 = 0.50714125
z2_pipe3 = 23.01512

x3_pipe3 = 0.988 + 0.00238125
z3_pipe3 = 23.01512 + 0.2804

x4_pipe3 = 0.988
z4_pipe3 = 23.01512 + 0.2804


coll_pipe31 = polygon(
    (
        [z1_pipe3, x1_pipe3],
        [z4_pipe3, x4_pipe3],
        [z3_pipe3, x3_pipe3],
        [z2_pipe3, x2_pipe3],
    ),
    notSource=False,
)
coll_pipe32 = polygon(
    (
        [z2_pipe3, -x2_pipe3],
        [z3_pipe3, -x3_pipe3],
        [z4_pipe3, -x4_pipe3],
        [z1_pipe3, -x1_pipe3],
    ),
    notSource=False,
)

##cylindrical sections
x1_pipe4 = 0.50476
z1_pipe4 = 23.010

x2_pipe4 = 0.50476 + 0.0047625
z2_pipe4 = 23.010

x3_pipe4 = 0.50476 + 0.0047625
z3_pipe4 = 23.010 + 0.454

x4_pipe4 = 0.50476
z4_pipe4 = 23.010 + 0.454

coll_pipe41 = polygon(
    (
        [z1_pipe4, x1_pipe4],
        [z4_pipe4, x4_pipe4],
        [z3_pipe4, x3_pipe4],
        [z2_pipe4, x2_pipe4],
    ),
    notSource=False,
)
coll_pipe42 = polygon(
    (
        [z2_pipe4, -x2_pipe4],
        [z3_pipe4, -x3_pipe4],
        [z4_pipe4, -x4_pipe4],
        [z1_pipe4, -x1_pipe4],
    ),
    notSource=False,
)

##conical pipe
x1_pipe5 = 0.504775
z1_pipe5 = 23.464

x2_pipe5 = 0.504775 + 0.0047625
z2_pipe5 = 23.464

x3_pipe5 = 0.52833 + 0.0047625
z3_pipe5 = 23.464 + 0.6304

x4_pipe5 = 0.52833
z4_pipe5 = 23.464 + 0.6304


coll_pipe51 = polygon(
    (
        [z1_pipe5, x1_pipe5],
        [z4_pipe5, x4_pipe5],
        [z3_pipe5, x3_pipe5],
        [z2_pipe5, x2_pipe5],
    ),
    notSource=False,
)
coll_pipe52 = polygon(
    (
        [z2_pipe5, -x2_pipe5],
        [z3_pipe5, -x3_pipe5],
        [z4_pipe5, -x4_pipe5],
        [z1_pipe5, -x1_pipe5],
    ),
    notSource=False,
)

##flange+bellow
x1_pipe6 = 0.5235
z1_pipe6 = 24.0944

x2_pipe6 = 0.55335
z2_pipe6 = 24.0944

x3_pipe6 = 0.5536
z3_pipe6 = 24.3067

x4_pipe6 = 0.525
z4_pipe6 = 24.3067

coll_pipe61 = polygon(
    (
        [z1_pipe6, x1_pipe6],
        [z4_pipe6, x4_pipe6],
        [z3_pipe6, x3_pipe6],
        [z2_pipe6, x2_pipe6],
    ),
    notSource=False,
)
coll_pipe62 = polygon(
    (
        [z2_pipe6, -x2_pipe6],
        [z3_pipe6, -x3_pipe6],
        [z4_pipe6, -x4_pipe6],
        [z1_pipe6, -x1_pipe6],
    ),
    notSource=False,
)

##conical pipe
x1_pipe7 = 0.5266
z1_pipe7 = 24.3067

x2_pipe7 = 0.5266 + 0.00635
z2_pipe7 = 24.3067

x3_pipe7 = 0.550 + 0.00635
z3_pipe7 = 24.3067 + 0.1873

x4_pipe7 = 0.550
z4_pipe7 = 24.3067 + 0.1873


coll_pipe71 = polygon(
    (
        [z1_pipe7, x1_pipe7],
        [z4_pipe7, x4_pipe7],
        [z3_pipe7, x3_pipe7],
        [z2_pipe7, x2_pipe7],
    ),
    notSource=False,
)
coll_pipe72 = polygon(
    (
        [z2_pipe7, -x2_pipe7],
        [z3_pipe7, -x3_pipe7],
        [z4_pipe7, -x4_pipe7],
        [z1_pipe7, -x1_pipe7],
    ),
    notSource=False,
)


##conical pipe
x1_pipe8 = 0.550
z1_pipe8 = 24.494

x2_pipe8 = 0.550 + 0.01905
z2_pipe8 = 24.494

x3_pipe8 = 0.74645 + 0.01905
z3_pipe8 = 24.494 + 6.506

x4_pipe8 = 0.74645
z4_pipe8 = 24.494 + 6.506

coll_pipe81 = polygon(
    (
        [z1_pipe8, x1_pipe8],
        [z4_pipe8, x4_pipe8],
        [z3_pipe8, x3_pipe8],
        [z2_pipe8, x2_pipe8],
    ),
    notSource=False,
)
coll_pipe82 = polygon(
    (
        [z2_pipe8, -x2_pipe8],
        [z3_pipe8, -x3_pipe8],
        [z4_pipe8, -x4_pipe8],
        [z1_pipe8, -x1_pipe8],
    ),
    notSource=False,
)


##pipe after Vaccum chamber after hybrid
##Step
x1_pipe14 = 0.600
z1_pipe14 = 12.405 + 4.5

x2_pipe14 = 1.2627
z2_pipe14 = 12.405 + 4.5

x3_pipe14 = 1.2627
z3_pipe14 = 12.4431 + 4.5

x4_pipe14 = 0.600
z4_pipe14 = 12.4431 + 4.5

coll_pipe141 = polygon(
    (
        [z1_pipe14, x1_pipe14],
        [z4_pipe14, x4_pipe14],
        [z3_pipe14, x3_pipe14],
        [z2_pipe14, x2_pipe14],
    ),
    notSource=False,
)
coll_pipe142 = polygon(
    (
        [z2_pipe14, -x2_pipe14],
        [z3_pipe14, -x3_pipe14],
        [z4_pipe14, -x4_pipe14],
        [z1_pipe14, -x1_pipe14],
    ),
    notSource=False,
)

##pipe
x1_pipe15 = 1.250
z1_pipe15 = 12.4431 + 4.5

x2_pipe15 = 1.2627
z2_pipe15 = 12.4431 + 4.5

x3_pipe15 = 1.2627
z3_pipe15 = 18.8569 + 4.5

x4_pipe15 = 1.250
z4_pipe15 = 18.8569 + 4.5

coll_pipe151 = polygon(
    (
        [z1_pipe15, x1_pipe15],
        [z4_pipe15, x4_pipe15],
        [z3_pipe15, x3_pipe15],
        [z2_pipe15, x2_pipe15],
    ),
    notSource=False,
)
coll_pipe152 = polygon(
    (
        [z2_pipe15, -x2_pipe15],
        [z3_pipe15, -x3_pipe15],
        [z4_pipe15, -x4_pipe15],
        [z1_pipe15, -x1_pipe15],
    ),
    notSource=False,
)

##Step
x1_pipe16 = 0.952
z1_pipe16 = 18.8569 + 4.5

x2_pipe16 = 1.2627
z2_pipe16 = 18.8569 + 4.5

x3_pipe16 = 1.2627
z3_pipe16 = 18.895 + 4.5

x4_pipe16 = 0.952
z4_pipe16 = 18.895 + 4.5


coll_pipe161 = polygon(
    (
        [z1_pipe16, x1_pipe16],
        [z4_pipe16, x4_pipe16],
        [z3_pipe16, x3_pipe16],
        [z2_pipe16, x2_pipe16],
    ),
    notSource=False,
)
coll_pipe162 = polygon(
    (
        [z2_pipe16, -x2_pipe16],
        [z3_pipe16, -x3_pipe16],
        [z4_pipe16, -x4_pipe16],
        [z1_pipe16, -x1_pipe16],
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

#### sub-quartz array detector to give an idea about the available space before photons become an issue again

sub_det_inner_radius = (
    0.6  # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
)
sub_det_outer_radius = 0.689  # ring 6 quartz ends at 1.2, PMTs begin at 1.3
sub_det_z_pos = 26.5
sub_det_z_extent = 1.0  # was = .02 for ideal detector
# sub_det_inner_radius=0.06 # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
# sub_det_outer_radius=0.689 # ring 6 quartz ends at 1.2, PMTs begin at 1.3
# sub_det_z_pos=6.0
# sub_det_z_extent=1.0 # was = .02 for ideal detector

sub_quartz1 = polygon(
    (
        [sub_det_z_pos, sub_det_inner_radius],
        [sub_det_z_pos + sub_det_z_extent, sub_det_inner_radius],
        [sub_det_z_pos + sub_det_z_extent, sub_det_outer_radius],
        [sub_det_z_pos, sub_det_outer_radius],
    ),
    isDetector=True,
)
sub_quartz2 = polygon(
    (
        [sub_det_z_pos, -sub_det_outer_radius],
        [sub_det_z_pos + sub_det_z_extent, -sub_det_outer_radius],
        [sub_det_z_pos + sub_det_z_extent, -sub_det_inner_radius],
        [sub_det_z_pos, -sub_det_inner_radius],
    ),
    isDetector=True,
)


# quartz1 = polygon( ([28.0, 0.55], [28.02, 0.55], [28.02, 1.3], [28, 1.3]), isDetector=True )
# quartz2 = polygon( ([28.0, -1.3], [28.02, -1.3], [28.02, -0.55], [28, -0.55]), isDetector=True )

##################################################################################################################################

sources.append(target)

# allpolys.append(tgt_US_1)
# allpolys.append(tgt_US_2)
# allpolys.append(tgt_DS_1)
# allpolys.append(tgt_DS_2)

# allpolys.append(tgt_TopShield_top)

# allpolys.append(tgt_DSShield_top)
# allpolys.append(tgt_DSShield_bottom)

# allpolys.append(tgt_barite1_top)
# allpolys.append(tgt_barite1_bottom)

# allpolys.append(tgt_barite2_top)
# allpolys.append(tgt_barite2_bottom)

# allpolys.append(tgt_pipe0_up)
# allpolys.append(tgt_pipe0_lo)

# allpolys.append(tgt_pipe1_up)
# allpolys.append(tgt_pipe1_lo)

allpolys.append(tgt_pipe4_5_up)
allpolys.append(tgt_pipe4_5_lo)

allpolys.append(tgt_flange4_1_1_up)
allpolys.append(tgt_flange4_1_1_lo)
allpolys.append(tgt_flange4_1_2_up)
allpolys.append(tgt_flange4_1_2_lo)
allpolys.append(tgt_flange4_2_1_up)
allpolys.append(tgt_flange4_2_1_lo)
allpolys.append(tgt_flange4_2_2_up)
allpolys.append(tgt_flange4_2_2_lo)

allpolys.append(tgt_pipe5_1_up)
allpolys.append(tgt_pipe5_1_lo)
allpolys.append(tgt_pipe5_2_up)
allpolys.append(tgt_pipe5_2_lo)
allpolys.append(tgt_pipe5_3_up)
allpolys.append(tgt_pipe5_3_lo)

allpolys.append(tgt_flange5_1_1_up)
allpolys.append(tgt_flange5_1_1_lo)
allpolys.append(tgt_flange5_1_2_up)
allpolys.append(tgt_flange5_1_2_lo)
allpolys.append(tgt_flange5_2_1_up)
allpolys.append(tgt_flange5_2_1_lo)
allpolys.append(tgt_flange5_2_2_up)
allpolys.append(tgt_flange5_2_2_lo)

allpolys.append(tgt_pipe6_1_up)
allpolys.append(tgt_pipe6_1_lo)

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

allpolys.append(US_Coil)

allpolys.append(coll_pipe01)
allpolys.append(coll_pipe02)

allpolys.append(USCAN_Front_up)
allpolys.append(USCAN_Front_low)

# allpolys.append(USCAN_Bot)
# allpolys.append(USCAN_Top)

allpolys.append(USCAN_Back_up)
allpolys.append(USCAN_Back_low)

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

# allpolys.append(DSShield_11)
# allpolys.append(DSShield_12)

# allpolys.append(DSShield_21)
# allpolys.append(DSShield_22)

# allpolys.append(coll_pipe11_1)
# allpolys.append(coll_pipe12_1)
#
# allpolys.append(coll_pipe11_2)
# allpolys.append(coll_pipe12_2)
#
# allpolys.append(coll_pipe11_3)
# allpolys.append(coll_pipe12_3)
#
# allpolys.append(coll_pipe11_4)
# allpolys.append(coll_pipe12_4)
#
# allpolys.append(coll_pipe11_5)
# allpolys.append(coll_pipe12_5)
#
# allpolys.append(coll_pipe11_6)
# allpolys.append(coll_pipe12_6)

# allpolys.append(coll_pipe31)
# allpolys.append(coll_pipe32)
#
# allpolys.append(coll_pipe41)
# allpolys.append(coll_pipe42)
#
# allpolys.append(coll_pipe51)
# allpolys.append(coll_pipe52)
#
# allpolys.append(coll_pipe61)
# allpolys.append(coll_pipe62)
#
# allpolys.append(coll_pipe71)
# allpolys.append(coll_pipe72)
#
# allpolys.append(coll_pipe81)
# allpolys.append(coll_pipe82)

# allpolys.append(coll_pipe141)
# allpolys.append(coll_pipe142)

# allpolys.append(coll_pipe151)
# allpolys.append(coll_pipe152)
#
# allpolys.append(coll_pipe161)
# allpolys.append(coll_pipe162)

# allpolys.append(coll_pipe171)
# allpolys.append(coll_pipe172)
#
# allpolys.append(coll_pipe181)
# allpolys.append(coll_pipe182)
#
# allpolys.append(coll_pipe191)
# allpolys.append(coll_pipe192)
#
# allpolys.append(coll_pipe201)
# allpolys.append(coll_pipe202)
#
# allpolys.append(coll_pipe211)
# allpolys.append(coll_pipe212)
#
# allpolys.append(coll_pipe221)
# allpolys.append(coll_pipe222)
#
# allpolys.append(coll_pipe231)
# allpolys.append(coll_pipe232)
#
# allpolys.append(coll_pipe241)
# allpolys.append(coll_pipe242)

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
# allpolys.append(sub_quartz1)
# allpolys.append(sub_quartz2)

########################################################################
#  Rough out blocking areas

# for i in range(6):
#    z = 10 + i*3.0
#    ghost  = polygon(([z,-1.4],[z+0.001,-1.4],[z+0.001,1.4], [z,1.4]), isEthereal=True )
#   ghost  = polygon(([z,-1.4],[z+1.5,-1.4],[z+1.5,1.4], [z,1.4]), isEthereal=True )
#    allpolys.append(ghost)

#  One bounce ghost regions
##################################1
# ghost1a = polygon(([28,-1.4], [28, -1.39], [uscoll1_z-uscoll1_thick/2+0.01, uscoll1_r1_up], [uscoll1_z-uscoll1_thick/2, uscoll1_r1_up]), isEthereal=True)
###############################################2
# ghost1b = polygon(([28,-0.6], [28, -0.59], [uscoll1_z+uscoll1_thick/2+0.01, uscoll1_r1_dn], [uscoll1_z+uscoll1_thick/2, uscoll1_r1_dn]), isEthereal=True)

# ghost2a = polygon(([28,-1.4], [28, -1.39], [dscoll1_z-dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z-dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

# ghost2b = polygon(([28,-0.6], [28, -0.59], [dscoll1_z+dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

# allpolys.append(ghost1a)
# allpolys.append(ghost1b)
# allpolys.append(ghost2a)
# allpolys.append(ghost2b)

#  Raw

# z1 = 6.1
# z2 = 7.1

# t = uscoll2_r2 - uscoll2_r1

# slope = (dscoll2_r1- uscoll2_r1)/(dscoll2_thick/2+dscoll2_z - uscoll2_z-uscoll2_thick/2)

# gr1 = uscoll2_r1 + slope*(z1 - uscoll2_z - uscoll2_thick/2)
# gr2 = uscoll2_r1 + slope*(z2 - uscoll2_z - uscoll2_thick/2)

# smallghost1 = polygon(( [z1, -gr1-t], [z2, -gr2-t], [z2, -gr2], [z1, -gr1]), isEthereal = False)

# print "Ghost blocking points:"
# print smallghost1.pts[0][0], smallghost1.pts[0][1]
# print "\t", smallghost1.pts[3][1]
# print smallghost1.pts[1][0], smallghost1.pts[1][1]
# print "\t", smallghost1.pts[2][1]


# smallghost2 = polygon( ([10.1729, -0.0277], [10.7712, -0.0738], [13.7226, -0.1123], [11.374, -0.0320] ), isEthereal=False)

# smallghost1 = polygon(( [6.3932, -0.0350], [8.0240, -0.0425], [7.6242, -0.0334], [6.2734, -0.0281]), isEthereal = False)
# smallghost2 = polygon( ([10.1729, -0.0277], [10.6515, -0.0566], [13.2529, -0.0882], [11.374, -0.0320] ), isEthereal=False)


# straight z
# smallghost1 = polygon(( [6.2734, -0.0334], [7.6852, -0.0385], [7.6852, -0.0334], [6.2734, -0.0281]), isEthereal = False)
# smallghost2 = polygon( ([10.1729, -0.0277], [10.1729, -0.0566], [11.3749, -0.0566], [11.374, -0.0320] ), isEthereal=False)

# Reduce z
# smallghost1 = polygon(( [6.273, -0.039 ], [7.874, -0.0474], [7.874, -0.0383691664116], [6.273, -0.0274]), isEthereal = False)
# smallghost2 = polygon( ([10.472, -0.0431780215291], [10.472, -0.0697], [12.074, -0.079], [12.074, -0.0490] ), isEthereal=False)

#################################################################
# allpolys.append(smallghost1)
###by YX3
#################################################################

# allpolys.append(smallghost2)

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

# print "Ghost intersections:"

#  Print out ghost region values
# for aghost in [ghost1a, ghost1b, smallghost1]:
#    for aface in aghost.faces:
# 	print "Of ", aface.v1[0], aface.v1[1], " -> ", aface.v2[0], aface.v2[1]
# 	for lface in aface.getlitfaces():
# 	    print "\t", lface.v1[0], lface.v1[1], " -> ", lface.v2[0], lface.v2[1]

mydraw = drawlight(allpolys + sources)

Gtk.main()
