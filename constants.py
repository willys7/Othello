class Constants():
    Black = 0
    White = 1
    Depth = 0
    Max = float('-Inf')
    Min = float('Inf')

    def __init__(self, depth):
        self.Depth = depth

    def setColor(self, color):
        if color == 1:
            self.Black = 1
            self.White = 2
        else:
            self.Black = 2
            self.White = 1