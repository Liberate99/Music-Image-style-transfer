# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/1 18:45
@Author  : DJ
@File    : dataPrepare.py
"""
from dataPrepare.getSpectrogram import getSpectrogram

def process(musicDir,spectrogramDir):
    print("获取语谱图")
    getSpectrogram(musicDir,spectrogramDir)