import math

########################
# PYTAGORAS
########################
def pytagoras(delta_x, delta_y) -> float:
    return math.sqrt(delta_x**2 + delta_y**2)


def distance_to(pos1, pos2) -> float:
    """ Returns the distance between two object on a 2d plane (using the formula of Pytagoras) """
    return pytagoras(pos1[0] - pos2[0], pos1[1] - pos2[1])


def distance_to_3d(pos1, pos2) -> float:
    """ Returns the distance between two object on a 3d plane (using the formula of Pytagoras) """
    delta_x, delta_y, delta_z = abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]), abs(pos1[2] - pos2[2])
    delta_xz = pytagoras(delta_x, delta_z)
    return pytagoras(delta_xz, delta_y)


########################
# Triangle
########################
def translate_triangle(x, y, diagonal, new_len) -> (float, float):
    """ To translate a 90deg triangle with a x sized diagonal to a smaller/bigger diagonal triangle
    per example: the famous 3 4 5 triangle could become: .6 .8 1 """
    mul = new_len / diagonal
    return x * mul, y * mul

########################
# UNIT CIRCLE
########################
def radian_to(pos1, pos2) -> float:
    """ Get a radian between two objects on a 2d plane """
    distance = distance_to(pos1, pos2)
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    dx, dy = translate_triangle(delta_x, delta_y, distance, 1)

    return math.acos(dx) * (-1 if dy > 0 else 1)


########################
# INTERSECTION
########################
# def intersection(line1, line2):
#     """ Get the coordinates of the intersection of two lines """
#     line1_delta = (line1[1][0] - line1[0][0], line1[1][1] - line1[0][1])
#     a = line1_delta[1] / line1_delta[0]
#     print("a", a)

#     line2_delta = (line2[1][0] - line2[0][0], line2[1][1] - line2[0][1])
#     a = line2_delta[1] / line2_delta[0]
#     print("a", a)


# if __name__ == "__main__":
#     print(intersection(
#         ((0, 0), (5, 1)),
#         ((1, 0), (1, 4))
#     ))
