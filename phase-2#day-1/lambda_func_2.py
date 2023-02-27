"""l=[2,4,6,8,10,12,14]
r=map(lambda x:x**0.5,l)
print(list(r))"""

import math
l=[2,4,6,8,10,12,14]
r=map(lambda x:math.sqrt(x),l)
print(list(r))


