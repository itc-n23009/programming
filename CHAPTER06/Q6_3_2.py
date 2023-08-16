class Square(Rectangle):
    """正方形"""

    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"
