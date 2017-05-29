#!/usr/bin/env python3

import pprint


class Matrix_2D:

    def __init__(self, mat):
        if type(mat) == type(self):
            self.mat = mat.mat
            self.x = mat.x
            self.y = mat.y
        else:

            self.mat = mat_rpad(tuple(tuple(i) for i in mat))
        self.x = 0
        self.y = 0

    def __getitem__(self, key):
        '''if the key is found, return its index, else try to index'''
        for idx, elt in enumerate(self.mat):
            try:
                x = elt.index(key)
            except ValueError:
                pass
            else:
                return Twople([x, idx])

        if isinstance(key, int):
            return self.mat[self.y][self.x]
        if isinstance(key, slice):
            return self.mat[key.stop][key.start]

        raise TypeError("failed to getitem with key {} of type {}"
                        .format(key, type(key)))

    def __iadd__(self, rhs):
        '''changes .x if int, or both if list'''
        if isinstance(rhs, int):
            self.x_chg(rhs)

        elif type(rhs) in (tuple, list, Twople):
            self.x_chg(rhs[0])
            self.y_chg(rhs[1])
        return self

    def __imul__(self, rhs):
        '''changes .y if int, or both if list'''
        if isinstance(rhs, int):
            self.y_chg(rhs)

        elif type(rhs) in (tuple, list, Twople):
            self.x_chg(rhs[0])
            self.y_chg(rhs[1])
        return self

    def __itruediv__(self, rhs):
        '''sets the .x and .y'''
        if type(rhs) in (tuple, list, Twople):
            self.x = rhs[0]
            self.y = rhs[1]
        return self

    def __imod__(self, rhs):
        '''changes the matrix itself'''
        self.mat = tuple(tuple(i) for i in rhs)
        return self

    def __pos__(self):
        '''returns max for y'''
        return len(self.mat)

    def __invert__(self):
        '''returns max for x'''
        if not len(self.mat):
            return 0
        return len(self.mat[0])

    def x_chg(self, n):
        self.x = self._chgx(n)

    def y_chg(self, n):
        self.y = self._chgy(n)

    def _chgx(self, n):
        v = self.x + n
        if v < 0: return 0
        if v > len(self.mat[self.y]) - 1: return len(self.mat[self.y]) - 1
        return v

    def _chgy(self, n):
        v = self.y + n
        if v < 0: return 0
        if v > len(self.mat) - 1: return len(self.mat) - 1
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


def walk_rec(kbd, wlk, dbg=False):  # , _last=None):
    '''
        Use recursion to determine whether a string is a walk of a keyboard.
    '''
    lw = len(wlk)
    if lw < 2: return True
    if lw % 2:
        if not walk_rec(kbd, wlk[-2:], dbg=dbg):
            return False

    kbd_mat = Matrix_2D(kbd)
    first, second = wlk[:2]
    fi, si = kbd_mat[first], kbd_mat[second]
    diff   = Twople( map( abs, fi - si ) ).sort()
    valid  = tuple(diff) in ( (0, 0), (0, 1), (1, 1) )

    if dbg: print(first, fi, second, si, diff, valid)

    if valid: return walk_rec(kbd, wlk[2:], dbg=dbg)

    return False


def walk(kbd, wlk):
    return walk_rec(kbd, wlk, dbg=False)


def gen_rand_walk(kbd, wlk_len):
    from random import randrange, seed, choice
    from time import time

    seed(time() * 100)
    wlk            = []
    kbd_mat        = Matrix_2D(kbd)
    while kbd_mat[0] != " ":
        startx, starty = randrange(~kbd_mat), randrange(+kbd_mat)
        kbd_mat /= (startx, starty)

    from itertools import permutations
    dirs     = tuple(permutations((0, 1, -1), 2))

    for c in range(wlk_len):
        td = choice(dirs)  # or dirs[c % (len(dirs) - 1) ]
        kbd_mat += td
        wlk     += kbd_mat[0]

    return wlk


def mat_rpad(mat, padwith=None):
    maxlen = max(map(len, mat))

    if padwith is None:
        padwith = " " if type(mat[0][0]) == str else 0
    for idx, elt in enumerate(mat):
        diff = maxlen - len(elt)
        if diff:
            mat[idx] += [padwith] * diff
    return mat


def main():
    kbd = ["qwertyu", "asdfghj", " zxcvbn"]  # input("kbd: ").split(" ")
    # wlk = "wsdcvb"
    wl  = 4
    print(gen_rand_walk(kbd, wl))
    return

    kbd_mat = Matrix_2D(kbd)
    pprint.pprint(kbd_mat)
    kbd_mat += (2, 1)
    kbd_mat *= -1
    pprint.pprint(kbd_mat)
    kbd_mat /= (1, 1)
    kbd_mat %= reversed(kbd_mat)
    pprint.pprint(kbd_mat)
    print(kbd_mat["a"])


if __name__ == '__main__':
    main()
