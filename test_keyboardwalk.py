#!/usr/bin/env python3

import unittest
import keyboardwalk


linear_walks = [
    "wsdxcv",
    "wsdcvb",
    "qwertyuiop",
    "asdfgbnh",
    "poklmn",
    "asdfgfdsa",
    "jkli",
    "plkio",
    "plm",
    "l",
    "llllllllllp"
]
not_linear_walks = [
    "jklu",
    "asdfguipooi",
    "plu"
]

simple_nonlinear_walks = [
    "qasdfw",
    "wsdxcve",
    "poiul",
    "asdfghjklq",
    "fgds",
    "asdqwzxc"
]
not_simple_nonlinear_walks = [
    "asdqwezxc",
    "asdfhjkl",
    "plqa",
    "oweiru",
    "nmfgtr",
]

KB = keyboardwalk.Keyboards.QWERTY


class TestKBW(unittest.TestCase):
    def test_linear_walks(self):
        for w in linear_walks:
            self.assertTrue(keyboardwalk.walk_lnr(w))

        for w in not_linear_walks:
            self.assertFalse(keyboardwalk.walk_lnr(w))

    def test_nonlinear_walks(self):
        for w in simple_nonlinear_walks:
            print("doing", w)
            self.assertFalse(keyboardwalk.walk_lnr(w))
            self.assertTrue(keyboardwalk.walk_smpl_nlnr(w, dbg=True))

        for w in not_simple_nonlinear_walks:
            self.assertFalse(keyboardwalk.walk_lnr(w))
            self.assertFalse(keyboardwalk.walk_smpl_nlnr(w))

    def test_mat_rpad(self):
        ms = [
            ("abc", "def", "g"),
            ("abcde", "gh", "yuip"),
            ("qwertyuiop", "asdfghjkl", "zxcvb"),
        ]
        ams = [
            ("abc", "def", "g  "),
            ("abcde", "gh   ", "yuip "),
            ("qwertyuiop", "asdfghjkl ", "zxcvb     "),
        ]
        for i in range(len(ms)):
            res = tuple(
                "".join(i)
                for i in keyboardwalk.mat_rpad(ms[i], padwith=" ")
            )
            cmp = ams[i]
            self.assertEqual(res, cmp)

    def test_gen_rand_walk(self):
        self.assertTrue(
            map(
                lambda w: keyboardwalk.walk(w),
                (keyboardwalk.gen_rand_walk(50) for i in range(50))
            )
        )


def suiteFactory(
        *testcases,
        testSorter   = None,
        suiteMaker   = unittest.makeSuite,
        newTestSuite = unittest.TestSuite):
    """
    make a test suite from test cases, or generate test suites from test cases.

    *testcases     = TestCase subclasses to work on
    testSorter     = sort tests using this function over sorting by line number
    suiteMaker     = should quack like unittest.makeSuite.
    newTestSuite   = should quack like unittest.TestSuite.
    """

    if testSorter is None:
        ln         = lambda f:    getattr(tc, f).__code__.co_firstlineno
        testSorter = lambda a, b: ln(a) - ln(b)

    test_suite = newTestSuite()
    for tc in testcases:
        test_suite.addTest(suiteMaker(tc, sortUsing=testSorter))

    return test_suite


def caseFactory(
        scope        = globals().copy(),
        caseSorter   = lambda f: __import__("inspect").findsource(f)[1],
        caseSuperCls = unittest.TestCase,
        caseMatches  = __import__("re").compile("^Test")):
    """
    get TestCase-y subclasses from frame "scope", filtering name and attribs

    scope        = iterable to use for a frame; preferably a hashable
                   (dictionary).
    caseMatches  = regex to match function names against; blank matches every
                   TestCase subclass
    caseSuperCls = superclass of test cases; unittest.TestCase by default
    caseSorter   = sort test cases using this function over sorting by line
                   number
    """

    from re import match

    return sorted(
        [
            scope[obj] for obj in scope
            if match(caseMatches, obj)
            and issubclass(scope[obj], caseSuperCls)
        ],
        key=caseSorter
    )


if __name__ == '__main__':

    cases = suiteFactory(*caseFactory())
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(cases)
