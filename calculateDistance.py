# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt
import numpy as np
# def distance(lon1, lat1, lon2, lat2):
     
#     # The math module contains a function named
#     # radians which converts from degrees to radians.
#     lon1 = radians(lon1)
#     lon2 = radians(lon2)
#     lat1 = radians(lat1)
#     lat2 = radians(lat2)
      
#     # Haversine formula
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
#     c = 2 * asin(sqrt(a))
    
#     # Radius of earth in miles. Use 3956 for miles
#     r = 3958.8
      
#     # calculate the result
#     return(c * r)



# print(distance(-73.99787903,	40.67464066,	-73.95763397,	40.72217178), "K.M")
			
# print(distance(-73.94198608,	40.82260132,	-73.96685791,	40.77243423), "K.M")

# print(distance(-73.95199585,	40.78979874,	-73.93942261,	40.80517197), "K.M")

# print(distance(-73.91838074,	40.76974106,	-73.8571701	,   40.75680161), "K.M")

# print(distance(-73.94372559,	40.83879852,	-73.94526672,	40.8328476), "K.M")

# print(distance(-73.98318481,	40.67287445,	-73.98426819,	40.67172241), "K.M")

plan = [2,3,4]
patients = [5, 4, 3, 2, 1]

conv = np.convolve(plan, patients)
print(conv)


