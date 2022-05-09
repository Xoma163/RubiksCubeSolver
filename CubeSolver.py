from copy import deepcopy, copy

from utils import flat_list, thread_executor


class CubeSolver:
    def __init__(self, cube):
        self.cube = cube
        self.cube_class = self.cube.__class__

    def solve(self):
        step = 0
        states = [self.cube]
        while True:
            try:
                new_states = flat_list(thread_executor(self.get_new_one_state, states))
                # new_states = self.get_new_states(states)
            except RuntimeWarning as e:
                return e.args[0]
            states = new_states
            step += 1
            print(step)
            print(len(states))

    def get_new_states(self, states):
        new_states = []
        for state in states:
            new_states.append(self.get_new_one_state(state))
        return new_states

    def get_new_one_state(self, state):
        new_states = []
        for move in state.get_allowed_moves():
            copy_cube = copy(state)
            copy_cube.state = deepcopy(state.state)
            copy_cube.moves = deepcopy(state.moves)
            copy_cube.rotate(move)
            if copy_cube.solved:
                raise RuntimeWarning(copy_cube.moves)
            new_states.append(copy_cube)
        return new_states
