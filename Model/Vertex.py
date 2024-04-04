from uuid import uuid4


class Vertex:
    def __init__(self, value: str, duration: int) -> None:
        self.id = uuid4()
        self.value: str = value
        self.duration: int = duration
        self.previousVertices: list[Vertex] = []
    
    
    def addPreviousVertex(self, vertex: object) -> None:
        if isinstance(vertex, Vertex):
            self.previousVertices.append(vertex)
        else:
            print("\nERROR:\nLocation: Vertex Class - addNextVertex\nDescription: Object passed to function is not a Vertex.")

    def print(self):
        print("Vertex :",self.value," with duration : ",self.duration)
