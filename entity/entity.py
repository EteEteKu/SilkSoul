

class Entity:
    def __init__(self) -> None:
        self.position = (0,0)
        self.speed = 10

    def gravitation(self):
        self.rect.x-=self.speed
    
    