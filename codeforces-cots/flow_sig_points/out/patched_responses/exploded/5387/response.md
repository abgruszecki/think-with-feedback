<think>
Okay, let's see. The problem is about determining which faces of a box Vasya can see from his position and summing the corresponding numbers. The box is axis-aligned with one corner at (0,0,0) and the opposite at (x1, y1, z1). The six faces each have a number, and we need to check which are visible from (x,y,z).

Hmm. So the main task is to figure out for each face whether Vasya's position is such that he can see that face. Remember that he can't see a face if he's on its plane. Also, each face is part of the box, which is a cuboid. So the six faces are:

Let me list the faces properly. According to the problem statement:

- a1 is on the face lying on the ZOX plane. That's the Y=0 face. The opposite face is Y=y1, which is a2. So if the box is from (0,0,0) to (x1,y1,z1), then the Y=0 face is a1, and Y=y1 is a2.

Similarly, a3 is on the XOY plane (Z=0), and a4 is on Z=z1. Wait, wait. Let me recheck:

Wait, the description says:

a3 is written on the face that lies on the XOY plane. The XOY plane is where z=0. Then a4 is the face parallel to that, which would be z = z1.

a5 is on the YOZ plane (x=0), and a6 is on x=x1.

So the six faces are:

a1: y=0 (the bottom face in Y direction)
a2: y=y1 (the top face)
a3: z=0 (front face in Z direction)
a4: z=z1 (back face)
a5: x=0 (left face)
a6: x=x1 (right face)

Wait, perhaps I should model each face and determine whether Vasya is outside of the box and can see that face.

The approach is: For each of the six faces, determine whether the point (x,y,z) is in a position such that the face is visible. To see a face, the point must be outside the box and on the side of the face. For example, for the a1 face (y=0), the box's y ranges from 0 to y1. If the point's y coordinate is less than 0, then the a1 face is on the positive y side. Wait, no. Let's think: the box is from (0,0,0) to (x1, y1, z1). So for the a1 face, which is on the Y=0 plane, that face is part of the box. So any point outside the box that is on the side where y < 0 would be looking at the a1 face from the outside. Similarly, for the a2 face (y=y1), points with y > y1 would see the a2 face.

So for each face, we need to check if the point is in the region where it can see that face.

So the steps are:

For each of the six faces, check if the point is in a position that would make that face visible.

Let's break down each face:

Face a1 (y=0): The box's y coordinates are from 0 to y1. So, the a1 face is the face at y=0. To see this face, the point must be in the region where y < 0. Also, the x and z coordinates of the point must be such that they are within the projection of the face. Wait, no. Because even if the point is in y <0, but outside the x or z range of the face, then the face is not visible. Wait, but how does that work?

Wait, the face is a rectangle. The a1 face is the Y=0 face, which spans from x=0 to x1, z=0 to z1. So, if Vasya is at (x,y,z) where y <0, and his position is such that the line from him to the center of the face (x1/2, 0, z1/2) doesn't pass through any other face. Wait, no. Because the problem says that if he can see the center of the face, then he can see the number. So it's enough that the line from his position to the center of the face is unobstructed by the box. But since the box is a solid cuboid, if he's outside the box and in a region where the face is visible, then he can see the face.

Wait, but how to determine if a face is visible. The way to think is: for a face to be visible from a point outside the box, the point must lie in the half-space that is "outside" the face, and the line from the point to the face is not blocked by any other part of the box.

But perhaps there's a simpler way. For each face, the direction from the point to the box determines whether that face is visible. For example, for the a1 face (y=0), if the point's y-coordinate is less than 0, then that face is on the positive y side of the box relative to the point. So the point is in the negative y direction of the box's a1 face. But how to determine if that face is visible.

Alternatively, the face is visible if the point is outside the box and lies in the direction perpendicular to the face. For example, the a1 face is at y=0. So, any point with y <0 would see a1 face if the other coordinates are within the box's x and z ranges. Wait, no. Because if the point is at (x,y,z) where x is way larger than x1, then even if y is <0, the face a1 might be visible but not necessarily. Hmm, this is getting complicated.

Wait, maybe the correct approach is: For each face, the face is visible from the point (x,y,z) if the point lies in the region outside the box where, when you project the point onto the axis perpendicular to the face, you are on the side of the face. For example, for the a1 face (y=0), the perpendicular direction is the y-axis. So if the point's y is less than 0, then it's on the negative side of the a1 face. But the a1 face is part of the box's lower y boundary. So, if the point is in y <0, then the a1 face is the closest face in that direction, and thus visible. Wait, but other faces might block it. No, because the box is convex. So, the visibility of each face depends on which direction the point is in relative to the box.

