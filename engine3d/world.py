import os
from .config import BLOCK_SIZE
from .functions import distance_to_3d


class World:
    def __init__(self, file_name):
        self.world_name = f"{'/'.join(os.path.realpath(__file__).split('/')[:-1])}/worlds/{file_name}.3d"
        self.load_word()

        self.__walls = None
        print(self.walls)

    def load_word(self):
        with open(self.world_name) as file:
            self.matrix = [
                [
                    list(z_plane) for z_plane in y_plane.split("\n")
                ] for y_plane in file.read().split("\n\n")
            ]

    @property
    def walls(self):
        if self.__walls is None:
            self.__walls = self.__get_walls()
        return self.__walls

    def __get_walls(self):
        cubes = []

        # put in all cubes
        for z in range(len(self.matrix)):
            for y in range(len(self.matrix[z])):
                for x in range(len(self.matrix[z][y])):
                    if self.matrix[z][y][x] == "#":
                        cubes.append(
                            (
                                (
                                    x * BLOCK_SIZE,
                                    y * BLOCK_SIZE,
                                    z * BLOCK_SIZE
                                ),
                                (
                                    (x + 1) * BLOCK_SIZE,
                                    (y + 1) * BLOCK_SIZE,
                                    (z + 1) * BLOCK_SIZE
                                ),
                            )
                        )

        # merge neighbours
        # changes = 1
        # while changes > 0:
        #     changes = 0
        #     for cube in cubes:
        #         for c in cubes:
        #             if cube == c:
        #                 continue
        #             distance = abs(distance_to_3d(cube[0], c[0]))

        #             if distance == BLOCK_SIZE:
        #                 cubes.remove(cube)
        #                 cubes.remove(c)

        #                 new_cube = (cube[0], c[1])
        #                 cubes.append(new_cube)

        #                 changes += 1
        #                 break

        #         if changes > 0:
        #             break

        return cubes
