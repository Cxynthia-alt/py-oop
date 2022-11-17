from triangle import Triangle


class ColoredTriangle(Triangle):
    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color

    def describe(self):
        msg = super().describe()
        return msg + f" My color is {self.color}"
