class LFSR():
    def __init__(self, polyn):
        """"(list(int)) -> None"""
        self.polyn = polyn[::-1][1:len(polyn)]

    def step(self):
        """(None) -> bool"""
        numb = 0
        for _ in range(len(self.polyn)):
            numb ^= self.polyn[_] & self.state[_]
        self.state.insert(0, numb)
        return self.state.pop()

    def gener_sequence(self, length):
        """(int) -> list(int)"""
        result = []
        for _ in range(length):
            result.append(self.step())
        return result

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

    def gener_sequence(self, length):
        """(int) -> list(int)"""
        result = []
        for _ in range(length):
            result.append(self.step())
        return result