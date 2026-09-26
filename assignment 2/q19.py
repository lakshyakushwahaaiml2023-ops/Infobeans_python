cube_side = 7
cuboid_s1 = 7
cuboid_s2 = 4
cuboid_s3 = 8

cube_vol = cube_side**3
cuboid_vol = cuboid_s1*cuboid_s2*cuboid_s3
print(f"Volume of cube: {cube_vol} cubic units")
print(f"Volume of cuboid: {cuboid_vol} cubic units")    

print("Volume of cube is greater than volume of cuboid") if cube_vol > cuboid_vol else print("Volume of cuboid is greater than volume of cube")