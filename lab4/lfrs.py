class LFSR():
    def __init__(self, polyn):
        self.polyn = polyn[1:len(polyn)][::-1]

    def step(self):
        numb = 0
        for _ in range(len(self.polyn)):
            if self.polyn[_] & self.state[_] == 1:
                numb ^= 1
        self.state.append(numb)
        return self.state.pop(0)

    def gener_sequence(self, length):
        return [self.step() for _ in range(length)]

    def set_state(self, state):
        self.state = state


class GeffeGen():
    def __init__(self, l1, l2, l3):
        self.l1, self.l2, self.l3 = l1, l2, l3

    def step(self):
        x, y, s = self.l1.step(), self.l2.step(), self.l3.step()
        return s & x ^ (1 ^ s) & y

    def set_state(self, st1, st2, st3):
        self.l1.state, self.l2.state, self.l3.state = st1, st2, st3

    def gen_sequence(self, length):
        return [self.step() for _ in range(length)]