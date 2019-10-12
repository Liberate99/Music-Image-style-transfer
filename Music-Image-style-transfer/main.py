# -*- coding: utf-8 -*-
'''
@Time    : 2019/10/11 15:20
@Author  : DJ
@File    : main.py
'''

from MusicEmotionRecognition.recognition import recognition
from NurelStyleTransfer.transfer import transfer



def main():
    print("=======================音乐情感识别引导图片风格迁移========================")

    # todo 音频情感识别
    recognition()

    # todo 图片风格迁移
    transfer()


main()