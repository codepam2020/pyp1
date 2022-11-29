# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_drugsearch.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from drug_data import DrugData

drugData = DrugData()
searchDrugList = []
detailedDrugName = 'none'




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabDrugRegister = QtWidgets.QWidget()
        self.tabDrugRegister.setObjectName("tabDrugRegister")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabDrugRegister)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.groupBox = QtWidgets.QGroupBox(self.tabDrugRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, 40, 20, 40)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.TextEditDrugSearch = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextEditDrugSearch.sizePolicy().hasHeightForWidth())
        self.TextEditDrugSearch.setSizePolicy(sizePolicy)
        self.TextEditDrugSearch.setMinimumSize(QtCore.QSize(200, 30))
        self.TextEditDrugSearch.setMaximumSize(QtCore.QSize(180, 30))
        self.TextEditDrugSearch.setObjectName("TextEditDrugSearch")
        self.verticalLayout_2.addWidget(self.TextEditDrugSearch, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.buttonSearchDrug = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearchDrug.sizePolicy().hasHeightForWidth())
        self.buttonSearchDrug.setSizePolicy(sizePolicy)
        self.buttonSearchDrug.setMinimumSize(QtCore.QSize(150, 30))
        self.buttonSearchDrug.setObjectName("buttonSearchDrug")
        self.verticalLayout_2.addWidget(self.buttonSearchDrug, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout_15.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabDrugRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(15, 40, 15, 40)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ListWidgetDrugList = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListWidgetDrugList.sizePolicy().hasHeightForWidth())
        self.ListWidgetDrugList.setSizePolicy(sizePolicy)
        self.ListWidgetDrugList.setMinimumSize(QtCore.QSize(210, 400))
        self.ListWidgetDrugList.setObjectName("ListWidgetDrugList")
        self.verticalLayout_4.addWidget(self.ListWidgetDrugList)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.buttonSelectedDrugRegister = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSelectedDrugRegister.sizePolicy().hasHeightForWidth())
        self.buttonSelectedDrugRegister.setSizePolicy(sizePolicy)
        self.buttonSelectedDrugRegister.setMinimumSize(QtCore.QSize(200, 30))
        self.buttonSelectedDrugRegister.setObjectName("buttonSelectedDrugRegister")
        self.verticalLayout_4.addWidget(self.buttonSelectedDrugRegister, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout_14.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_14, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabDrugRegister, "")
        self.tabDrugList = QtWidgets.QWidget()
        self.tabDrugList.setObjectName("tabDrugList")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tabDrugList)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabDrugList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.listWidgetDangerDrugInfo = QtWidgets.QListWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetDangerDrugInfo.sizePolicy().hasHeightForWidth())
        self.listWidgetDangerDrugInfo.setSizePolicy(sizePolicy)
        self.listWidgetDangerDrugInfo.setMinimumSize(QtCore.QSize(200, 150))
        self.listWidgetDangerDrugInfo.setObjectName("listWidgetDangerDrugInfo")
        self.verticalLayout_8.addWidget(self.listWidgetDangerDrugInfo)
        self.gridLayout_7.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tabDrugList)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.textDrugDetailedInfo = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textDrugDetailedInfo.setObjectName("textDrugDetailedInfo")
        self.gridLayout_11.addWidget(self.textDrugDetailedInfo, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabDrugList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.listWidgetDbDrugList = QtWidgets.QListWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetDbDrugList.sizePolicy().hasHeightForWidth())
        self.listWidgetDbDrugList.setSizePolicy(sizePolicy)
        self.listWidgetDbDrugList.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidgetDbDrugList.setMaximumSize(QtCore.QSize(220, 16777215))
        self.listWidgetDbDrugList.setObjectName("listWidgetDbDrugList")
        self.verticalLayout_9.addWidget(self.listWidgetDbDrugList, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem6)
        self.buttonSelectedDrugDelete = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSelectedDrugDelete.sizePolicy().hasHeightForWidth())
        self.buttonSelectedDrugDelete.setSizePolicy(sizePolicy)
        self.buttonSelectedDrugDelete.setMinimumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonSelectedDrugDelete.setFont(font)
        self.buttonSelectedDrugDelete.setObjectName("buttonSelectedDrugDelete")
        self.verticalLayout_9.addWidget(self.buttonSelectedDrugDelete, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem7)
        self.buttonRenew = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRenew.sizePolicy().hasHeightForWidth())
        self.buttonRenew.setSizePolicy(sizePolicy)
        self.buttonRenew.setMinimumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonRenew.setFont(font)
        self.buttonRenew.setObjectName("buttonRenew")
        self.verticalLayout_9.addWidget(self.buttonRenew, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem8, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabDrugList, "")
        self.tabSetting = QtWidgets.QWidget()
        self.tabSetting.setObjectName("tabSetting")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabSetting)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tabSetting)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 421, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 291, 16))
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_10, 2, 1, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tabSetting)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.groupBox_7)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.radioElderTrue = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioElderTrue.sizePolicy().hasHeightForWidth())
        self.radioElderTrue.setSizePolicy(sizePolicy)
        self.radioElderTrue.setMinimumSize(QtCore.QSize(100, 0))
        self.radioElderTrue.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioElderTrue.setObjectName("radioElderTrue")
        self.horizontalLayout_5.addWidget(self.radioElderTrue)
        self.radioElderFalse = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioElderFalse.sizePolicy().hasHeightForWidth())
        self.radioElderFalse.setSizePolicy(sizePolicy)
        self.radioElderFalse.setMinimumSize(QtCore.QSize(100, 0))
        self.radioElderFalse.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioElderFalse.setObjectName("radioElderFalse")
        self.horizontalLayout_5.addWidget(self.radioElderFalse)
        self.horizontalLayout.addWidget(self.widget)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.groupBox_7)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.radioPragnantTrue = QtWidgets.QRadioButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioPragnantTrue.sizePolicy().hasHeightForWidth())
        self.radioPragnantTrue.setSizePolicy(sizePolicy)
        self.radioPragnantTrue.setMinimumSize(QtCore.QSize(100, 0))
        self.radioPragnantTrue.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioPragnantTrue.setObjectName("radioPragnantTrue")
        self.horizontalLayout_8.addWidget(self.radioPragnantTrue)
        self.radioPragnantFalse = QtWidgets.QRadioButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioPragnantFalse.sizePolicy().hasHeightForWidth())
        self.radioPragnantFalse.setSizePolicy(sizePolicy)
        self.radioPragnantFalse.setMinimumSize(QtCore.QSize(100, 0))
        self.radioPragnantFalse.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioPragnantFalse.setObjectName("radioPragnantFalse")
        self.horizontalLayout_8.addWidget(self.radioPragnantFalse)
        self.horizontalLayout_4.addWidget(self.widget_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.groupBox_7)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.radioMaxTrue = QtWidgets.QRadioButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioMaxTrue.sizePolicy().hasHeightForWidth())
        self.radioMaxTrue.setSizePolicy(sizePolicy)
        self.radioMaxTrue.setMinimumSize(QtCore.QSize(100, 0))
        self.radioMaxTrue.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioMaxTrue.setObjectName("radioMaxTrue")
        self.horizontalLayout_10.addWidget(self.radioMaxTrue)
        self.radioMaxFalse = QtWidgets.QRadioButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioMaxFalse.sizePolicy().hasHeightForWidth())
        self.radioMaxFalse.setSizePolicy(sizePolicy)
        self.radioMaxFalse.setMinimumSize(QtCore.QSize(100, 0))
        self.radioMaxFalse.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioMaxFalse.setObjectName("radioMaxFalse")
        self.horizontalLayout_10.addWidget(self.radioMaxFalse)
        self.horizontalLayout_3.addWidget(self.widget_5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(200, 0))
        self.label_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.radioDayTrue = QtWidgets.QRadioButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioDayTrue.sizePolicy().hasHeightForWidth())
        self.radioDayTrue.setSizePolicy(sizePolicy)
        self.radioDayTrue.setMinimumSize(QtCore.QSize(100, 0))
        self.radioDayTrue.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioDayTrue.setObjectName("radioDayTrue")
        self.horizontalLayout_7.addWidget(self.radioDayTrue)
        self.radioDayFalse = QtWidgets.QRadioButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioDayFalse.sizePolicy().hasHeightForWidth())
        self.radioDayFalse.setSizePolicy(sizePolicy)
        self.radioDayFalse.setMinimumSize(QtCore.QSize(100, 0))
        self.radioDayFalse.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioDayFalse.setObjectName("radioDayFalse")
        self.horizontalLayout_7.addWidget(self.radioDayFalse)
        self.horizontalLayout_6.addWidget(self.widget_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout_16.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_12, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem13, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabSetting, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #! 클릭 이벤트들
        
        # 검색 버튼
        self.buttonSearchDrug.clicked.connect(self.clickDrugSearchButton)
        # 등록 버튼 클릭
        self.buttonSelectedDrugRegister.clicked.connect(self.clickDrugRegisterButton)
        # 리스트 아이템 약물 더블클릭
        self.listWidgetDbDrugList.itemDoubleClicked.connect(self.clickDoubleDrugListItem)
        # 새로고침 버튼 클릭
        self.buttonRenew.clicked.connect(self.clickRenewButton)
        # 선택 약물 삭제 버튼
        self.buttonSelectedDrugDelete.clicked.connect(self.clickDeleteSelectedDrug)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "약물 검색"))
        self.buttonSearchDrug.setText(_translate("MainWindow", "검색"))
        self.groupBox_2.setTitle(_translate("MainWindow", "약물 리스트"))
        self.buttonSelectedDrugRegister.setText(_translate("MainWindow", "선택 약물 등록"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDrugRegister), _translate("MainWindow", "약물 등록"))
        self.groupBox_4.setTitle(_translate("MainWindow", "위험 정보"))
        self.groupBox_5.setTitle(_translate("MainWindow", "약물 상세 정보"))
        
        detailedInfo = [{
          'itemName':'', 
          'efcyQesitm':'',
          'useMethodQesitm':'',
          'atpnWarnQesitm':'',
          'atpnQesitm':'',
          'intrcQesitm':'',
          'seQesitm':'',
          'depositMethodQesitm':''
        }]
        try:
          detailedInfo = drugData.getDetailedDrugInfo(self.listWidgetDbDrugList.selectedItems()[0].text())
        except:
          pass
        self.textDrugDetailedInfo.setHtml(_translate("MainWindow", f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:400; font-style:normal;\">\n" 

"<h4>제품명</h4>"
f"{detailedInfo[0]['itemName']} <br />"
'<h4>약의 효능</h4>'
f"{detailedInfo[0]['efcyQesitm']} <br />"
'<h4>약 사용 방법</h4>'
f"{detailedInfo[0]['useMethodQesitm']} <br />"
'<h4>약 사용전 알아야 될 내용</h4>'
f"{detailedInfo[0]['atpnWarnQesitm']} <br />"
'<h4>약 복용 및 사용시 주의사항</h4>'
f"{detailedInfo[0]['atpnQesitm']} <br />"
'<h4>약 복용 및 사용시 주의해야 할 약 또는 음식</h4>'
f"{detailedInfo[0]['intrcQesitm']} <br />"
'<h4>약 복용 및 사용시 나타날 수 있는 이상반응</h4>'
f"{detailedInfo[0]['seQesitm']} <br />"
'<h4>약 보관방법</h4>'
f"{detailedInfo[0]['depositMethodQesitm']} <br />"

"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "약물 리스트"))
        self.buttonSelectedDrugDelete.setText(_translate("MainWindow", "선택 약물 삭제"))
        self.buttonRenew.setText(_translate("MainWindow", "새로고침"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDrugList), _translate("MainWindow", "약물 리스트"))
        self.groupBox_6.setTitle(_translate("MainWindow", "제작 정보"))
        self.label_4.setText(_translate("MainWindow", "Made by Yook"))
        self.label_5.setText(_translate("MainWindow", "alsue2000@gmail.com"))
        self.groupBox_7.setTitle(_translate("MainWindow", "정보 설정"))
        self.label.setText(_translate("MainWindow", "노인 복용 주의 경고 표시"))
        self.radioElderTrue.setText(_translate("MainWindow", "표시함"))
        self.radioElderFalse.setText(_translate("MainWindow", "표시 안함"))
        self.label_2.setText(_translate("MainWindow", "임산부 복용 주의 경고 표시"))
        self.radioPragnantTrue.setText(_translate("MainWindow", "표시함"))
        self.radioPragnantFalse.setText(_translate("MainWindow", "표시 안함"))
        self.label_3.setText(_translate("MainWindow", "용량 주의 경고 표시"))
        self.radioMaxTrue.setText(_translate("MainWindow", "표시함"))
        self.radioMaxFalse.setText(_translate("MainWindow", "표시 안함"))
        self.label_6.setText(_translate("MainWindow", "투여기간 주의 경고 표시"))
        self.radioDayTrue.setText(_translate("MainWindow", "표시함"))
        self.radioDayFalse.setText(_translate("MainWindow", "표시 안함"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), _translate("MainWindow", "설정"))
        
    # 첫 화면 검색 버튼 클릭
    def clickDrugSearchButton(self):
      drugName = self.TextEditDrugSearch.toPlainText()
      if drugName == '':
        pass
      else:
        try:
          searchedDrugList = drugData.getDrugName(drugName)
        except:
          pass
      
      self.ListWidgetDrugList.clear()
      self.ListWidgetDrugList.addItems(searchedDrugList)
      
    # 첫 화면 약물 등록 버튼 클릭
    def clickDrugRegisterButton(self):
      try:
        drugName = self.ListWidgetDrugList.selectedItems()[0].text()
        ingrCode = drugData.getDrugIngrCode(drugName)
        ingrNameKor = drugData.getDrugIngrNameKor(drugName)
        drugInfo = pd.DataFrame({'name': drugName, 'ingrCode':[ingrCode], 'ingrNameKor': [ingrNameKor]})
        drugData.saveDrugDB(drugInfo)
        
        db = drugData.readDrugDB()
        self.listWidgetDbDrugList.addItems(list(db['name']))
      except:
        pass
      
      
    # 두번재 화면 약물 리스트 더블 클릭
    def clickDoubleDrugListItem(self):
      _translate = QtCore.QCoreApplication.translate
      try:
          name = self.listWidgetDbDrugList.selectedItems()[0].text()
          for i in range(3, len(name)):
            try:
              detailedInfo = drugData.getDetailedDrugInfo(name[:i])
            except:
              pass
          self.textDrugDetailedInfo.setHtml(_translate("MainWindow", f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:400; font-style:normal;\">\n" 

"<h4>제품명</h4>"
f"{detailedInfo[0]['itemName']} <br />"
'<h4>약의 효능</h4>'
f"{detailedInfo[0]['efcyQesitm']} <br />"
'<h4>약 사용 방법</h4>'
f"{detailedInfo[0]['useMethodQesitm']} <br />"
'<h4>약 사용전 알아야 될 내용</h4>'
f"{detailedInfo[0]['atpnWarnQesitm']} <br />"
'<h4>약 복용 및 사용시 주의사항</h4>'
f"{detailedInfo[0]['atpnQesitm']} <br />"
'<h4>약 복용 및 사용시 주의해야 할 약 또는 음식</h4>'
f"{detailedInfo[0]['intrcQesitm']} <br />"
'<h4>약 복용 및 사용시 나타날 수 있는 이상반응</h4>'
f"{detailedInfo[0]['seQesitm']} <br />"
'<h4>약 보관방법</h4>'
f"{detailedInfo[0]['depositMethodQesitm']} <br />"

"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>"))
      except:
        pass
      
    # 두번재 화면 새로고침 버튼 클릭
    def clickRenewButton(self):
      try:
        self.listWidgetDbDrugList.clear()
        db = drugData.readDrugDB()
        self.listWidgetDbDrugList.addItems(list(db['name']))

      except:
        pass
      
    # 선택 약물 삭제 버튼 클릭
    def clickDeleteSelectedDrug(self):
      try:
        db = drugData.readDrugDB()
        delIndex = self.listWidgetDbDrugList.selectedIndexes()[0].row()
        newDB = db.drop(delIndex)
        newDB = newDB.reset_index(drop=True)
        self.listWidgetDbDrugList.clear()
        self.listWidgetDbDrugList.addItems(list(newDB['name']))
        newDB.to_csv('db.csv')
      except:
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

