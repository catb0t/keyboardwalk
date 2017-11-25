#!/usr/bin/env python3
import keyboardwalk
import itertools
# from pprint import pprint
kb = keyboardwalk.Matrix_2D(
  ["qw", "as"]
)

print(kb)

combs = set(map(
    lambda x: keyboardwalk.Twople(*x),
    itertools.permutations([-1, -1, 0, 0, 1, 1], 2)
))


def make_tree_level(l, keyboard):
    for m in range(~keyboard):
        for n in range(+keyboard):
            surr_chars = []
            for c in combs:
                mn = keyboardwalk.Twople(m, n)
                add = mn + c
                if mn != add and (abs(add) == add):
                    surr_chars.append(c)

            l[ keyboard[m:n] ] = {keyboard[x]: dict() for x in surr_chars}

    return l


l = make_tree_level(dict(), kb)
