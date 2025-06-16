import pygame
from pygame import Vector2, Vector3
from triangle import Triangle
from mesh import Mesh
from math import tan

pygame.init()

TITLE = "3D Rendering"

SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 880
SCREEN_COLOR = (0, 0, 0)

FOV = 90
RADIAN_FOV = FOV * 3.14159 / 180

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

cube = Mesh(size=250, color=(255, 255, 255))
cube.triangles = [Triangle(Vector3(0, 0, 0), Vector3(0, 1, 0), Vector3(1, 1, 0)), 
                  Triangle(Vector3(0, 0, 0), Vector3(1, 1, 0), Vector3(1, 0, 0)),
                  Triangle(Vector3(1, 0, 0), Vector3(1, 1, 0), Vector3(1, 1, 0.1)),
                  Triangle(Vector3(1, 0, 0), Vector3(1, 1, 0.1), Vector3(1, 0, 0.1)),
                  Triangle(Vector3(1, 0, 0.1), Vector3(1, 1, 0.1), Vector3(0, 1, 0.1)),
                  Triangle(Vector3(1, 0, 0.1), Vector3(0, 1, 0.1), Vector3(0, 0, 0.1)),
                  Triangle(Vector3(0, 0, 0.1), Vector3(0, 1, 0.1), Vector3(0, 1, 0)),
                  Triangle(Vector3(0, 0, 0.1), Vector3(0, 1, 0), Vector3(0, 0, 0)),
                  Triangle(Vector3(0, 1, 0), Vector3(0, 1, 0.1), Vector3(1, 1, 0.1)), 
                  Triangle(Vector3(0, 1, 0), Vector3(1, 1, 0.1), Vector3(1, 1, 0)),
                  Triangle(Vector3(0, 0, 0.1), Vector3(0, 0, 0), Vector3(1, 0, 0)),
                  Triangle(Vector3(0, 0, 0.1), Vector3(1, 0, 0), Vector3(1, 0, 0.1))]

pyramid = Mesh(size=200, color=(255, 255, 255))
pyramid.triangles = [Triangle(Vector3(2, 0, 0), Vector3(2.5, -1, 0.05), Vector3(3, 0, 0)), 
                     Triangle(Vector3(3, 0, 0), Vector3(2.5, -1, 0.05), Vector3(3, 0, 0.1)), 
                     Triangle(Vector3(3, 0, 0.1), Vector3(2.5, -1, 0.05), Vector3(2, 0, 0.1)), 
                     Triangle(Vector3(2, 0, 0.1), Vector3(2.5, -1, 0.05), Vector3(2, 0, 0)), 
                     Triangle(Vector3(2, 0, 0), Vector3(2, 0, 0.1), Vector3(3, 0, 0.1)), 
                     Triangle(Vector3(2, 0, 0), Vector3(3, 0, 0.1), Vector3(3, 0, 0))]

renderer_clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    
    screen.fill(SCREEN_COLOR)

    keys_pressed = pygame.key.get_pressed()

    move_vector = Vector3()
    if keys_pressed[pygame.K_w]: move_vector.y += 0.001
    if keys_pressed[pygame.K_a]: move_vector.x += 0.001
    if keys_pressed[pygame.K_s]: move_vector.y -= 0.001
    if keys_pressed[pygame.K_d]: move_vector.x -= 0.001
    if keys_pressed[pygame.K_UP]: move_vector.z -= 0.001
    if keys_pressed[pygame.K_DOWN]: move_vector.z += 0.001

    for triangle in cube.triangles:
        for vertex in triangle.vertices: vertex += move_vector

        projectedVertices = [Vector2(triangle.vertices[0].x, triangle.vertices[0].y),
                             Vector2(triangle.vertices[1].x, triangle.vertices[1].y),
                             Vector2(triangle.vertices[2].x, triangle.vertices[2].y)]
        
        for index, projectedVertex in enumerate(projectedVertices):
            projectedVertex.x *= 200
            projectedVertex.y *= 200

            projectedVertex.x /= triangle.vertices[index].z * tan(RADIAN_FOV / 2) + 1
            projectedVertex.y /= triangle.vertices[index].z * tan(RADIAN_FOV / 2) + 1

            projectedVertex.x += (SCREEN_WIDTH / 2 - cube.size / 2)
            projectedVertex.y += (SCREEN_HEIGHT / 2 - cube.size / 2)

        pygame.draw.line(screen, cube.color, projectedVertices[0], projectedVertices[1])
        pygame.draw.line(screen, cube.color, projectedVertices[1], projectedVertices[2])
        pygame.draw.line(screen, cube.color, projectedVertices[2], projectedVertices[0])

    for triangle in pyramid.triangles:
        for vertex in triangle.vertices: vertex += move_vector

        projectedVertices = [Vector2(triangle.vertices[0].x, triangle.vertices[0].y),
                             Vector2(triangle.vertices[1].x, triangle.vertices[1].y),
                             Vector2(triangle.vertices[2].x, triangle.vertices[2].y)]
        
        for index, projectedVertex in enumerate(projectedVertices):
            projectedVertex.x *= 200
            projectedVertex.y *= 200
            
            projectedVertex.x /= triangle.vertices[index].z * tan(RADIAN_FOV / 2) + 1
            projectedVertex.y /= triangle.vertices[index].z * tan(RADIAN_FOV / 2) + 1

            projectedVertex.x += (SCREEN_WIDTH / 2 - cube.size / 2)
            projectedVertex.y += (SCREEN_HEIGHT / 2 - cube.size / 2)

        pygame.draw.line(screen, pyramid.color, projectedVertices[0], projectedVertices[1])
        pygame.draw.line(screen, pyramid.color, projectedVertices[1], projectedVertices[2])
        pygame.draw.line(screen, pyramid.color, projectedVertices[2], projectedVertices[0])

    pygame.display.flip()

    renderer_clock.tick()
    print(f"FPS: {renderer_clock.get_fps()}")

pygame.quit()