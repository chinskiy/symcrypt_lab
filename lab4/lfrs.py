class LFSR():
    def __init__(self, polyn, state):
        """"(list(int), list(int)) -> None"""
        self.polyn, self.state = polyn[::-1][1:len(polyn)], state

    def step(self):
        """(None) -> int"""
        numb = 0
        for _ in range(len(self.polyn)):
            numb ^= self.polyn[_] & self.state[_]
        self.state.insert(0, numb)
        return self.state.pop()


class GeffeGen():
    def __init__(self, l1, l2, l3):
        """(list(int), list(int), list(int) -> None"""
        self.l1, self.l2, self.l3 = l1, l2, l3
