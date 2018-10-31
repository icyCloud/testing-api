#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 下午4:31
# @Author  : Ganodermaking

import ConfigParser
import os


class Config:
    # 项目根目录
    base_dir = "/Users/ganodermaking/code/python/testing-api/"

    def __init__(self):
        pass

    @staticmethod
    def get(section, key, filename="config.ini"):
        os.chdir(Config.base_dir)
        cf = ConfigParser.ConfigParser()
        cf.read(filename)
        return cf.get(section, key)
