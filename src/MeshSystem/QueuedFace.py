class QueuedFace:
    # record that can be buffored and has all information needed for rendering
    def __init__(self, points, color, depth):
        self.points = points
        self.color = color
        self.depth = depth
