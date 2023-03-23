from math import sqrt, atan2
import math

# polyres = 0.01
# polyres = 0.15
# polyres = 0.01
polyres = 0.1

CLOCKWISE_WARNING = True  # If warning should be printed over clockwise definition, otherwise exception will be raised


class polyError(Exception):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return repr(self.value)


class face:
    def __init__(
        self, pt1, pt2, isDetector=False, isEthereal=False, notSource=False, parent=None
    ):
        self.v1 = pt1
        self.v2 = pt2
        self.parent = parent
        self.norm = self.calcnorm(pt1, pt2)
        self.lit1 = []  # pairs between 0,1 which is lit
        # of first order lighting
        self.lit2 = []  # pairs between 0,1 which is lit
        # of second order lighting
        self.prob = []  # pairs between 0,1 which is lit
        # and sees detector
        self.isDetector = isDetector
        self.isEthereal = isEthereal
        self.notSource = notSource
        self.length = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

    def getlitfaces(self, order=1):
        if order == 1:
            litspan = self.lit1
        if order == 2:
            litspan = self.lit2
        if order == 3:
            litspan = self.prob

        if len(litspan) == 0:
            return ()

        litfaces = []
        for span in litspan:
            startx = self.v1[0] * (1.0 - span[0]) + span[0] * self.v2[0]
            starty = self.v1[1] * (1.0 - span[0]) + span[0] * self.v2[1]

            stopx = self.v1[0] * (1.0 - span[1]) + span[1] * self.v2[0]
            stopy = self.v1[1] * (1.0 - span[1]) + span[1] * self.v2[1]

            litfaces.append(
                face(
                    [startx, starty],
                    [stopx, stopy],
                    isDetector=self.isDetector,
                    notSource=self.notSource,
                    isEthereal=self.isEthereal,
                    parent=self,
                )
            )

        return litfaces

    def getpoint(self, z):
        if self.length == 0:
            return (self.v1[0], self.v2[0])

        #  Nudge these guys JUST a little to make corners
        #  better behaved
        if z == 0.0:
            z += polyres * 1e-6 / self.length
        if z == 1.0:
            z -= polyres * 1e-6 / self.length

        x = self.v1[0] * (1.0 - z) + z * self.v2[0]
        y = self.v1[1] * (1.0 - z) + z * self.v2[1]

        return (x, y)

    def isleft(self, pt):
        # test if point is left of ray v1->v2
        if (self.v1[0] - pt[0]) * self.norm[0] + (self.v1[1] - pt[1]) * self.norm[
            1
        ] < 0.0:
            return False
        return True

    def intersects(self, v1, v2=None):
        if self.parent:
            return self.parent.intersects(v1, v2)

        if v2:
            f = face(v1, v2)
        else:
            f = v1

        test1 = self.isleft(f.v1)
        test2 = self.isleft(f.v2)
        #  if both points are on one side we can't
        #  intersect
        if test1 == test2:
            return False

        test3 = f.isleft(self.v1)
        test4 = f.isleft(self.v2)
        return test3 != test4

    def calcnorm(self, pt1, pt2):
        # normal unit vector for ray pt1->pt2
        dx = pt2[1] - pt1[1]
        dy = pt1[0] - pt2[0]
        norm = sqrt(dx**2 + dy**2)

        if norm == 0:
            return [0, 0]

        dx /= norm
        dy /= norm

        return [dx, dy]

    def light(self, source, blocking, order):
        #        print "lighting ", self.v1, " -> ", self.v2, " with source ", source.v1, " -> ", source.v2

        idxmax = int(self.length / polyres) + 1

        currlit = False

        for fidx in range(idxmax):
            fz = fidx * polyres / self.length
            blocked = True

            curseesDet = False
            for sidx in range(idxmax):
                sz = sidx * polyres / self.length

                anyBlockage = False

                # Make sure the rays are on the correct sides
                startpt = source.getpoint(sz)
                stoppt = self.getpoint(fz)

                if source.dotwithnorm(startpt, stoppt) <= 0.0:
                    anyBlockage = True

                if self.dotwithnorm(startpt, stoppt) >= 0.0:
                    anyBlockage = True

                # Faster to check this than all faces
                #                if self.islit( fz, order ):
                #                    continue

                if not anyBlockage:
                    for block in blocking:
                        if block.intersects(startpt, stoppt) and not block.isEthereal:
                            anyBlockage = True
                            break

                if not anyBlockage:
                    if not curseesDet:
                        if self.isDetector:
                            startsee = sz
                            curseesDet = True
                    blocked = False
                elif curseesDet:
                    curseesDet = False
                    if self.isDetector:
                        source.addlight(
                            startsee, sz, 3
                        )  # Flag this region as problematic

            if curseesDet:
                if self.isDetector:
                    source.addlight(startsee, sz, 3)  # Flag this region as problematic

            if not blocked and not currlit:
                currlit = True
                startlight = fz

            if blocked and currlit:
                currlit = False
                self.addlight(startlight, fz, order)
        if currlit:
            self.addlight(startlight, fz, order)

    def addlight(self, z1, z2, order=1):
        if self.parent:
            self.parent.addlight(z1, z2, order)

        if order == 1:
            span = self.lit1
        if order == 2:
            span = self.lit2
        if order == 3:
            span = self.prob

        if self.isEthereal:
            print("Adding light ", z1, z2, " to ", span, "!")
        added = False
        for s in span:
            if s[0] <= z1 and z1 <= s[1]:
                if s[1] <= z2:
                    s[1] = z2
                added = True
            elif s[0] <= z2 and z2 <= s[1]:
                if z1 <= s[0]:
                    s[0] = z1
                added = True
            elif s[0] <= z1 and z2 <= s[1]:
                # envelopes the whole thing
                s[0] = z1
                s[1] = z2
                added = True

        if not added:
            span.append([z1, z2])

    def islit(self, z, order=1):
        if self.parent:
            if self.parent.islit(z, order):
                return True

        if order == 1:
            span = self.lit1
        if order == 2:
            span = self.lit2

        for s in span:
            if s[0] <= z and z <= s[1]:
                return True
        return False

    def dotwithnorm(self, p1, p2):
        dotp = self.norm[0] * (p2[0] - p1[0]) + self.norm[1] * (p2[1] - p1[1])

        return dotp


