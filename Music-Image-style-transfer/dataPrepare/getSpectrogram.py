# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/1 18:43
@Author  : DJ
@File    : getSpectrogram.py
"""

import os
import librosa
import librosa.display
import matplotlib.pyplot as plt


# 谱图是通过视觉表示频谱的频率、声音或其他信号，因为它们随时间变化。
# 频谱图有时被称为超声波仪，声纹或语音图。

def getSpectrogram(musicDir, spectrogramDir):
    print("获取音乐语谱图...")

    # 目录下由多个子文件夹组成，每个文件夹中由若干个音频文件组成
    # 将音乐对应的语谱图放入对应文件夹下
    destinationDir = spectrogramDir
    if os.path.exists(musicDir):
        for root, dirs, files in os.walk(musicDir):
            for dir in dirs:
                if not (os.path.exists(destinationDir + "\\" + dir)):
                    os.makedirs(destinationDir + "\\" + dir)
                for root, dirs, files in os.walk(musicDir + "\\" + dir):
                    plt.figure(figsize=(14, 5))
                    for file in files:
                        plt.clf()
                        fileName = file.split(".")[0]
                        audio_path = musicDir + "\\" + dir + "\\" + file
                        desPath = destinationDir + "\\" + dir + "\\" + fileName + ".png"
                        x, sr = librosa.load(audio_path)
                        X = librosa.stft(x)
                        Xdb = librosa.amplitude_to_db(abs(X))
                        librosa.display.specshow(Xdb, sr=sr)
                        plt.savefig(desPath)
    else:
        print("音乐路径错误")
        return


# def getImage(sourcePath, desPath):
#     audio_path = sourcePath
#     x, sr = librosa.load(audio_path)
#     X = librosa.stft(x)
#     Xdb = librosa.amplitude_to_db(abs(X))
#
#     plt.figure(figsize=(14, 5))
#     librosa.display.specshow(Xdb, sr=sr)
#     plt.savefig(desPath)
