from Cube2x2 import Cube2x2
from CubeSolver import CubeSolver


def main():
    cube2x2 = Cube2x2()
    cube2x2.shuffle()
    cube2x2.print_state()

    cs = CubeSolver(cube2x2)
    solution = cs.solve()
    print("Solution:")
    print(cube2x2.prettify_ways(solution))


if __name__ == "__main__":
    main()
