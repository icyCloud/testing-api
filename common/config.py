#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 下午4:31
# @Author  : Ganodermaking

import ConfigParser
import os


class Config:
    # 项目根目录
    base_dir = "./"

    def __init__(self):
        pass

    @staticmethod
    def get(section, key, file="config.ini"):
        os.chdir(Config.base_dir)
        cf = ConfigParser.ConfigParser()
        cf.read(file)
        return cf.get(section, key)
