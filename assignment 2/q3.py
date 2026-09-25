l_tile = 13
b_tile = 7

l_reg = 520
b_reg = 140

area_tile = l_tile * b_tile
area_reg = l_reg * b_reg

num_tiles = area_reg / area_tile
print(f"Number of tiles needed: {num_tiles}")