import math
s1 = 10
s2 = 9
peri = 36
s = peri/2
s3 = peri - s1 - s2
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(f"Area = {area}sq cm")