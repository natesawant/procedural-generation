import random


class BSPTreeNode:
    """ """

    def __init__(self, x, y, width, height, depth):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.depth = depth
        self.min_dimension = 5

        self.left = None
        self.right = None

        if (
            self.depth > 0
            and self.width > self.min_dimension
            and self.height > self.min_dimension
        ):
            self.left, self.right = self.split()
            
        while not self.left and not self.right and self.width * self.height > 625:
            self.left, self.right = self.split()

    def split(self):
        if self.left or self.right:
            raise ValueError("This node has already been split")

        if self.width > self.height:
            split = random.randint(1, self.width - self.min_dimension)
            left = BSPTreeNode(self.x, self.y, split, self.height, self.depth - 1)
            right = BSPTreeNode(
                self.x + split, self.y, self.width - split, self.height, self.depth - 1
            )
        else:

            split = random.randint(1, self.height - self.min_dimension)
            left = BSPTreeNode(self.x, self.y, self.width, split, self.depth - 1)
            right = BSPTreeNode(
                self.x, self.y + split, self.width, self.height - split, self.depth - 1
            )

        for dimension in (left.width, left.height, right.width, right.height):
            if dimension < self.min_dimension:
                return None, None

        return left, right

    def __str__(self):
        return f"BSPTreeNode(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __repr__(self):
        return self.__str__()


class BSPTreeRoomGenerator:
    def __init__(self, width=200, height=50, depth=100):
        self.width = width
        self.height = height
        self.depth = depth

        self.array = [["." for x in range(self.width)] for y in range(self.height)]

    def generate_level(self):
        self.root = BSPTreeNode(0, 0, self.width, self.height, self.depth - 1)

    def print_level(self):
        stack = [self.root]

        characters = list(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        )

        while stack:
            node = stack.pop()

            print(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            if not node.left and not node.right:
                c = characters.pop(0) if characters else "#"
                for y in range(node.y, node.y + node.height):
                    for x in range(node.x, node.x + node.width):
                        self.array[y][x] = c

        for h in range(len(self.array)):
            row = ""
            for w in range(len(self.array[h])):
                row += self.array[h][w]

            print(row)


if __name__ == "__main__":
    generator = BSPTreeRoomGenerator()
    generator.generate_level()
    generator.print_level()
