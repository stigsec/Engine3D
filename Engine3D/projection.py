import numpy as np

def project_point(v, screen_width, screen_height):
    factor = 200 / (v[2] + 3)
    x = int(v[0] * factor + screen_width / 2)
    y = int(-v[1] * factor + screen_height / 2)
    return x, y
