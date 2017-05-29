#!/usr/bin/env python3

import unittest
import keyboardwalk


class TestKBW(unittest.TestCase):
    def test_walks(self):
        walks = [
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
        notwalks = [
            "jklu",
            "asdfguipooi",
            "plu"
        ]
        kb = [
            "qwertyuiop",
            "asdfghjkl ",
            " zxcvbnm  "
        ]
        '''
        for w in walks:
            print("`" + w + "`")
        for w in notwalks:
            print("`" + w + "`")'''

        for w in walks:
            self.assertTrue(keyboardwalk.walk_rec(kb, w))

        for w in notwalks:
            self.assertFalse(keyboardwalk.walk_rec(kb, w))

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
        kb = [
            "qwertyuiop",
            "asdfghjkl ",
            " zxcvbnm  "
        ]
        self.assertTrue(
            map(
                lambda w: keyboardwalk.walk(kb, w),
                (keyboardwalk.gen_rand_walk(kb, 50) for i in range(50))
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
