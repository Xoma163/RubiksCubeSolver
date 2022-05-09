from enum import Enum


class Color(Enum):
    RED = 1
    ORANGE = 2
    BLUE = 3
    GREEN = 4
    WHITE = 5
    YELLOW = 6


color_code = {
    Color.RED: "\033[31m",
    Color.ORANGE: "\033[35m",
    Color.BLUE: "\033[34m",
    Color.GREEN: "\033[32m",
    Color.WHITE: "\033[38m",
    Color.YELLOW: "\033[33m"
}