Let me think differently. For each face, the visibility condition is that the point lies in the half-space that is outside the box and in the direction of that face. For example, for the a1 face (y=0), the face is part of the box's lower y boundary. So the half-space for this face is y <0. If the point is in this half-space, then it can see the a1 face only if it's within the x and z range of the face. Wait, no. Because even if the point is in y <0, but x is outside the box's x range (x <0 or x >x1), then the a1 face (which is x from 0 to x1, z from 0 to z1) is not visible. So in that case, the point's projection onto the face's plane would be outside the face's area, so the face isn't visible.

Wait, but how to model this. Let's take an example.

Suppose the box is from (0,0,0) to (1,1,1). The a1 face is the y=0 face. A point (0.5, -1, 0.5) is directly below the a1 face. So yes, he can see the a1 face. But a point (2, -1, 0.5) is to the right of the box. Then, when he looks towards the box, the a1 face's x ranges from 0 to 1, but his x is 2. So the line from (2,-1,0.5) to the center (0.5, 0, 0.5) would go through the a6 face (x=1). So he can't see the a1 face in this case.

So the visibility of the face depends on the point's position relative to all the box's dimensions.

Hmm, this is getting complicated. Maybe the correct approach is to check for each face if the point is in the half-space outside the box in the direction of the face, and also that the projections onto the other axes are within the box's ranges.

Alternatively, think of each face as being on a certain side. For the a1 face (y=0), to see it, the point must be in the region where y <0, and the x is between 0 and x1, and z is between 0 and z1. Wait, no. Because even if the x is outside 0-x1, but the point is in y <0 and z is within 0-z1, then the a1 face is visible only if the x is within 0-x1. Otherwise, looking from x outside, the face might be occluded by another face.

Alternatively, perhaps each face is visible if the point is in the region where:

For a1 (y=0 face):

y <0 and x is between 0 and x1, and z is between 0 and z1.

But wait, in the first example:

Sample Input 1:

2 2 2

1 1 1

1 2 3 4 5 6

So the box is from (0,0,0) to (1,1,1). The point is (2,2,2). So for each face:

a1 is y=0. The point's y is 2, which is greater than 0, so it's in the positive y direction. So a1 is not visible.

a2 is y=1. The point's y is 2, which is greater than 1. So the point is in the positive y direction. So for a2, the face is at y=1. The point is y=2>1, so the a2 face is visible.

But how about the x and z? For a2 to be visible, the point's x and z must be within 0 to x1 (which is 1) and 0 to z1 (1). The point's x and z are 2 and 2, which are outside. So how is a2 visible in the first sample?

Wait, the first sample's output is 12, which is a2 (2) + a6 (6) + a4 (4) = 12. So according to the sample, the a2 face is visible. But the point is (2,2,2), which is outside the box in all dimensions.

So for a2 face (y=1), the point is in y>1. So the face is in the direction of the point's negative y. But the x and z of the point are 2, which are beyond the box's x and z ranges (1 each). So how can the a2 face be visible?

Ah, perhaps my initial approach is wrong. So maybe the x and z ranges don't matter for the a2 face. Wait, maybe the way to think is: the face is visible if the point is in the region where its coordinate in the direction perpendicular to the face is beyond the face's position, and the other coordinates are not inside the box. Wait, this is confusing.

Alternatively, perhaps the visibility is determined by the direction of the point relative to the box. For example, the a2 face is the face with maximum y (y=y1). So any point with y > y1 will see the a2 face if, when looking towards the box from that direction, the a2 face is the one closest along that direction. But perhaps the other coordinates (x and z) determine whether the point is in the area where the a2 face is the one directly in front.

Wait, perhaps this is a problem of checking for each face whether the point lies in the octant where that face is the closest.

Alternatively, perhaps the correct approach is to check for each face:

For the face to be visible, the point must be in the region outside the box and such that the face is the first one hit when moving along the direction from the point towards the box.

But that seems computationally intensive. However, given the constraints (point is outside the box), maybe we can model it as follows.

For each face, the face is visible if the point is in the half-space determined by the face (i.e., for a1, y <0), and for the other two axes, the point's coordinates are within the box's range. Wait, no. Because in the first sample, the point is (2,2,2), which is beyond x1=1, y1=1, z1=1. So for the a2 face (y=1), the point's y is 2>1, so that's the y direction. For the x and z axes, the point is outside (x=2>1, z=2>1). So how is a2 visible?

