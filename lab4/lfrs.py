class LFSR():
    def __init__(self, polyn):
        """"(list(int)) -> None"""
        self.polyn = polyn[1:len(polyn)][::-1]

    def step(self):
        """(None) -> bool"""
        numb = 0
        for _ in range(len(self.polyn)):
            numb ^= self.polyn[_] & self.state[_]
        self.state.append(numb)
        return self.state.pop(0)

    def gener_sequence(self, length):
        """(int) -> list(int)"""
        return [self.step() for _ in range(length)]

    def set_state(self, state):
        """(list(int)) -> None"""
        self.state = state


class GeffeGen():
    def __init__(self, l1, l2, l3):
        """(LFSR, LFSR, LFSR) -> None"""
        self.l1, self.l2, self.l3 = l1, l2, l3

    def step(self):
        """(None) -> bool"""
        x, y, s = self.l1.step(), self.l2.step(), self.l3.step()
        return s & x ^ (1 ^ s) & y

    def set_state(self, st1, st2, st3):
        """(list(int), list(int), list(int)) -> None"""
        self.l1.state, self.l2.state, self.l3.state = st1, st2, st3

    def gen_sequence(self, length):
        """(int) -> list(int)"""
        return [self.step() for _ in range(length)]