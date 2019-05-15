#!/usr/bin/env python3
import keyboardwalk

kb = keyboardwalk.Matrix_2D(keyboardwalk.Keyboards.QWERTY)
gph = keyboardwalk.matrix_to_adjlist(kb)
# print(keyboardwalk.edge_exists_between("a", "w", gph))
# print(keyboardwalk.edge_exists_between("a", "o", gph))
# print(keyboardwalk.matrix_to_edgelist(
#   keyboardwalk.Matrix_2D(keyboardwalk.Keyboards.QWERTY)))
# print(keyboardwalk.walk_cplx_nlnr_graph("asd"))
print(keyboardwalk.has_path_to("q", "p", gph))