Ah, perhaps the answer is that even if the point is beyond x1 and z1, but in the y direction beyond the a2 face, the a2 face is visible because it's the only face in that direction. Wait, but the box is a solid, so looking from a point that's in the positive y direction, but x and z are outside, the line from the point to the center of the a2 face would pass through other faces. For example, in the first sample, the point is (2,2,2). The center of a2 is (0.5, 1, 0.5). The line from (2,2,2) to (0.5,1,0.5) would pass through the a6 face (x=1) and a4 face (z=1), but perhaps the a2 face is still visible. Wait, maybe the problem considers that the face is visible as long as the point is in the direction of the face's normal, regardless of the other coordinates. That is, for the a2 face (y=y1), the point is in y > y1, and thus can see the a2 face regardless of x and z. But that can't be right.

Wait, the problem says that Vasya can see a face if he can see the center of the face. So the line from his position to the center of the face must not pass through the box. But if the point is outside the box, then the line from the point to the center of the face (which is on the face) is a straight line. Since the face is part of the box, the line would pass through the face. But since the box is solid, if the line passes through the box, then he can't see the face. Wait, but the line from the point to the center of the face is passing through the box only if the point is not in the direction of the face. For example, if the point is in the same direction as the face, then the line from the point to the center of the face would not pass through the box. Because the face is the closest part of the box in that direction.

Hmm, perhaps the key insight here is that for a face to be visible from a point outside the box, the point must lie in the direction of the face's normal, outside the box, and the line from the point to the center of the face does not pass through any part of the box except the face itself.

Alternatively, perhaps the face is visible if the point is in the direction perpendicular to the face. For example:

- For a1 (y=0 face), the normal points in the negative y direction. So if the point is in y <0, then the a1 face is visible if the point's x is between 0 and x1, and z between 0 and z1.

But if the point is in y <0, but x is outside 0 or x1, then the line from the point to the center of the a1 face would pass through another face (like the a5 or a6 face), thus the a1 face would not be visible.

So how do we model this?

Let me think of each face and the conditions under which the point can see it.

For the a1 face (y=0):

The face is part of the box's minimum y boundary. To see this face, the point must be in y <0. Additionally, the x coordinate must be between 0 and x1, and the z coordinate between 0 and z1. Because otherwise, when the point is looking towards the face, but his x or z are outside the box's x or z range, then the line to the center of the a1 face would pass through another face (like a5 or a6 for x, a3 or a4 for z), thus the a1 face is not visible.

Wait, but the line from the point (x,y,z) to the center of the a1 face (x1/2, 0, z1/2) would be a straight line. For example, if the point is at (2, -1, 0.5), then the line from (2,-1,0.5) to (0.5,0,0.5) would have x decreasing from 2 to 0.5, y increasing from -1 to 0. So during this line's path, when y reaches 0 (the a1 face), the x is 0.5 (within 0 and x1) and z is 0.5 (within 0 and z1). So the line first hits the a1 face, which is part of the box. So the a1 face is visible.

But if the point is (2, -1, 2), then the line to the a1 face's center (0.5,0,0.5) would have z decreasing from 2 to 0.5. So when y reaches 0, x is 0.5 (within x1) and z is 0.5 (within z1). So the a1 face is hit, so visible. But the point's z is outside the box (since z1 is 1, for example). Wait, but the box's z ranges from 0 to z1. So in this case, the line passes through the a1 face, which is part of the box, so the point can see the a1 face. So in this case, even though the point's z is outside the box (z=2 > z1=1), the a1 face is still visible.

Wait, this is conflicting with earlier thoughts. So perhaps the key is that the face is visible if the point is in the direction of the face's normal, and the line from the point to the center of the face does not pass through any other part of the box.

Alternatively, perhaps the visibility is determined by the following: for a face, the point must be in the direction of that face (i.e., outside the box in that direction), and the line from the point to the center of the face exits the box only through that face.

But how to check that.

Alternatively, perhaps for each face, the point is in the direction of that face, and for the other two axes, the point's coordinates are within the box's range for those axes.

For example, for the a1 face (y=0), the point must be in y <0, and x must be between 0 and x1, and z between 0 and z1. Only then can the a1 face be visible. Because if the x is outside that range, then the line from the point to the center would pass through another face (like a5 or a6) which is in the same direction, thus blocking the a1 face.

Wait, let's take an example. Suppose the box is (0,0,0) to (1,1,1). The a1 face is y=0. Let's say the point is (2, -1, 0.5). So the line from (2, -1, 0.5) to (0.5, 0, 0.5) would pass through x=1 at some point. The x=1 is the a6 face. So when moving along this line from the point towards the a1 face, the line first enters the box through the a6 face (x=1), then exits through the a1 face. Therefore, the a1 face is behind the a6 face when viewed from the point, so the a1 face is not visible.

