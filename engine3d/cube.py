

class Cube:
    def __init__(self, corners):
        self.corners = corners

        print()
        print(self.corners)
        print(self.get_planes(85, 15, 45))

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

        return new_planes

    def intersect(self, line):
        planes = self.get_planes(line[0][0], line[0][1], line[0][2])
        return True, 0.5
