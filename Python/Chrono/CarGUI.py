# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/jérôme/Desktop/Freescale/freescale-cup-dan-jerome/Python/GUI Qt/CarGUI.ui'
#
# Created: Tue Feb  3 21:35:41 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 593)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setMargin(5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.COM_GroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COM_GroupBox.sizePolicy().hasHeightForWidth())
        self.COM_GroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.COM_GroupBox.setFont(font)
        self.COM_GroupBox.setObjectName(_fromUtf8("COM_GroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.COM_GroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_connect = QtGui.QPushButton(self.COM_GroupBox)
        self.btn_connect.setObjectName(_fromUtf8("btn_connect"))
        self.gridLayout.addWidget(self.btn_connect, 2, 1, 1, 1)
        self.text_port = QtGui.QLabel(self.COM_GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_port.sizePolicy().hasHeightForWidth())
        self.text_port.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_port.setFont(font)
        self.text_port.setObjectName(_fromUtf8("text_port"))
        self.gridLayout.addWidget(self.text_port, 0, 0, 1, 1)
        self.btn_refresh = QtGui.QPushButton(self.COM_GroupBox)
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.gridLayout.addWidget(self.btn_refresh, 2, 0, 1, 1)
        self.btn_disconnect = QtGui.QPushButton(self.COM_GroupBox)
        self.btn_disconnect.setObjectName(_fromUtf8("btn_disconnect"))
        self.gridLayout.addWidget(self.btn_disconnect, 2, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(self.COM_GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setEditable(False)
        self.comboBox.setMinimumContentsLength(4)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 3)
        self.text_connected = QtGui.QLabel(self.COM_GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_connected.sizePolicy().hasHeightForWidth())
        self.text_connected.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.text_connected.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_connected.setFont(font)
        self.text_connected.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_connected.setObjectName(_fromUtf8("text_connected"))
        self.gridLayout.addWidget(self.text_connected, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.COM_GroupBox)
        self.Logger_GroupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Logger_GroupBox.setFont(font)
        self.Logger_GroupBox.setObjectName(_fromUtf8("Logger_GroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Logger_GroupBox)
        self.gridLayout_2.setMargin(5)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lbl_selvar = QtGui.QLabel(self.Logger_GroupBox)
        self.lbl_selvar.setObjectName(_fromUtf8("lbl_selvar"))
        self.gridLayout_2.addWidget(self.lbl_selvar, 3, 0, 1, 1)
        self.btn_plot = QtGui.QPushButton(self.Logger_GroupBox)
        self.btn_plot.setObjectName(_fromUtf8("btn_plot"))
        self.gridLayout_2.addWidget(self.btn_plot, 3, 2, 1, 1)
        self.btn_write = QtGui.QPushButton(self.Logger_GroupBox)
        self.btn_write.setObjectName(_fromUtf8("btn_write"))
        self.gridLayout_2.addWidget(self.btn_write, 4, 2, 1, 1)
        self.spb_selvar = QtGui.QSpinBox(self.Logger_GroupBox)
        self.spb_selvar.setAccelerated(True)
        self.spb_selvar.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.spb_selvar.setMinimum(-65535)
        self.spb_selvar.setMaximum(65535)
        self.spb_selvar.setObjectName(_fromUtf8("spb_selvar"))
        self.gridLayout_2.addWidget(self.spb_selvar, 4, 1, 1, 1)
        self.txt_active = QtGui.QLabel(self.Logger_GroupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.txt_active.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_active.setFont(font)
        self.txt_active.setTextFormat(QtCore.Qt.RichText)
        self.txt_active.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_active.setObjectName(_fromUtf8("txt_active"))
        self.gridLayout_2.addWidget(self.txt_active, 0, 1, 1, 2)
        self.txt_log = QtGui.QLabel(self.Logger_GroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_log.setFont(font)
        self.txt_log.setObjectName(_fromUtf8("txt_log"))
        self.gridLayout_2.addWidget(self.txt_log, 0, 0, 1, 1)
        self.btn_activate = QtGui.QPushButton(self.Logger_GroupBox)
        self.btn_activate.setMinimumSize(QtCore.QSize(116, 0))
        self.btn_activate.setObjectName(_fromUtf8("btn_activate"))
        self.gridLayout_2.addWidget(self.btn_activate, 1, 0, 1, 1)
        self.varliste = QtGui.QTableWidget(self.Logger_GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.varliste.sizePolicy().hasHeightForWidth())
        self.varliste.setSizePolicy(sizePolicy)
        self.varliste.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.varliste.setDragEnabled(False)
        self.varliste.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.varliste.setAlternatingRowColors(True)
        self.varliste.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.varliste.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.varliste.setShowGrid(False)
        self.varliste.setWordWrap(False)
        self.varliste.setRowCount(5)
        self.varliste.setObjectName(_fromUtf8("varliste"))
        self.varliste.setColumnCount(5)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.varliste.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.varliste.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.varliste.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.varliste.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.varliste.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.varliste.setItem(0, 0, item)
        self.varliste.horizontalHeader().setVisible(True)
        self.varliste.horizontalHeader().setCascadingSectionResizes(False)
        self.varliste.horizontalHeader().setDefaultSectionSize(30)
        self.varliste.horizontalHeader().setHighlightSections(True)
        self.varliste.horizontalHeader().setMinimumSectionSize(25)
        self.varliste.horizontalHeader().setStretchLastSection(True)
        self.varliste.verticalHeader().setVisible(False)
        self.varliste.verticalHeader().setDefaultSectionSize(20)
        self.varliste.verticalHeader().setMinimumSectionSize(11)
        self.gridLayout_2.addWidget(self.varliste, 2, 0, 1, 3)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.verticalLayout_2.addWidget(self.Logger_GroupBox)
        self.Control_GroupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Control_GroupBox.setFont(font)
        self.Control_GroupBox.setObjectName(_fromUtf8("Control_GroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Control_GroupBox)
        self.gridLayout_3.setMargin(6)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.btn_restart = QtGui.QPushButton(self.Control_GroupBox)
        self.btn_restart.setObjectName(_fromUtf8("btn_restart"))
        self.gridLayout_3.addWidget(self.btn_restart, 0, 2, 1, 1)
        self.btn_start_log = QtGui.QPushButton(self.Control_GroupBox)
        self.btn_start_log.setCheckable(True)
        self.btn_start_log.setObjectName(_fromUtf8("btn_start_log"))
        self.gridLayout_3.addWidget(self.btn_start_log, 1, 2, 1, 1)
        self.btn_stop = QtGui.QPushButton(self.Control_GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        self.btn_stop.setCheckable(True)
        self.btn_stop.setChecked(False)
        self.btn_stop.setDefault(False)
        self.btn_stop.setFlat(False)
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.gridLayout_3.addWidget(self.btn_stop, 0, 0, 2, 1)
        self.verticalLayout_2.addWidget(self.Control_GroupBox)
        self.debug = QtGui.QPushButton(self.centralwidget)
        self.debug.setObjectName(_fromUtf8("debug"))
        self.verticalLayout_2.addWidget(self.debug)
        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.btn_refresh)
        MainWindow.setTabOrder(self.btn_refresh, self.btn_connect)
        MainWindow.setTabOrder(self.btn_connect, self.btn_disconnect)
        MainWindow.setTabOrder(self.btn_disconnect, self.btn_activate)
        MainWindow.setTabOrder(self.btn_activate, self.varliste)
        MainWindow.setTabOrder(self.varliste, self.btn_plot)
        MainWindow.setTabOrder(self.btn_plot, self.spb_selvar)
        MainWindow.setTabOrder(self.spb_selvar, self.btn_write)
        MainWindow.setTabOrder(self.btn_write, self.btn_stop)
        MainWindow.setTabOrder(self.btn_stop, self.btn_restart)
        MainWindow.setTabOrder(self.btn_restart, self.btn_start_log)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Car GUI", None))
        self.COM_GroupBox.setTitle(_translate("MainWindow", "COM Ports", None))
        self.btn_connect.setText(_translate("MainWindow", "CONNECT", None))
        self.text_port.setText(_translate("MainWindow", "STATUS:", None))
        self.btn_refresh.setText(_translate("MainWindow", "REFRESH", None))
        self.btn_disconnect.setText(_translate("MainWindow", "DISCONNECT", None))
        self.text_connected.setText(_translate("MainWindow", "NOT CONNECTED", None))
        self.Logger_GroupBox.setTitle(_translate("MainWindow", "DistantIO", None))
        self.lbl_selvar.setText(_translate("MainWindow", "No var", None))
        self.btn_plot.setText(_translate("MainWindow", "Plot", None))
        self.btn_write.setText(_translate("MainWindow", "WRITE", None))
        self.txt_active.setText(_translate("MainWindow", "INACTIVE", None))
        self.txt_log.setText(_translate("MainWindow", "STATUS:", None))
        self.btn_activate.setText(_translate("MainWindow", "RETRIEVE TABLE", None))
        item = self.varliste.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.varliste.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.varliste.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type", None))
        item = self.varliste.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size", None))
        item = self.varliste.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Value", None))
        __sortingEnabled = self.varliste.isSortingEnabled()
        self.varliste.setSortingEnabled(False)
        self.varliste.setSortingEnabled(__sortingEnabled)
        self.Control_GroupBox.setTitle(_translate("MainWindow", "CarControl", None))
        self.btn_restart.setText(_translate("MainWindow", "RESTART CAR", None))
        self.btn_start_log.setText(_translate("MainWindow", "START LOGGING", None))
        self.btn_stop.setText(_translate("MainWindow", "START CAR", None))
        self.btn_stop.setShortcut(_translate("MainWindow", "Return", None))
        self.debug.setText(_translate("MainWindow", "Debug", None))

