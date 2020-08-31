#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

import unittest
from converter import *
from main import *


class ExampleTest(unittest.TestCase):
    """Jack unittest """
    def test_read_js(self):
        text = "/Users/hadooper/PycharmProjects/BCDE321_Assignment2/JStest1.js"
        result = cli().do_read_js(text)
        self.assertTrue(result)
    #
    # def test_uml_diagram_fig(self):
    #     text = "/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -fig"
    #     result = CLI().do_uml_diagram(text)
    #     self.assertTrue(result)
    #
    # def test_uml_diagram_dot(self):
    #     text = "/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -dot"
    #     result = CLI().do_uml_diagram(text)
    #     self.assertTrue(result)
    #
    # def test_uml_diagram_wrong(self):
    #     text = "/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -png"
    #     result = CLI().do_uml_diagram(text)
    #     self.assertFalse(result)
    #
    # def test_chart(self):
    #     result = CLI().do_chart('/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -b')
    #     self.assertTrue(result)
    #
    # def test_table(self):
    #     result = CLI().do_chart('/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -t')
    #     self.assertTrue(result)
    #
    # def test_chart_wrong(self):
    #     result = CLI().do_chart('/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -a')
    #     self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
