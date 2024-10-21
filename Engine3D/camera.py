import numpy as np

class Camera:
    def __init__(self, position):
        self.position = np.array(position)

    def get_view_matrix(self):
        translation = translation_matrix(-self.position[0], -self.position[1], -self.position[2])
        return translation

def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
