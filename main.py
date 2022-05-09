from Cube2x2 import Cube2x2
from Cube3x3 import Cube3x3


def main():
    cube2x2 = Cube2x2()
    cube2x2.shuffle()
    cube2x2.print_state()

    cube3x3 = Cube3x3()
    cube3x3.shuffle()
    cube3x3.print_state()
    pass


if __name__ == "__main__":
    main()
