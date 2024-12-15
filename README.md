
# Python 3D Engine

This is a simple 3D engine built using Python and Pygame. It provides basic functionality for rendering 3D points in a 2D space using matrix transformations and projection techniques.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

To use this 3D engine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/stigsec/Engine3D.git
   cd Engine3D
   ```

2. **Install dependencies:**
   Ensure you have Python 3 and Pygame installed. You can install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. **Importing the engine:**
   You can import the engine in your Python script as follows:
   ```python
   from Engine3D import Renderer
   ```

## Usage

To use the engine, create a `Renderer` object, provide the screen dimensions, and set the camera position. Then, call the `draw` method with a list of points or shapes to render.

### Initializing the Renderer

```python
import numpy as np
from Engine3D import Renderer

# Screen dimensions
width = 800
height = 600

# Camera position (x, y, z)
camera_position = [0, 0, 0]

# Create the renderer
renderer = Renderer(width, height, camera_position)
```

### Drawing Points

You can draw points by passing a list of 3D points to the `draw` method. Each point should be a list or a numpy array of three coordinates (x, y, z).

```python
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
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE file](LICENSE) for more details.
