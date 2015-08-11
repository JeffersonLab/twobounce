from math import sqrt

class convex:
    def __init__(self, pts):
	self.pts = self.makeconvex(list(pts))
	self.lit = [False]*len(self.pts)

    def addpoint(self, pt):
	self.pts.append(pt)
	self.pts = self.makeconvex(self.pts)
	self.lit = [False]*len(self.pts)

    def intersects(self, l1, l2, exclude = None):
	for i in range(len(self.pts)):
	    if self.intersects_face(l1, l2, i) and exclude != (i-1+len(self.pts))%len(self.pts) and exclude != i:
		return True
	return False

    def overlaps(self, aconv):
	# Test for overlap such that no point is
	# always to the left of all faces

	for apt in aconv.pts:
	    everright = False
	    for i in range(len(self.pts)):
		if not self.isleft(self.pts[i-1], self.pts[i], apt):
		    everright = True
	    if not everright:
		return True
	return False

    def intersects_face(self, l1, l2, i):
	test1 = self.isleft( l1, l2, self.pts[i-1])
	test2 = self.isleft( l1, l2, self.pts[i])
	return test1 != test2

    def isleft(self, v1, v2, pt):
	# test if point is left of ray v1->v2
	norm = self.calcnorm(v1,v2)
        if (v1[0]-pt[0])*norm[0] + (v1[1]-pt[1])*norm[1] < 0.0:
	    return False
	return True

    def facenorm(self, i):
	#  Unit normal vector to face
	pt1 = self.pts[i-1]
	pt2 = self.pts[i]
	return self.calcnorm(pt1, pt2)

    def calcnorm(self, pt1, pt2):
	# normal unit vector for ray pt1->pt2
	dx = pt2[1] - pt1[1]
	dy = pt1[0] - pt2[0]
	norm = sqrt(dx**2 + dy**2)
	
	dx /= norm
	dy /= norm

	return [dx, dy]

    def makeconvex(self, pts):
	ordered = [pts.pop(0)]
	stale = False
	considered = []

	while len(pts) > 0:
	    toconsider = pts.pop(0)
	    alltoleft = True
	    for apt in pts+ordered[:-1]+considered:
		if not self.isleft(ordered[-1],toconsider,apt):
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

    def getrayareas(self, source):
	# Return convex ray
	# areas given a source
	# Face is lit if ray does not intersect
	# any faces

	newrayareas = []

	for sidx in range(-1, len(source.pts)):
	    for cidx in list(xrange(len(self.pts), -2, -1)):
		smod = (sidx+len(source.pts))%len(source.pts)
		cmod = (cidx+len(self.pts))%len(self.pts)
		if source.intersects( source.pts[smod], self.pts[cmod], exclude=smod):
		    continue
		if self.intersects( source.pts[smod], self.pts[cmod], exclude=cmod):
		    continue

		smod2 = (sidx+1+len(source.pts))%len(source.pts)
		cmod2 = (cidx-1+len(self.pts))%len(self.pts)

		# Now we have one ray which is good
		# Let's see if we can make a triangle of source -> self1, self2
		if not (self.intersects( source.pts[smod], self.pts[cmod2], exclude=cmod2) or self.intersects( source.pts[smod], self.pts[cmod2], exclude=cmod2) ):
		    # we have a triangle
		    newrayareas.append( rayarea( (source.pts[smod], self.pts[cmod]), (source.pts[smod], self.pts[cmod2]), ((source.pts[smod], self.pts[cmod], self.pts[cmod2]) ) ))

		# Let's see if we can make a triangle of source1 -> self1 and source2 -> self2
#		if not source.intersects( source.pts[smod2], self.pts[cmod], exclude=smod2):
#		    newrayareas.append( rayarea( (source.pts[smod], self.pts[cmod]), (source.pts[smod2], self.pts[cmod]), (source.pts[smod], source.pts[smod2], self.pts[cmod])  ))

	return newrayareas



class rayarea(convex):
    def __init__(self, ray1, ray2, pts):
	self.ray1 = ray1
	self.ray2 = ray2
	convex.__init__(self,pts)

    def castshadows(self, c):
	# return sub-rayareas not shadowed
	# by convex area c
	return

    
	
	    



