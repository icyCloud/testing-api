#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 下午8:41
# @Author  : Ganodermaking

import unittest


class DemoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 测试用例们被执行前执行的方法
        print 1

    def setUp(self):
        # 在执行每个测试用例之前被执行，任何异常（除了unittest.SkipTest和AssertionError异常以外）都会当做是error而不是failure，且会终止当前测试用例的执行。
        print 2

    def test_equal1(self):
        print 9
        self.assertEqual(1, 1, '1 not equals 1')

    def test_equal2(self):
        print 9
        self.assertEqual(1, 1, '1 not equals 1')

    def test_equal3(self):
        print 9
        self.assertEqual(1, 1, '1 not equals 1')

    def tearDown(self):
        # 执行了setUp()方法后，不论测试用例执行是否成功，都执行tearDown()方法。如果tearDown()的代码有异常(除了unittest.SkipTest和AssertionError异常以外)，会多算一个error。
        print 3

    @classmethod
    def tearDownClass(cls):
        # 测试用例被执行后执行的方法
        print 4
