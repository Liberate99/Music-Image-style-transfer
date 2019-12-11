# -*- coding: utf-8 -*-
'''
@Time    : 2019/10/11 15:20
@Author  : DJ
@File    : main.py
'''

from MusicEmotionRecognition.recognition import recognition
from NurelStyleTransfer.transfer import transfer
from dataPrepare.dataPrepare import process
import sys



def main():
    print("=======================音乐引导图片风格迁移========================")

    # 音乐文件夹：
    musicDir = "C:\\Users\\lab233\\Desktop\\wavs"
    # 音乐语谱图对应文件夹
    spectrogramDir = ".\\inputs\\spectrogram"

    # 解决最大递归限制报错
    sys.setrecursionlimit(3930)  # 例如这里设置为一百万
    # 数据准备
    process(musicDir, spectrogramDir)

    # todo 音频特征转换网络

    # todo 图片风格迁移
    # transfer()


main()
