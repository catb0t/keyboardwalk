#!/usr/bin/env python3


class Matrix_2D:
    '''
        Arguments:  mat (a 2d iterable), x (an int) and y (an int)
        Returns:    None
        Throws:     no
        Effects:    none

        Create a new Matrix_2D object for manipulating 2D matricies, given a
            2D iterable.

        If mat is already a Matrix_2D instance, its attributes are copied,
            losslessly, and the x and y arguments are ignored.

        Otherwise, its elements' elements are converted to tuples, and the
            top-level elements converted to tuples.

        x and y default to 0 if they are not provided.
    '''

    def __init__(self, mat, x = 0, y = 0):
        if type(mat) == type(self):
            self.mat = mat.mat
            self.x = mat.x
            self.y = mat.y
        else:
            self.mat = mat_rpad(tuple(tuple(i) for i in mat))
        self.x = x
        self.y = y

    def __getitem__(self, key):
        '''
            Arguments:  key (an object)
            Returns:    key's index in self (if it was found), or the
                currently-indexed element of self.mat with self.x and self.y
                (if key was any int, like self[0] or self[234]), or key's slice
                attributes (if key was a slice, self[1:2] -> .mat[2][1])
            Throws:     IndexError if key isn't found as an element and not an
                        instance of int or slice
            Effects:    no

            If the key is found as an element, return its index as (x, y).

            Else, and if the key is an int, return .mat[.y][.x].

            Else, and if the key is a slice instance, return the element given
                by indexing .mat using slice attributes as .y and .x.

            Note that accesses to .mat with x, y are swapped because of the
                order of indexing.

            That is, .mat[y][x] is what you meant when you said self[x:y],
                since we are taught to list x before y in math class.
        '''
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

        raise IndexError("failed to getitem with key {} of type {}"
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
        self.mat = mat_rpad(tuple(tuple(i) for i in rhs))
        return self

    def __pos__(self):
        '''returns max for y'''
        return len(self.mat)

    def __invert__(self):
        '''returns max for x'''
        if not len(self.mat):
            return 0
        return len(self.mat[0])

    def __neg__(self):
        return ~self

    def x_chg(self, n):
        self.x = self._chgx(n)
        return self.x

    def y_chg(self, n):
        self.y = self._chgy(n)
        return self.y

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

    def repad(self, padwith=None):
        self.mat = mat_rpad(self.mat)

    def __repr__(self):
        import pprint
        return "{} {} {}\n{}".format(
            self.x, self.y, self[0],
            pprint.pformat(self.mat, indent=4, width=50)
        )


class Twople(tuple):
    def __sub__(self, rhs):
        return Twople( (self[0] - rhs[0], self[1] - rhs[1]) )

    def __or__(self, rhs):
        return self[0] | self[1] | rhs

    def __abs__(self):
        return Twople(map(abs, self))

    def sort(self):
        return Twople(sorted(self))


def walk_rec(kbd, wlk, dbg=False):
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
    try:
        fi, si = kbd_mat[first], kbd_mat[second]
    except IndexError:
        return False
    diff   = abs(fi - si).sort()
    valid  = 1 == (diff | 1)  # diff in ( (0, 0), (0, 1), (1, 1) )

    if dbg: print(first, fi, second, si, diff, valid)

    if valid: return walk_rec(kbd, wlk[2:], dbg=dbg)

    return False


def walk(kbd, wlk):
    return walk_rec(kbd, wlk, dbg=False)


def gen_rand_walk(kbd, wlk_len):
    from random import randrange, seed, choice
    from time import time

    seed(time() * 100)
    wlk     = []
    kbd_mat = Matrix_2D(kbd)
    while kbd_mat[0] not in (" ", 0, type( kbd[0][0] ) () ):
        startx, starty  = randrange(~kbd_mat), randrange(+kbd_mat)
        kbd_mat        /= (startx, starty)

    from itertools import permutations
    dirs = tuple(permutations((0, 1, -1), 2))

    for c in range(wlk_len + 1):
        td       = choice(dirs)  # or dirs[c % (len(dirs) - 1) ]
        kbd_mat += td
        wlk     += kbd_mat[0]

    return wlk


def mat_rpad(mat, padwith=None):
    maxlen = max(map(len, mat))

    if padwith is None:
        padwith = type(mat[0][0]) ()

    copy = list( map( lambda x: list(x).copy(), mat))

    for idx, elt in enumerate(copy):
        diff = maxlen - len(elt)
        if diff:
            copy[idx] += [padwith] * diff

    return tuple(map(tuple, copy))


def main():
    '''
    kbd_mat = Matrix_2D(kbd)
    pprint.pprint(kbd_mat)
    kbd_mat += (2, 1)
    kbd_mat *= -1
    pprint.pprint(kbd_mat)
    kbd_mat /= (1, 1)
    kbd_mat %= reversed(kbd_mat)
    pprint.pprint(kbd_mat)
    print(kbd_mat["a"])
    '''
    kbd = ["qwertyu", "asdfghj", " zxcvbn"]  #
    # input("kbd: ").split(" ")
    wlk = input("walk: ")  # "wsdcvb"
    print(walk(kbd, wlk))
    return


if __name__ == '__main__':
    main()
