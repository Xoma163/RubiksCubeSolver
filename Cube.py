import random
from typing import List

from Color import Color, color_code
from Movement import Movement, MovementWay
from Side import Side


class Cube:
    DIM = 0

    def __init__(self):
        self.state = {
            Movement.U: Side(self.DIM, Color.YELLOW),
            Movement.L: Side(self.DIM, Color.RED),
            Movement.F: Side(self.DIM, Color.GREEN),
            Movement.R: Side(self.DIM, Color.ORANGE),
            Movement.B: Side(self.DIM, Color.BLUE),
            Movement.D: Side(self.DIM, Color.WHITE)
        }
        self.allowed_moves = set(x.value for x in Movement)

    def shuffle(self):
        random_moves = 5
        moves = []
        for _ in range(random_moves):
            if len(moves) > 0:
                allowed_moves_now = self.allowed_moves - moves[-1].anti_ways
            else:
                allowed_moves_now = self.allowed_moves
            move = random.sample(allowed_moves_now, 1)[0]
            moves.append(move)
            self.rotate(move)

        print(self.prettify_ways(moves))

    @staticmethod
    def prettify_ways(moves: List[MovementWay]):
        new_moves = []
        for move in moves:
            if len(new_moves) != 0 and new_moves[-1] == move.real_name:
                new_moves[-1] = new_moves[-1] + "2"
            else:
                new_moves.append(move.real_name)
        return " ".join([x for x in new_moves])

    def rotate(self, _dir: MovementWay):
        rotate_map = {
            Movement.L.value.side: self.rotate_l,
            Movement.R.value.side: self.rotate_r,
            Movement.U.value.side: self.rotate_u,
            Movement.D.value.side: self.rotate_d,
            Movement.F.value.side: self.rotate_f,
            Movement.B.value.side: self.rotate_b
        }
        method = rotate_map[_dir.side]
        if _dir.double_way:
            method(_dir.back_way)
            # self.print_state()
        method(_dir.back_way)
        # self.print_state()

    def rotate_r(self, back_way):
        self.state[Movement.R].rotate(back_way)
        self.rotate_rl(back_way, index=-1)

    def rotate_l(self, back_way):
        self.state[Movement.L].rotate(back_way)
        self.rotate_rl(not back_way, index=0)

    def rotate_rl(self, back_way, index):
        index2 = -1 if index == 0 else 0
        state_1 = [x[index] for x in self.state[Movement.F].matrix]
        state_2 = [x[index] for x in self.state[Movement.U].matrix]
        state_3 = [x[index2] for x in self.state[Movement.B].matrix]
        state_4 = [x[index] for x in self.state[Movement.D].matrix]

        if back_way:
            state_1, state_2, state_3, state_4 = state_3, state_4, state_1, state_2
            state_1 = list(reversed(state_1))
        else:
            state_3 = list(reversed(state_3))
        state_2 = list(reversed(state_2))

        for i in range(self.DIM):
            self.state[Movement.F].matrix[i][index] = state_4[i]
            self.state[Movement.U].matrix[i][index] = state_1[i]
            self.state[Movement.B].matrix[i][index2] = state_2[i]
            self.state[Movement.D].matrix[i][index] = state_3[i]

    def rotate_u(self, back_way):
        self.state[Movement.U].rotate(back_way)
        self.rotate_ud(back_way, index=0)

    def rotate_d(self, back_way):
        self.state[Movement.D].rotate(back_way)
        self.rotate_ud(not back_way, index=-1)

    def rotate_ud(self, back_way, index):
        state_1 = self.state[Movement.F].matrix[index]
        state_2 = self.state[Movement.L].matrix[index]
        state_3 = self.state[Movement.B].matrix[index]
        state_4 = self.state[Movement.R].matrix[index]

        if back_way:
            state_1, state_2, state_3, state_4 = state_3, state_4, state_1, state_2

        self.state[Movement.F].matrix[index] = state_4
        self.state[Movement.L].matrix[index] = state_1
        self.state[Movement.B].matrix[index] = state_2
        self.state[Movement.R].matrix[index] = state_3

    def rotate_f(self, back_way):
        self.state[Movement.F].rotate(back_way)
        self.rotate_fb(back_way, index=-1)

    def rotate_b(self, back_way):
        self.state[Movement.B].rotate(back_way)
        self.rotate_fb(not back_way, index=0)

    def rotate_fb(self, back_way, index):
        index2 = -1 if index == 0 else 0

        state_1 = self.state[Movement.U].matrix[index]
        state_2 = [x[index2] for x in self.state[Movement.R].matrix]
        state_3 = self.state[Movement.D].matrix[index2]
        state_4 = [x[index] for x in self.state[Movement.L].matrix]
        if back_way:
            state_1, state_2, state_3, state_4 = state_3, state_4, state_1, state_2
            state_1 = list(reversed(state_1))
            state_3 = list(reversed(state_3))
        else:
            state_2 = list(reversed(state_2))
            state_4 = list(reversed(state_4))

        self.state[Movement.U].matrix[index] = state_4
        for i in range(self.DIM):
            self.state[Movement.R].matrix[i][index2] = state_1[i]
        self.state[Movement.D].matrix[index2] = state_2
        for i in range(self.DIM):
            self.state[Movement.L].matrix[i][index] = state_3[i]

    def print_state(self):
        print("\033[40m", end="")

        MARGIN_LEFT = " " * (self.DIM * 2 + 1)
        for i in range(self.DIM):
            for j in range(self.DIM):

                item = self.state[Movement.U].matrix[i][j]
                item_color = f"{color_code[item]}■ "
                if j == 0:
                    print(MARGIN_LEFT + item_color, end="")
                else:
                    print(item_color, end="")
            print()
        for i in range(self.DIM):
            for m in [Movement.L, Movement.F, Movement.R, Movement.B]:
                for j in range(self.DIM):
                    item = self.state[m].matrix[i][j]
                    item_color = f"{color_code[item]}■ "
                    print(item_color, end="")
                print(" ", end="")
            print()
        for i in range(self.DIM):
            for j in range(self.DIM):
                item = self.state[Movement.D].matrix[i][j]
                item_color = f"{color_code[item]}■ "
                if j == 0:
                    print(MARGIN_LEFT + item_color, end="")
                else:
                    print(item_color, end="")
            print()
        # 0 2
        # 1 3
        print("\033[0m")
