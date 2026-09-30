b_len = 15
b_bre = 8
b_hei = 5

w_len = 15*100
w_bre = 10*100
w_hei = 8*100

b_vol = b_len*b_bre*b_hei
w_vol = w_len*w_bre*w_hei

print(f"Number of bricks required: {w_vol/b_vol}")