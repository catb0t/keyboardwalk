#!/usr/bin/env python3

import pprint


class Matrix_2D:

    def __init__(self, mat ):
        self.mat = tuple(tuple(i) for i in mat)
        self.x = 0
        self.y = 0

    def __getitem__(self, key):
        for idx, elt in enumerate(self.mat):
            try:
                x = elt.index(key)
            except ValueError:
                pass
            else:
                return Twople([x, idx])

        if isinstance(key, int):
            return self.mat[self.y][self.x]
            raise ValueError("expected slice (got int)")
        if isinstance(key, slice):
            return self.mat[key.stop][key.start]

    def __iadd__(self, rhs):
        if isinstance(rhs, int):
            self.x_chg(rhs)
            return self
        if any(isinstance(rhs, c) for c in (tuple, list)):
            self.x_chg(rhs[0])
            self.y_chg(rhs[1])
            return self

    def __imul__(self, rhs):
        if isinstance(rhs, int):
            self.y_chg(rhs)
            return self
        if any(isinstance(rhs, c) for c in (tuple, list)):
            self.x_chg(rhs[0])
            self.y_chg(rhs[1])
            return self

    def __itruediv__(self, rhs):
        if any(isinstance(rhs, c) for c in (tuple, list)):
            self.x = rhs[0]
            self.y = rhs[1]
            return self

    def __imod__(self, rhs):
        self.mat = tuple(tuple(i) for i in rhs)
        return self

    def x_chg(self, n):
        self.x = self._chgx(n)

    def y_chg(self, n):
        self.y = self._chgy(n)

    def _chgx(self, n):
        v = self.x + n
        if v < 0: return 0
        if v > len(self.mat[self.y]): return len(self.mat[self.y])
        return v

    def _chgy(self, n):
        v = self.y + n
        if v < 0: return 0
        if v > len(self.mat): return len(self.mat)
        return v

    def __repr__(self):
        return "{} {} {}\n{}".format(
            self.x, self.y, self[0],
            pprint.pformat(self.mat, indent=4, width=50)
        )


class Twople(tuple):
    def __sub__(self, rhs):
        return (self[0] - rhs[0], self[1] - rhs[1])

    def sort(self):
        return Twople(sorted(self))


def walk_rec(kb, wk, dbg=False):  # , _last=None):
    '''
        Use recursion to determine whether a string is a walk of a keyboard.
    '''
    lw = len(wk)
    if lw < 2: return True
    if lw % 2:
        if not walk_rec(kb, wk[-2:], dbg=dbg):
            return False

    m = Matrix_2D(kb)
    first, second = wk[:2]
    fi, si = m[first], m[second]
    diff   = Twople( map( abs, fi - si ) ).sort()
    valid  = tuple(diff) in ( (0, 0), (0, 1), (1, 1) )

    if dbg: print(first, fi, second, si, diff, valid)

    if valid: return walk_rec(kb, wk[2:], dbg=dbg)

    return False


def main():
    kb = ["qwerty", "asdfgh", " zxcvbn"]  # input("kb: ").split(" ")
    wk = "wsdcvb"
    print(walk_rec(kb, wk))
    return
    m = Matrix_2D(kb)
    pprint.pprint(m)
    m += (2, 1)
    m *= -1
    pprint.pprint(m)
    m /= (1, 1)
    m %= reversed(kb)
    pprint.pprint(m)
    print(m["a"])


if __name__ == '__main__':
    main()
