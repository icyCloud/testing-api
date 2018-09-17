#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 下午4:59
# @Author  : Ganodermaking

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import unittest
from common.config import Config


class PassportTestCase(unittest.TestCase):
    url = Config.get('runner', 'RUNNER_URL')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogin(self):
        url = self.url + "/passport/login"
        data = {"username": "15450100032", "password": "qqqqqq"}

        result = requests.post(url, data)
        ret = result.json()

        self.assertEqual(100, ret['code'])

if __name__ == "__main__":
    unittest.main()
