#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 下午4:59
# @Author  : Ganodermaking

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import unittest
from common.excel import Excel
from common.config import Config


class PassportTestCase(unittest.TestCase):
    url = Config.get('runner', 'RUNNER_URL')
    filename = Config.get('runner', 'CASE_URL')
    sheet_name = 'passport'

    execl = Excel(filename, sheet_name)

    def action(self, row, i):
        url = self.url + row['url']
        data = row['data']

        result = requests.post(url, data)
        res = result.json()

        self.execl.write(i + 2, res['code'], res['msg'])
        self.assertEqual(res['code'], row['code'])

    @staticmethod
    def getTestFunc(row, i):
        def func(self):
            self.action(row, i)

        return func


def __generate_test_cases():
    rows = PassportTestCase.execl.read()
    for i in range(len(rows)):
        setattr(PassportTestCase, 'test_func_%s_%s' % (rows[i]['url'], i),
                PassportTestCase.getTestFunc(rows[i], i))
__generate_test_cases()

if __name__ == "__main__":
    unittest.main()
