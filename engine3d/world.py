import os


class World:
    def __init__(self, file_name):
        self.world_file_name = f"{'/'.join(os.path.realpath(__file__).split('/')[:-1])}/worlds/{file_name}.3d"
        self.load_word()

    def load_word(self):
        with open(self.world_file_name) as file:
            self.matrix = [
                [list(z_plane) for z_plane in y_plane.split("\n")]
                 for y_plane in file.read().split("\n\n")
                ]
