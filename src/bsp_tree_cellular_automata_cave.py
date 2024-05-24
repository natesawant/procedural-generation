import random


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def center(self):
        return int(self.x + self.w // 2, self.y + self.h // 2)

    def __str__(self) -> str:
        return f"{self.w} x {self.h} - ({self.x},{self.y})"


class BSPNode:
    def __init__(self, rect):
        self.rect = rect
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.rect}"


def create_bsp_tree(rect, max_depth, min_size):
    if max_depth == 0 or rect.w < min_size or rect.h < min_size:
        return None

    # Choose split axis (randomly for simplicity)
    split_axis = random.choice(["x", "y"])

    # Choose split position
    split_value = (
        random.uniform(rect.x + min_size, rect.x + rect.w - min_size)
        if split_axis == "x"
        else random.uniform(rect.y + min_size, rect.y + rect.h - min_size)
    )

    new_node = BSPNode(rect)

    # Split rectangle based on chosen axis
    if split_axis == "x":
        left_rect = Rect(rect.x, rect.y, split_value - rect.x, rect.h)
        right_rect = Rect(split_value, rect.y, rect.w - (split_value - rect.x), rect.h)
    else:
        left_rect = Rect(rect.x, rect.y, rect.w, split_value - rect.y)
        right_rect = Rect(rect.x, split_value, rect.w, rect.h - (split_value - rect.y))

    new_node.left = create_bsp_tree(left_rect, max_depth - 1, min_size)
    new_node.right = create_bsp_tree(right_rect, max_depth - 1, min_size)

    return new_node


# Example usage
room_size = 100
max_depth = 4
min_room_size = 50

ascii_grid = [["0" for x in range(room_size)] for y in range(room_size)]

root_rect = Rect(0, 0, room_size, room_size)
bsp_tree = create_bsp_tree(root_rect, max_depth, min_room_size)

num = list(range(1, 10))

stack = [bsp_tree]

while stack:
    current = stack.pop()
    print(current)
    if current.left:
        stack.append(current.left)
    if current.right:
        stack.append(current.right)

    # Leaf
    if not current.left and not current.right:
        for dx in range(int(current.rect.x)):
            for dy in range(int(current.rect.y)):
                x = int(current.rect.w + dx)
                y = int(current.rect.h + dy)

                ascii_grid[x][y] = f"{num.pop()}"

for h in range(len(ascii_grid)):
    row = ""
    for w in range(len(ascii_grid[h])):
        row += ascii_grid[h][w]

    print(row)

# This example doesn't handle visualizing the BSP tree
# You can define functions to traverse and process the tree structure
# for your specific needs
