from enum import Enum


class Color(Enum):
    RED = "Red"
    ORANGE = "Orange"
    BLUE = "Blue"
    GREEN = "Green"
    WHITE = "White"
    YELLOW = "Yellow"


color_code = {
    Color.RED: "\033[31m",
    Color.ORANGE: "\033[35m",
    Color.BLUE: "\033[34m",
    Color.GREEN: "\033[32m",
    Color.WHITE: "\033[38m",
    Color.YELLOW: "\033[33m"
}