Ah! So in this case, the a6 face is between the point and the a1 face, so the a1 face is not visible. Hence, the condition for a1 to be visible is that the point's x is between 0 and x1, and z between 0 and z1. Otherwise, when the point is in y <0, but x is outside 0-x1 or z is outside 0-z1, then the line to the a1 face's center would first hit another face (like a5 or a6 for x, a3 or a4 for z).

So the visibility of a face depends on the point being in the direction of the face's normal (y <0 for a1), and the other two coordinates (x and z for a1) being within the box's ranges (0 <= x <=x1 and 0 <= z <=z1). Only then can the line from the point to the center of the face not pass through any other face.

Similarly for other faces:

For a2 (y=y1):

Point must be in y> y1, x between 0 and x1, z between 0 and z1.

For a3 (z=0):

Point must be in z <0, x between 0 and x1, y between 0 and y1.

For a4 (z=z1):

Point must be in z> z1, x between 0 and x1, y between 0 and y1.

For a5 (x=0):

Point must be in x <0, y between 0 and y1, z between 0 and z1.

For a6 (x=x1):

Point must be in x> x1, y between 0 and y1, z between 0 and z1.

So for each face, the condition is:

Check if the point is in the direction of the face's normal (i.e., outside the box in that direction), and the other two coordinates are within the box's ranges for their respective axes.

So, for each face, we need to check three things:

1. The point is outside the box in the direction of the face's normal.

2. The other two coordinates of the point are within the box's ranges (0 to x1, 0 to y1, 0 to z1, depending on the face).

If both conditions are met, then the face is visible.

So the algorithm is:

For each of the six faces:

- Determine the axis and direction (e.g., a1 is y=0, direction is y <0).

- Check if the point's coordinate along the face's axis is outside the box in that direction.

- Check if the other two coordinates are within the box's range (0 to ...).

If both are true, add the face's value to the sum.

Let's apply this to the first sample:

Sample Input 1:

Point (2,2,2), box (1,1,1). So x1=1, y1=1, z1=1.

Check each face:

a1: y=0. Point's y is 2>0. So not in the direction (y <0). So no.

a2: y=1. Point's y=2>1. So direction is y>y1. Check other axes: x=2 (which is >1), z=2>1. So other axes are not within 0-1. So a2 is not visible. Wait, but the sample output says a2 is visible. So this contradicts.

Hmm, but according to the first sample's explanation, Vasya can see a2. So according to this approach, the code would not add a2, but the sample says to add a2. So this approach must be wrong.

Wait, what's the sample explanation? In the first sample, Vasya sees a2 (the top face), a6 (right face), and a4 (back face). So according to the sample, the conditions for those faces are met.

But according to the current approach, a2's condition is:

Point's y> y1 (yes, 2>1).

Other axes: x must be between 0 and x1 (1) and z between 0 and z1 (1). But point's x is 2 and z is 2, which are outside. So according to the current approach, a2 is not visible. But the sample says it is. So there's a mistake in the approach.

Therefore, the initial approach is incorrect. So where's the error?

Let me re-examine the problem.

The sample input 1's point is (2,2,2) outside the box (0-1 in all axes). The box is a cube. So when Vasya looks at the box, which face does he see? According to the sample explanation, he sees the a2 (top face), a6 (right face), and a4 (back face). So each of these faces is visible from the point.

Let's think of the point (2,2,2) relative to the box (0-1 in all axes). The point is in the direction where x>1, y>1, z>1. So the line from the point to the center of each of these faces (a2, a4, a6) is such that they are the first faces encountered.

For a6 (x=1 face):

The point's x is 2>1. The other axes (y and z) are 2>1 and 2>1. So according to the previous approach, the condition is x> x1 (yes) and y between 0 and y1 (1) (no, y is 2>1) and z between 0 and z1 (1) (no, z is 2>1). So according to the previous approach, a6 is not visible. But according to the sample, it is visible.

So the previous approach must be wrong. Therefore, the initial conditions for visibility are incorrect.

So what's the correct way to determine visibility?

Alternative approach: For each face, the point is in the direction of the face's normal. And even if other coordinates are outside the box's range, the face is visible. Because in such cases, the line from the point to the face's center passes through the face's plane first. For example, for the a6 face (x=1), if the point is (2, 2, 2), then the line from (2,2,2) to (1, 0.5, 0.5) (the center of a6 face) would pass through the a6 face. Since the other coordinates (y=0.5 and z=0.5) are within the box's ranges (0-1), the line would enter the box through the a6 face. But since the box is solid, the face is visible.

