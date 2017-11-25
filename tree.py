#!/usr/bin/env python3
import keyboardwalk

kb = keyboardwalk.Matrix_2D(["qwe", "asd", "zxc"])
gph = keyboardwalk.matrix_to_adjlist(kb)
print(keyboardwalk.edge_exists_between("a", "w", gph))
print(keyboardwalk.edge_exists_between("a", "o", gph))
