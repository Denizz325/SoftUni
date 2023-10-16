from math import floor
from math import sqrt
def which_point_is_closer(dist1, dist2):
    if dist1 <= dist2:
        return f"({x_1}, {y_1})"
    return f"({x_2}, {y_2})"
x_1 = floor(float(input()))
y_1 = floor(float(input()))
x_2 = floor(float(input()))
y_2 = floor(float(input()))
first_point_distance_1 = floor(sqrt(x_1 ** 2 + y_1 ** 2))
second_point_distance_1 = floor(sqrt(x_2 ** 2 + y_2 ** 2))
print(which_point_is_closer(first_point_distance_1, second_point_distance_1))