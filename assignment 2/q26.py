path_len = 120
path_bre = 2.4

brick_len = 24/100
brick_bre = 15/100

path_area = path_len * path_bre
brick_area = brick_len * brick_bre

print(f"Number of bricks required: {path_area/brick_area}")