class polygon:
    def __init__(self, pts, isDetector=False, isEthereal=False, notSource=False):
        self.pts = pts
        self.isClockwise(self.pts)
        self.faces = self.makefaces(self.pts, isDetector, isEthereal, notSource)
        self.ispoly()

    def makefaces(self, pt, isDetector=False, isEthereal=False, notSource=False):
        faces = []
        for i in range(len(self.pts)):
            faces.append(
                face(self.pts[i - 1], self.pts[i], isDetector, isEthereal, notSource)
            )
        return faces

    def intersects(self, l1, l2):
        for face in self.faces:
            if face.intersects(l1, l2):
                return True
        return False

    def ispoly(self):
        # Is polygon if no faces intersect
        for idx in range(len(self.faces)):
            thisface = self.faces[idx]

            flist = []

            # Ignore adjoining faces
            if idx == 0:
                flist += self.faces[idx + 2 : -1]
            elif idx == len(self.faces) - 2:
                flist += self.faces[:-3]
            elif idx == len(self.faces) - 1:
                flist += self.faces[1:-2]
            else:
                flist += self.faces[0 : idx - 1]
                flist += self.faces[idx + 2 :]

            for aface in flist:
                if aface.intersects(thisface):
                    raise polyError()
                    return False
        return True

    def makeconvex(self, pts):
        ordered = [pts.pop(0)]
        stale = False
        considered = []

        while len(pts) > 0:
            toconsider = pts.pop(0)
            alltoleft = True
            for apt in pts + ordered[:-1] + considered:
                if not self.isleft(ordered[-1], toconsider, apt):
                    alltoleft = False
            if not alltoleft:
                considered.append(toconsider)
            else:
                ordered.append(toconsider)
                pts += considered
                considered = []
        return ordered

    def isconvexset(self, pts):
        if len(pts) == len(self.makeconvex(list(pts))):
            return True
        return False

    def getCentroid(self, pts):
        x = [p[0] for p in pts]
        y = [p[1] for p in pts]
        return [sum(x) / len(x), sum(y) / len(y)]

    def isClockwise(self, pts):
        center = self.getCentroid(pts)
        getAngle = lambda p: atan2(  # Define function to calculate between x axis and vector formed by the point and the centroid
            p[1] - center[1], p[0] - center[0]
        )
        max_p = max(pts, key=getAngle)  # get the value with the max angle
        max_p_i = pts.index(max_p)  # get the index of such point
        rotate_arr = (  # Rotate the array so that the max point is in front
            pts[max_p_i:] + pts[:max_p_i]
        )

        # Make sure the rotated array is always decreasing. If not, the point are not defined in a clockwise manner.
        prev = getAngle(max_p)  # Set initial value
        for pt in rotate_arr[1:]:
            if getAngle(pt) > prev:
                if CLOCKWISE_WARNING:
                    print("Warning: Geometry not clockwise. Automatically fixing...")
                else:
                    raise polyError("Points not defined in a clockwise manner")
            prev = getAngle(pt)
        self.pts = sorted(pts, key=getAngle, reverse=True)

    def light(self, sourcepolys, polys, order=1):
        sourcefaces = []
        polyfaces = []

        for apoly in sourcepolys:
            sourcefaces += apoly.faces

        for apoly in polys:
            polyfaces += apoly.faces

        for fidx in range(len(self.faces)):
            otherfaces = list(self.faces)
            thisface = otherfaces.pop(fidx)

            for sidx in range(len(sourcefaces)):
                othersources = list(sourcefaces)
                thissource = othersources.pop(sidx)

                if (
                    thissource
                    and not thissource.isEthereal
                    and not thissource.isDetector
                    and not thissource.notSource
                ):
                    if order == 1:
                        thisface.light(
                            thissource, otherfaces + othersources + polyfaces, order
                        )
                    if order == 2:
                        for litface in thissource.getlitfaces(1):
                            thisface.light(
                                litface, otherfaces + othersources + polyfaces, order
                            )
