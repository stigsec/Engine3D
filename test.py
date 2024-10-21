from Engine3D import Renderer
import numpy as np

# Screen dimensions
width = 800
height = 600

# Camera position (x, y, z)
camera_position = [0, 0, 0]

# Create the renderer
renderer = Renderer(width, height, camera_position)
# Cube verticies to draw
cube_vertices = np.array([
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [1, -1, -1],
    [-1, 1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, -1, -1]
])

# Cube edges to draw
cube_edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),  # Right face
    (4, 5), (5, 7), (7, 6), (6, 4),  # Left face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

# Start rendering
renderer.draw(cube_vertices, cube_edges)