s_len = 15
s_bre = 15
r_side = 15
s_area = s_len*s_bre
r_area = r_side**2

print(f"Shelly's garden area: {s_area}, Rachel's garden area: {r_area}")
if(s_area == r_area):
    print("Both have same area in their gardens")
else:
    print("Shelly's garden is bigger") if (s_area > r_area) else print(f"Rachel's garden is bigger")