Wait, but the point is outside the box in all axes. So the line from the point to the center of the a6 face (x=1) would pass through x=1 (a6 face) at some point. At that point, the other coordinates (y and z) are 0.5, which are inside the box's y and z ranges. So the line passes through the a6 face, which is part of the box. So the a6 face is visible.

But according to the previous approach, since the point's y and z are outside the box's ranges, a6 would not be visible. That's the mistake.

So the correct condition for a face to be visible is:

The point is outside the box in the direction of the face's normal (i.e., for a6, x> x1), and the line from the point to the face's center passes through the face first (before passing through any other face).

But how to check that.

Perhaps the correct condition is that the point is in the direction of the face's normal (i.e., outside the box in that direction), and the other two coordinates are within the box's ranges when projected onto those axes. Because if the point's other coordinates are outside the box's ranges, then the line from the point to the face's center would have to pass through another face first.

Wait, for example:

a6 face is x=x1. The center is (x1, y1/2, z1/2).

A point (x, y, z) is outside the box in x direction (x> x1). So to see the a6 face, the line from (x,y,z) to (x1, y1/2, z1/2) must pass through the a6 face before any other face.

But the line's parametric equations would be x(t) = x1 + (x - x1)*t, y(t) = y + (y1/2 - y)*t, z(t) = z + (z1/2 - z)*t, where t=0 is the point, and t=1 is the center of the a6 face.

We need to find the value of t where the line first enters the box. The box is defined by 0 <= x <=x1, 0<=y<=y1, 0<=z <=z1. Since the point is at x> x1, y> y1, z> z1 (as in sample 1), the line is moving towards (x1, y1/2, z1/2). So the line will first hit the x=x1 face (a6) when t is such that x(t) =x1. Solving for t:

x1 + (x -x1)*t =x1 → t must be zero. Wait, but x is already x1. So this is confusing. Let me re-express the parametric equations.

Wait, the line from (2,2,2) to (1, 0.5, 0.5) (the a6 center) can be parametrized as:

x(t) = 2 - t*(1) → 2 -t.

y(t) = 2 - t*(1.5) → 2 -1.5t.

z(t) = 2 - t*(1.5) → 2-1.5t.

t ranges from 0 to 1.

At t=0, the point is (2,2,2).

At t=1, it's (1,0.5,0.5).

But the box is from (0,0,0) to (1,1,1). So the line passes through x=1 when t=1 (x=1 at t=1). At that point, y=0.5 and z=0.5, which are within the box's ranges. So the line enters the box at x=1 (a6 face), and then proceeds into the box. But since the box is solid, the a6 face is the one that is hit first. Therefore, the a6 face is visible.

So in this case, the other coordinates (y and z) are outside the box's ranges (y=2>1, z=2>1), but the line to the a6 face's center hits the a6 face first. So the a6 face is visible.

So the condition for a face to be visible is:

- The point is outside the box in the direction of the face's normal.

- The projection of the point's other two coordinates onto the face's plane is within the face's boundaries.

Wait, perhaps the correct approach is:

For a given face, the point can see the face if:

The point is in the direction of the face's normal (i.e., outside the box along that axis), and when you look at the other two axes, the point's coordinates are such that when you move towards the face's center, the first point of contact with the box is that face.

This is equivalent to checking that, for the other two axes, the point's coordinates are within the box's ranges. Because if, for example, the point's y is outside the box's y range (y > y1), then the line to the face's center would have to pass through the a2 face (y=y1) first, which is on another axis.

Wait, in the first sample, the point is (2,2,2), and the a2 face is y=1. The line from (2,2,2) to a2's center (0.5,1,0.5) would pass through y=1 before x=0.5 and z=0.5. So when does the line hit the box?

Let's parametrize this line:

x(t) = 2 - (2-0.5)*t = 2 -1.5t.

y(t) = 2 - (2-1)*t = 2 - t.

z(t) = 2 - (2-0.5)*t = 2 -1.5t.

The box is 0<=x<=1, y<=1, z<=1.

We need to find the first t where the line enters the box. Let's see:

The earliest t where any of the coordinates enter the box.

For y(t) to be 1: t= (2-1)/1 =1.

For x(t) to be 1: 2-1.5t =1 → t= (2-1)/1.5 = 0.666...

For z(t) to be 1: 2-1.5t=1 → t= (2-1)/1.5=0.666...

So the earliest t is 0.666..., when x and z reach 1 (a6 and a4 faces). At this t, y(t) is 2 -0.666... =1.333... which is greater than 1. So the line hits the a6 and a4 faces (x=1, z=1) before entering the box. But since the box is solid, the line would hit the a6 and a4 faces. But how can that be? At t=0.666..., the point is (1,1.333...,1). Which is outside the box in y (since y=1.333>1). So the line hasn't entered the box yet.

