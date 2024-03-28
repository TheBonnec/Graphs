from uuid import uuid4


class Vertex:
    def __init__(self, value: str, duration: int) -> None:
        self.id = uuid4()
        self.value: str = value
        self.duration: int = duration
        self.nextVertices: list[Vertex] = []
    
    
    def addNextVertex(self, vertex: object) -> None:
        if isinstance(vertex, Vertex):
            self.nextVertices.append(vertex)
        else:
            print("\nERROR:\nLocation: Vertex Class - addNextVertex\nDescription: Object passed to function is not a Vertex.")
