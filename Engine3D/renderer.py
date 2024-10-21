import pygame
import numpy as np
from .camera import Camera
from .projection import project_point

class Renderer:
    def __init__(self, width, height, camera_position):
        pygame.init()
        self.width = width
        self.height = height
        self.camera = Camera(camera_position)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Engine 3D")
        self.running = True

        self.angle_x = 0
        self.angle_y = 0

    def rotation_matrix_x(self, angle):
        c = np.cos(angle)
        s = np.sin(angle)
        return np.array([
            [1, 0, 0],
            [0, c, -s],
            [0, s, c]
        ])

    def rotation_matrix_y(self, angle):
        c = np.cos(angle)
        s = np.sin(angle)
        return np.array([
            [c, 0, s],
            [0, 1, 0],
            [-s, 0, c]
        ])

    def draw(self, vertices, edges):
        while self.running:
            self.screen.fill((255, 255, 255))
            view_matrix = self.camera.get_view_matrix()

            self.angle_x += 0.0001 # Rotation speed
            self.angle_y += 0.0001


            rot_x = self.rotation_matrix_x(self.angle_x)
            rot_y = self.rotation_matrix_y(self.angle_y)

            rotated_points = np.dot(vertices, rot_x)
            rotated_points = np.dot(rotated_points, rot_y)

            for point in rotated_points:
                transformed_point = np.dot(view_matrix, np.append(point, 1))[:3]
                x, y = project_point(transformed_point, self.width, self.height)
                pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 5)

            for edge in edges:
                start, end = edge
                start_point = np.dot(view_matrix, np.append(rotated_points[start], 1))[:3]
                end_point = np.dot(view_matrix, np.append(rotated_points[end], 1))[:3]
                start_x, start_y = project_point(start_point, self.width, self.height)
                end_x, end_y = project_point(end_point, self.width, self.height)
                pygame.draw.line(self.screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

        pygame.quit()
