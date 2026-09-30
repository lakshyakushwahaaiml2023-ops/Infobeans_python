cube_side = 3
box_len = 15
box_bred = 9
box_hei = 12
box_vol = box_len * box_bred * box_hei
cube_vol = cube_side**3
print(f"Number of boxes that can be filled in the carton: {box_vol/cube_vol}")