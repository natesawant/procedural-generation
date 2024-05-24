import random


class SimpleCellularAutomataCaveGenerator:
    """
    Procedurally generates a `self.width` by `self.height` level that looks like a cave using cellular automata
    """

    EMPTY = "."
    WALL = "#"

    def __init__(
        self,
        width=200,
        height=50,
        percent_fill=0.48,
        border_thickness=5,
        smooth_passes=5,
        border=True,
    ):
        self.width = width
        self.height = height
        self.percent_fill = percent_fill
        self.border_thickness = border_thickness
        self.smooth_passes = smooth_passes
        self.border = border

        self.array = [
            [random.uniform(0.0, 1.0) < self.percent_fill for x in range(self.width)]
            for y in range(self.height)
        ]

    def generate_level(self):
        """
        Randomly fills in the level and then smooths it `self.smooth_passes` times
        """

        for _ in range(self.smooth_passes):
            self.smooth()

        if self.border:
            self.add_border()
            self.smooth()

    def smooth(self):
        """
        Determines if a cell in the level becomes `EMPTY` or a `WALL`
        """
        copy = self.array

        def in_range(x, y) -> bool:
            return x >= 0 and x < self.width and y >= 0 and y < self.height

        def get_neighbor_count(x, y) -> int:
            count = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    count += (
                        1
                        if (in_range(x + dx, y + dy) and copy[y + dy][x + dx])
                        or not in_range(x + dx, y + dy)
                        else 0
                    )
            return count

        for h in range(self.height):
            for w in range(self.width):
                self.array[h][w] = get_neighbor_count(w, h) >= 5

    def add_border(self):
        """
        Adds a border of `self.border_thickness` around the level
        """
        for i, row in enumerate(self.array):
            self.array[i] = (
                [True] * self.border_thickness + row + [True] * self.border_thickness
            )

        self.array = (
            self.border_thickness * [[True] * len(self.array[0])]
            + self.array
            + [[True] * len(self.array[0])] * self.border_thickness
        )

    def print_level(self):
        """
        Prints out the level in as ASCII art
        """
        for h in range(len(self.array)):
            row = ""
            for w in range(len(self.array[h])):
                row += (
                    SimpleCellularAutomataCaveGenerator.WALL
                    if self.array[h][w]
                    else SimpleCellularAutomataCaveGenerator.EMPTY
                )

            print(row)


if __name__ == "__main__":
    generator = SimpleCellularAutomataCaveGenerator()
    generator.generate_level()
    generator.print_level()
