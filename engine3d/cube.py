from .functions import distance_to_3d


def cord_in_range(cord, rnge):
    for i in range(3):
        if min(rnge[0][i], rnge[1][i]) <= cord[i] <= max(rnge[0][i], rnge[1][i]):
            pass
        else:
            return False

    return True


class Cube:
    def __init__(self, corners):
        self.corners = corners

        print(self.corners)

    def get_planes(self, x, y, z) -> [((int), (int))]:
        planes = []

        for corner, other_corner in zip(self.corners, reversed(self.corners)):
            for i in range(3):
                plane_other_corner = list(other_corner)
                plane_other_corner[i] = corner[i]

                planes.append(
                    (
                        corner,
                        plane_other_corner
                    )
                )

        x_planes = planes[0], planes[3]
        y_planes = planes[1], planes[4]
        z_planes = planes[2], planes[5]

        new_planes = []

        for axis_num, planes, axis in zip([0, 1, 2], [x_planes, y_planes, z_planes], [x, y, z]):
            if min(planes[0][0][axis_num], planes[1][0][axis_num]) > axis:
                new_planes.append(min(planes[0], planes[1]))
            elif max(planes[0][0][axis_num], planes[1][0][axis_num]) < axis:
                new_planes.append(max(planes[0], planes[1]))
            else:
                new_planes.append(None)

        return new_planes

    def intersect(self, line):

        # print()
        # print(self.corners)
        # print(line)
        planes = self.get_planes(line[0][0], line[0][1], line[0][2])

        delta_x = line[0][0] - line[1][0]
        delta_y = line[0][1] - line[1][1]
        delta_z = line[0][2] - line[1][2]

        try:
            y_a = delta_y / delta_x
            z_a = delta_z / delta_y
        except ZeroDivisionError:
            return False, 0

        for axis, plane in enumerate(planes):
            if plane is None:
                continue

            y = plane[0][axis] * y_a + line[0][1]
            x = y / y_a + line[0][0]
            z = z_a * plane[0][axis] + line[0][2]

            intersect_cord = (x, y, z)

            print("checkign")
            if cord_in_range(intersect_cord, self.corners) and cord_in_range(intersect_cord, line):
                print("tes")
                return True, distance_to_3d(line[1], intersect_cord)

        return False, 0
