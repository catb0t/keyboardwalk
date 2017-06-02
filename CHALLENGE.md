Keyboard Walk or Keyboard Strikeout?
Is it a Key-Boardwalk?
Is it a keyboard walk?

# Classify keyboard walks

---

## Introduction

([This question](https://math.stackexchange.com/questions/2303535/notation-or-formula-for-matrix-traversal) is also a breakdown of this, algorithmically.)

A *walk* of a *keyboard* is any ordered traversal of the *keyboard* in which all characters in the *walk* have coordindates within (1, 1) of at least one other character.

From experimentation, implementation, and testing, I have determined there to be **three distinct kinds of walks** over a given keyboard.

For the purpose of this challenge, a string is **only** a *walk* over a *keyboard* iff the **entire** string is a *walk* -- partial walks are not.

<sub>We're going to use a standard English (US) QWERTY keyboard for example, because that's what I use. We're only interested in the letter keys for now, but you must handle arbitrary keyboards.</sub>

```
Q W E R T Y U I O P
A S D F G H J K L *
* Z X C V B N M * *
```

* **Linear**: `AASD`, `ERFG`, and `KUYHJK` are all *linear walks* on the QWERTY keyboard above, in that if you follow each string's characters through the grid in order, the following is always true of any two successive elements A and B:
```
| (Ax, Ay) − (Bx, By) | ≤ (1, 1)
```

  That is, for two immediately successive elements, their coordinate pairs (x,y) never differ by more than (1,1).

  A recursive algorithm is:

  1. Let `S` be the input string.
  2. If the sorted, absolute difference between the coordinates of `S[1 + n]` and `S[2 + n]` is in the set `{ (0, 0), (0, 1), (1, 1) }`, repeat this step, letting `n` be the number of *previous* steps.
  3. Otherwise, only the part of S traversed thus far is a linear walk on *keyboard*, which may be empty.

  Strings of length 1 are **always** linear walks.

* **Simple** or **trivial nonlinear**:  `FGHD`, `ASDQ`, `TGHR`, and `ZXCVBS` are all **simple nonlinear** (or simply nonlinear) walks on the keyboard above, in that

## Input

- A *keyboard*, as a list of strings or a string with newlines.
- A *test* string, which may or may not be a walk.

You *must* properly handle these cases as well:
* The *test* string may contain some or all of the characters in *keyboard*, or none at all, and vice versa.
* The *test* string and the *keyboard* may each repeat characters, arbitrarily.

Your solution **can** fail, or spontaneously combust, *or* give the correct response, if:
* There are non-ASCII byte values in the *keyboard* or the *test*, or
* there are unprintable (whitespace, `NUL`, `DEL`, etc) characters in the *test*.


## Output

* for a *linear walk*: the text `Linear: walk the bases in order`

* for a *simple nonlinear walk*: `Simple nonlinear: steal second, then home`

* for a *complex nonlinear walk*: `Complex nonlinear: walk home from another dimension`

* else, if the string is not a walk at all, the text `No walk: you struck out!`

## Test Cases

```
need some
```