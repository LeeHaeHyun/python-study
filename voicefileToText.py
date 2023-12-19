# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
import os
from PyQt5.QtGui import *
import speech_recognition as sr  # 음성인식 모듈
import pydub
import webbrowser as wb

# from pydub import AudioSegment
import time

form_class = uic.loadUiType("voiceTotext.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon("pagichacha.png"))
        self.setupUi(self)

        self.pushButton.clicked.connect(self.voiceToText)
        self.toolButton.clicked.connect(self.selectFile)

    def m4aToWav(self, fromVoiceFile):  # 휴대폰 통화 녹음파일
        # m4a_file = 'sunny.m4a'
        # wav_filename = 'sunny.wav'
        voiceFile = fromVoiceFile
        name, ext = os.path.splitext(voiceFile)
        dir = os.path.dirname(file[0])
        os.chdir(dir)
        m4asound = pydub.AudioSegment.from_file(fromVoiceFile, format="m4a")
        m4asound.export(name + ".wav", format="wav")

    def mp3ToWav(self, fromVoiceFile):  # 일반 음악 파일
        voiceFile = fromVoiceFile
        name, ext = os.path.splitext(voiceFile)
        dir = os.path.dirname(file[0])
        os.chdir(dir)
        mp3sound = pydub.AudioSegment.from_mp3(fromVoiceFile)
        mp3sound.export(name + ".wav", format="wav")  # mp3 -> wav파일로 변환

    def voiceToText(self):
        if self.lineEdit.text():
            voiceFile = os.path.basename(file[0])
            print(voiceFile, "++++++++++++++++++ 1")
            name, ext = os.path.splitext(voiceFile)
            print(name, "++++++++", ext)
            dir = os.path.dirname(file[0])
            os.chdir(dir)

            if not (ext == ".m4a" or ext == ".mp3" or ext == ".wav"):
                print("m4a, mp3, wav 파일이 아닙니다.")
                print("m4a, mp3, wav 파일 외에는 음성파일을 사용할 수 없습니다.")
                self.textEdit.setText("m4a, mp3, wav 파일 외에는 음성파일을 사용할 수 없습니다.")
            else:
                if ext == ".m4a":
                    print("m4a 형식의 파일을 wav 파일로 변환합니다.")
                    self.textEdit.setText("m4a 형식의 파일을 wav 파일로 변환합니다.")
                    self.m4aToWav(voiceFile)
                elif ext == ".mp3":
                    print("mp3 형식의 파일을 wav 파일로 변환합니다.")
                    self.textEdit.setText("mp3 형식의 파일을 wav 파일로 변환합니다.")
                    self.mp3ToWav(voiceFile)
                elif ext == ".wav":
                    print("wav 형식의 파일을 선택하셨습니다.")
                    self.textEdit.setText("wav 형식의 파일을 선택하셨습니다.")
                else:
                    print("m4a, mp3, wav 파일 외에는 음성파일을 사용할 수 없습니다.")
                    self.textEdit.setText("m4a, mp3, wav 파일 외에는 음성파일을 사용할 수 없습니다.")

                time.sleep(3)

                # 음성인식 부분
                r = sr.Recognizer()
                harvard = sr.AudioFile(name + ".wav")
                with harvard as source:  # <---------------- 여기 에러부터 다시 시작
                    audio = r.record(source)  # .wav파일을 오디오 데이터 인스터스로 만듦

                text = r.recognize_google(
                    audio, language="ko-KR"
                )  # 만들어진 오디오 데이터 인스턴스를 다시 구글 음성인식 모듈로 텍스트로 변환함

                print(text)  # 구글 번연(AI)으로 음성(.wav)파일의 음성을 텍스트로 변환
                self.textEdit.setText(text)

                with open(
                    "memo.txt", "w", encoding="utf-8"
                ) as f:  # memo.txt 파일로 번역된 텍스트 저장
                    f.write(str(text) + "\n")

        else:
            print("음성파일을 선택하지 않았거나, 파일명을 입력하지 않았습니다.")
            self.textEdit.setText("음성파일을 선택하지 않았거나, 파일명을 입력하지 않았습니다.")

    def selectFile(self):
        pass
        global file
        file = QtWidgets.QFileDialog.getOpenFileName()
        print(file)
        print(file[0])
        self.lineEdit.setText("{}".format(file[0]))


app = QApplication(sys.argv)
window = MyWindow()
window.show()
print("Before event loop")
app.exec_()
print("After event loop")
