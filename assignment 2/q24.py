b_len = 15
b_bre = 10
b_hei = 7.5

w_len = 20*100
w_bre = 0.75*100
w_hei = 2*100

b_vol = b_len*b_bre*b_hei
w_vol = w_len*w_bre*w_hei

price = 900

print(f"Number of bricks required: {w_vol/b_vol} and total bricks price: {(w_vol/b_vol)/1000 * price}")