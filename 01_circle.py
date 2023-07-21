PI = 3.1415926
R = 42
S = PI * R ** 2
print(round(S, 4))

point = (23, 34)
x = point[0]
y = point[1]
p_1 = (x ** 2 + y ** 2) ** 0.5
print(R == p_1)

point_2 = (30, 30)
x_2 = point_2[0]
y_2 = point_2[1]
p_2 = (x_2 ** 2 + y_2 ** 2) ** 0.5
print(R == (round(p_2, 0)))


