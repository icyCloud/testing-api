#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 下午4:59
# @Author  : Ganodermaking

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from case.passport import PassportTestCase
from common.HTMLTestRunnerCN import HTMLTestRunner
from common.config import Config

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(PassportTestCase))
loader.loadTestsFromModule(PassportTestCase)

runner_path = Config.get('runner', 'RUNNER_PTAH')
runner_title = Config.get('runner', 'RUNNER_TITLE')
runner_description = Config.get('runner', 'RUNNER_DESCRIPTION')
runner_tester = Config.get('runner', 'RUNNER_TESTER')

fp = file(runner_path, 'wb')
runner = HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title=runner_title,
    description=runner_description,
    tester=runner_tester
)

runner.run(suite)
fp.close()
