from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidget,QListWidgetItem
import pygame
import PLAYER
import threading
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 
        self.player=PLAYER.player()
        self.all_list=PLAYER.read_all_downloaded_list()
        self.fav_list=PLAYER.read_fav_list()



        # 
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1180, 820)
        MainWindow.setStyleSheet("background-color : rgb(46, 52, 54);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 60, 256, 761))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color:rgb(230,5, 64);\n"
"border: 3px solid rgb(230,5, 64);")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 60, 421, 30))
        self.lineEdit.setStyleSheet("background:rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 60, 91, 30))
        self.pushButton.setStyleSheet("color:rgb(255, 255, 255)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(360, 680, 461, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(311, 680, 41, 20))
        self.label.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 680, 41, 17))
        self.label_2.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 710, 40, 40))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 710, 40, 40))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 710, 40, 40))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 710, 40, 40))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/repeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 710, 40, 40))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/shuffle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 710, 40, 40))
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(930, 60, 251, 761))
        # self.listWidget.remo
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("color:rgb(230,5, 64);\n"
"border: 3px solid rgb(230,5, 64);")
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(689, 720, 131, 20))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setProperty("value", 100)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 40, 40))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/user.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 110, 561, 411))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icons/photo_2021-07-06_04-45-30.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(830, 710, 40, 40))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icons/volume-2.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 550, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_6.setText("")
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        # 

        self.listWidget.addItem(QListWidgetItem("all"))
        self.listWidget.addItem(QListWidgetItem("favorite"))
        self.listWidget.removeItemWidget(QListWidgetItem("all"))




        # 


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.download_from_youtube)
        self.listWidget_2.itemDoubleClicked['QListWidgetItem*'].connect(self.load_song)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.add_songs)
        self.horizontalSlider_2.sliderMoved['int'].connect(self.set_volume)
        self.pushButton_7.clicked.connect(self.add_to_list)
        self.pushButton_6.clicked.connect(self.shuffle)
        self.pushButton_5.clicked.connect(self.repeat)
        self.pushButton_4.clicked.connect(self.song_end_next)
        self.pushButton_3.clicked.connect(self.song_end_previous)
        self.pushButton_2.clicked.connect(self.play_pause)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "search"))
        self.label.setText(_translate("MainWindow", "00:00"))
        self.label_2.setText(_translate("MainWindow", "00:00"))



    def download_from_youtube(self):
        PLAYER.download_audio(self.lineEdit.text,"/MUSICS/")

    def play_pause(self):
        self.player.play_pause()   

    def song_end_next(self):
        self.player.song_end_next() 
    def song_end_previous(self):
        self.player.song_end_previous() 
        
    def set_volume(self,v):
        self.player.set_volume(round(v/100,1))

    def repeat(self):
        self.player.repeat()

    def shuffle(self):
        self.player.shuffle()

    def add_to_list(self):
        self.fav_list.append(self.player.playlist[self.player.index])
        PLAYER.write_fav_list(self.fav_list)
        PLAYER.write_all_songs()

    def add_songs(self,item):
        if item.text()=="all":
            self.player.load_playlist(PLAYER.read_fav_list())
            for i in PLAYER.read_fav_list():
                self.listWidget_2.addItem(QListWidgetItem(i))
        elif item.text()=="favorite":
            self.player.load_playlist(PLAYER.read_all_downloaded_list())
            for i in PLAYER.read_all_downloaded_list():
                self.listWidget_2.addItem(QListWidgetItem(i))


    def load_song(self,item):
        print(self.player.playlist)
        self.player.load_song(self.player.playlist.index(item.text()))


    def time_writer(self):
        cc=pygame.time.Clock()
        while threading.active_count()>1:
            print(self.player.current_time)
            self.label.text=str(self.player.current_time//60)+":"+str(round(self.player.current_time%60))
            self.horizontalSlider.setValue(round(self.player.current_time/self.player.duration*100))
            cc.tick(5)

if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    tt=threading.Thread(target=ui.time_writer)

    tt.start()
    MainWindow.show()
    sys.exit(app.exec_())
