from math import pi, radians, sin, cos, asin

# Task-1: Find the area of a circle from it's radius.
print("""TASK-1: FIND THE AREA OF A CIRCLE FROM IT\'S RADIUS
===============================================================================""")

r = float(input("Enter the value of your circle\'s radius: "))
area = pi * r**2
print(f"The area of your circle is {area} square unit.")

# Task-2: Find arc length from given angle and radius.
print("""\n\nTASK-2: FIND ARC LENGTH FROM GIVEN ANGLE AND RADIUS
===============================================================================""")

angle = radians(float(input("Enter the angle value in degree for find arc length: ")))
r = float(input("Enter the value of your circle\'s radius: "))
arc_length = angle * r
print(f"The arc length of your circle is {arc_length} unit.")

# Task-3: Find the euclidian distance of two points.
print("""\n\nTASK-3: FIND THE EUCLIDIAN DISTANCE OF TWO POINTS
===============================================================================""")

point1_x = float(input("Enter the x axis value of the first point: "))
point1_y = float(input("Enter the y axis value of the first point: "))
point2_x = float(input("Enter the x axis value of the second point: "))
point2_y = float(input("Enter the y axis value of the second point: "))
point_dist = ((point2_x - point1_x)**2 + (point2_y - point1_y)**2) ** 0.5
print(f"The distance between two points is {point_dist} unit.")

# Task-4: Find the distance of two points from it's latitude and longtitude.
print("""\n\nTASK-4: FIND THE DISTANCE OF TWO POINTS FROM IT\'S LATITUDE AND LONGITIUDE
===============================================================================""")

lat_1 = radians(float(input("Enter the latitude of first point: ")))
lon_1 = radians(float(input("Enter the longitude of first point: ")))
lat_2 = radians(float(input("Enter the latitude of second point: ")))
lon_2 = radians(float(input("Enter the longitude of second point: ")))
d_lat = lat_2 - lat_1
d_lon = lon_2 - lon_1
a = sin(d_lat/2)**2 + cos(lat_1) * cos(lat_2) * sin(d_lon/2)**2
c = asin(a**0.5) * 2
r = 6371
point_dist = c * r
print(f"The distance between two points is {point_dist} kilometers.")

# Task-5: Find the area of a trapezium from it's four arms.
print("""\n\nTASK-5: FIND THE AREA OF A TRAPEZIUM FOR IT\'S FOUR ARMS
===============================================================================""")

a = float(input("Enter the value of small arm of parallel sides: "))
b = float(input("Enter the value of large arm of parallel sides: "))
c = float(input("Enter the value of left arm of unparallel sides: "))
d = float(input("Enter the value of right arm of unparallel sides: "))
tri_s = (c+d+b-a)/2     # Inner traingle's semi-range
tri_area = (tri_s*(tri_s-c)*(tri_s-d)*(tri_s-(b-a))) ** 0.5     # Inner traingle's area
h = (2 * tri_area) / (b - a)        # Height of Traingle / Trapezium
area = ((a + b) / 2) * h        # Area of Trapezium
print(f"The area of the trapezium is {area} square unit.")

print("""\n\n===============================================================================
===============================================================================""")
input("Press enter to exit: ")