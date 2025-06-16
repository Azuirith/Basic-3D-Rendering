from pygame import Vector3

class Triangle:
    def __init__(self, vertex_0: Vector3, vertex_1: Vector3, vertex_2: Vector3) -> None:
        self.vertices: list[Vector3] = [vertex_0, vertex_1, vertex_2]