Wait, the box's y ranges up to y1=1. So for the line to enter the box, all coordinates must be within the box's ranges. So the earliest t when all coordinates are within the box.

So for the line to enter the box, all x(t) <=1, y(t) <=1, z(t)<=1.

But for the line from (2,2,2) to (0.5,1,0.5):

We can find the t for when each coordinate enters the box:

x(t) <=1 → t >= (2-1)/1.5 → 2/3 ≈0.666.

y(t) <=1 → t >= (2-1)/1 =1.

z(t) <=1 → t >= (2-1)/1.5 → 0.666.

So the earliest t where all three coordinates are <=1 is t=1. But at t=1, x(t) is 2-1.5*1=0.5 (<=1), y(t) is 2-1=1 (<=1), z(t) is 0.5 (<=1). So the line enters the box at t=1. So the entry point is (0.5,1,0.5), which is the center of the a2 face. So the line hits the a2 face first. But in this case, the point is (2,2,2), which is outside the box in all directions. So when he looks towards the a2 face's center, the line enters the box at the a2 face. Thus, the a2 face is visible.

But according to the previous approach, the a2 face is visible only if the other axes (x and z) are within 0 and x1 (1), and 0 and z1 (1). But the point's x is 2>1 and z is 2>1. So according to that approach, a2 would not be visible, which contradicts the sample.

So the initial approach is incorrect. Therefore, the correct condition is not that the other axes are within the box's ranges, but that when moving along the line from the point to the face's center, the first face that is hit is the current face.

But how to model this without doing complex line-box intersection calculations.

Alternative approach:

Each face is visible if the point is outside the box in the face's direction, and for the other two axes, the line from the point to the face's center intersects the box first through this face.

But how to compute this efficiently.

Another way: For each face, the face is visible if:

The point is in the direction of the face's normal, and for the other two axes, the point's coordinates are within the face's projections plus any possible extension. Wait, perhaps this is not clear.

Alternatively, think in terms of parameters:

For the a2 face (y=y1):

The face is visible from point (x,y,z) if y>y1, and (x is between 0 and x1) OR (z is between 0 and z1). No, that's not correct.

Alternatively, the face is visible if y>y1, and the line from the point to the face's center does not intersect any other face before reaching this face.

So for a2 face:

The line to the face's center is (x0, y0, z0) → (x_center, y1, z_center).

The line enters the box through the a2 face if the other two axes (x and z) of the point are within the box's ranges. But if the point's x is beyond x1 or z beyond z1, then the line would hit another face first (like a6 or a4) before reaching the a2 face.

But in the first sample, the line from (2,2,2) to (0.5,1,0.5) (a2's center) does enter the box through the a2 face. So why? Because even though x and z are outside, the line reaches the a2 face's y=1 before other faces.

Wait, no. In that case, when moving along the line, the first face hit is when y=1. At that point, what are x and z?

Let's parametrize the line from (2,2,2) to (0.5,1,0.5):

The line's parametric equations:

x(t) = 2 - 1.5t (since delta x is 0.5 -2 = -1.5, so x decreases by 1.5t)

y(t) = 2 - t (delta y is 1-2= -1)

z(t) = 2 - 1.5t (delta z is 0.5-2= -1.5)

We need to find the first t where any of the coordinates reaches the box's boundaries.

For the a2 face (y=1):

y(t) =1 → t=1.

At t=1, x(t)=2-1.5*1=0.5, which is within 0 and x1=1.

z(t)=2-1.5*1=0.5, which is within 0 and z1=1.

So the line enters the box at t=1, passing through (0.5,1,0.5), which is the center of the a2 face. So the a2 face is hit first.

But the point's x and z were initially 2 and 2. So in this case, even though the x and z are outside, the a2 face is visible because the line hits the a2 face first.

So the condition for a2 face visibility is:

y> y1, and the line from the point to the a2 face's center enters the box via the a2 face (i.e., at the same time, the x and z are within the box's ranges).

But how to compute this.

The line from the point to the a2 face's center will hit the a2 face if, for that face, the other two coordinates (x and z) are within the box's ranges at the moment when the line reaches y=y1.

So to compute this:

For a2 face (y=y1), check:

The point's y> y1.

The line from (x,y,z) to the a2's center (x1/2, y1, z1/2) must have x and z within the box's x and z ranges when y reaches y1.

But how to calculate this.

The line to the a2 face's center has direction vector (x_center -x, y1 -y, z_center -z).

The parametric equations can be written as:

x(t) = x + (x_center -x) * t

