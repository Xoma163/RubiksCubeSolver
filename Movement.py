from enum import Enum


class MovementWay:
    def __init__(self, real_name):
        self.real_name = real_name
        self.side = real_name[0]
        # self.full_name = full_names
        self.anti_ways = {self}

    @property
    def back_way(self):
        return self.real_name[-1] == "'"

    @property
    def double_way(self):
        return self.real_name[-1] == "2"

    def add_anti_ways(self, *anti_ways):
        self.anti_ways |= set(anti_ways)


L = MovementWay("L")
R = MovementWay("R")
U = MovementWay("U")
D = MovementWay("D")
F = MovementWay("F")
B = MovementWay("B")

L_ = MovementWay("L'")
R_ = MovementWay("R'")
U_ = MovementWay("U'")
D_ = MovementWay("D'")
F_ = MovementWay("F'")
B_ = MovementWay("B'")

L2 = MovementWay("L2")
R2 = MovementWay("R2")
U2 = MovementWay("U2")
D2 = MovementWay("D2")
F2 = MovementWay("F2")
B2 = MovementWay("B2")

L.add_anti_ways(L_, L2, R_)
R.add_anti_ways(R_, R2, L_)
U.add_anti_ways(U_, U2, D_)
D.add_anti_ways(D_, D2, U_)
F.add_anti_ways(F_, F2, B_)
B.add_anti_ways(B_, B2, F_)

L_.add_anti_ways(L, L2, R)
R_.add_anti_ways(R, R2, L)
U_.add_anti_ways(U, U2, D)
D_.add_anti_ways(D, D2, U)
F_.add_anti_ways(F, F2, B)
B_.add_anti_ways(B, B2, F)

L2.add_anti_ways(L2, L, L_)
R2.add_anti_ways(R2, R, R_)
U2.add_anti_ways(U2, U, U_)
D2.add_anti_ways(D2, D, D_)
F2.add_anti_ways(F2, F, F_)
B2.add_anti_ways(B2, B, B_)


# movements = [L, R, U, D, F, B, L_, R_, U_, D_, F_, B_, L2, R2, U2, D2, F2, B2]
# simple_movements = [L, R, U, D, F, B, L_, R_, U_, D_, F_, B_]


class Movement(Enum):
    L = L
    R = R
    U = U
    D = D
    F = F
    B = B
    L_ = L_
    R_ = R_
    U_ = U_
    D_ = D_
    F_ = F_
    B_ = B_
    L2 = L2
    R2 = R2
    U2 = U2
    D2 = D2
    F2 = F2
    B2 = B2
