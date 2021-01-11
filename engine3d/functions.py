import math

########################
# PYTAGORAS
########################
def __pytagoras(delta_x, delta_y):
    return math.sqrt(delta_x**2 + delta_y**2)


def distance_to(pos1, pos2) -> float:
    """ Returns the distance between two object on a 2d plane (using the formula of Pytagoras) """
    return __pytagoras(pos1[0] - pos2[0], pos1[1] - pos2[1])


def distance_to_3d(pos1, pos2):
    """ Returns the distance between two object on a 3d plane (using the formula of Pytagoras) """
    delta_x, delta_y, delta_z = abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]), abs(pos1[2] - pos2[2])
    delta_xz = __pytagoras(delta_x, delta_z)
    return __pytagoras(delta_xz, delta_y)


########################
# Triangle
########################
def translate_triangle(x, y, diagonal, new_len):
    """ To translate a 90deg triangle with a x sized diagonal to a smaller/bigger diagonal triangle
    per example: the famous 3 4 5 triangle could become: .6 .8 1 """
    mul = new_len / diagonal
    return x * mul, y * mul

########################
# UNIT CIRCLE
########################
def radian_to(pos1, pos2):
    """ Get a radian between two objects on a 2d plane """
    distance = distance_to(pos1, pos2)
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    dx, dy = translate_triangle(delta_x, delta_y, distance, 1)

    return math.acos(dx) * (-1 if dy > 0 else 1)