y(t) = y + (y1 -y) * t

z(t) = z + (z_center -z) * t

We want to find t such that y(t) = y1. Solving for t:

y + (y1 -y)*t = y1 → t = (y1 - y) / (y1 - y) = 1.

At t=1, we are at the a2 face's center. But this is when we have already traveled the entire line. So perhaps this approach is not helpful.

Alternative idea: For each face, the line from the point to the face's center will enter the box through that face only if, for the other two coordinates, when the line reaches the face's plane (e.g., y=y1 for a2), the other coordinates are within the box's ranges.

In other words, for the a2 face:

The line from (x,y,z) to (x1/2, y1, z1/2) enters the box through the a2 face if, when y(t) = y1, x(t) is between 0 and x1, and z(t) is between 0 and z1.

But x(t) when y(t) = y1 is:

x(t) = x + (x_center -x) * t

t = (y1 - y) / (y1 - y) → t=1 (since y starts at y> y1 and moves towards y1). So x(t) at t=1 is x_center = x1/2, which is between 0 and x1. Similarly, z(t) is z_center = z1/2, which is between 0 and z1.

Wait, this would always be true, but that's not the case. Because the line from (x,y,z) to the face's center is a straight line. So the center's coordinates are within the box's ranges. Therefore, when the line reaches the face's plane (y=y1), the x and z are x_center and z_center, which are within the box's ranges. So the line enters the box through the a2 face.

But this is only true if the line to the center is the direction. For example, if the line from the point to the center of the face's plane is such that the x and z are within the box's ranges.

But the center is always within the box's ranges, so x_center is between 0 and x1, z_center is between 0 and z1. So when the line reaches y=y1, the x and z are within the box's ranges. Therefore, the line enters the box through the a2 face.

But this would imply that whenever the point is in the direction of the a2 face (y> y1), the a2 face is visible. But that's not correct, as in some cases the line may hit another face before reaching the a2 face.

But according to the parametric equations in the first sample, the line enters the box through the a2 face. So the a2 face is visible.

But according to the previous approach, the a2 face is visible only if x and z are within the box's ranges, which they are not. So the previous approach is wrong.

So the correct condition is:

A face is visible if the point is outside the box in the direction of the face's normal.

Because when that's the case, the line from the point to the face's center will enter the box through that face, since the center is within the box's other ranges.

But why is that?

Because the center is at (x1/2, y1, z1/2) for a2 face. So when the line reaches the a2 face's plane (y=y1), the x and z are x1/2 and z1/2, which are within the box's x and z ranges. Therefore, the line enters the box through the a2 face.

Therefore, the condition is simply that the point is in the direction of the face's normal (outside the box in that direction). Because the line from the point to the face's center will enter the box through that face.

Thus, the correct approach is:

For each face, check if the point is outside the box in the direction of the face's normal. If yes, then the face is visible.

So the conditions are:

Face a1 (y=0): point.y <0.

Face a2 (y=y1): point.y > y1.

Face a3 (z=0): point.z <0.

Face a4 (z=z1): point.z > z1.

Face a5 (x=0): point.x <0.

Face a6 (x=x1): point.x > x1.

This is a much simpler condition. So for example, in the first sample:

point (2,2,2), box (1,1,1).

Check each face:

a2: point.y=2>1 → yes.

a6: point.x=2>1 → yes.

a4: point.z=2>1 → yes.

So the sum is a2 (2) + a6 (6) + a4 (4) = 12, which matches the sample.

Another sample:

Input:

0 0 10

3 2 3

1 2 3 4 5 6

Point (0,0,10), box (3,2,3).

Faces:

a4: z=3. Point.z=10>3 → yes. So a4 is visible. Other faces:

a1: y<0 → no.

a2: y>2 → no (y=0).

a3: z<0 → no.

a5: x<0 → no.

a6: x>3 → no.

Only a4 is visible. Sum is 4, which matches the sample.

So the correct approach is to check whether the point is in the direction of each face's normal (i.e., outside the box in that axis). If so, then the face is visible.

This is a much simpler condition. So the code needs to check for each face if the point is in the respective direction outside the box.

But wait, why does this work?

Because the line from the point to the center of the face must pass through the face's plane first, and since the center is within the box's other axes, the line enters the box through that face.

For example, if the point is at (2,2,2), and the box is (1,1,1), then for a2 (y=1), the line to the center (0.5,1,0.5) will reach y=1 first. At that point, x=0.5 and z=0.5, which are within the box's x and z ranges. So the line enters the box through the a2 face.

Similarly, for a6 face (x=1), the line to the center (1,0.5,0.5) will reach x=1 first. At that point, y=0.5 and z=0.5 are within the box's ranges, so the line enters through a6 face.

