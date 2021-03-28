



#      WIR SIND HIER !!!
#  WAS MUSSEN WIR MACHEN ??
#     ERROR HANDLING
#         POPUPs
#      SAUBEREN CODE






from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import start
from threading import Thread
import time
from start import loading,time_tk,limite
import json
from PIL import *
import os
import face_recognition as frc
import numpy as np
#import sass
limite = 100
class External(QtCore.QThread):
    signal = QtCore.pyqtSignal(int)
    
    signal_ = QtCore.pyqtSignal(int)

    def run(self):
        count = 0
        while count < limite:
            count += 1
            time.sleep(0.01)
            self.signal.emit(count)




        count = 0
        while count < start.limite:

            #print("count : ",count)
            #print("limite : ",start.limite)
            #print("time list : ",start.time_tk)
            #print("time taken : ",start.time_tk[count])

            time.sleep(start.time_tk[count])
            count +=1
            self.signal_.emit((count/start.limite)*100)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        global path
        global path_2
        path_2 = None
        path = None
        self.width = 1400
        self.height = 720
        MainWindow.resize(self.width,self.height)
        MainWindow.setStyleSheet("background-color: rgb(24, 24, 24);")
        self.color1 = QtGui.QColor(0, 0, 0)
        self.color2 = QtGui.QColor(20, 182, 216)
        self.color3 = QtGui.QColor(255, 40, 59)
        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
        fontstr = QtGui.QFontDatabase.applicationFontFamilies(id)[0]
        tab_font = QtGui.QFont(fontstr)
        tab_font.setPointSize(10)
        tab_font.setBold(False)
        tab_font.setItalic(False)
        tab_font.setWeight(5)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1400,720))

        self.tabWidget.setObjectName("tabWidget")
        #self.tabWidget.setStyleSheet("QTabBar::tab {;color:white} QTabBar::tab:selected {background-color:rgba(0,255,255,0.8);}")
        self.tabWidget.setStyleSheet("QTabBar::tab {padding:5px;background-color:rgba(0,255,255,0.2);border:0.5px solid rgb(99, 255, 255);color:rgb(99, 255, 255)} QTabBar::tab:selected {background-color:rgba(0,255,255,0.4)}")
        self.tabWidget.setFont(tab_font)
        self.shadow_tab = QtWidgets.QGraphicsDropShadowEffect(self.tabWidget,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(99, 255, 255))
        self.tabWidget.setGraphicsEffect(self.shadow_tab)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        

        self.tab_22 = QtWidgets.QWidget(self.tab_2)
        self.tab_22.setGeometry(QtCore.QRect(0, 0, 1400,720))
        self.tab_22.setObjectName("tab_22")
        self.tab_22.setStyleSheet("#tab_22{border-image:url('./src/images/hud_n-1.png');background-attachment: fixed;}")



        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")


        self.tab_11 = QtWidgets.QWidget(self.tab)
        self.tab_11.setGeometry(QtCore.QRect(0, 0, 1400,720))
        self.tab_11.setObjectName("tab_11")
        self.tab_11.setStyleSheet("#tab_11{border-image:url('./src/images/hud_.png');background-attachment: fixed;}")



        #self.page1.setLayout(self.page1Layout)

        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
        fontstr = QtGui.QFontDatabase.applicationFontFamilies(id)[0]
        font1 = QtGui.QFont(fontstr)
        font_ = QtGui.QFont(fontstr)
        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
        fontstr = QtGui.QFontDatabase.applicationFontFamilies(id)[0]

        font_.setPointSize(15)
        font_.setBold(False)
        font_.setItalic(False)
        font_.setWeight(5)
        self.contact = QtWidgets.QLabel(self.tab)
        self.contact.setText("Contact Informations :")
        self.contact.setObjectName("text_contact")
        self.contact.setGeometry(QtCore.QRect(750,10,600,100))
        self.contact.setStyleSheet("#text_contact{background:transparent;color:rgb(99, 255, 255);}")
        self.contact.setFont(font_)
        self.shadow_con = QtWidgets.QGraphicsDropShadowEffect(self.contact,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.contact.setGraphicsEffect(self.shadow_con)
        self.gen = QtWidgets.QLabel(self.tab)
        self.gen.setText("General Informations :")
        self.gen.setObjectName("text_contact")
        self.gen.setGeometry(QtCore.QRect(60,10,600,100))
        self.gen.setStyleSheet("#text_contact{background:transparent;color:rgb(99, 255, 255);}")
        self.gen.setFont(font_)
        self.shadow_con = QtWidgets.QGraphicsDropShadowEffect(self.gen,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.gen.setGraphicsEffect(self.shadow_con)

        self.id_upload = QtWidgets.QPushButton(self.tab)
        self.id_upload.setEnabled(True)
        self.id_upload.setGeometry(QtCore.QRect(40, 100-30, 200, 200))
        self.shadow_ = QtWidgets.QGraphicsDropShadowEffect(self.id_upload,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.id_upload.setObjectName("id_upload")
        self.id_upload.setStyleSheet("#id_upload{background:transparent;border-image:url('./src/images/image-1.png');}")
        self.id_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.id_upload.setMouseTracking(True)
        self.id_upload.setGraphicsEffect(self.shadow_)
        self.id_upload.clicked.connect(self.img_select_2)


        self.plainTextEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(240, 120, 201, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_4.setStyleSheet("#plainTextEdit_4:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_4{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_4.setFont(font1)
        self.plainTextEdit_4.setPlaceholderText("First Name")

        self.plainTextEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(240, 210-30, 201, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet("#plainTextEdit_2:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_2{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_2.setFont(font1)
        self.plainTextEdit_2.setPlaceholderText("Last Name")

        self.plainTextEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(80, 300-30, 131, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_5.setStyleSheet("#plainTextEdit_5:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_5{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_5.setFont(font1)
        self.plainTextEdit_5.setPlaceholderText("Day")

        self.plainTextEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setGeometry(QtCore.QRect(240, 300-30, 131, 31))
        self.plainTextEdit_9.setStyleSheet("#plainTextEdit_9:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_9{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_9.setFont(font1)
        self.plainTextEdit_9.setPlaceholderText("Month")

        self.plainTextEdit_55 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_55.setGeometry(QtCore.QRect(400, 300-30, 131, 31))
        self.plainTextEdit_55.setObjectName("plainTextEdit_5")
        self.plainTextEdit_55.setStyleSheet("#plainTextEdit_5:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_5{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_55.setFont(font1)
        self.plainTextEdit_55.setPlaceholderText("Year")


        self.plainTextEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(80, 350-30, 131, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet("#plainTextEdit_3:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_3{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_3.setFont(font1)
        self.plainTextEdit_3.setPlaceholderText("Country")

        self.plainTextEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(240, 350-30, 131, 31))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.plainTextEdit_6.setStyleSheet("#plainTextEdit_6:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_6{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_6.setFont(font1)
        self.plainTextEdit_6.setPlaceholderText("City")

        self.plainTextEdit = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 400-30, 131, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet("#plainTextEdit:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setPlaceholderText("Gender")





        self.plainTextEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setGeometry(QtCore.QRect(80, 450-30, 291, 31))
        self.plainTextEdit_10.setStyleSheet("#plainTextEdit_10:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_10{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_10.setFont(font1)
        self.plainTextEdit_10.setPlaceholderText("Job")

        self.plainTextEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setGeometry(QtCore.QRect(80, 500-30, 291, 31))
        self.plainTextEdit_11.setStyleSheet("#plainTextEdit_11:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_11{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_11.setFont(font1)
        self.plainTextEdit_11.setPlaceholderText("Work location")

        #CONTACT Informations
        self.plainTextEdit_111 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_111.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_111.setGeometry(QtCore.QRect(800, 120, 291, 31))
        self.plainTextEdit_111.setStyleSheet("#plainTextEdit_11:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_11{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_111.setFont(font1)
        self.plainTextEdit_111.setPlaceholderText("Phone Number 1")

        self.plainTextEdit_222 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_222.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_222.setGeometry(QtCore.QRect(800, 170, 291, 31))
        self.plainTextEdit_222.setStyleSheet("#plainTextEdit_11:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_11{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_222.setFont(font1)
        self.plainTextEdit_222.setPlaceholderText("Phone Number 2")

        self.plainTextEdit_333 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_333.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_333.setGeometry(QtCore.QRect(800, 170+50, 291, 31))
        self.plainTextEdit_333.setStyleSheet("#plainTextEdit_11:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_11{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_333.setFont(font1)
        self.plainTextEdit_333.setPlaceholderText("Email")

        self.plainTextEdit_444 = QtWidgets.QLineEdit(self.tab)
        self.plainTextEdit_444.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_444.setGeometry(QtCore.QRect(800, 170+100, 491, 231))
        self.plainTextEdit_444.setStyleSheet("#plainTextEdit_11:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#plainTextEdit_11{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.plainTextEdit_444.setFont(font1)
        self.plainTextEdit_444.setPlaceholderText("Residence Address")



        self.lab = QtWidgets.QLabel(self.tab_2)
        self.lab.setEnabled(True)
        self.lab.setObjectName("card")
        self.lab.setGeometry(QtCore.QRect(910, 20, 470, 320))
        self.lab.setStyleSheet("#card{background-color:rgba(0, 133, 57,0.2);border:1px solid green;border-top-right-radius:10px;border-bottom-left-radius:10px;}")


        self.lab2 = QtWidgets.QLabel(self.tab_2)
        self.lab2.setEnabled(True)
        self.lab2.setObjectName("card2")
        self.lab2.setGeometry(QtCore.QRect(910, 348, 470, 315))
        self.lab2.setStyleSheet("#card2{background-color:rgba(0, 124, 133,0.2);border:1px solid rgb(0, 179, 255);border-top-right-radius:10px;border-bottom-left-radius:10px;}")
        self.lab2_shadow_blue = QtWidgets.QGraphicsDropShadowEffect(self.lab2,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(0, 70, 99))
        self.lab2.setGraphicsEffect(self.lab2_shadow_blue)
        
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QtCore.QRect(0, 0, 0,0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.frame.setStyleSheet("#frame{background:transparent}")
        

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")

        self.frame2 = QtWidgets.QFrame(self.tab_2)
        self.frame2.setGeometry(QtCore.QRect(1030, 370, 231, 231))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.frame2.setStyleSheet(u"#frame2{background:transparent}")
        self.shadow_frame2 = QtWidgets.QGraphicsDropShadowEffect(self.frame2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 221, 255))
        self.frame2.setGraphicsEffect(self.shadow_frame2)

        self.frame2 = QtWidgets.QFrame(self.tab_2)
        self.frame2.setGeometry(QtCore.QRect(1030, 370, 231, 231))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.frame2.setStyleSheet(u"#frame2{background:transparent}")

        font_noinfo = QtGui.QFont(fontstr)
        font_noinfo.setPointSize(14)
        font_noinfo.setBold(False)
        font_noinfo.setItalic(False)
        font_noinfo.setWeight(50)




        self.label_noimg = QtWidgets.QLabel(self.lab)
        self.label_noimg.setGeometry(QtCore.QRect(180,20,350,200))
        self.label_noimg.setObjectName("label_noimg")
        self.label_noimg.setText("NO IMAGE")
        self.label_noimg.setStyleSheet("#label_noimg{background:transparent;color:rgba(0,255,68,0.6)}")
        self.label_noimg.setFont(font_noinfo)

        self.shadow_lab_ = QtWidgets.QGraphicsDropShadowEffect(self.label_noimg,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 255, 98))
        self.label_noimg.setGraphicsEffect(self.shadow_lab_)

        self.label_noimg2 = QtWidgets.QLabel(self.lab)
        self.label_noimg2.setGeometry(QtCore.QRect(175,60,350,200))
        self.label_noimg2.setObjectName("label_noimg")
        self.label_noimg2.setText("AVAILABLE")
        self.label_noimg2.setStyleSheet("#label_noimg{background:transparent;color:rgba(0,255,68,0.6)}")
        self.label_noimg2.setFont(font_noinfo)

        self.shadow_lab_2 = QtWidgets.QGraphicsDropShadowEffect(self.label_noimg2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 255, 98))
        self.label_noimg2.setGraphicsEffect(self.shadow_lab_2)

        self.label_noinfo = QtWidgets.QLabel(self.lab2)
        self.label_noinfo.setGeometry(QtCore.QRect(140,0,300,300))
        self.label_noinfo.setObjectName("label_noinfo")
        self.label_noinfo.setText("NO INFORMATIONS")
        self.label_noinfo.setStyleSheet("#label_noinfo{background:transparent;color:rgba(0,255,255,0.6)}")
        self.label_noinfo.setFont(font_noinfo)

        self.shadow_frame2_ = QtWidgets.QGraphicsDropShadowEffect(self.label_noinfo,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 221, 255))
        self.label_noinfo.setGraphicsEffect(self.shadow_frame2_)

        self.label_err_face = QtWidgets.QLabel(self.lab)
        #self.label_err_face.setGeometry(QtCore.QRect(160,70,350,200))
        self.label_err_face.setObjectName("label_err_face")
        self.label_err_face.setText("")
        self.label_err_face.setStyleSheet("#label_err_face{background:transparent;color:rgba(255, 28, 51,0.9)}")
        self.label_err_face.setFont(font_noinfo)

        self.popup_icon_err_shadow = QtWidgets.QGraphicsDropShadowEffect(self.label_err_face,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.label_err_face.setGraphicsEffect(self.popup_icon_err_shadow)


        self.popup_icon_err = QtWidgets.QFrame(self.lab)
        self.popup_icon_err.setObjectName("popup_icon_err")
        self.popup_icon_err.setStyleSheet("#popup_icon_err{background:transparent}")
        self.popup_icon_err.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup_icon_err.setFrameShadow(QtWidgets.QFrame.Raised)

        self.popup_icon_err_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_icon_err,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_icon_err.setGraphicsEffect(self.popup_icon_err_shadow)


        self.frame_err = QtWidgets.QFrame(self.tab_2)
        self.frame_err.setObjectName(u"frame_err")
        self.frame_err.setStyleSheet(u"#frame_err{background:transparent}")
        self.frame_err.setGeometry(QtCore.QRect(1030, 500, 411, 51))

        self.frame_err.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_err.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shadow_frame_err = QtWidgets.QGraphicsDropShadowEffect(self.frame_err,blurRadius=30,xOffset=1,yOffset=1,color=QtGui.QColor(222, 18, 21))
        self.frame_err.setGraphicsEffect(self.shadow_frame_err)
        
        self.alert_err = QtWidgets.QFrame(self.tab_2)
        self.alert_err.setObjectName(u"alert_err")
        self.alert_err.setStyleSheet(u"#alert_err{background:transparent}")
        

        self.alert_err.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alert_err.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_err = QtWidgets.QLabel(self.frame_err)
        #self.label_err.setGeometry(QtCore.QRect(75, 80, 50, 50))
        self.label_err.setObjectName("label_err")
        self.label_err.setStyleSheet("#label_err{background:transparent;color:rgba(255, 28, 51,0.9)}")


        self.frame_22 = QtWidgets.QFrame(self.frame2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"#frame_22{background:transparent}")


        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label2 = QtWidgets.QLabel(self.frame_22)
        self.label2.setGeometry(QtCore.QRect(75, 80, 100, 50))
        self.label2.setStyleSheet("#label2{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(23, 65, 66, 200));\n"
"font: 25pt \"Roboto Slab\";\n"
"color: rgb(0, 221, 255);}")

        self.label2.setObjectName("label2")
        self.shadow_label2 = QtWidgets.QGraphicsDropShadowEffect(self.label2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 221, 255))
        self.label2.setGraphicsEffect(self.shadow_label2)




        font = QtGui.QFont(fontstr)
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)





        self.upload = QtWidgets.QPushButton(self.tab_2)
        self.upload.setEnabled(True)
        self.upload.setGeometry(QtCore.QRect(270, 20, 355, 350))

        self.upload.setObjectName("upload")
        self.upload.setStyleSheet("#upload{background:transparent;border-image:url('./src/images/face1.png');}")
        self.upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload.setMouseTracking(True)
        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect(self.upload,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.upload.setGraphicsEffect(self.shadow2)
        self.upload.clicked.connect(self.img_select)

        #pix = QtGui.QPixmap('./imgs/abstract-flat-face-recognition-background_23-2148189720-removebg-preview.png')
        #self.upload.setPixmap(pix)
        self.upload2 = QtWidgets.QPushButton(self.tab_2)
        self.upload2.setEnabled(True)
        self.upload2.setGeometry(QtCore.QRect(480, 496, 120, 50))

        self.upload2.setText("Search")


        self.upload2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload2.setMouseTracking(True)
        self.upload2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.upload2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.upload2.setAutoFillBackground(False)
        self.upload2.setFont(font)
        self.upload2.setStyleSheet("#upload2:hover {background: rgba(0, 252, 150, 0.17);}#upload2{background: rgba(0, 252, 139, 0.1);padding:5px;color:rgb(0, 252, 160);border: 1px solid rgb(0, 252, 160);border-top-right-radius:10px;border-bottom-left-radius:10px;border-color:rgb(0, 252, 139);}")
        self.shadow1 = QtWidgets.QGraphicsDropShadowEffect(self.upload2,blurRadius=20,xOffset=1,yOffset=1)
        self.upload2.setGraphicsEffect(self.shadow1)

        self.upload2.clicked.connect(self.prc)
        self.upload2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.upload2.setShortcut("")
        self.upload2.setCheckable(False)
        self.upload2.setObjectName("upload2")



        self.remove = QtWidgets.QPushButton(self.tab_2)
        self.remove.setEnabled(True)
        self.remove.setGeometry(QtCore.QRect(325, 496, 120, 50))

        self.remove.setText("Reload")


        self.remove.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove.setMouseTracking(True)
        self.remove.setFocusPolicy(QtCore.Qt.NoFocus)
        self.remove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remove.setAutoFillBackground(False)
        self.remove.setFont(font)
        self.remove.setStyleSheet("#remove:hover {background: rgba(255, 106, 0, 0.17);}#remove{background: rgba(255, 106, 0, 0.1);padding:5px;color:rgb(255, 106, 0);border: 1px solid rgb(255, 106, 0);border-top-right-radius:10px;border-bottom-left-radius:10px;border-color:rgb(255, 106, 0);}")
        self.shadow1 = QtWidgets.QGraphicsDropShadowEffect(self.remove,blurRadius=20,xOffset=1,yOffset=1)
        self.remove.setGraphicsEffect(self.shadow1)
        self.remove.clicked.connect(self.reload)
        self.remove.setInputMethodHints(QtCore.Qt.ImhNone)
        self.remove.setShortcut("")
        self.remove.setCheckable(False)
        self.remove.setObjectName("remove")

       #git test





        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(590, 580, 90, 35))

        self.pushButton.setText("Add")

        self.pushButton.clicked.connect(self.add)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton:hover {background: rgba(0, 214, 252, 0.17);}#pushButton{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-top-right-radius:10px;border-bottom-left-radius:10px;border-color:rgb(20, 182, 216);}")
        self.shadow1 = QtWidgets.QGraphicsDropShadowEffect(self.pushButton,blurRadius=20,xOffset=1,yOffset=1)
        self.pushButton.setGraphicsEffect(self.shadow1)

        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setShortcut("")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")

       

        self.popup = QtWidgets.QFrame(self.tab_2)
        #self.popup.setGeometry(QtCore.QRect(0,0,20,20))
        self.popup.setObjectName("popup")
        self.popup.setStyleSheet("#popup{background:transparent}")
        self.popup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup.setFrameShadow(QtWidgets.QFrame.Raised)

        self.popup_remove = QtWidgets.QPushButton(self.popup)
       # self.popup_remove.setGeometry(QtCore.QRect(0,0,0,0))
        self.popup_remove.setObjectName("popup_remove")
        self.popup_remove.setStyleSheet("#popup_remove{background:transparent}")

        self.popup_icon_frame = QtWidgets.QFrame(self.popup)
        self.popup_icon_frame.setObjectName("popup_icon_frame")
        self.popup_icon_frame.setStyleSheet("#popup_icon_frame{background:transparent}")
        self.popup_icon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup_icon_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.popup_text_frame = QtWidgets.QLabel(self.popup)
        self.popup_text_frame.setObjectName("popup_text_frame")
        self.popup_text_frame.setStyleSheet("#popup_text_frame{background:transparent}")
        


        self.popup_error_input = QtWidgets.QFrame(self.tab)
        self.popup_error_input.setObjectName("popup_error_input")
        self.popup_error_input.setStyleSheet("#popup_error_input{background:transparent}")
        

        self.popup_remove_input = QtWidgets.QPushButton(self.popup_error_input)
        #self.popup_remove_input.setGeometry(QtCore.QRect(0,0,0,0))
        self.popup_remove_input.setObjectName("popup_remove_input")
        self.popup_remove_input.setStyleSheet("#popup_remove_input{background:transparent}")

        self.popup_icon_frame_input = QtWidgets.QFrame(self.popup_error_input)
        self.popup_icon_frame_input.setObjectName("popup_icon_frame_input")
        self.popup_icon_frame_input.setStyleSheet("#popup_icon_frame_input{background:transparent}")
        self.popup_icon_frame_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup_icon_frame_input.setFrameShadow(QtWidgets.QFrame.Raised)

        self.popup_text_frame_input = QtWidgets.QLabel(self.popup_error_input)
        self.popup_text_frame_input.setObjectName("popup_text_frame_input")
        self.popup_text_frame_input.setStyleSheet("#popup_text_frame_input{background:transparent}")
        





        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def img_select_2(self):
        global path_2
        path_2 = None
        file_select = QtWidgets.QFileDialog()
        filters = "Image files (*.jpg *.png *jpeg)"
        path_2 = QtWidgets.QFileDialog.getOpenFileName(file_select,"Select an image","./",filters)


        if path_2 != None and path_2[0] != "":
         self.id_upload.setGeometry(QtCore.QRect(100, 120, 100, 100))
         self.id_upload.setStyleSheet(str("#id_upload{border-image:url('")+path_2[0]+str("');border-radius:5px}"))
    def add(self):

        input_error = False
        first_name = self.plainTextEdit_4.text()
        last_name = self.plainTextEdit_2.text()
        day = self.plainTextEdit_5.text()
        month = self.plainTextEdit_9.text()
        year = self.plainTextEdit_55.text()
        country = self.plainTextEdit_3.text()
        city = self.plainTextEdit_6.text()
        gender = self.plainTextEdit.text()
        job = self.plainTextEdit_10.text()
        work_location = self.plainTextEdit_11.text()
        num_1 = self.plainTextEdit_111.text()
        num_2 = self.plainTextEdit_222.text()
        email = self.plainTextEdit_333.text()
        addr = self.plainTextEdit_444.text()

        info_list = [first_name,last_name,day,month,year,country,city,gender,job,work_location,num_1,num_2,email,addr]
        for info in info_list:
            if str(info) != "" and path_2 != None and path_2[0] != "":

                 input_error = False


            else:
               input_error = True



        if input_error != False:

            self.popup_error_input_func()
        else:
            img = Image.open(path_2[0])
            input1 = frc.load_image_file(path_2[0])
            face = frc.face_locations(input1,model="hog")
            enc = frc.face_encodings(input1,face)
            jdict = {"name":str(first_name)+" "+str(last_name),"dob":str(day)+"."+str(month)+"."+str(year),
            "cc":str(country)+"/"+str(city),"gen":gender,"cit":num_1,"job":job,"phone_n1":num_1,"phone_n2":num_2,"job_loc":work_location,"addr":addr,"email":email}
            res = json.dumps(jdict)
            name = str(first_name)+" "+str(last_name)
            os.mkdir(f"./data/{name}")
            np.save(f"./data/{name}/enc.npy",enc)
            img.save(f"./data/{name}/{name}.jpg")
            with open(f"./data/{name}/data.json","w") as f:
             f.write(res)
             f.close()







    def popup_error_input_func(self):
        self.popup_error_input.show()

        blured_elements = [self.tab_11,self.plainTextEdit,self.plainTextEdit_2,self.plainTextEdit_3,self.plainTextEdit_4,self.plainTextEdit_5,
        self.plainTextEdit_6,self.plainTextEdit_9,self.plainTextEdit_10,self.plainTextEdit_11,self.plainTextEdit_55,self.plainTextEdit_111,
        self.plainTextEdit_222,self.plainTextEdit_333,self.plainTextEdit_444,self.pushButton,self.id_upload,self.gen,self.contact]
        for elements in blured_elements:
            elements.setEnabled(False)
            self.blur_effect_input = QtWidgets.QGraphicsBlurEffect(elements)
            self.blur_effect_input.setBlurRadius(7)
            elements.setGraphicsEffect(self.blur_effect_input)



        self.popup_error_input.setGeometry(QtCore.QRect(500,200,300,150))
        self.popup_error_input.setStyleSheet("#popup_error_input{background-color:rgba(110, 0, 0,0.3);border:1px solid red;border-top-right-radius:10px;border-bottom-left-radius:10px;}")

        self.popup_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_error_input,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_error_input.setGraphicsEffect(self.popup_shadow)


        self.popup_remove_input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.popup_remove_input.setMouseTracking(True)
        self.popup_remove_input.setFocusPolicy(QtCore.Qt.NoFocus)
        self.popup_remove_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.popup_remove_input.setAutoFillBackground(False)
        self.popup_remove_input.clicked.connect(self.popup_remove_func_input)
        self.popup_remove_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.popup_remove_input.setShortcut("")
        self.popup_remove_input.setCheckable(False)


        self.popup_icon_frame_input.setGeometry(QtCore.QRect(110,10,80,80))
        self.popup_icon_frame_input.setStyleSheet("#popup_icon_frame_input{background:transparent;border-image:url('./src/images/image(4).png')}")

        self.popup_icon_frame_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_icon_frame_input,blurRadius=5,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_icon_frame_input.setGraphicsEffect(self.popup_icon_frame_shadow)

        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
        font_popup = QtGui.QFontDatabase.applicationFontFamilies(id)[0]
        popup_font = QtGui.QFont(font_popup)
        popup_font.setPointSize(10)
        popup_font.setBold(False)
        popup_font.setItalic(False)
        popup_font.setWeight(30)

        self.popup_text_frame_input.setGeometry(QtCore.QRect(40,80,300,50))
        self.popup_text_frame_input.setStyleSheet("#popup_text_frame_input{background:transparent;color:rgb(255, 28, 51)}")
        self.popup_text_frame_input.setText("Informations uncompleted")
        self.popup_text_frame_input.setFont(popup_font)

        self.popup_text_frame_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_text_frame_input,blurRadius=5,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_text_frame.setGraphicsEffect(self.popup_text_frame_shadow)

        self.popup_remove_input.setGeometry(QtCore.QRect(282,8,10,10))
        self.popup_remove_input.setStyleSheet("#popup_remove_input{background:transparent;border-image:url('./src/images/image(6).png')}")

        self.popup_remove_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_remove_input,blurRadius=5,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_remove_input.setGraphicsEffect(self.popup_remove_shadow)


    def popup_remove_func_input(self):

        self.popup_error_input.hide()


        blured_elements = [self.tab_11,self.plainTextEdit,self.plainTextEdit_2,self.plainTextEdit_3,self.plainTextEdit_4,self.plainTextEdit_5,self.plainTextEdit_6,
        self.plainTextEdit_9,self.plainTextEdit_10,self.plainTextEdit_11,self.plainTextEdit_55,self.plainTextEdit_111,
        self.plainTextEdit_222,self.plainTextEdit_333,self.plainTextEdit_444,self.pushButton,self.id_upload,self.gen,self.contact]
        for elements in blured_elements:
            elements.setEnabled(True)
            self.blur_effect_input.setEnabled(False)
            elements.setGraphicsEffect(self.blur_effect_input)


        self.pushButton.setEnabled(True)
        

    def popup_remove_func(self):

        self.popup.hide()

        blured_elements = [self.upload2,self.frame,self.frame2,self.upload,self.remove,self.lab,self.lab2,self.label_err,self.tab_22]
        for elements in blured_elements:
            self.blur_effect.setEnabled(False)
            elements.setGraphicsEffect(self.blur_effect)


        self.shadow1 = QtWidgets.QGraphicsDropShadowEffect(self.upload2,blurRadius=20,xOffset=1,yOffset=1)
        self.upload2.setGraphicsEffect(self.shadow1)

        self.shadow1_ = QtWidgets.QGraphicsDropShadowEffect(self.remove,blurRadius=20,xOffset=1,yOffset=1)
        self.remove.setGraphicsEffect(self.shadow1_)

        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect(self.upload,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.upload.setGraphicsEffect(self.shadow2)

        self.shadow_frame = QtWidgets.QGraphicsDropShadowEffect(self.frame,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 255, 98))
        self.frame.setGraphicsEffect(self.shadow_frame)

        self.shadow_frame2 = QtWidgets.QGraphicsDropShadowEffect(self.frame2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 221, 255))
        self.frame2.setGraphicsEffect(self.shadow_frame2)

        self.upload2.setEnabled(True)
        self.remove.setEnabled(True)
        self.upload.setEnabled(True)

    def load(self,value):
        
        self.frame.setGeometry(QtCore.QRect(1030, 50, 231, 231))
        self.shadow_frame = QtWidgets.QGraphicsDropShadowEffect(self.frame,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 255, 98))
        self.frame.setGraphicsEffect(self.shadow_frame)
        self.frame.setStyleSheet(u"#frame{background:transparent}")
        
        self.frame_2.setStyleSheet(u"#frame_2{background:transparent}")
        
        
        self.label.setStyleSheet("#label{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"font: 25pt \"Roboto Slab\";\n"
"color: rgb(0, 255, 8);}")
        self.label.setGeometry(QtCore.QRect(75, 80, 100, 50))
        
        self.shadow_label = QtWidgets.QGraphicsDropShadowEffect(self.label,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 255, 8))
        self.label.setGraphicsEffect(self.shadow_label)
        self.value = value

        self.styleSheet = "#frame{background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:{p1} rgb(0, 255, 98), stop:{p2} rgba(16, 145, 196, 20));border-radius:115;}"

        self.prog = (self.value)/100
        self.p1 = str(self.prog-0.0001)
        self.p2 = str(self.prog)

        self.newStylesheet = self.styleSheet.replace("{p1}", self.p1).replace("{p2}", self.p2)
        self.label_noimg2.setText("")
        self.label_noimg.setText("")
        self.frame_2.setGeometry(QtCore.QRect(5, 6, 221, 221))
        self.frame_2.setStyleSheet(u"#frame_2{border-radius:109px;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.994318, stop:1 rgba(23, 65, 66, 200));}")
        self.frame.setStyleSheet(self.newStylesheet)
        self.label.setText(f"{value} %")
    def load_2(self,value1):
        self.value1 = value1

        self.styleSheet1 = "#frame2{background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:{p11} rgb(0, 221, 255), stop:{p22} rgba(16, 145, 196, 20));border-radius:115;}"

        self.prog1 = (self.value1)/100

        self.p11 = str(self.prog1-0.0001)
        self.p22 = str(self.prog1)

        self.newStylesheet1 = self.styleSheet1.replace("{p11}", self.p11).replace("{p22}", self.p22)
        self.frame2.setStyleSheet(self.newStylesheet1)
        #self.label_noinfo.setText("")
        self.frame_22.setStyleSheet(u"#frame_22{border-radius:109px;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.994318, stop:1 rgba(23, 65, 66, 200));}")
        self.frame_22.setGeometry(QtCore.QRect(5, 6, 221, 221))
        self.label2.setText(f"{value1} %")
        if self.value1 == 100:
            time.sleep(1)
            self.value1 = 0
    def img_select(self):
        global path
        file_select = QtWidgets.QFileDialog()
        filters = "Image files (*.jpg *.png *jpeg)"
        path = None
        path = QtWidgets.QFileDialog.getOpenFileName(file_select,"Select an image","./",filters)
        #self.reload
        if path != None and path[0] != "":
         img = QtGui.QImage(path[0])
         img_w = img.width()
         img_h = img.height()
         w = 230
         if img_w > 550:
            img_w = 700
            w = 100
         if img_h > 440:
            img_h = 400
         self.upload.setGeometry(QtCore.QRect(w, 50, img_w, img_h))
         self.upload.setStyleSheet(str("#upload{border-image:url(")+path[0]+str(");}"))
        else:
            print("Please select an image")


    def prc(self):
        if path != None and path[0] != "":
        
            self.sig = External()
            self.sig.signal.connect(self.load)
            self.sig1 = External()
            self.sig1.signal_.connect(self.load_2)
            self.sig.start()
            if self.frame.visibleRegion().isEmpty() and self.frame_2.visibleRegion().isEmpty():
                    self.frame.show()
                    self.frame_2.show()






            Thread(target = self.process).start()
        else:

           self.popup_error()


    def popup_error(self):
        self.popup.show()

        blured_elements = [self.upload2,self.frame,self.frame2,self.upload,self.remove,self.lab,self.lab2,self.label_err,self.tab_22]
        for elements in blured_elements:
            self.blur_effect = QtWidgets.QGraphicsBlurEffect(elements)
            self.blur_effect.setBlurRadius(7)
            elements.setGraphicsEffect(self.blur_effect)

        self.upload2.setEnabled(False)
        self.remove.setEnabled(False)
        self.upload.setEnabled(False)

        self.popup.setGeometry(QtCore.QRect(500,200,300,150))
        self.popup.setStyleSheet("#popup{background-color:rgba(110, 0, 0,0.3);border:1px solid red;border-top-right-radius:10px;border-bottom-left-radius:10px;}")

        self.popup_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup.setGraphicsEffect(self.popup_shadow)


        self.popup_remove.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.popup_remove.setMouseTracking(True)
        self.popup_remove.setFocusPolicy(QtCore.Qt.NoFocus)
        self.popup_remove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.popup_remove.setAutoFillBackground(False)
        self.popup_remove.clicked.connect(self.popup_remove_func)
        self.popup_remove.setInputMethodHints(QtCore.Qt.ImhNone)
        self.popup_remove.setShortcut("")
        self.popup_remove.setCheckable(False)


        self.popup_icon_frame.setGeometry(QtCore.QRect(110,10,80,80))
        self.popup_icon_frame.setStyleSheet("#popup_icon_frame{background:transparent;border-image:url('./src/images/image(4).png')}")

        self.popup_icon_frame_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_icon_frame,blurRadius=5,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_icon_frame.setGraphicsEffect(self.popup_icon_frame_shadow)

        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
        font_popup = QtGui.QFontDatabase.applicationFontFamilies(id)[0]
        popup_font = QtGui.QFont(font_popup)
        popup_font.setPointSize(10)
        popup_font.setBold(False)
        popup_font.setItalic(False)
        popup_font.setWeight(30)

        self.popup_text_frame.setGeometry(QtCore.QRect(47,80,300,50))
        self.popup_text_frame.setStyleSheet("#popup_text_frame{background:transparent;color:rgb(255, 28, 51)}")
        self.popup_text_frame.setText("Please select an image")
        self.popup_text_frame.setFont(popup_font)

        self.popup_text_frame_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_text_frame,blurRadius=5,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_text_frame.setGraphicsEffect(self.popup_text_frame_shadow)

        self.popup_remove.setGeometry(QtCore.QRect(282,8,10,10))
        self.popup_remove.setStyleSheet("#popup_remove{background:transparent;border-image:url('./src/images/image(6).png')}")

        self.popup_remove_shadow = QtWidgets.QGraphicsDropShadowEffect(self.popup_remove,blurRadius=5,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.popup_remove.setGraphicsEffect(self.popup_remove_shadow)


    def popup_remove_func(self):

        self.popup.hide()

        blured_elements = [self.upload2,self.frame,self.frame2,self.upload,self.remove,self.lab,self.lab2,self.label_err,self.tab_22]
        for elements in blured_elements:
            self.blur_effect.setEnabled(False)
            elements.setGraphicsEffect(self.blur_effect)


        self.shadow1 = QtWidgets.QGraphicsDropShadowEffect(self.upload2,blurRadius=20,xOffset=1,yOffset=1)
        self.upload2.setGraphicsEffect(self.shadow1)

        self.shadow1_ = QtWidgets.QGraphicsDropShadowEffect(self.remove,blurRadius=20,xOffset=1,yOffset=1)
        self.remove.setGraphicsEffect(self.shadow1_)

        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect(self.upload,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.upload.setGraphicsEffect(self.shadow2)

        self.shadow_frame = QtWidgets.QGraphicsDropShadowEffect(self.frame,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 255, 98))
        self.frame.setGraphicsEffect(self.shadow_frame)

        self.shadow_frame2 = QtWidgets.QGraphicsDropShadowEffect(self.frame2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 221, 255))
        self.frame2.setGraphicsEffect(self.shadow_frame2)

        self.upload2.setEnabled(True)
        self.remove.setEnabled(True)
        self.upload.setEnabled(True)



    def process(self):
           
            self.sig1.start()
            
                    
            id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
            fontstr = QtGui.QFontDatabase.applicationFontFamilies(id)[0]

            font = QtGui.QFont(fontstr)
            font.setPointSize(14)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            style = '''#upload{background-size:img_w img_h;background-image:url('./src/images/id.jpeg');}'''
            self.label_err_face.setText("")
            self.alert_err.setStyleSheet("#alert_err{background:transparent}")
            start.load(path[0])
            self.label_err.setText("")

            self.frame2.setGeometry(QtCore.QRect(1030, 370, 231, 231))
            self.frame2.setStyleSheet(u"#frame2{background:transparent}")
            self.shadow_frame2 = QtWidgets.QGraphicsDropShadowEffect(self.frame2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 221, 255))
            self.frame2.setGraphicsEffect(self.shadow_frame2)


            self.start_error = start.start(path[0])
            if self.frame2.visibleRegion().isEmpty() and self.frame_22.visibleRegion().isEmpty():
                    
                    self.frame2.show()
                    self.frame_22.show()
            if self.start_error == False:
                
                
                    
                self.shadow_lab_red = QtWidgets.QGraphicsDropShadowEffect()
                self.shadow_lab_red.setEnabled(False)
                self.lab.setGraphicsEffect(self.shadow_lab_red)
                self.lab.setStyleSheet("#card{border-image:url('./src/images/id2_.png');}")
                
                start.search(path[0])
                err_id = start.id_card()
                time.sleep(0.5)
                if err_id == False:
                        if not self.frame.visibleRegion().isEmpty() and not self.frame_22.visibleRegion().isEmpty() and not self.frame2.visibleRegion().isEmpty() and not self.frame_2.visibleRegion().isEmpty():
                          self.frame2.hide()
                          self.frame_22.hide()
                          self.frame.hide()
                          self.frame_2.hide()
                        self.label_err_face.setText("")
                        self.popup_icon_err.setStyleSheet("#popup_icon_err{background:transparent;}")
                        self.frame.setStyleSheet(u"#frame{background:transparent}")
                        #self.frame2.setStyleSheet(u"#frame2{background:transparent}")
                        self.frame_22.setStyleSheet(u"#frame_22{background:transparent}")
                        self.frame_2.setStyleSheet(u"#frame_2{background:transparent}")
                        self.alert_err.setStyleSheet("#alert_err{background:transparent}")
                        self.label.setText("")
                        self.label2.setText("")


                        self.alert_err.setGeometry(QtCore.QRect(1070, 370, 150, 150))
                        #self.label_face.setGeometry(QtCore.QRect(0,0,280,250))
                        self.label_err.setGeometry(QtCore.QRect(0,0,400,50))
                        self.label_err.setText("FACE DOESN'T EXIST")
                        self.label_noinfo.setText("")
                        self.lab2.setStyleSheet("#card2{background-color:rgba(110, 0, 0,0.2);border:1px solid red;border-top-right-radius:10px;border-bottom-left-radius:10px;}")
                        self.lab2_shadow = QtWidgets.QGraphicsDropShadowEffect(self.lab2,blurRadius=60,xOffset=1,yOffset=1,color=QtGui.QColor(222, 18, 21))
                        self.lab2.setGraphicsEffect(self.lab2_shadow)

                        self.alert_err.setStyleSheet("#alert_err{background:transparent;border-image:url('./src/images/image(4).png');}")
                        self.label_err.setFont(font)
                        self.shadow_red = QtWidgets.QGraphicsDropShadowEffect(self.alert_err,blurRadius=30,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
                        self.alert_err.setGraphicsEffect(self.shadow_red)


                else:

                     
                     self.shadow_frame = QtWidgets.QGraphicsDropShadowEffect(self.frame,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 255, 98))
                     self.frame.setGraphicsEffect(self.shadow_frame)

                     self.label_noinfo.setText("")
                     self.label_err_face.setText("")
                     
                     self.popup_icon_err.setStyleSheet("#popup_icon_err{background:transparent;}")
                     self.frame.setStyleSheet(u"#frame{background:transparent}")
                     self.frame2.setStyleSheet(u"#frame2{background:transparent}")
                     self.frame_22.setStyleSheet(u"#frame_22{background:transparent}")
                     self.frame_2.setStyleSheet(u"#frame_2{background:transparent}")
                     
                     self.label.setText("")
                     self.label2.setText("")
                     if not self.frame.visibleRegion().isEmpty() and not self.frame_2.visibleRegion().isEmpty():
                       self.frame.hide()
                       self.frame2.hide()
                       self.frame_22.hide()
                       self.frame_2.hide()
                     self.lab2.setStyleSheet("#card2{background:transparent;border-image:url('./src/images/id2.png');}")
                     self.lab2_shadow_blue = QtWidgets.QGraphicsDropShadowEffect(self.lab2,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(0, 70, 99))
                     self.lab2.setGraphicsEffect(self.lab2_shadow_blue)
            elif self.start_error == None:
                self.no_faces_error_func()
            else:
                self.many_faces_error_func()




    def no_faces_error_func(self):


        self.label_noinfo.setText("NO INFORMATIONS")
        self.popup_icon_err.setGeometry(QtCore.QRect(170,30,150,150))
        self.popup_icon_err.setStyleSheet("#popup_icon_err{background:transparent;border-image:url('./src/images/image(4).png');}")
        self.label_err_face.setGeometry(QtCore.QRect(135,70,350,200))
        self.label_err_face.setText("NO FACE DETECTED")


        if not self.frame.visibleRegion().isEmpty() and not self.frame_2.visibleRegion().isEmpty():
            self.frame.hide()
            self.frame2.hide()
            self.frame_22.hide()
            self.frame_2.hide()


        self.shadow_lab_red = QtWidgets.QGraphicsDropShadowEffect(self.lab,blurRadius=30,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.lab.setGraphicsEffect(self.shadow_lab_red)

        self.lab.setStyleSheet("#card{background-color:rgba(110, 0, 0,0.2);border:1px solid red;border-top-right-radius:10px;border-bottom-left-radius:10px;}")
        self.lab2.setStyleSheet("#card2{background-color:rgba(0, 124, 133,0.2);border:1px solid rgb(0, 179, 255);border-top-right-radius:10px;border-bottom-left-radius:10px;}")



        self.lab2_shadow_blue = QtWidgets.QGraphicsDropShadowEffect(self.lab2,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(0, 70, 99))
        self.lab2.setGraphicsEffect(self.lab2_shadow_blue)

    def many_faces_error_func(self):


        self.label_noinfo.setText("NO INFORMATIONS")
        self.popup_icon_err.setGeometry(QtCore.QRect(170,30,150,150))
        self.label_err_face.setGeometry(QtCore.QRect(70,70,380,200))
        self.popup_icon_err.setStyleSheet("#popup_icon_err{background:transparent;border-image:url('./src/images/image(4).png');}")
        self.label_err_face.setText("TOO MANY FACES DETECTED")


        if not self.frame.visibleRegion().isEmpty() and not self.frame_2.visibleRegion().isEmpty():
            self.frame.hide()
            self.frame2.hide()
            self.frame_22.hide()
            self.frame_2.hide()


        self.shadow_lab_red = QtWidgets.QGraphicsDropShadowEffect(self.lab,blurRadius=30,xOffset=0,yOffset=0,color=QtGui.QColor(222, 18, 21))
        self.lab.setGraphicsEffect(self.shadow_lab_red)

        self.lab.setStyleSheet("#card{background-color:rgba(110, 0, 0,0.2);border:1px solid red;border-top-right-radius:10px;border-bottom-left-radius:10px;}")
        self.lab2.setStyleSheet("#card2{background-color:rgba(0, 124, 133,0.2);border:1px solid rgb(0, 179, 255);border-top-right-radius:10px;border-bottom-left-radius:10px;}")



        self.lab2_shadow_blue = QtWidgets.QGraphicsDropShadowEffect(self.lab2,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(0, 70, 99))
        self.lab2.setGraphicsEffect(self.lab2_shadow_blue)

    def reload(self):
        global path
        path = None
        self.label_err_face.setText("")
        self.popup_icon_err.setStyleSheet("#popup_icon_err{background:transparent;}")

        self.shadow_lab_red = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_lab_red.setEnabled(False)
        self.lab.setGraphicsEffect(self.shadow_lab_red)

        self.lab.setStyleSheet("#card{background-color:rgba(0, 133, 57,0.2);border:1px solid green;border-top-right-radius:10px;border-bottom-left-radius:10px;}")
        self.lab2.setStyleSheet("#card2{background-color:rgba(0, 124, 133,0.2);border:1px solid rgb(0, 179, 255);border-top-right-radius:10px;border-bottom-left-radius:10px;}")

        self.frame_22.setStyleSheet(u"#frame_22{background:transparent}")
        self.upload.setGeometry(QtCore.QRect(270, 20, 355, 350))
        self.frame2.setGeometry(QtCore.QRect(1030, 370, 231, 231))
        self.upload.setStyleSheet("#upload{background:transparent;border-image:url('./src/images/face1.png');}")
        self.frame.setStyleSheet(u"#frame{background:transparent}")
        self.frame2.setStyleSheet(u"#frame2{background:transparent}")
        self.alert_err.setStyleSheet("#alert_err{background:transparent}")
        self.shadow_frame2 = QtWidgets.QGraphicsDropShadowEffect(self.frame2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 221, 255))
        self.frame2.setGraphicsEffect(self.shadow_frame2)
        self.lab2_shadow_blue = QtWidgets.QGraphicsDropShadowEffect(self.lab2,blurRadius=60,xOffset=0,yOffset=0,color=QtGui.QColor(0, 70, 99))
        self.lab2.setGraphicsEffect(self.lab2_shadow_blue)
        self.frame_2.setStyleSheet(u"#frame_2{background:transparent}")
        self.frame_err.setStyleSheet("#frame_err{background:transparent}")
        self.label.setText("")
        self.label2.setText("")
        self.label_err.setText("")
        self.label_noimg.setText("NO IMAGE")
        self.label_noimg2.setText("AVAILABLE")
        self.label_noinfo.setText("NO INFORMATIONS")




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Polaris", "Polaris"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Search for faces"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add faces"))
