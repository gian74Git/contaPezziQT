# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contapezzi.ui'
#
# Created: Tue Mar 15 22:40:37 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_contaPezzi(object):
    def setupUi(self, contaPezzi):
        contaPezzi.setObjectName("contaPezzi")
        contaPezzi.resize(1534, 885)
        self.centralwidget = QtWidgets.QWidget(contaPezzi)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.verticalFrame.setObjectName("verticalFrame")
        self.vlTitolo = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.vlTitolo.setObjectName("vlTitolo")
        self.lbCliente = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lbCliente.setFont(font)
        self.lbCliente.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCliente.setObjectName("lbCliente")
        self.vlTitolo.addWidget(self.lbCliente)
        self.lbData = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbData.setFont(font)
        self.lbData.setObjectName("lbData")
        self.vlTitolo.addWidget(self.lbData)
        self.verticalLayout.addWidget(self.verticalFrame)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setEnabled(True)
        self.widget_5.setBaseSize(QtCore.QSize(0, 0))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbPrevisto = QtWidgets.QLabel(self.widget_5)
        self.lbPrevisto.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lbPrevisto.setFont(font)
        self.lbPrevisto.setTextFormat(QtCore.Qt.AutoText)
        self.lbPrevisto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPrevisto.setObjectName("lbPrevisto")
        self.verticalLayout_3.addWidget(self.lbPrevisto)
        self.lbPzPrevisti = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(96)
        font.setBold(True)
        font.setWeight(75)
        self.lbPzPrevisti.setFont(font)
        self.lbPzPrevisti.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPzPrevisti.setObjectName("lbPzPrevisti")
        self.verticalLayout_3.addWidget(self.lbPzPrevisti)
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbFatto = QtWidgets.QLabel(self.widget_6)
        self.lbFatto.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lbFatto.setFont(font)
        self.lbFatto.setTextFormat(QtCore.Qt.AutoText)
        self.lbFatto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFatto.setObjectName("lbFatto")
        self.verticalLayout_4.addWidget(self.lbFatto)
        self.lbPzFatti = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(96)
        font.setBold(True)
        font.setWeight(75)
        self.lbPzFatti.setFont(font)
        self.lbPzFatti.setAutoFillBackground(False)
        self.lbPzFatti.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.505, y1:1, x2:0.505, y2:0, stop:0 rgba(0, 174, 68, 255), stop:1 rgba(0, 255, 67, 255));")
        self.lbPzFatti.setFrameShape(QtWidgets.QFrame.Box)
        self.lbPzFatti.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbPzFatti.setLineWidth(0)
        self.lbPzFatti.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPzFatti.setObjectName("lbPzFatti")
        self.verticalLayout_4.addWidget(self.lbPzFatti)
        self.lbGiornaliero = QtWidgets.QLabel(self.widget_6)
        self.lbGiornaliero.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lbGiornaliero.setFont(font)
        self.lbGiornaliero.setTextFormat(QtCore.Qt.AutoText)
        self.lbGiornaliero.setAlignment(QtCore.Qt.AlignCenter)
        self.lbGiornaliero.setObjectName("lbGiornaliero")
        self.verticalLayout_4.addWidget(self.lbGiornaliero)
        self.lbPzGiorn = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(96)
        font.setBold(True)
        font.setWeight(75)
        self.lbPzGiorn.setFont(font)
        self.lbPzGiorn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPzGiorn.setObjectName("lbPzGiorn")
        self.verticalLayout_4.addWidget(self.lbPzGiorn)
        self.horizontalLayout.addWidget(self.widget_6)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.qfOre = QtWidgets.QFrame(self.widget_4)
        self.qfOre.setObjectName("qfOre")
        self.vlOre = QtWidgets.QVBoxLayout(self.qfOre)
        self.vlOre.setSpacing(3)
        self.vlOre.setObjectName("vlOre")
        self.lbOra = QtWidgets.QLabel(self.qfOre)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbOra.setFont(font)
        self.lbOra.setObjectName("lbOra")
        self.vlOre.addWidget(self.lbOra)
        self.horizontalLayout_3.addWidget(self.qfOre)
        self.qfPrev = QtWidgets.QFrame(self.widget_4)
        self.qfPrev.setObjectName("qfPrev")
        self.vlPrev = QtWidgets.QVBoxLayout(self.qfPrev)
        self.vlPrev.setObjectName("vlPrev")
        self.lbPrevistoOra = QtWidgets.QLabel(self.qfPrev)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbPrevistoOra.setFont(font)
        self.lbPrevistoOra.setObjectName("lbPrevistoOra")
        self.vlPrev.addWidget(self.lbPrevistoOra)
        self.horizontalLayout_3.addWidget(self.qfPrev)
        self.qfFatti = QtWidgets.QFrame(self.widget_4)
        self.qfFatti.setObjectName("qfFatti")
        self.vlFatti = QtWidgets.QVBoxLayout(self.qfFatti)
        self.vlFatti.setObjectName("vlFatti")
        self.lbFattoOra = QtWidgets.QLabel(self.qfFatti)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbFattoOra.setFont(font)
        self.lbFattoOra.setObjectName("lbFattoOra")
        self.vlFatti.addWidget(self.lbFattoOra)
        self.horizontalLayout_3.addWidget(self.qfFatti)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbError = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbError.setFont(font)
        self.lbError.setAutoFillBackground(False)
        self.lbError.setStyleSheet("color: rgb(255, 9, 9);")
        self.lbError.setText("")
        self.lbError.setAlignment(QtCore.Qt.AlignCenter)
        self.lbError.setObjectName("lbError")
        self.horizontalLayout_4.addWidget(self.lbError)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2.addWidget(self.frame)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbNumPezzi = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbNumPezzi.sizePolicy().hasHeightForWidth())
        self.lbNumPezzi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbNumPezzi.setFont(font)
        self.lbNumPezzi.setObjectName("lbNumPezzi")
        self.gridLayout_2.addWidget(self.lbNumPezzi, 2, 0, 1, 1)
        self.leNumPezzi = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leNumPezzi.sizePolicy().hasHeightForWidth())
        self.leNumPezzi.setSizePolicy(sizePolicy)
        self.leNumPezzi.setMaximumSize(QtCore.QSize(200, 16777215))
        self.leNumPezzi.setObjectName("leNumPezzi")
        self.gridLayout_2.addWidget(self.leNumPezzi, 2, 2, 1, 1)
        self.btnTest = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTest.sizePolicy().hasHeightForWidth())
        self.btnTest.setSizePolicy(sizePolicy)
        self.btnTest.setMinimumSize(QtCore.QSize(0, 35))
        self.btnTest.setObjectName("btnTest")
        self.gridLayout_2.addWidget(self.btnTest, 2, 4, 1, 1)
        self.btnChiudi = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChiudi.sizePolicy().hasHeightForWidth())
        self.btnChiudi.setSizePolicy(sizePolicy)
        self.btnChiudi.setMinimumSize(QtCore.QSize(0, 35))
        self.btnChiudi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnChiudi.setObjectName("btnChiudi")
        self.gridLayout_2.addWidget(self.btnChiudi, 2, 5, 1, 1)
        self.btnImposta = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImposta.sizePolicy().hasHeightForWidth())
        self.btnImposta.setSizePolicy(sizePolicy)
        self.btnImposta.setMinimumSize(QtCore.QSize(0, 35))
        self.btnImposta.setBaseSize(QtCore.QSize(0, 0))
        self.btnImposta.setObjectName("btnImposta")
        self.gridLayout_2.addWidget(self.btnImposta, 2, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.frame_3)
        contaPezzi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(contaPezzi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1534, 25))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        contaPezzi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(contaPezzi)
        self.statusbar.setObjectName("statusbar")
        contaPezzi.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(contaPezzi)
        self.toolBar.setObjectName("toolBar")
        contaPezzi.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEsci = QtWidgets.QAction(contaPezzi)
        self.actionEsci.setObjectName("actionEsci")
        self.menuFIle.addAction(self.actionEsci)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(contaPezzi)
        QtCore.QMetaObject.connectSlotsByName(contaPezzi)

    def retranslateUi(self, contaPezzi):
        _translate = QtCore.QCoreApplication.translate
        contaPezzi.setWindowTitle(_translate("contaPezzi", "Piece Counter"))
        self.lbCliente.setText(_translate("contaPezzi", "- Cliente -"))
        self.lbData.setText(_translate("contaPezzi", "- Data di sitema -"))
        self.lbPrevisto.setText(_translate("contaPezzi", "Previsto"))
        self.lbPzPrevisti.setText(_translate("contaPezzi", "0"))
        self.lbFatto.setText(_translate("contaPezzi", "Fatto"))
        self.lbPzFatti.setText(_translate("contaPezzi", "0"))
        self.lbGiornaliero.setText(_translate("contaPezzi", "Giorn"))
        self.lbPzGiorn.setText(_translate("contaPezzi", "0"))
        self.lbOra.setText(_translate("contaPezzi", "Ora"))
        self.lbPrevistoOra.setText(_translate("contaPezzi", "Previsto"))
        self.lbFattoOra.setText(_translate("contaPezzi", "Fatto"))
        self.lbNumPezzi.setText(_translate("contaPezzi", "Num. pezzi partenza:"))
        self.btnTest.setText(_translate("contaPezzi", "Test"))
        self.btnChiudi.setText(_translate("contaPezzi", "Chiudi"))
        self.btnImposta.setText(_translate("contaPezzi", "Imposta"))
        self.menuFIle.setTitle(_translate("contaPezzi", "FIle"))
        self.toolBar.setWindowTitle(_translate("contaPezzi", "toolBar"))
        self.actionEsci.setText(_translate("contaPezzi", "Esci"))