Thus, the face is visible if the point is in the direction of the face's normal.

So the code should check for each face:

a1: y <0 → add a1.

a2: y > y1 → add a2.

a3: z <0 → add a3.

a4: z > z1 → add a4.

a5: x <0 → add a5.

a6: x > x1 → add a6.

Thus, the solution is to check for each of these six conditions, and sum the corresponding a's.

So, the code will be:

Read x,y,z.

Read x1,y1,z1.

Read a1, a2, a3, a4, a5, a6.

sum =0

if y <0: sum +=a1

if y > y1: sum +=a2

if z <0: sum +=a3

if z > z1: sum +=a4

if x <0: sum +=a5

if x >x1: sum +=a6

print(sum)

Wait, but this seems too simple. But according to the samples, it works.

Another test case: what if the point is outside in x and y directions, but not z.

For example, point (2,3,5), box (1,2,4).

x1=1, y1=2, z1=4.

x=2>1 → a6 is added.

y=3>2 → a2 is added.

z=5>4 → a4 is added.

Sum is a6 +a2 +a4.

But according to the condition, this is correct.

Yes, because the line from the point to the a6's center (1,1,2) would enter the box through a6 face (x=1) first. So the a6 is visible.

Similarly for a2 and a4.

But what if the point is in a direction where two faces are possible?

For example, point (2,3,5), box (2,3,5). So x1=2, y1=3, z1=5.

Point (3,4,6) → x>2, y>3, z>5.

So all three faces (a2, a4, a6) are added.

The line from (3,4,6) to a6's center (2, 1.5, 2.5) would reach x=2 first. At x=2, y and z are 4 and 6, which are beyond the box's y and z ranges. So the line would hit the a6 face (x=2), but since the point is outside in y and z, the line to the a6's center is (3→2, 4→1.5, 6→2.5). The parametric equations:

x(t) =3 -t*(3-2) =3 -t. So x=2 when t=1.

At t=1, y=4 -t*(4-1.5) =4-2.5=1.5 → within y1=3.

z=6 -t*(6-2.5) =6-3.5t → at t=1, z=6-3.5=2.5 → within z1=5.

So the line enters the box through the a6 face.

Thus, the a6 face is visible, and similarly for a2 and a4.

Thus, the code is correct.

So the solution is to check for each face's direction and sum the a's accordingly.

This is a O(1) solution, which is optimal given the constraints (no time issues).

So the code can be written as follows:

Read x, y, z.

Read x1, y1, z1.

Read a1, a2, a3, a4, a5, a6.

sum =0

if y < 0:
    sum +=a1
if y > y1:
    sum +=a2
if z <0:
    sum +=a3
if z > z1:
    sum +=a4
if x <0:
    sum +=a5
if x >x1:
    sum +=a6

print(sum)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    x, y, z = map(int, input_stream.readline().rstrip("\n").split())
    x1, y1, z1 = map(int, input_stream.readline().rstrip("\n").split())
    a1, a2, a3, a4, a5, a6 = map(int, input_stream.readline().rstrip("\n").split())

    total = 0
    if y < 0:
        total += a1
    if y > y1:
        total += a2
    if z < 0:
        total += a3
    if z > z1:
        total += a4
    if x < 0:
        total += a5
    if x > x1:
        total += a6

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
0 0 10
3 2 3
1 2 3 4 5 6
""",
            "output": \
"""\
4
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

Second sample:

Input:
0 0 10
3 2 3
1 2 3 4 5 6

z=10>3 → add a4 (4).

Other conditions: x=0 is not <0 or >3. y=0 is not <0 or>2. So sum is 4. Correct.

Another test case where x is <0:

Point (-1,0,0). x=-1 <0 → a5 is added. Others: y is 0 (not <0 or >y1?), z is 0 (not <0 or> z1?).

So if the box has x1=3, y1=2, z1=4.

So sum is a5.

This code would correctly add a5.

Yes, because the line from (-1,0,0) to a5's center (0, 1, 2) would enter the box through the a5 face (x=0). At x=0, y=0 and z=0 are within the box's ranges (y=0 <2, z=0 <4). So the a5 face is visible.

Thus, the code works.
</think>

```python
x, y, z = map(int, input().split())
x1, y1, z1 = map(int, input().split())
a1, a2, a3, a4, a5, a6 = map(int, input().split())

total = 0
if y < 0:
    total += a1
if y > y1:
    total += a2
if z < 0:
    total += a3
if z > z1:
    total += a4
if x < 0:
    total += a5
if x > x1:
    total += a6

print(total)
```
