from triangle import Triangle

class Mesh:
    def __init__(self, size: int, color: tuple) -> None:
        self.triangles: list[Triangle] = []
        self.size = size
        self.color = color